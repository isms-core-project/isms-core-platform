<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.7-IT:framework:POL:a.5.7 -->
**ISMS-POL-A.5.7 — Intelligence sulle minacce**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Politica sull'intelligence sulle minacce |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.7 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data da definire] | RSSI | Politica iniziale per la certificazione ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Direttore dei Sistemi Informativi (DSI)
- Rischio: Responsabile del rischio (CRO)
- Conformità: Responsabile Legale/Conformità
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-IMP-A.5.7.1-UG/TG (Valutazione delle fonti di intelligence sulle minacce)
- ISMS-IMP-A.5.7.2-UG/TG (Valutazione della raccolta e analisi dell'intelligence)
- ISMS-IMP-A.5.7.3-UG/TG (Valutazione dell'integrazione e distribuzione dell'intelligence)
- ISO/IEC 27001:2022 Controllo A.5.7

---

# Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per l'intelligence sulle minacce al fine di consentire una difesa proattiva, informare la gestione del rischio e potenziare le operazioni di sicurezza conformemente al Controllo A.5.7 della norma ISO/IEC 27001:2022.

**Scopo**: Definire i requisiti organizzativi per la governance dell'intelligence sulle minacce. Questa politica stabilisce COSA è richiesto in termini di capacità di intelligence sulle minacce e CHI è responsabile. Le procedure di attuazione (COME) sono documentate separatamente in ISMS-IMP-A.5.7 (varianti UG/TG).

**Perimetro**: Tutte le attività di intelligence sulle minacce (raccolta, analisi, produzione, diffusione); tutti i tipi di intelligence (strategica, tattica, operativa); tutte le fonti di intelligence (piattaforme commerciali, OSINT, feed governativi, telemetria interna); tutto il personale coinvolto nelle operazioni di sicurezza; tutti gli strumenti di sicurezza che integrano l'intelligence sulle minacce.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Perimetro

## Controllo ISO/IEC 27001:2022 A.5.7

**ISO/IEC 27001:2022 Allegato A.5.7 — Intelligence sulle minacce**

> *Le informazioni relative alle minacce alla sicurezza delle informazioni devono essere raccolte e analizzate per produrre intelligence sulle minacce.*

**Obiettivo del controllo**: Stabilire una politica organizzativa per i controlli di intelligence sulle minacce che consentano il rilevamento proattivo delle minacce, informino le decisioni di gestione del rischio, prioritizzino gli investimenti nella sicurezza e migliorino l'efficacia della risposta agli incidenti.

## Limiti della politica

**Questa politica affronta** (COSA/CHI): Requisiti di raccolta dell'intelligence sulle minacce da più tipi di fonti; requisiti di analisi e produzione dell'intelligence; requisiti di diffusione dell'intelligence agli stakeholder; requisiti di integrazione con la valutazione del rischio (Clausola 6.1 ISO 27001); requisiti di integrazione con la gestione degli incidenti (Controlli A.5.24-5.28); ruoli e responsabilità organizzativi; quadri di eccezione e governance.

**Questa politica NON affronta** (COME — vedere ISMS-IMP-A.5.7): Dettagli tecnici di implementazione e configurazione della piattaforma; strumenti specifici di intelligence sulle minacce o selezione dei fornitori; quadri di analisi dettagliati e procedure degli analisti; metodologie specifiche di misurazione dei KPI; procedure di deployment degli IoC; criteri di valutazione e punteggio delle fonti.

## Copertura organizzativa

**Nel perimetro**: Tutti i dipendenti (permanenti, temporanei, appaltatori); tutti i team di operazioni di sicurezza e risposta agli incidenti; tutte le funzioni di gestione del rischio e conformità; fornitori di servizi terzi con accesso all'intelligence sulle minacce; tutte le sedi e le unità aziendali.

**Fuori dal perimetro**: Operazioni offensive informatiche o azioni di rappresaglia (vietate); indagini delle forze dell'ordine (cooperazione supportata, non condotta); scansione delle vulnerabilità e test di penetrazione (trattati nel Controllo A.8.8); operazioni di threat hunting (trattate nel Controllo A.8.16).

---

# Enunciati di politica

## Raccolta dell'intelligence sulle minacce

[Organizzazione] DEVE implementare la raccolta dell'intelligence sulle minacce da più categorie di fonti per garantire una visibilità completa sulle minacce.

**Categorie di fonti richieste**:

- **Piattaforme commerciali**: Feed di intelligence sulle minacce curati con validazione
- **Intelligence open source (OSINT)**: Dati pubblici sulle minacce, database delle vulnerabilità
- **Feed governativi/CERT**: Avvisi CERT nazionali, avvisi per infrastrutture critiche
- **Condivisione del settore (ISAC/ISAO)**: Minacce specifiche del settore e collaborazione tra pari (raccomandata)
- **Telemetria interna**: Avvisi degli strumenti di sicurezza, dati sugli incidenti, risultati forensi

**Requisiti di gestione delle fonti**:

- Tutte le fonti DEVONO essere valutate per affidabilità e credibilità prima dell'operativizzazione
- Le fonti DEVONO essere validate periodicamente per accuratezza e prestazioni
- I requisiti di protezione dei dati DEVONO essere applicati a tutta l'intelligence raccolta
- La condivisione con terze parti DEVE essere governata dalle classificazioni del Protocollo semaforo (TLP)

**Riferimento all'implementazione**: Inventario delle fonti e criteri di valutazione documentati in ISMS-IMP-A.5.7.1.

## Analisi e produzione dell'intelligence sulle minacce

[Organizzazione] DEVE implementare un'analisi strutturata dell'intelligence per trasformare i dati grezzi sulle minacce in intelligence attuabile.

**Requisiti di produzione dell'intelligence**:

**Intelligence strategica** (Audience Direzione generale):

- Valutazioni del panorama delle minacce e analisi delle tendenze
- Raccomandazioni per gli investimenti nella sicurezza basate sul rischio
- Prodotta almeno trimestralmente, o attivata da eventi significativi

**Intelligence tattica** (Audience Operazioni di sicurezza):

- Profili degli attori delle minacce e TTP
- Analisi delle campagne e schemi di attacco
- Prodotta almeno mensilmente, o attivata da minacce emergenti

**Intelligence operativa** (Audience Tecnica):

- Indicatori di compromissione (IoC) per il rilevamento
- Firme di malware e indicatori comportamentali
- Prodotta continuamente tramite feed automatizzati, con revisione giornaliera degli analisti

**Requisiti di qualità**:

- Tutti i prodotti di intelligence DEVONO citare le fonti con valutazione dell'affidabilità
- L'intelligence DEVE essere convalidata attraverso più fonti ove possibile
- L'intelligence DEVE essere connessa al modello di minaccia e agli asset di [Organizzazione]
- L'intelligence DEVE includere raccomandazioni attuabili o indicazioni per il rilevamento
- L'intelligence DEVE essere classificata utilizzando il TLP e gli schemi di classificazione interni

**Riferimento all'implementazione**: Quadri di analisi e metriche di produzione documentati in ISMS-IMP-A.5.7.2.

## Diffusione dell'intelligence sulle minacce

[Organizzazione] DEVE implementare una diffusione strutturata dell'intelligence garantendo che l'intelligence giusta raggiunga gli stakeholder giusti.

**Requisiti di diffusione**:

- La Direzione generale DEVE ricevere valutazioni strategiche delle minacce
- Le Operazioni di sicurezza DEVONO ricevere IoC operativi e TTP tattici
- La Risposta agli incidenti DEVE ricevere intelligence rilevante per le indagini
- La Gestione del rischio DEVE ricevere dati sulle minacce per gli aggiornamenti della valutazione del rischio
- Le Operazioni IT DEVONO ricevere indicazioni di blocco pertinenti all'infrastruttura

**Controlli sulla condivisione**:

- La condivisione esterna DEVE essere governata dal Protocollo semaforo (TLP)
- I consumatori di intelligence DEVONO fornire feedback sull'efficacia dell'intelligence
- I cicli di feedback bidirezionali DEVONO essere stabiliti tra consumatori e produttori

**Riferimento all'implementazione**: Monitoraggio della diffusione e coinvolgimento degli stakeholder documentati in ISMS-IMP-A.5.7.3.

## Integrazione nella valutazione del rischio (OBBLIGATORIA)

L'intelligence sulle minacce DEVE informare il processo di valutazione del rischio di [Organizzazione] per la Clausola 6.1 ISO 27001:2022.

**Requisiti di integrazione**:

- I risultati dell'intelligence sulle minacce DEVONO informare le stime di probabilità per i rischi di sicurezza
- Le campagne di minacce emergenti DEVONO attivare la rivalutazione del rischio quando prendono di mira il settore di [Organizzazione]
- L'intelligence sullo sfruttamento delle vulnerabilità DEVE informare le valutazioni dell'impatto
- Le raccomandazioni dell'intelligence sulle minacce DEVONO informare la selezione e la prioritizzazione dei controlli
- Gli aggiornamenti del registro dei rischi DEVONO fare riferimento incrociato ai report di intelligence sulle minacce di supporto

**Requisiti di documentazione**:

- Ogni aggiornamento della valutazione del rischio DEVE documentare la fonte dell'intelligence sulle minacce
- DEVE essere mantenuta la tracciabilità tra i report di intelligence sulle minacce e le voci del registro dei rischi

**Riferimento all'implementazione**: Monitoraggio dell'integrazione del rischio documentato in ISMS-IMP-A.5.7.3.

## Integrazione nella gestione degli incidenti (OBBLIGATORIA)

L'intelligence sulle minacce DEVE migliorare il rilevamento, l'indagine e la risposta agli incidenti per i Controlli A.5.24-5.28.

**Requisiti di integrazione**:

- Gli IoC dall'intelligence sulle minacce DEVONO essere distribuiti agli strumenti di rilevamento
- I TTP degli attori delle minacce DEVONO essere tradotti in regole di rilevamento
- L'intelligence sulle minacce DEVE fornire contesto durante le indagini sugli incidenti
- I risultati degli incidenti DEVONO contribuire alla raccolta interna di intelligence sulle minacce
- Le revisioni post-incidente DEVONO validare l'efficacia dell'intelligence sulle minacce

**Riferimento all'implementazione**: Monitoraggio dell'integrazione incidente-TI documentato in ISMS-IMP-A.5.7.3.

## Integrazione nella gestione delle vulnerabilità (OPZIONALE)

Quando [Organizzazione] implementa il Controllo A.8.8 (Gestione delle vulnerabilità tecniche), l'integrazione dell'intelligence sulle minacce è OPZIONALE ma raccomandata.

**Se implementata**: L'intelligence sulle vulnerabilità DEVE combinare i dati CVE con lo stato di sfruttamento; l'intelligence sullo sfruttamento attivo DEVE informare la prioritizzazione della remediation; i punteggi CVSS combinati con l'intelligence sulle minacce DEVONO consentire la prioritizzazione basata sul rischio.

## Misurazione dell'efficacia

[Organizzazione] DEVE misurare l'efficacia del programma di intelligence sulle minacce attraverso metriche oggettive.

**Aree di misurazione richieste**:

- Aggiornamenti della valutazione del rischio guidati dall'intelligence sulle minacce
- Incidenti prevenuti o rilevati tramite l'intelligence sulle minacce
- Accuratezza e prestazioni delle fonti
- Arricchimento delle indagini sugli incidenti con l'intelligence sulle minacce
- Decisioni di sicurezza informate dall'intelligence sulle minacce
- Soddisfazione degli stakeholder per i prodotti di intelligence

**Maturità del programma**: [Organizzazione] DEVE valutare annualmente la maturità del programma di intelligence sulle minacce, coprendo raccolta, analisi, diffusione, operativizzazione e governance.

---

# Ruoli e responsabilità

## Matrice delle responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Direzione generale** | Approvazione strategica, allocazione delle risorse, approvazione della politica |
| **RSSI** | Proprietà della politica, supervisione del programma, approvazione delle eccezioni |
| **CRO** | Integrazione della valutazione del rischio, approvazione degli aggiornamenti del rischio guidati dall'intelligence |
| **Responsabile team intelligence sulle minacce** | Gestione del programma, produzione dell'intelligence, gestione delle fonti |
| **Analisti dell'intelligence sulle minacce** | Raccolta, analisi, produzione e assicurazione della qualità dell'intelligence |
| **Operazioni di sicurezza (SOC)** | Operativizzazione dell'intelligence, deployment degli IoC, ottimizzazione del rilevamento |
| **Team di risposta agli incidenti** | Applicazione dell'intelligence durante le indagini, estrazione degli IoC |
| **Operazioni IT** | Implementazione tecnica dei controlli guidati dall'intelligence |
| **Team di gestione del rischio** | Aggiornamenti della valutazione del rischio basati sull'intelligence sulle minacce |
| **Conformità/Legale** | Interpretazione normativa, conformità alla protezione dei dati |
| **Tutto il personale** | Sensibilizzazione alle minacce, segnalazione di attività sospette |

## Percorso di escalation

- Questioni operative: Analista → Responsabile team TI → Team di sicurezza → RSSI
- Eccezioni tecniche: Responsabile team TI → Team di sicurezza → RSSI
- Preoccupazioni di conformità: Responsabile team TI → Conformità → RSSI → Direzione generale
- Correlate al rischio: Responsabile team TI → CRO → RSSI → Direzione generale
- Incidenti di sicurezza: Chiunque → SOC → Risposta agli incidenti → RSSI

## Requisiti di formazione

- **Tutto il personale**: Formazione annuale sulla sensibilizzazione alla sicurezza inclusa la panoramica del panorama delle minacce
- **Analisti TI**: Formazione specializzata sui quadri di analisi e la redazione dei report
- **Personale SOC**: Formazione sull'operativizzazione dell'intelligence e il deployment degli IoC
- **Leadership della sicurezza**: Briefing strategici sull'intelligence sulle minacce

## Continuità operativa

[Organizzazione] DEVE garantire la continuità delle capacità critiche di intelligence sulle minacce: analisti primari e di backup designati per ciascuna funzione di intelligence; ridondanza delle fonti per le categorie di intelligence critiche; procedure di failover documentate per la piattaforma di intelligence sulle minacce; test annuale della continuità operativa per le operazioni di intelligence sulle minacce.

---

# Conformità ed eccezioni

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria**:

| Normativa | Requisiti chiave |
|-----------|-----------------|
| **nLPD svizzera** | Art. 8 — Misure tecniche e organizzative per il rilevamento delle minacce |
| **RGPD dell'UE** | Art. 32 — Misure di sicurezza incluso il monitoraggio delle minacce |
| **ISO/IEC 27001:2022** | Controllo A.5.7 — Raccolta e analisi dell'intelligence sulle minacce |

**Livello 2 — Applicabilità condizionale** (per ISMS-POL-00): FINMA (istituto finanziario svizzero regolamentato); DORA (entità dei servizi finanziari UE); NIS2 (entità essenziale/importante UE).

## Gestione delle eccezioni

Le eccezioni ai requisiti di intelligence sulle minacce richiedono giustificazione aziendale documentata, valutazione del rischio e approvazione formale.

**Tipi di eccezione**: Eccezioni alla copertura delle fonti (vincoli di budget); eccezioni alla tempistica di integrazione (complessità tecnica); eccezioni alle risorse (organico insufficiente); eccezioni agli obiettivi KPI (programma di nuova implementazione).

**Requisiti per le eccezioni**: A tempo limitato con date di scadenza esplicite; controlli compensativi documentati e verificati; revisione trimestrale della necessità dell'eccezione; prove dei progressi verso la piena conformità.

**Autorità di approvazione**: RSSI: eccezioni a fonti, integrazione e KPI; RSSI + Direzione generale: eccezioni alle risorse.

---

# Governance della politica

## Revisione della politica

- **Frequenza**: Annuale come minimo
- **Trigger**: Cambiamenti normativi, incidenti gravi, cambiamenti significativi del panorama delle minacce, cambiamenti organizzativi, risultati di audit
- **Revisori**: RSSI, Responsabile team intelligence, Team di sicurezza, Gestione del rischio, Conformità
- **Approvazione**: RSSI (tecnica), Direzione generale (strategica)

## Aggiornamenti della politica

- **Minori** (chiarimenti, riferimenti): Approvazione RSSI, comunicazione entro 30 giorni
- **Maggiori** (cambiamenti di perimetro, nuovi requisiti): Catena di approvazione completa
- **Emergenza** (minacce critiche): Approvazione RSSI, comunicazione immediata

---

# Documenti correlati

## Integrazione con il SGSI

- **Valutazione del rischio** (Clausola 6.1): L'intelligence sulle minacce informa l'identificazione e l'analisi dei rischi
- **Dichiarazione di Applicabilità** (Clausola 6.1.3): L'applicabilità del Controllo A.5.7 è documentata
- **Audit interno** (Clausola 9.2): Il programma di intelligence sulle minacce è incluso nell'ambito dell'audit SGSI

## Controlli correlati

| Controllo | Tipo di integrazione | Descrizione |
|-----------|---------------------|-------------|
| **A.5.24-5.28** | OBBLIGATORIA | Gestione degli incidenti — L'intelligence migliora il rilevamento e la risposta |
| **A.8.16** | OBBLIGATORIA | Attività di monitoraggio — L'intelligence fornisce contesto per il rilevamento |
| **A.8.8** | OPZIONALE | Gestione delle vulnerabilità — L'intelligence prioritizza la remediation |
| **A.5.19-5.22** | OPZIONALE | Sicurezza dei fornitori — L'intelligence valuta i rischi delle terze parti |
| **A.5.23** | OPZIONALE | Sicurezza cloud — L'intelligence copre le minacce specifiche del cloud |

## Risorse di implementazione

- **ISMS-IMP-A.5.7.1-UG/TG**: Valutazione delle fonti di intelligence sulle minacce
- **ISMS-IMP-A.5.7.2-UG/TG**: Valutazione della raccolta e analisi dell'intelligence
- **ISMS-IMP-A.5.7.3-UG/TG**: Valutazione dell'integrazione e distribuzione dell'intelligence

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Intelligence sulle minacce** | Raccolta, analisi e diffusione di informazioni sulle minacce attuali o emergenti, per consentire una difesa proattiva e decisioni di sicurezza informate |
| **Intelligence strategica** | Intelligence di alto livello che affronta le minacce generali e le tendenze, a supporto delle decisioni esecutive e della strategia a lungo termine |
| **Intelligence tattica** | Intelligence che descrive le tattiche, tecniche e procedure (TTP) degli avversari, a supporto delle operazioni di sicurezza e della pianificazione della difesa |
| **Intelligence operativa** | Intelligence tecnica attuabile inclusi IoC e regole di rilevamento, a supporto delle operazioni di sicurezza immediate |
| **Indicatore di compromissione (IoC)** | Artefatto osservabile che indica che si è verificata o è in corso una violazione della sicurezza (indirizzi IP, domini, hash di file) |
| **Tattiche, Tecniche e Procedure (TTP)** | Schemi di attività utilizzati dagli attori delle minacce, documentati in quadri come MITRE ATT&CK |
| **Protocollo semaforo (TLP)** | Standard di condivisione delle informazioni che utilizza codici colore (ROSSO, ARANCIONE, ARANCIONE+STRICT, VERDE, CHIARO) per indicare le restrizioni alla condivisione |
| **CVSS** | Common Vulnerability Scoring System — Standard per la valutazione della gravità delle vulnerabilità (0,0-10,0) |
| **Attore della minaccia** | Individuo, gruppo o organizzazione che conduce attività informatiche malevole |

---

# Prove per questa politica

**Prove per la Fase 1**: Documento di politica con firme di approvazione; quadro di governance dell'intelligence sulle minacce definito; tipi di fonti e requisiti di raccolta documentati; requisiti di analisi e produzione specificati; requisiti di distribuzione e stakeholder documentati; requisiti di integrazione nella valutazione del rischio e nella gestione degli incidenti definiti; ruoli e responsabilità assegnati; procedure di governance ed eccezione definite.

**Prove per la Fase 2**: Valutazioni delle fonti di intelligence sulle minacce completate per ISMS-IMP-A.5.7.1; valutazioni della raccolta e analisi dell'intelligence per ISMS-IMP-A.5.7.2 (analisi della copertura, mappatura MITRE ATT&CK, metriche di produzione); valutazioni dell'integrazione e distribuzione per ISMS-IMP-A.5.7.3 (stato dell'integrazione degli strumenti, deployment degli IoC, coinvolgimento degli stakeholder); aggiornamenti della valutazione del rischio guidati dall'intelligence sulle minacce (≥3 esempi per trimestre con tracciabilità); documentazione degli incidenti prevenuti (≥3 esempi per trimestre con prove di convalida); rapporti di convalida delle prestazioni delle fonti (trimestrali); documenti di formazione per il personale dell'intelligence sulle minacce.

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Direttore dei Sistemi Informativi (DSI)** | [Nome] | [Data da definire] |
| **Responsabile del rischio (CRO)** | [Nome] | [Data da definire] |
| **Responsabile Legale/Conformità** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per l'intelligence sulle minacce. Le procedure di attuazione sono documentate in ISMS-IMP-A.5.7 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
