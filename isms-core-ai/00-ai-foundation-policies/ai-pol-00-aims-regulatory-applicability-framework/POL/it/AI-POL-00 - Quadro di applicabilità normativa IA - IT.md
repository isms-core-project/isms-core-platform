<!-- ISMS-CORE:POLICY:AI-POL-00-IT:ai:POL:00 -->
**AI-POL-00 — Quadro di applicabilità normativa IA**
**Riferimento autorevole per gli obblighi di conformità del sistema di gestione dell'IA**

---

## Controllo del documento

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Quadro di applicabilità normativa IA |
| **Tipo di documento** | Politica |
| **ID documento** | AI-POL-00 |
| **Autore del documento** | Responsabile della Governance IA (RGIA) / Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto AIMS** | 1.0 |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 0.1 | [Data - 8 settimane] | RGIA | Bozza iniziale — quadro a tre livelli, perimetro Regolamento IA UE + ISO 42001 |
| 0.2 | [Data - 6 settimane] | RGIA + Legale | Aggiunta degli obblighi settoriali, collocazione ISO 42005:2025 nel livello |
| 0.3 | [Data - 4 settimane] | RSSI | Allineamento con la metodologia ISMS-POL-00; aggiunto il contesto della strategia IA svizzera |
| 0.4 | [Data - 2 settimane] | RGIA / Legale / RSSI | Integrazione del feedback degli stakeholder; sezione di monitoraggio della legislazione imminente |
| 1.0 | [Data] | RGIA / Legale / RSSI | Prima versione approvata |

**Ciclo di revisione**: Annuale (o in caso di modifiche significative alle normative IA, pubblicazione di nuovi standard o variazioni al perimetro di certificazione)
**Data della prossima revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Primaria: Responsabile della Governance IA (o RSSI designato in assenza di una funzione dedicata alla governance IA)
- Secondaria: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Conformità: Responsabile Legale / Compliance
- Autorità finale: Direzione generale

**Documenti correlati**:

- AI-POL-01 — Quadro di governance e processo decisionale AIMS
- ISMS-POL-00 — Quadro di applicabilità normativa (base ISMS — riferimento obbligatorio)
- ISO/IEC 42001:2023 Clausola 4.2 (Comprensione delle esigenze e aspettative delle parti interessate)
- ISO/IEC 42001:2023 Clausola 4.3 (Determinazione del perimetro del sistema di gestione dell'IA)
- Tutti i documenti di politica AIMS (riferimento obbligatorio)

**Distribuzione**: Tutti gli stakeholder AIMS, responsabili della governance IA, autori di politiche, proprietari di sistemi IA, funzione legale/compliance, revisori
**Richiamato da**: Tutti i documenti di politica AIMS (AI-POL-01, tutte le politiche di gruppo di controllo AI-POL-A.x.x)

**Strategia linguistica**: Ove i termini tecnici o normativi siano internazionalmente consolidati (es. EU AI Act, GPAI, ISO/IEC, AISIA, NIST AI RMF), si mantiene la terminologia in inglese per preservare la precisione e facilitare i riferimenti normativi transfrontalieri.

---

## Sintesi esecutiva

Il presente documento fornisce il **riferimento autorevole** per l'interpretazione dell'applicabilità delle normative e dei quadri regolatori IA nell'intero Sistema di Gestione dell'IA (AIMS).

**Scopo**: Eliminare ambiguità e incoerenze nel modo in cui le leggi, i regolamenti e i quadri di governance IA vengono richiamati nelle politiche, procedure e controlli AIMS.

**Perimetro**: Tutti i riferimenti a leggi IA, regolamenti IA e quadri di governance IA nella documentazione AIMS.

**Relazione con l'ISMS**: La presente politica è il complemento specifico per l'IA di **ISMS-POL-00** (Quadro di applicabilità normativa). ISMS-POL-00 disciplina gli obblighi di sicurezza delle informazioni. AI-POL-00 disciplina gli obblighi di gestione e governance dell'IA. Ove gli obblighi si sovrappongano (es. RGPD Articolo 22 — decisioni automatizzate, o i requisiti di sicurezza del Regolamento IA UE per l'IA ad alto rischio), ISMS-POL-00 prevale per la dimensione della sicurezza delle informazioni; AI-POL-00 disciplina la dimensione della governance IA. Gli obblighi in materia di privacy derivanti dal trattamento di dati personali da parte dei sistemi IA sono affrontati in coordinamento con PRIV-POL-00.

**Principio fondamentale**: **L'applicabilità normativa in materia di IA deve essere esplicita, non presunta.** I riferimenti alle normative e ai quadri IA si suddividono in tre categorie:

1. **Conformità obbligatoria** — Obblighi legali che si applicano all'organizzazione
2. **Applicabilità condizionale** — Requisiti che si applicano solo al verificarsi di specifiche condizioni
3. **Riferimento informativo** — Migliori pratiche e orientamenti tecnici

**Utilizzo**: Tutte le politiche AIMS DEVONO includere una sezione "Quadro normativo" che richiama il presente documento, identificando il livello di appartenenza di ciascuna normativa o standard citato.

**Termini chiave**: Le definizioni dei termini utilizzati nella presente politica sono fornite nel **Glossario** al termine del documento.

---

## Autorità e confini della politica

### Scopo e perimetro della presente politica

