<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.31.1-IT:framework:POL:a.5.31.1 -->
**ISMS-POL-A.5.31.1 — Riepilogo esecutivo e allineamento dei controlli**
**Requisiti legali, normativi e contrattuali**

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Requisiti legali, normativi e contrattuali: Riepilogo esecutivo e allineamento dei controlli |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.31.1 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Quadro di politica iniziale per la prima certificazione ISO 27001:2022 |

---

# Controllo ISO 27001:2022 A.5.31

Questa politica implementa il Controllo A.5.31 dell'Allegato A della norma ISO 27001:2022:

> **Controllo A.5.31: Requisiti legali, normativi e contrattuali**
>
> I requisiti legali, normativi e contrattuali pertinenti alla sicurezza delle informazioni e l'approccio dell'organizzazione per soddisfare tali requisiti devono essere identificati, documentati e mantenuti aggiornati.

**Tipo di controllo**: Controllo organizzativo
**Riferimento ISO 27002:2022**: Sezione 5.31
**Attributo del controllo**: Preventivo

Questo controllo richiede che [Organizzazione] stabilisca e mantenga un approccio sistematico per: identificare i requisiti legali, normativi e contrattuali applicabili; documentare tali requisiti e l'approccio dell'organizzazione per soddisfarli; mantenere aggiornate queste informazioni con l'evolversi del panorama normativo.

---

## Come questo quadro soddisfa il Controllo A.5.31 della norma ISO 27001:2022

Il Controllo A.5.31 richiede alle organizzazioni di:

**1. IDENTIFICARE i requisiti legali, normativi e contrattuali pertinenti alla sicurezza delle informazioni**

**Soddisfatto da**: ISMS-POL-A.5.31.2 (Metodologia di applicabilità normativa)

Implementazione del quadro: fonti monitorate (§2.2); screening iniziale (§2.3); valutazione dell'applicabilità tridimensionale (§3); logica di decisione strutturata (§3.4); output: ISMS-POL-00 (Quadro di applicabilità normativa).

**2. DOCUMENTARE i requisiti e l'approccio dell'organizzazione per soddisfarli**

**Soddisfatto da**: ISMS-POL-A.5.31.3 (Quadro di estrazione dei requisiti e mappatura dei controlli)

Implementazione del quadro: estrazione dei requisiti (§2); categorizzazione dei requisiti (§2.2); mappatura dei controlli (§3); identificazione delle lacune (§4); tracciabilità (§5); output: Registro dei requisiti, Matrice di mappatura dei controlli, Registro delle lacune.

**3. MANTENERE AGGIORNATO il quadro con l'evolversi dei requisiti**

**Soddisfatto da**: ISMS-POL-A.5.31.4 (Quadro di gestione dei cambiamenti e delle prove)

Implementazione del quadro: monitoraggio normativo (§2); valutazione dell'impatto (§3); aggiornamenti del quadro (§4); cicli di revisione (§2.4); output: Registro dei cambiamenti normativi, Registro dei requisiti aggiornato, Mappature dei controlli aggiornate.

**Architettura di integrazione del quadro**:

```
┌─────────────────────────────────────────────────────────────────┐
│             Controllo ISO 27001:2022 A.5.31                     │
│  «Identificare, documentare, mantenere aggiornato»              │
└────────────┬─────────────────────────────────┬──────────────────┘
             │                                  │
             ▼                                  ▼
    ┌────────────────┐                  ┌──────────────────┐
    │  IDENTIFICARE  │                  │  MANTENERE       │
    │  POL-5.31.2:   │                  │  POL-5.31.4:     │
    │  Metodologia   │────────┐         │  Monitoraggio e  │
    │  Applicabilità │        │         │  Cambiamenti     │
    └────────────────┘        │         └──────────────────┘
             │                │                  │
             │                ▼                  │
             │       ┌─────────────────┐         │
             └──────►│  DOCUMENTARE    │◄────────┘
                     │  POL-5.31.3:    │
                     │  Requisiti e    │
                     │  Mappature      │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │  DIMOSTRARE     │
                     │  POL-5.31.4 §5: │
                     │  Prove          │
                     └─────────────────┘
```

