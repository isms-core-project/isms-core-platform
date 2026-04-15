<!-- ISMS-CORE:POLICY:AI-POL-A.4.2-6-IT:ai:POL:a.4.2-6 -->
**AI-POL-A.4.2-6 — Risorse dei sistemi IA**

---

## Controllo del documento

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Risorse dei sistemi IA |
| **Tipo di documento** | Politica |
| **ID del documento** | AI-POL-A.4.2-6 |
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

**Ciclo di revisione**: Annuale (o in caso di variazioni significative al portafoglio di sistemi IA o all'infrastruttura delle risorse)
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Primaria: Responsabile della Governance IA (RGIA)
- Secondaria: Direttore Tecnico (DT) / Responsabile IA Engineering
- Conformità: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Autorità finale: Direzione generale

**Documenti correlati**:

- AI-POL-00 (Quadro di applicabilità normativa IA)
- AI-POL-01 (Quadro di governance e processo decisionale AIMS)
- AI-POL-A.3.2-3 (Ruoli e responsabilità IA — competenza delle risorse umane)
- AI-IMP-A.4.2-6-UG (Risorse dei sistemi IA — Guida utente)
- AI-IMP-A.4.2-6-TG (Risorse dei sistemi IA — Guida tecnica)
- ISO/IEC 42001:2023 Controlli A.4.2, A.4.3, A.4.4, A.4.5, A.4.6
- ISO/IEC 42001:2023 Clausola 7.1 (Risorse)
- ISO/IEC 42001:2023 Allegato B.4 (Linee guida di attuazione — Risorse per i sistemi IA)

---

## Sintesi esecutiva

La presente politica stabilisce i requisiti dell'[Organizzazione] per l'identificazione, la documentazione e la gestione di tutte le risorse associate ai sistemi IA nel corso dei loro cicli di vita — in conformità con i Controlli A.4.2–A.4.6 della norma ISO/IEC 42001:2023.

**Ambito**: Tutti i sistemi IA nell'ambito dell'AIMS; tutti i tipi di risorse utilizzati in qualsiasi fase del ciclo di vita dei sistemi IA (dati, strumenti, infrastruttura, risorse umane).

**Scopo**: Definire QUALE documentazione delle risorse deve essere mantenuta, CHI è responsabile del suo aggiornamento e QUANDO deve essere rivista e aggiornata. Le procedure di attuazione sono contenute in AI-IMP-A.4.2-6-UG e AI-IMP-A.4.2-6-TG.

**Motivazione dei controlli combinati**: A.4.2–A.4.6 formano collettivamente il requisito di identificazione e documentazione delle risorse per l'AIMS. Comprendere le risorse da cui dipende un sistema IA — attraverso dati, strumenti, capacità di calcolo e capitale umano — è fondamentale per una valutazione accurata dei rischi e dell'impatto. A.4.2 stabilisce l'obbligo generale di documentazione; A.4.3–A.4.6 specificano le categorie di risorse da documentare.

---

## Ambito e applicabilità

### Dichiarazioni dei controlli ISO/IEC 42001:2023

**Controllo A.4.2 — Documentazione delle risorse**
L'organizzazione deve identificare e documentare le risorse pertinenti richieste per le attività nelle determinate fasi del ciclo di vita di un sistema IA e per altre attività legate all'IA rilevanti per l'organizzazione.

**Controllo A.4.3 — Risorse di dati**
Nel quadro dell'identificazione delle risorse, l'organizzazione deve documentare le informazioni sulle risorse di dati utilizzate per il sistema IA.

**Controllo A.4.4 — Risorse strumentali**
Nel quadro dell'identificazione delle risorse, l'organizzazione deve documentare le informazioni sulle risorse strumentali utilizzate per il sistema IA.

**Controllo A.4.5 — Risorse di sistema e di calcolo**
Nel quadro dell'identificazione delle risorse, l'organizzazione deve documentare le informazioni sulle risorse di sistema e di calcolo utilizzate per il sistema IA.

**Controllo A.4.6 — Risorse umane**
Nel quadro dell'identificazione delle risorse, l'organizzazione deve documentare le informazioni sulle risorse umane e le loro competenze utilizzate per lo sviluppo, il dispiegamento, l'esercizio, la gestione dei cambiamenti, la manutenzione, il trasferimento e la dismissione, nonché la verifica e l'integrazione del sistema IA.

### Cosa copre la presente politica

- Requisiti per il Registro delle risorse dei sistemi IA
- Standard di documentazione per ogni categoria di risorse (dati, strumenti, calcolo, risorse umane)
- Obblighi di revisione e aggiornamento delle risorse
- Documentazione delle competenze e gestione delle lacune per le risorse umane

### Cosa NON copre la presente politica

- Processi dettagliati di qualità e gestione dei dati (trattati in AI-POL-A.7.2-6)
- Gestione dei fornitori di risorse IA (trattata in AI-POL-A.10.2-4)
- Processi tecnici del ciclo di vita dei sistemi IA (trattati in AI-POL-A.6.2)

### Quadro normativo

**Livello 1: Conformità obbligatoria** (per AI-POL-00):

- **Regolamento IA UE (Regolamento 2024/1689)**: Articolo 11 (la documentazione tecnica per l'IA ad alto rischio deve includere informazioni sui dati di addestramento, le risorse di calcolo e l'infrastruttura di supervisione umana); Articolo 9 (il SGQ deve affrontare la gestione delle risorse)

**Livello 2: Condizionale** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controlli A.4.2–A.4.6 — applicabile se la certificazione AIMS rientra nell'ambito o è richiesta contrattualmente

**Livello 3: Informativo** (per AI-POL-00):

- NIST AI RMF: GOVERN 4.x — responsabilità del team organizzativo per i rischi IA; MAP 1.x — definizione del contesto IA inclusa l'identificazione delle risorse

---

## Dichiarazioni di politica: Documentazione delle risorse (A.4.2)

### Registro delle risorse dei sistemi IA

L'[Organizzazione] DEVE mantenere un **Registro delle risorse dei sistemi IA** che documenti tutte le risorse significative associate a ciascun sistema IA nell'ambito. Il registro deve essere mantenuto come documento controllato ai sensi della Clausola 7.5 della norma ISO 42001:2023 e aggiornato in ogni fase del ciclo di vita.

Il registro deve identificare le risorse per:

- Fase del ciclo di vita (sviluppo / addestramento / validazione / dispiegamento / esercizio / dismissione)
- Categoria di risorse (dati / strumenti / calcolo / risorse umane)
- Stato della risorsa (in uso / archiviata / dismessa)
- Proprietario o parte responsabile

Il Proprietario del sistema IA è responsabile della manutenzione delle voci del registro delle risorse per il proprio sistema IA. Il RGIA è responsabile della completezza e dell'integrità del registro consolidato.

---

## Dichiarazioni di politica: Risorse di dati (A.4.3)

### Requisito di documentazione delle risorse di dati

Per ciascun sistema IA, l'[Organizzazione] DEVE documentare le risorse di dati utilizzate in tutte le fasi del ciclo di vita.

### Documentazione richiesta per le risorse di dati

| Campo | Contenuto richiesto |
|-------|---------------------|
| Nome / identificativo del dataset | Nome o riferimento di ogni dataset utilizzato |
| Fase del ciclo di vita | Addestramento / validazione / test / esercizio |
| Fonte dei dati | Origine dei dati (sistema interno, dataset su licenza, dataset pubblico, dati raccolti) |
| Tipo di dati | Strutturati / non strutturati / immagini / testo / tabulare / serie temporali / altro |
| Volume | Scala approssimativa (record, GB, token) |
| Frequenza di aggiornamento | Statica / aggiornamento periodico / flusso in tempo reale |
| Licenza / diritti | Proprietà o licenza con cui i dati vengono utilizzati |
| Dati personali | Sì / No — in caso affermativo, collegamento a PRIV-POL-00 e alla DPIA pertinente |
| Classificazione di sensibilità | Secondo lo schema di classificazione dei dati ISMS |
| Riferimento alla valutazione della qualità dei dati | Collegamento al registro di valutazione della qualità (A.7.4) |
| Riferimento al registro di provenienza | Collegamento al registro di provenienza dei dati (A.7.5) |
| Periodo di conservazione | Durata di conservazione dei dati dopo l'utilizzo |

I requisiti dettagliati di gestione dei dati sono regolati da AI-POL-A.7.2-6.

---

## Dichiarazioni di politica: Risorse strumentali (A.4.4)

### Requisito di documentazione delle risorse strumentali

Per ciascun sistema IA, l'[Organizzazione] DEVE documentare le risorse strumentali utilizzate in tutte le fasi del ciclo di vita.

### Documentazione richiesta per le risorse strumentali

| Campo | Contenuto richiesto |
|-------|---------------------|
| Nome e versione dello strumento | Nome e versione di ogni strumento IA, framework o libreria |
| Categoria dello strumento | Framework ML / IDE / strumento di annotazione / strumento di valutazione / piattaforma MLOps / registro di modelli / altro |
| Fase/i del ciclo di vita | Dove nel ciclo di vita viene utilizzato lo strumento |
| Tipo di licenza | Open source (con identificativo di licenza) / commerciale / proprietario |
| Fornitore / responsabile della manutenzione | Organizzazione o progetto che mantiene lo strumento |
| Version pinning | Se la versione dello strumento è fissata; motivazione in caso contrario |
| Valutazione della sicurezza | Riferimento alla valutazione delle vulnerabilità o allo stato di monitoraggio CVE |
| Rischio di sostituzione / deprecazione | Data di fine vita nota o rischio di migrazione |

---

## Dichiarazioni di politica: Risorse di sistema e di calcolo (A.4.5)

### Requisito di documentazione delle risorse di sistema e di calcolo

Per ciascun sistema IA, l'[Organizzazione] DEVE documentare le risorse di infrastruttura di sistema e di calcolo utilizzate.

### Documentazione richiesta per le risorse di sistema e di calcolo

| Campo | Contenuto richiesto |
|-------|---------------------|
| Componente infrastrutturale | Nome / identificativo di ogni componente infrastrutturale |
| Tipo di componente | GPU / cluster CPU / servizio cloud / server on-premise / dispositivo edge / altro |
| Fornitore | IT interno / fornitore cloud (AWS, Azure, GCP, ecc.) / servizio di terze parti |
| Capacità | Specifiche di calcolo, memoria e archiviazione rilevanti per il carico di lavoro IA |
| Fase/i del ciclo di vita | Dove nel ciclo di vita la risorsa viene utilizzata |
| Requisiti di disponibilità | Requisiti di uptime / SLA per l'IA operativa |
| Controlli di sicurezza | Collegamento ai controlli ISMS-POL pertinenti che regolano l'infrastruttura |
| Impronta ambientale | Dati sul consumo energetico o sulle emissioni di carbonio ove applicabile (supporta la consapevolezza dell'impatto sociale ai sensi di A.5.5) |
| Punti di guasto singoli | SPOF identificati e stato delle misure di mitigazione |

---

## Dichiarazioni di politica: Risorse umane (A.4.6)

### Requisito di documentazione delle risorse umane e delle competenze

L'[Organizzazione] DEVE documentare le risorse umane e le loro competenze coinvolte nel sistema IA in tutte le fasi del ciclo di vita, dallo sviluppo alla dismissione.

### Matrice delle competenze

Per ciascun sistema IA deve essere mantenuta una matrice delle competenze che identifichi:

| Attività del ciclo di vita | Competenze richieste | Ruolo/i attuale/i | Stato delle competenze |
|---------------------------|---------------------|-------------------|------------------------|
| Sviluppo del sistema IA | ML/AI engineering, progettazione IA responsabile, data science | Ingegnere IA / Data Scientist | Valutato / Lacuna identificata |
| Gestione dei dati | Data engineering, qualità dei dati, governance dei dati | Data Engineer / Responsabile governance dei dati | Valutato / Lacuna identificata |
| Verifica e validazione | Test IA, valutazione dell'equità, test adversarial | Ingegnere QA / Valutatore IA | Valutato / Lacuna identificata |
| Dispiegamento | MLOps, sicurezza del dispiegamento, configurazione del monitoraggio | Ingegnere MLOps / DevOps | Valutato / Lacuna identificata |
| Esercizio e monitoraggio | Monitoraggio delle prestazioni IA, rilevamento della deriva, risposta agli incidenti | Operazioni IA / Team di piattaforma | Valutato / Lacuna identificata |
| Gestione dei cambiamenti | Valutazione dell'impatto dei cambiamenti IA, trigger di rivalutazione | Proprietario del sistema IA / Responsabile rischi IA | Valutato / Lacuna identificata |
| Trasferimento e integrazione | Architettura di integrazione IA, gestione delle API | Architetto di soluzioni / Responsabile engineering | Valutato / Lacuna identificata |
| Dismissione | Eliminazione dei dati, ritiro del modello, archiviazione della documentazione | Proprietario del sistema IA / Responsabile governance dei dati | Valutato / Lacuna identificata |
| Supervisione della governance | ISO 42001, Regolamento IA UE, governance AIMS | RGIA | Valutato / Lacuna identificata |

### Gestione delle lacune di competenza

Quando viene identificata una lacuna di competenza nella matrice:

1. Il RGIA viene notificato
2. HR e la funzione interessata concordano un piano di risoluzione: formazione, assunzione o coinvolgimento di consulenza esterna
3. Il piano di risoluzione viene documentato nel Registro delle risorse con la data obiettivo
4. Le lacune vengono segnalate alla revisione della direzione come elementi aperti fino alla loro risoluzione

### Sensibilizzazione

Tutte le persone che lavorano su o con sistemi IA devono ricevere una formazione di sensibilizzazione sull'IA che comprenda:

- La Politica IA dell'organizzazione e i principi di IA responsabile
- Il loro ruolo specifico nell'AIMS e i suoi obiettivi
- Come segnalare le preoccupazioni relative all'IA (A.3.3)
- I requisiti applicabili per l'uso responsabile (AI-POL-A.9.2-4)

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **RGIA** | Proprietario del Registro consolidato delle risorse dei sistemi IA; revisione della completezza durante la revisione della direzione; identificazione delle lacune sistemiche nelle risorse |
| **Proprietari di sistemi IA** | Manutenzione delle voci del registro delle risorse per i propri sistemi IA; aggiornamento della documentazione ad ogni transizione del ciclo di vita |
| **DT / Responsabile IA Engineering** | Garantire che la documentazione delle risorse strumentali e di calcolo sia tecnicamente accurata; gestire la sicurezza degli strumenti e il rischio di deprecazione |
| **Responsabile governance dei dati** | Manutenzione della documentazione delle risorse di dati; garantire l'accuratezza delle voci relative a licenze e provenienza dei dati |
| **HR** | Supporto alle valutazioni delle competenze delle risorse umane; coordinamento della formazione per le lacune di competenza |

---

## Requisiti probatori

| Evidenza | Descrizione | Conservazione |
|----------|-------------|---------------|
| Registro delle risorse dei sistemi IA | Registro consolidato che copre tutte le categorie di risorse per ciascun sistema IA | Versione corrente + 3 anni |
| Matrici delle competenze | Valutazioni delle competenze per sistema IA con stato delle lacune | Versione corrente + 3 anni |
| Piani di risoluzione delle lacune di competenza | Piani documentati per affrontare le lacune identificate | Fino alla chiusura della lacuna + 2 anni |
| Registri della formazione di sensibilizzazione | Prove del completamento della formazione di sensibilizzazione sull'IA | Versione corrente + 3 anni |
| Valutazioni della sicurezza degli strumenti | Valutazioni CVE/vulnerabilità per gli strumenti IA | Versione corrente + 2 anni |

---

## Considerazioni per l'audit

Gli auditor che verificano la conformità con A.4.2–A.4.6 dovranno trovare:

- Un Registro delle risorse dei sistemi IA che copra tutte e quattro le categorie di risorse (dati, strumenti, calcolo, risorse umane) per ciascun sistema IA nell'ambito
- Voci delle risorse di dati con riferimenti a licenze, sensibilità e provenienza
- Voci degli strumenti con informazioni su versione e licenza
- Documentazione delle risorse di calcolo con riferimenti a disponibilità e sicurezza
- Matrici delle competenze con persone nominate e stato della competenza valutato
- Prove della gestione delle lacune dove sono state identificate lacune di competenza

---

<!-- QA_VERIFIED: 2026-04-15 -->