La presente politica definisce l'**identificazione e l'applicabilità** dei requisiti legali, statutari, normativi e contrattuali per il Sistema di Gestione dell'IA dell'[Organizzazione].

**La presente politica stabilisce:**

- Quali leggi e standard IA si applicano all'[Organizzazione]
- La categorizzazione degli obblighi IA (Obbligatorio, Condizionale, Informativo)
- La metodologia di valutazione per determinare l'applicabilità in base al ruolo dell'organizzazione nel campo dell'IA
- I processi di revisione e aggiornamento in risposta ai cambiamenti del quadro normativo IA

**La presente politica NON stabilisce:**

- Le decisioni di trattamento del rischio IA (affrontate nella gestione del rischio AIMS)
- I requisiti di implementazione dei controlli (affrontati nelle politiche di gruppo di controllo e nei documenti IMP)
- Lo stato di conformità o le verifiche (affrontati nei processi di monitoraggio della conformità)
- Gli obblighi di sicurezza delle informazioni (affrontati in ISMS-POL-00)
- Gli obblighi di privacy per il trattamento di dati personali da parte dell'IA (affrontati in PRIV-POL-00)

**Principio di confine**: La presente politica stabilisce l'applicabilità normativa IA. L'implementazione, l'applicazione e la verifica sono gestite attraverso processi e politiche di gruppo di controllo AIMS separati.

**Integrazione con ISO/IEC 42001:2023:**

- **Clausola 4.2 (Parti interessate)**: I requisiti normativi IA costituiscono gli obblighi principali verso le parti interessate. La presente politica li identifica esplicitamente.
- **Clausola 4.3 (Perimetro)**: La determinazione del perimetro è influenzata dagli obblighi di Livello 1 applicabili e dal ruolo dell'organizzazione nel campo dell'IA (fornitore, operatore o entrambi).
- **Clausola 6 (Valutazione del rischio)**: Gli obblighi normativi confluiscono nel registro dei rischi IA. Livello 1 = priorità Alta, Livello 2 condizionale = priorità Media, Livello 3 = input informativo.

**Integrazione con ISMS-POL-00 e PRIV-POL-00:**

La presente politica opera congiuntamente a ISMS-POL-00 e PRIV-POL-00. Ove una normativa IA abbia dimensioni relative alla sicurezza delle informazioni (es. Regolamento IA UE Articolo 15 — accuratezza, robustezza e sicurezza informatica), ISMS-POL-00 disciplina l'interpretazione in materia di sicurezza. Ove una normativa IA abbia dimensioni relative alla privacy (es. RGPD Articolo 22 — decisioni individuali automatizzate), PRIV-POL-00 disciplina l'interpretazione in materia di protezione dei dati. AI-POL-00 disciplina l'interpretazione in materia di gestione e governance IA.

---

## Determinazione del ruolo dell'organizzazione nel campo dell'IA

**Questo passaggio deve essere completato prima di applicare il quadro normativo.** Gli obblighi normativi IA differiscono in modo significativo a seconda del ruolo dell'organizzazione nella catena del valore IA.

### Ruoli definiti dal Regolamento IA UE (Regolamento 2024/1689)

| Ruolo | Definizione | Obblighi |
|-------|------------|---------|
| **Fornitore IA** | Sviluppa un sistema IA o un modello IA per uso generale con l'intenzione di immetterlo sul mercato o metterlo in servizio con il proprio nome o marchio, anche mediante download | Livello di obbligo più elevato — valutazione della conformità, documentazione tecnica, monitoraggio post-commercializzazione |
| **Operatore IA** | Utilizza un sistema IA sotto la propria autorità per finalità professionali | Applicare le istruzioni del fornitore, effettuare la VIDF per l'IA ad alto rischio, conservare i registri, garantire la supervisione umana |
| **Importatore IA** | Immette sul mercato UE un sistema IA recante il nome di un soggetto stabilito fuori dall'UE | Verificare la conformità, conservare la documentazione, segnalare alle autorità |
| **Distributore IA** | Mette a disposizione sul mercato UE un sistema IA, diversamente dal fornitore o dall'importatore | Verificare la marcatura CE, la documentazione e la registrazione |

### Ruoli definiti da ISO/IEC 42001:2023

| Ruolo | Definizione |
|-------|------------|
| **Fornitore IA** | Sviluppa, addestra, distribuisce o mantiene sistemi IA (per uso interno o esterno) |
| **Utente IA / Operatore IA** | Integra o utilizza sistemi IA sviluppati da terze parti |
| **Entrambi** | La maggior parte delle organizzazioni aziendali — sviluppa internamente alcune funzionalità IA e utilizza strumenti IA di terze parti |

**Azione di valutazione richiesta**: L'[Organizzazione] DEVE documentare il proprio ruolo nell'inventario dei sistemi IA (AI-POL-01) per ciascun sistema IA in perimetro. I ruoli possono differire per ogni sistema IA.

---

## Categorie di applicabilità normativa

**Conformità obbligatoria**
Obblighi legali o contrattuali IA cui l'[Organizzazione] DEVE conformarsi. Il mancato rispetto comporta responsabilità legale, sanzioni normative, indagini da parte delle autorità di vigilanza o perdita della certificazione.

**Caratteristiche**:

- Applicabile da un'autorità normativa o da un tribunale
- Il mancato rispetto ha conseguenze legali o finanziarie (sanzioni, ordini esecutivi, restrizioni all'accesso al mercato)
- Richiede prove documentate di conformità (valutazioni della conformità, documentazione tecnica, registrazioni degli incidenti)
- Soggetto ad audit normativi, ispezioni e poteri delle autorità di vigilanza

**Applicabilità condizionale**
Requisiti IA che si applicano solo al verificarsi di condizioni specifiche (es. tipologie specifiche di sistema IA, esposizione geografica al mercato, certificazione ricercata, contratti con clienti, settori regolamentati).

**Caratteristiche**:

- L'applicabilità dipende dalle caratteristiche del sistema IA, dal contesto di deployment o dalla geografia di mercato
- Può diventare obbligatoria in base alle attività aziendali o ai requisiti contrattuali
- Richiede rivalutazione periodica con l'evoluzione delle attività aziendali e dei sistemi IA

**Riferimento informativo / Allineamento alle migliori pratiche**
Quadri e standard utilizzati per orientamenti tecnici e organizzativi, benchmarking o allineamento volontario. Questi informano le pratiche di governance IA ma non costituiscono requisiti di conformità obbligatoria.

**Caratteristiche**:

- Adozione volontaria per le migliori pratiche
- Nessun meccanismo di enforcement legale diretto
- Utilizzati come orientamento per l'implementazione dell'IA responsabile
- Possono diventare obbligatori se richiamati in contratti o requisiti di certificazione

---

## Gerarchia di conformità

```
┌─────────────────────────────────────────────────────────────────────┐
│              GERARCHIA DI CONFORMITÀ IA                             │
├─────────────────────────────────────────────────────────────────────┤
│  LIVELLO 1: OBBLIGATORIO (Legale / Contrattuale)                    │
│  • Regolamento IA UE (Reg. 2024/1689) — ove si immette IA sul       │
│    mercato UE o si mette IA in servizio nell'UE                     │
│  • Obblighi IA settoriali (DORA, MiFID II, MDR, ecc.)               │
│  • RGPD Articolo 22 — ove l'IA adotta decisioni automatizzate su    │
│    individui con effetti legali o significativi                     │
│                                                                     │
│  LIVELLO 2: CONDIZIONALE (Dipendente dal contesto)                  │
│  • ISO/IEC 42001:2023 — ove si ricerca la certificazione o          │
│    richiesto contrattualmente                                       │
│  • ISO/IEC 42005:2025 — metodologia VISIA (complemento a 42001,     │
│    applicabile ove 42001 sia in perimetro)                          │
│  • Obblighi di valutazione della conformità per IA ad alto rischio  │
│    (ove il sistema IA sia classificato ad alto rischio — Allegato III)│
│  • Leggi IA nazionali nei mercati in cui l'organizzazione opera     │
│                                                                     │
│  LIVELLO 3: INFORMATIVO (Migliori pratiche / Orientamenti tecnici)  │
│  • NIST AI Risk Management Framework 1.0 (NIST AI RMF)             │
│  • ISO/IEC 23894:2023 (orientamenti sulla gestione del rischio IA)  │
│  • ISO/IEC 38507:2022 (governance dell'IA)                          │
│  • Principi OCSE sull'IA (2019, rivisti 2024)                       │
│  • Raccomandazione UNESCO sull'etica dell'IA (2021)                 │
│  • Strategia IA del Consiglio federale svizzero (2023)              │
│                                                                     │
│  IN ARRIVO (Da monitorare — adottare alla pubblicazione/entrata      │
│  in vigore)                                                         │
│  • Legislazione IA nazionale svizzera (prevista)                    │
│  • ISO/IEC 42006 — orientamenti per l'audit interno AIMS (in svi.)  │
│  • Direttiva UE sulla responsabilità civile per l'IA (in sviluppo)  │
└─────────────────────────────────────────────────────────────────────┘
```

> *Se i caratteri grafici non vengono visualizzati correttamente, fare riferimento alle sezioni sottostanti per le definizioni dei livelli.*

---

# Conformità obbligatoria (Livello 1)

> **Nota sulla classificazione di ISO/IEC 42001:2023**: ISO/IEC 42001:2023 è classificato come **Livello 2 (Applicabilità condizionale)** nel presente quadro. Non è una normativa legalmente vincolante. Diventa obbligatorio per l'[Organizzazione] ove si ricerchi attivamente la certificazione o ove un contratto con un cliente richieda esplicitamente la conformità AIMS. Ove nessuna delle due condizioni si applichi, funziona come quadro volontario di migliori pratiche. Per i dettagli completi, si rimanda alla sezione ISO/IEC 42001:2023 nel Livello 2.

## Regolamento sull'intelligenza artificiale dell'UE (Regolamento 2024/1689)

**Applicabilità**: Ove si immetta un sistema IA sul mercato UE, lo si metta in servizio nell'UE, o ove i risultati del sistema IA siano utilizzati nell'UE — indipendentemente da dove sia stabilita l'organizzazione. Si applica integralmente dal 2 agosto 2026 (con le disposizioni sull'IA vietata in vigore dal 2 febbraio 2025 e le disposizioni GPAI dal 2 agosto 2025).

**Quadro di classificazione del rischio**:

Il Regolamento IA UE adotta un approccio basato sul rischio. Ogni sistema IA deve essere classificato:

| Livello di rischio | Definizione | Obblighi |
|-------------------|------------|---------|
| **Rischio inaccettabile** (Vietato) | Sistemi IA che rappresentano una minaccia evidente ai diritti fondamentali o alla sicurezza | Divieto assoluto — non possono essere immessi sul mercato. Esempi: manipolazione subliminale, punteggio sociale, identificazione biometrica remota in tempo reale negli spazi pubblici (salvo limitate eccezioni per le forze dell'ordine), sfruttamento delle vulnerabilità legate all'età/disabilità |
| **Ad alto rischio** (Allegato III) | Sistemi IA in settori regolamentati o con impatto significativo sui diritti fondamentali | Obblighi completi di conformità — v. sotto |
| **A rischio limitato** | Sistemi IA con specifici obblighi di trasparenza | Comunicare all'utente l'interazione con l'IA (chatbot, deepfake) |
| **A rischio minimo** | Tutti gli altri sistemi IA | Nessun requisito obbligatorio; codici di condotta volontari |
| **IA per uso generale (GPAI)** | Modelli IA con capacità generali (es. LLM) | Trasparenza, conformità al diritto d'autore; modelli a rischio sistemico hanno obblighi aggiuntivi |

**Categorie di sistemi IA ad alto rischio (Allegato III)**:

- Identificazione e categorizzazione biometrica
- Gestione e funzionamento delle infrastrutture critiche
- Istruzione e formazione professionale (accesso, valutazione)
- Occupazione, gestione dei lavoratori e accesso al lavoro autonomo
- Accesso e fruizione di servizi e prestazioni private e pubbliche essenziali
- Attività di contrasto
- Gestione della migrazione, dell'asilo e del controllo delle frontiere
- Amministrazione della giustizia e processi democratici

**Requisiti principali per i fornitori IA ad alto rischio**:

- Articolo 9: Sistema di gestione della qualità (SGQ) comprensivo di gestione del rischio
- Articolo 10: Requisiti per i dati di addestramento, validazione e test
- Articolo 11: Documentazione tecnica (prima dell'immissione sul mercato)
- Articolo 12: Conservazione dei registri (registrazione per tutto il ciclo di vita operativo)
- Articolo 13: Trasparenza e fornitura di informazioni agli operatori
- Articolo 14: Misure di supervisione umana
- Articolo 15: Requisiti di accuratezza, robustezza e sicurezza informatica
- Articolo 16: Obblighi dei fornitori (registrazione, marcatura CE, monitoraggio post-commercializzazione)
- Articolo 26: Obblighi degli operatori (valutazione dell'impatto sui diritti fondamentali per enti pubblici e determinati operatori privati)

**Requisiti principali per i fornitori di modelli GPAI**:

- Articolo 53: Trasparenza e conformità al diritto d'autore (documentazione tecnica, sintesi dei dati di addestramento)
- Articolo 55: Modelli a rischio sistemico (test avversariali, segnalazione degli incidenti, misure di sicurezza informatica)

**Impatto sull'AIMS**:

- L'inventario dei sistemi IA deve classificare ogni sistema per categoria di rischio ai sensi del Regolamento IA UE
- I sistemi ad alto rischio richiedono la valutazione della conformità prima dell'immissione sul mercato UE
- La documentazione tecnica è mantenuta ai sensi dei requisiti dell'Articolo 11
- La VISIA (A.5.2–A.5.5) è allineata con la Valutazione d'Impatto sui Diritti Fondamentali (VIDF) per l'IA ad alto rischio
- A.6.2.6 (operazione e monitoraggio) deve recepire gli obblighi di monitoraggio post-commercializzazione
- A.8.4 (comunicazione degli incidenti) deve recepire le tempistiche di segnalazione degli incidenti gravi ai sensi del Regolamento IA UE

**Autorità di vigilanza**: Autorità nazionale di sorveglianza del mercato di ogni Stato membro UE; Ufficio europeo per l'IA (Commissione europea) per i modelli GPAI

**Riferimento**: Regolamento (UE) 2024/1689, Gazzetta ufficiale dell'UE, 12 luglio 2024. Date di applicazione: IA vietata dal 2 febbraio 2025; disposizioni GPAI dal 2 agosto 2025; applicazione integrale dal 2 agosto 2026.

---

## RGPD Articolo 22 — Decisioni automatizzate

**Applicabilità**: Ove l'[Organizzazione] utilizzi sistemi IA per adottare **decisioni basate esclusivamente su trattamento automatizzato** che producano **effetti giuridici** o **incidano in modo significativo** sugli individui (es. credit scoring automatizzato, screening automatizzato delle candidature, determinazione automatizzata dell'ammissibilità a prestazioni, rilevamento automatizzato di frodi con conseguente blocco dell'account).

**Requisiti principali**:

- Diritto a non essere soggetti a decisioni basate esclusivamente su trattamento automatizzato con effetti legali o significativi (Articolo 22(1))
- Eccezioni: consenso esplicito, necessità contrattuale o autorizzazione da parte della normativa dell'Unione o di uno Stato membro — tutte richiedono salvaguardie
- Ove le eccezioni si applichino: informare gli individui, implementare una supervisione umana significativa, garantire il diritto di contestare la decisione e ottenere una revisione umana
- Valutazioni d'impatto sulla protezione dei dati (DPIA) obbligatorie per il trattamento automatizzato sistematico che potrebbe comportare un rischio elevato (Articolo 35)

**Impatto sull'AIMS**:

- I sistemi IA che adottano decisioni automatizzate con conseguenze significative devono essere identificati nell'inventario dei sistemi IA
- Controlli obbligatori di supervisione umana (A.6.2.6) per le decisioni guidate dall'IA che interessano individui
- Le comunicazioni di trasparenza (A.8.2, A.8.5) devono recepire gli obblighi informativi del RGPD Articolo 22
- Collegamento a PRIV-POL-00 e PRIV-POL-A.1.3.11 (Decisioni automatizzate) per gli obblighi completi di protezione dei dati

**Autorità di vigilanza**: Autorità di protezione dei dati (DPA) competente UE/SEE

**Riferimento**: Regolamento (UE) 2016/679 Articolo 22; Linee guida 05/2020 sul processo decisionale automatizzato individuale e sulla profilazione (EDPB)

---

## Obblighi IA settoriali

Determinati settori regolamentati impongono obblighi specifici in materia di IA in aggiunta al Regolamento IA UE. L'applicabilità dipende dal settore e dalle attività dell'[Organizzazione].

**Servizi finanziari — DORA (Regolamento 2022/2554)**:

- Articoli 28–30: La gestione del rischio delle TIC di terze parti si applica agli strumenti IA e ai fornitori di servizi IA
- DORA classifica gli strumenti IA utilizzati in funzioni critiche come dipendenze TIC di terze parti soggette agli obblighi completi di TPRM
- I sistemi IA utilizzati nel trading, nella gestione del rischio o nei servizi ai clienti rientrano nel perimetro della segnalazione degli incidenti TIC
- **Condizione di applicabilità**: L'[Organizzazione] è un soggetto regolamentato da DORA (istituto finanziario, impresa di investimento, impresa di assicurazione, prestatore di servizi per le cripto-attività, ecc.)

**Dispositivi medici — MDR (Regolamento 2017/745) e IVDR (Regolamento 2017/746)**:

- I dispositivi medici basati su IA e i dispositivi medico-diagnostici in vitro sono soggetti alla valutazione della conformità MDR/IVDR
- Il software per dispositivi medici basato su IA (SaMD) può essere classificato ad alto rischio sia ai sensi del MDR che del Regolamento IA UE — potrebbe applicarsi una doppia valutazione della conformità
- **Condizione di applicabilità**: L'[Organizzazione] sviluppa o immette sul mercato dispositivi medici basati su IA o software diagnostico

**Aviazione, Automotive, Ferroviario, Marittimo (regimi di marcatura CE)**:

- I sistemi IA integrati in prodotti safety-critical regolamentati dalla legislazione esistente sulla sicurezza dei prodotti potrebbero richiedere una doppia conformità sia ai sensi del Regolamento IA UE che delle normative settoriali specifiche
- **Condizione di applicabilità**: L'[Organizzazione] sviluppa sistemi IA integrati in prodotti safety-critical di questi settori

**Azione di valutazione richiesta**: Il Responsabile Legale/Compliance deve valutare gli obblighi IA settoriali annualmente e documentare i risultati nel registro normativo.

---

# Applicabilità condizionale (Livello 2)

Queste normative e questi standard si applicano **solo al verificarsi di condizioni specifiche**.

## ISO/IEC 42001:2023 — Sistema di gestione dell'IA

**Standard**: ISO/IEC 42001:2023 (Prima edizione) — Tecnologia dell'informazione — Intelligenza artificiale — Sistema di gestione

**Condizioni di applicabilità**:

- L'[Organizzazione] **ricerca la certificazione ISO/IEC 42001:2023** (autonoma o combinata con la certificazione ISO 27001)
- Un contratto con un cliente **richiede esplicitamente** la conformità AIMS a questo standard
- L'[Organizzazione] **adotta volontariamente** ISO 42001 come quadro di governance IA (in questo caso trattato come vincolante a livello operativo)

**Nota di classificazione**: ISO/IEC 42001:2023 è classificato Livello 2 (Condizionale) nel presente quadro. Non è una normativa legalmente vincolante. Non diventa obbligatorio semplicemente perché l'[Organizzazione] sviluppa o utilizza sistemi IA — il Regolamento IA UE svolge questa funzione per l'esposizione al mercato UE. Ove si ricerchi la certificazione o sia richiesta contrattualmente, è trattato come un impegno operativo vincolante equivalente al Livello 1 per la durata della certificazione.

**Requisiti principali**:

- Clausola 4: Contesto dell'organizzazione (comprensione del contesto, parti interessate, perimetro AIMS)
- Clausola 5: Leadership (politica IA, ruoli e responsabilità, impegno dell'alta direzione)
- Clausola 6: Pianificazione (valutazione del rischio IA, valutazione dell'impatto del sistema IA, obiettivi IA)
- Clausola 7: Supporto (risorse, competenza, consapevolezza, comunicazione, informazioni documentate)
- Clausola 8: Attività operative (pianificazione operativa, esecuzione della valutazione del rischio IA, trattamento del rischio, esecuzione della VISIA)
- Clausola 9: Valutazione delle prestazioni (monitoraggio, audit interno, riesame della direzione)
- Clausola 10: Miglioramento (non conformità, azioni correttive, miglioramento continuo)
- Allegato A (normativo): 36 controlli in 9 domini (A.2–A.10)
- Allegato B (normativo): Orientamenti di implementazione per tutti i controlli dell'Allegato A

**Erogazione AIMS**: Il set completo di controlli dell'Allegato A di ISO 42001 è erogato tramite le politiche di gruppo di controllo AI-POL-A.x.x in `53-isms-core-ai/`. La Dichiarazione di Applicabilità (DDA) dell'[Organizzazione] deve fare riferimento a queste politiche.

**Integrazione con ISO 27001**: ISO 42001 utilizza la stessa struttura di alto livello (HLS/Annex SL) di ISO 27001:2022. Le organizzazioni in possesso della certificazione ISO 27001 possono integrare o combinare i processi AIMS e ISMS sotto un sistema di gestione condiviso. Le aree di clausola comuni (7, 9, 10) possono riutilizzare l'infrastruttura ISMS esistente.

**Riferimento**: ISO/IEC 42001:2023, Tecnologia dell'informazione — Intelligenza artificiale — Sistema di gestione, dicembre 2023

---

## ISO/IEC 42005:2025 — Valutazione dell'impatto del sistema IA

**Standard**: ISO/IEC 42005:2025 (Prima edizione) — Tecnologia dell'informazione — Intelligenza artificiale — Valutazione dell'impatto del sistema IA

**Condizioni di applicabilità**:

- ISO/IEC 42001:2023 è in perimetro (si applica la condizione Livello 2 di cui sopra) — ISO 42005:2025 fornisce la metodologia per la Clausola 6.1.4 di ISO 42001 (valutazione dell'impatto del sistema IA) e i controlli dell'Allegato A da A.5.2 a A.5.5
- L'[Organizzazione] adotta formalmente la VISIA come parte del proprio programma di governance IA
- Contratti con clienti o obblighi normativi (es. requisiti VIDF del Regolamento IA UE) richiedono una metodologia documentata di valutazione dell'impatto IA

**Contenuto di ISO 42005:2025**:

- Clausola 5: Sviluppo e implementazione del processo VISIA (perimetro, soglie, usi sensibili, usi limitati, scale di impatto, responsabilità, approvazione, monitoraggio e revisione)
- Clausola 6: Documentazione della valutazione dell'impatto del sistema IA (descrizione del sistema IA, funzionalità e capacità, uso previsto, informazioni e qualità dei dati, informazioni su algoritmi e modelli, ambiente di deployment, parti interessate pertinenti, impatti effettivi e ragionevolmente prevedibili, benefici e danni, misure per affrontare i danni)
- Allegato A (informativo): Orientamenti per l'utilizzo con ISO/IEC 42001
- Allegato B (informativo): Orientamenti per l'utilizzo con ISO/IEC 23894 (gestione del rischio IA)

**Impatto sull'AIMS**:

- Tutti i modelli VISIA in `53-isms-core-ai/` devono essere costruiti rispetto ai requisiti di documentazione della Clausola 6 di ISO 42005:2025
- La metodologia VISIA nei documenti AIMS deve fare riferimento a ISO 42005:2025, non a orientamenti generici
- La VISIA di ISO 42005:2025 è allineata con la Valutazione d'Impatto sui Diritti Fondamentali (VIDF) del Regolamento IA UE — le organizzazioni soggette a entrambe dovrebbero documentare il riferimento incrociato

**Riferimento**: ISO/IEC 42005:2025, Tecnologia dell'informazione — Intelligenza artificiale — Valutazione dell'impatto del sistema IA, maggio 2025

---

## Valutazione della conformità per IA ad alto rischio (Regolamento IA UE)

**Condizione di applicabilità**: L'[Organizzazione] agisce come fornitore IA o operatore IA per un sistema IA classificato come **ad alto rischio** ai sensi dell'Allegato III del Regolamento IA UE.

**Obblighi aggiuntivi attivati**:

- Procedura di valutazione della conformità (Articolo 43) — controllo interno o valutazione di terza parte (organismo notificato) a seconda della categoria del sistema IA
- Registrazione nel database del Regolamento IA UE (Articolo 49) prima dell'immissione sul mercato
- Marcatura CE e dichiarazione di conformità
- Sistema di monitoraggio post-commercializzazione (Articolo 72)
- Segnalazione degli incidenti gravi all'autorità nazionale (Articolo 73) entro le tempistiche definite

**Azione di valutazione richiesta**: Per ogni sistema IA in perimetro per il mercato UE, classificare ai sensi delle categorie di rischio del Regolamento IA UE e documentare nell'inventario dei sistemi IA. La classificazione ad alto rischio attiva la pianificazione della valutazione della conformità.

---

# Riferimento informativo (Livello 3)

Questi quadri informano le pratiche di governance IA ma non costituiscono requisiti di conformità obbligatoria. Sono utilizzati per orientamento, benchmarking e implementazione delle migliori pratiche.

## NIST AI Risk Management Framework 1.0 (NIST AI RMF)

**Pubblicato**: Gennaio 2023 — National Institute of Standards and Technology (USA)

**Rilevanza**: Fornisce un quadro volontario per la gestione dei rischi IA attraverso quattro funzioni principali: GOVERN, MAP, MEASURE, MANAGE. Riconosciuto a livello internazionale come riferimento pratico per la gestione del rischio IA anche al di fuori degli USA.

**Utilizzo nell'AIMS**:

- La struttura del registro dei rischi IA è informata dalla tassonomia dei rischi del NIST AI RMF (GOVERN, MAP, MEASURE, MANAGE)
- Il concetto di profilo NIST AI RMF supporta la prioritizzazione del rischio IA specifica dell'organizzazione
- Crosswalk: le mappature NIST AI RMF ↔ ISO 42001 assistono le organizzazioni che operano con entrambi i quadri

**Riferimento**: NIST AI RMF 1.0, NIST AI 100-1, gennaio 2023

---

## ISO/IEC 23894:2023 — Gestione del rischio IA

**Pubblicato**: Febbraio 2023

**Rilevanza**: Fornisce orientamenti su come le organizzazioni possono gestire i rischi specificamente correlati all'IA. Estende ISO 31000 (gestione del rischio) con considerazioni specifiche per l'IA. Richiamato dall'Allegato B di ISO 42001 e dall'Allegato B di ISO 42005.

**Utilizzo nell'AIMS**:

- La metodologia di valutazione del rischio IA è informata dagli orientamenti di identificazione e analisi del rischio di ISO 23894
- La tassonomia del rischio IA è informata dalle categorie di ISO 23894 (tecnico, operativo, sociale)

**Riferimento**: ISO/IEC 23894:2023, Tecnologia dell'informazione — Intelligenza artificiale — Orientamenti sulla gestione del rischio

---

## ISO/IEC 38507:2022 — Governance dell'IA per le organizzazioni

**Pubblicato**: Aprile 2022

**Rilevanza**: Fornisce orientamenti sulle implicazioni in materia di governance dell'utilizzo dell'IA da parte delle organizzazioni. Affronta come i membri degli organi di governance possano abilitare, estendere e sviluppare la governance IA. Richiamato nell'Allegato B.2.3 di ISO 42001.

**Utilizzo nell'AIMS**:

- La struttura di governance per l'IA (A.3.2) è informata dagli orientamenti di ISO 38507 sulla governance IA a livello di organo direttivo
- Il quadro di accountability dell'alta direzione è allineato ai principi di ISO 38507

**Riferimento**: ISO/IEC 38507:2022, Tecnologia dell'informazione — Intelligenza artificiale — Implicazioni in materia di governance dell'uso dell'IA da parte delle organizzazioni

---

## Principi OCSE sull'IA (2019, rivisti 2024)

**Pubblicato**: Maggio 2019 (rivisto giugno 2024) — Organizzazione per la Cooperazione e lo Sviluppo Economico

**Rilevanza**: Riferimento internazionale per l'IA responsabile. Adottati dal G20. Ampiamente richiamati nella legislazione IA nazionale incluso il Regolamento IA UE. Cinque principi: crescita inclusiva e benessere; valori umani e equità; trasparenza e spiegabilità; robustezza e sicurezza; accountability.

**Utilizzo nell'AIMS**:

- I principi di IA responsabile in AI-POL-01 sono allineati ai Principi OCSE sull'IA
- I Considerando del Regolamento IA UE richiamano i Principi OCSE — l'allineamento riduce le lacune interpretative

**Riferimento**: Principi OCSE sull'IA, OECD/LEGAL/0449, adottati il 22 maggio 2019, rivisti nel 2024

---

## Strategia IA del Consiglio federale svizzero (2023)

**Pubblicato**: Dicembre 2023 — Consiglio federale svizzero

**Rilevanza**: La strategia IA del governo svizzero delinea i principi di IA responsabile per la pubblica amministrazione e segnala la direzione per la futura legislazione IA svizzera. Non giuridicamente vincolante per il settore privato come del 2026.

**Contesto svizzero**: La Svizzera non ha adottato una legge IA nazionale autonoma come dell'aprile 2026. La governance IA per le organizzazioni del settore privato in Svizzera è affrontata principalmente attraverso:

- nLPD svizzera (Legge federale sulla protezione dei dati, RS 235.1) — si applica al trattamento IA di dati personali
- LCSi svizzera (Legge federale sulla sicurezza delle informazioni, RS 128) — si applica ai sistemi IA nelle infrastrutture critiche nazionali
- Strategia IA del Consiglio federale svizzero — principi volontari
- Regolamento IA UE — si applica alle organizzazioni svizzere che immettono IA sul mercato UE

**Monitorare**: Si prevede che la legislazione IA nazionale svizzera segua il quadro del Regolamento IA UE. Assegnare la responsabilità del monitoraggio al Responsabile Legale/Compliance.

---

# In arrivo (Da monitorare — adottare alla pubblicazione o all'entrata in vigore)

Questi strumenti sono in fase di sviluppo o previsti. L'[Organizzazione] deve monitorarli e adottarli alla pubblicazione o all'entrata in vigore.

| Strumento | Stato | Impatto previsto |
|----------|-------|-----------------|
| **Legislazione IA nazionale svizzera** | Prevista — nessuna bozza pubblicata come dell'aprile 2026 | Probabile allineamento con il Regolamento IA UE per i sistemi IA sul mercato CH; AIMS già allineato |
| **ISO/IEC 42006** — Requisiti per l'audit dei sistemi di gestione dell'IA | In sviluppo (ISO/IEC JTC 1/SC 42) | Definirà i requisiti di audit AIMS interno/esterno — aggiornare il programma di audit AIMS alla pubblicazione |
| **Direttiva UE sulla responsabilità civile per l'IA** | In sviluppo | Potrebbe imporre responsabilità civile per danni causati da sistemi IA; attiva aggiornamenti al registro dei rischi AIMS |
| **Atti delegati del Regolamento IA UE** | Previsti 2025–2026 | Dettagli tecnici per la valutazione della conformità, mandati di standardizzazione, soglie per i modelli GPAI |
| **NIST AI RMF 2.0 / profili settoriali** | Previsti periodicamente | Aggiornare il riferimento NIST AI RMF Livello 3 alla pubblicazione |

**Responsabilità di monitoraggio**: Responsabile Legale/Compliance, con il supporto del Responsabile della Governance IA. Ciclo di revisione: scansione trimestrale, aggiornamento annuale della politica se attivato.

---

# Processo di valutazione e revisione

## Determinazione dell'applicabilità

Per ogni nuovo sistema IA sviluppato o acquisito, e ad ogni ciclo di revisione annuale, il Responsabile della Governance IA e il Responsabile Legale/Compliance devono:

1. **Identificare il ruolo dell'[Organizzazione] nel campo dell'IA** per il sistema (fornitore, operatore, entrambi) secondo le definizioni di ruolo sopra riportate
2. **Valutare l'applicabilità del Livello 1** — classificazione del rischio ai sensi del Regolamento IA UE; condizione RGPD Articolo 22; condizioni settoriali specifiche
3. **Valutare le condizioni del Livello 2** — Si ricerca la certificazione ISO 42001 o è richiesta contrattualmente? Il sistema è ad alto rischio ai sensi del Regolamento IA UE e richiede una valutazione della conformità?
4. **Esaminare la rilevanza del Livello 3** — Documentare quali quadri informativi informano l'implementazione per il sistema
5. **Aggiornare l'inventario dei sistemi IA** (AI-POL-01) con i risultati della classificazione normativa
6. **Aggiornare la DDA AIMS** se i nuovi obblighi influiscono sulla selezione dei controlli

## Revisione annuale

La presente politica deve essere rivista annualmente dal Responsabile della Governance IA e dal Responsabile Legale/Compliance. Condizioni per la revisione fuori ciclo:

- Nuova normativa IA adottata in una giurisdizione in cui l'[Organizzazione] opera
- Nuovo standard IA pubblicato che influisce sul quadro dei controlli AIMS
- Variazione significativa nel portafoglio IA dell'[Organizzazione] (nuovo sistema IA in categoria ad alto rischio)
- Azione di enforcement normativo nei confronti di un'organizzazione dello stesso settore che rivela una nuova interpretazione di un obbligo

---

# Glossario

| Termine | Definizione |
|---------|------------|
| **Regolamento IA** | Regolamento sull'intelligenza artificiale dell'UE — Regolamento (UE) 2024/1689 sull'intelligenza artificiale |
| **Operatore IA** | Persona fisica o giuridica che utilizza un sistema IA sotto la propria autorità per finalità professionali (definizione del Regolamento IA UE) |
| **Fornitore IA** | Persona o soggetto che sviluppa un sistema IA o un modello GPAI con l'intenzione di immetterlo sul mercato UE (definizione del Regolamento IA UE) |
| **Sistema IA** | Sistema basato su macchine progettato per operare con vari livelli di autonomia, che può presentare carattere adattivo e che — per obiettivi espliciti o impliciti — inferisce, dall'input ricevuto, come generare output quali previsioni, contenuti, raccomandazioni o decisioni (definizione ISO/IEC 42001:2023, allineata con l'Articolo 3 del Regolamento IA UE) |
| **AIMS** | Sistema di Gestione dell'IA — sistema di gestione per lo sviluppo, il deployment e l'utilizzo responsabile dei sistemi IA |
| **VISIA** | Valutazione d'Impatto del Sistema IA — valutazione formale delle potenziali conseguenze di un sistema IA per individui e società (ISO/IEC 42001:2023 Clausola 6.1.4; dettagli in ISO/IEC 42005:2025) |
| **VIDF** | Valutazione d'Impatto sui Diritti Fondamentali — richiesta ai sensi dell'Articolo 26 del Regolamento IA UE per gli operatori di determinati sistemi IA ad alto rischio che interessano persone fisiche |
| **GPAI** | IA per uso generale — modello IA addestrato su dati ampi, in grado di svolgere più compiti (es. modelli linguistici di grandi dimensioni); soggetto a obblighi specifici ai sensi del Titolo V del Regolamento IA UE |
| **IA ad alto rischio** | Sistema IA rientrante nelle categorie dell'Allegato III del Regolamento IA UE, soggetto a obblighi completi di conformità prima dell'immissione sul mercato UE |
| **Obbligatorio** | Livello 1 — obbligo legalmente o contrattualmente vincolante con conseguenze in caso di inadempimento |
| **Condizionale** | Livello 2 — obbligo che diventa applicabile al verificarsi di condizioni specifiche |
| **Informativo** | Livello 3 — quadro volontario di migliori pratiche che informa l'implementazione AIMS senza enforcement diretto |
| **DDA** | Dichiarazione di Applicabilità — documento che elenca tutti i 36 controlli dell'Allegato A di ISO 42001 con le decisioni di applicabilità e le relative giustificazioni |
| **Rischio sistemico** | Rischio associato a modelli GPAI con calcolo di addestramento molto elevato (≥10^25 FLOP) che comporta effetti negativi su scala UE |

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