**Criteri di valutazione per l'auditor**:

| Requisito ISO 27001 | Componente del quadro | Domanda di valutazione | Stato |
|--------------------|-----------------------|-----------------------|-------|
| Identificare i requisiti | POL-5.31.2 + ISMS-POL-00 | Le normative applicabili sono identificate sistematicamente? | ✅ Documentato |
| Documentare l'approccio | POL-5.31.3 requisiti + mappature | I requisiti sono mappati ai controlli con lacune identificate? | ✅ Documentato |
| Mantenere aggiornato | POL-5.31.4 monitoraggio + valutazione impatto | Esiste un processo per rilevare e rispondere ai cambiamenti? | ✅ Documentato |
| Conservazione prove (implicita) | POL-5.31.4 §5 gestione prove | Le prove di conformità sono sistematicamente mantenute? | ✅ Documentato |

---

# Riepilogo esecutivo

## La sfida della conformità normativa

[Organizzazione] opera in un ambiente normativo sempre più complesso. I requisiti legali, normativi e contrattuali che disciplinano la sicurezza delle informazioni, la protezione dei dati e i servizi IT continuano a proliferare e ad evolversi. Questi obblighi possono derivare da: requisiti legali e normativi nelle giurisdizioni in cui [Organizzazione] opera; mandati normativi delle autorità di vigilanza e dei regolatori del settore; obblighi contrattuali con clienti, partner e fornitori; requisiti di certificazione per standard e framework di settore.

Le conseguenze della non conformità sono sostanziali: sanzioni normative, penali contrattuali, danni reputazionali, perdita della fiducia dei clienti e, nei casi gravi, restrizioni operative o revoca delle licenze.

## L'inadeguatezza della conformità superficiale

Gli approcci tradizionali alla conformità normativa spesso si riducono a comportamenti rituali — imitando la forma della conformità senza la sostanza. Il semplice enunciare «[Organizzazione] si conforma a tutte le leggi e normative applicabili» non soddisfa alcun requisito di audit o di controllo.

Quando un auditor chiede «Come sa di essere conforme alla Normativa X?», la risposta «Perché abbiamo una politica che dice che ci conformiamo a tutte le leggi applicabili» è un ragionamento circolare che non soddisfa nessuno.

## L'approccio ingegneristico alla conformità normativa

Questo quadro adotta un approccio fondamentalmente diverso — applicando la metodologia dell'ingegneria dei sistemi per creare un'**architettura di conformità normativa** che è: **sistematica** (ogni processo è definito, ripetibile e produce output documentati); **tracciabile** (esistono percorsi chiari dalle normative → requisiti → controlli → prove); **basata sulle prove** (le affermazioni di conformità sono supportate da prove tangibili, non da mere asserzioni); **adattiva** (il quadro si adatta ai cambiamenti normativi attraverso processi definiti di gestione dei cambiamenti); **verificabile** (gli auditor esterni possono verificare la conformità seguendo i processi documentati ed esaminando le prove).

Il quadro stabilisce il **ciclo di vita della conformità normativa**: Identificare → Valutare → Estrarre → Mappare → Implementare → Documentare → Monitorare → Adattare → Riferire.

## Cosa fornisce questo quadro

**Per [Organizzazione]**: chiara comprensione di quali normative si applicano e perché; processo sistematico per estrarre e gestire i requisiti normativi; metodologia definita per mappare i requisiti ai controlli di sicurezza; approccio strutturato all'identificazione e al rimedio delle lacune; quadro per dimostrare la conformità con prove tangibili; processo per rimanere aggiornati con i cambiamenti normativi; approccio scalabile con la crescita dell'organizzazione.

**Per auditor e regolatori**: metodologia trasparente che mostra come è stata determinata l'applicabilità; tracciabilità completa dalle normative attraverso i requisiti e i controlli fino alle prove; processi documentati che possono essere esaminati e convalidati.

**Per la direzione generale**: visibilità sullo stato della conformità per tutte le normative applicabili; prioritizzazione basata sul rischio delle lacune di conformità; prise de décision informata sull'allocazione delle risorse; fondamento per il reporting della conformità al consiglio, ai clienti e ai regolatori.

## La natura meta-quadro del Controllo A.5.31

Il Controllo A.5.31 è unico tra i controlli ISO 27001. Mentre la maggior parte dei controlli è **operativa** (implementare controlli degli accessi, configurare firewall, cifrare dati), A.5.31 è un **controllo meta-quadro** — stabilisce la struttura che determina cosa significa conformità per [Organizzazione].

Senza un'implementazione sistematica di A.5.31, [Organizzazione] implementerebbe i controlli ISO 27001 in un vuoto di conformità, incapace di dimostrare come questi controlli soddisfino specifici obblighi normativi.

## Integrazione con ISMS-POL-00

[Organizzazione] ha stabilito **ISMS-POL-00 (Quadro di applicabilità normativa)**, che funge da **registro normativo autorevole** — l'elenco definitivo dei requisiti legali, normativi e contrattuali applicabili a [Organizzazione], organizzato in una struttura a tre livelli (Obbligatorio/Condizionale/Informativo).

Questo quadro (ISMS-POL-A.5.31) definisce **COME** viene creato, mantenuto e utilizzato ISMS-POL-00: processi per identificare e valutare l'applicabilità normativa; metodologia per estrarre requisiti e mapparli ai controlli; procedure per monitorare i cambiamenti normativi e aggiornare POL-00; quadro per gestire le prove di conformità per normativa.

---

# Perimetro e applicabilità

## Perimetro del quadro

**Copertura normativa**: TUTTI i requisiti legali, normativi e contrattuali pertinenti alla sicurezza delle informazioni, comprese: leggi sulla protezione dei dati e sulla privacy; normative sulla cybersicurezza; normative sui servizi finanziari (dove applicabile); normative sanitarie (dove applicabile); requisiti di protezione delle infrastrutture critiche; standard di sicurezza delle informazioni specifici del settore; requisiti contrattuali dei clienti; accordi con i fornitori con obblighi di conformità a cascata; requisiti di certificazione e accreditamento.

**Perimetro organizzativo**: Tutte le unità aziendali; tutte le ubicazioni geografiche; tutti i servizi e prodotti offerti; tutte le giurisdizioni in cui [Organizzazione] opera o serve clienti.

## Quadro universale e indipendente dal settore

Questo quadro è progettato per essere **universale e indipendente dal settore**: nessuna normativa specifica è presupposta; funziona per qualsiasi panorama normativo; adattabile ai cambiamenti organizzativi; neutrale rispetto alla tecnologia e ai fornitori.

## Fuori dal perimetro

**Consulenza legale**: Questo quadro NON fornisce consulenza legale né pareri legali sull'interpretazione normativa. L'interpretazione legale delle normative deve essere eseguita o convalidata da professionisti legali qualificati.

**Conformità operativa**: Questo quadro NON implementa i controlli stessi (responsabilità dei proprietari dei controlli), né monitora la conformità operativa quotidiana.

---

## Stato dell'implementazione e perimetro normativo attuale

**Stato della documentazione (Fase 1)**: ✅ **COMPLETO** — Il quadro di conformità normativa A.5.31 è completamente documentato.

**Stato dell'esecuzione operativa (Fase 2)**: 🔄 **IN CORSO** — Esecuzione del quadro per roadmap di implementazione.

**Determinazioni normative attuali** (fonte: ISMS-POL-00 Sezione 8):

**Livello 1 — Conformità obbligatoria (attualmente applicabile)**: nLPD svizzera (FADP/nDSG) ✅; RGPD dell'UE ✅; ISO/IEC 27001:2022 ✅.

**Livello 2 — Applicabilità condizionale (valutata come non attualmente applicabile)**: DORA — Non applicabile (nessuna entità finanziaria UE); NIS2 — Non applicabile (nessuna entità essenziale/importante); PCI DSS v4.0.1 — Non applicabile (nessun trattamento di dati di carte di pagamento); FINMA — Non applicabile (nessuna licenza FINMA).

**In corso di valutazione**: Legge sull'IA dell'UE.

**Livello 3 — Riferimento informativo (uso attivo)**: NIST SP 800-series, CIS Controls v8.1, OWASP, ISO/IEC 27002:2022.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità | Autorità | Responsabilità per |
|-------|---------------|----------|-------------------|
| **Responsabile della conformità / Funzione legale** | Identificare le normative; condurre valutazioni dell'applicabilità; interpretazione legale; monitorare il panorama normativo | Approvare/rifiutare le determinazioni; coinvolgere consulenti legali | Accuratezza delle valutazioni; correttezza legale |
| **Responsabile del SGSI** | Possedere e mantenere il quadro; coordinare le attività di estrazione dei requisiti; mantenere le matrici di mappatura; riferire lo stato | Approvare le mappature dei controlli; prioritizzare le lacune | Completezza e accuratezza del registro; efficacia del quadro |
| **Proprietari dei controlli** | Implementare i controlli; mantenere la documentazione; raccogliere e mantenere le prove | Determinare l'approccio di implementazione; definire i metodi di raccolta delle prove | Implementazione efficace; qualità e disponibilità delle prove |
| **Audit interno / Team di conformità** | Convalidare la completezza delle prove; eseguire audit di conformità periodici; testare l'efficacia dei controlli | Determinare l'ambito e il calendario dell'audit; emettere risultati | Indipendenza e obiettività |
| **Direzione generale** | Approvare le determinazioni di applicabilità di Livello 1; approvare l'accettazione del rischio; allocare risorse; ricevere report di stato | Autorità di approvazione finale; accettazione del rischio; allocazione delle risorse | Postura di conformità complessiva |

---

# Architettura del quadro

## Livello 1: Quadro di politica (quattro sezioni di politica)

**ISMS-POL-A.5.31.1: Riepilogo esecutivo e allineamento dei controlli** (questo documento) — stabilisce il fondamento e la governance del controllo; definisce perimetro e applicabilità; chiarisce ruoli e responsabilità; fornisce una panoramica dell'architettura del quadro.

**ISMS-POL-A.5.31.2: Metodologia di applicabilità normativa** — definisce il processo sistematico per identificare le normative potenzialmente applicabili; stabilisce i criteri di valutazione tridimensionale; specifica il quadro di categorizzazione a tre livelli; dettaglia i requisiti di documentazione e approvazione.

**ISMS-POL-A.5.31.3: Quadro di estrazione dei requisiti e mappatura dei controlli** — definisce la metodologia per analizzare il testo normativo in requisiti azionabili; stabilisce l'approccio di categorizzazione dei requisiti; specifica la metodologia di mappatura dei controlli; definisce l'approccio all'analisi e alla prioritizzazione delle lacune; stabilisce i requisiti di tracciabilità.

**ISMS-POL-A.5.31.4: Quadro di gestione dei cambiamenti e delle prove** — definisce le fonti di monitoraggio normativo e la frequenza; stabilisce il processo di valutazione dell'impatto per i cambiamenti normativi; specifica le procedure di aggiornamento del quadro; definisce il quadro di gestione delle prove; specifica i requisiti di conservazione dei documenti.

## Livello 2: Guide all'implementazione (cinque sezioni di implementazione)

**ISMS-IMP-A.5.31.1–5**: Guida passo-passo per l'identificazione delle normative, l'estrazione dei requisiti, la mappatura dei controlli, il monitoraggio normativo e la gestione delle prove.

## Livello 3: Strumenti di valutazione (sei classeur e cruscotto)

Sei classeur Excel generati tramite script Python di automazione: Classeur 1 (Inventario normativo); Classeur 2 (Matrice di applicabilità); Classeur 3 (Registro dei requisiti); Classeur 4 (Matrice di mappatura dei controlli); Classeur 5 (Registro delle prove); Cruscotto (Panoramica della conformità normativa).

## Livello 4: Prove di conformità

Le prove tangibili che dimostrano la conformità: documenti di politica con firme di approvazione; documenti di procedura; configurazioni di sistema; log di sicurezza e report di monitoraggio; risultati di test e validazione; documenti di formazione; report di audit; documenti di risposta agli incidenti; certificazioni e attestazioni.

## Flusso del ciclo di vita del quadro

**Fase 1: Configurazione iniziale** (una tantum): Identificare le normative inizialmente applicabili; popolare ISMS-POL-00; estrarre i requisiti; mappare ai controlli; identificare le lacune iniziali; stabilire l'infrastruttura di monitoraggio.

**Fase 2: Operazione a regime** (continuativa): Monitorare il panorama normativo; raccogliere e mantenere le prove di conformità; condurre revisioni periodiche; riferire regolarmente lo stato della conformità.

**Fase 3: Gestione dei cambiamenti** (quando necessario): Rilevare i cambiamenti normativi; valutare l'impatto; aggiornare i requisiti e le mappature; implementare le modifiche ai controlli; aggiornare le prove.

---

# Prove per questa politica

**Prove per la Fase 1** (Revisione della documentazione): Documento di politica con firme di approvazione; metodologia di applicabilità normativa definita (ISMS-POL-A.5.31.2); quadro di estrazione dei requisiti documentato (ISMS-POL-A.5.31.3); quadro di gestione dei cambiamenti e delle prove specificato (ISMS-POL-A.5.31.4); tassonomia normativa a tre livelli stabilita (ISMS-POL-00 Sezione 3); ciclo di vita della conformità normativa definito; ruoli e responsabilità assegnati; governance e procedure di revisione definiti; punti di integrazione del consulente legale specificati.

**Prove per la Fase 2** (Efficacia operativa): Inventario normativo (classeur di valutazione ISMS-IMP-A.5.31.1); Matrice di applicabilità (classeur di valutazione ISMS-IMP-A.5.31.2); documenti di revisione del consulente legale per le determinazioni di Livello 1; ISMS-POL-00 Sezione 8 con motivazione dettagliata dell'applicabilità; Registro dei requisiti (classeur di valutazione ISMS-IMP-A.5.31.3); Matrice di mappatura dei controlli (classeur di valutazione ISMS-IMP-A.5.31.4); Registro delle lacune; Registro dei cambiamenti normativi; registrazioni del coinvolgimento del consulente legale; report di stato della conformità alla direzione generale.

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Valutazione dell'applicabilità** | Valutazione sistematica se una normativa specifica si applica a [Organizzazione] in base a criteri geografici, operativi e contrattuali |
| **Controllo** | Misura di sicurezza implementata per ridurre il rischio per la sicurezza delle informazioni (per ISO 27001) |
| **Mappatura dei controlli** | Processo di collegamento dei requisiti normativi a specifici controlli ISO 27001 che soddisfano tali requisiti |
| **Prova** | Artefatti tangibili (documenti, log, report, configurazioni, ecc.) che dimostrano l'implementazione e il funzionamento dei controlli |
| **Lacuna** | Requisito normativo per il quale non esiste alcun controllo o i controlli esistenti sono inadeguati |
| **SGSI** | Sistema di Gestione della Sicurezza delle Informazioni (per ISO 27001) |
| **Requisito normativo** | Obbligo specifico estratto da una normativa che impone un particolare controllo, processo o risultato |
| **Normativa** | Disposizione legale, normativa o contrattuale pertinente alla sicurezza delle informazioni |
| **Tracciabilità** | Capacità di tracciare dalla normativa attraverso i requisiti e i controlli fino alle prove, e viceversa |
| **Livello 1 (Conformità obbligatoria)** | Normative giuridicamente vincolanti o eseguibili contrattualmente per [Organizzazione] |
| **Livello 2 (Applicabilità condizionale)** | Normative che possono diventare applicabili o che vengono adottate volontariamente |
| **Livello 3 (Riferimento informativo)** | Quadri utilizzati per orientamento e benchmarking senza obbligo di conformità |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data] |
| **Consulente legale** | [Nome] | [Data] |
| **Responsabile del SGSI** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questo documento stabilisce il fondamento del quadro di conformità normativa di [Organizzazione] che implementa il Controllo A.5.31 della norma ISO 27001:2022. Le successive sezioni della politica (5.31.2, 5.31.3, 5.31.4) forniscono metodologia e processi dettagliati.*

<!-- QA_VERIFIED: 2026-04-03 -->
