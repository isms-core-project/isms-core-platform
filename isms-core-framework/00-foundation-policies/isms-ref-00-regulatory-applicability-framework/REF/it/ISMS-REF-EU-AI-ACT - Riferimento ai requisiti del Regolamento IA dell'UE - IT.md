<!-- ISMS-CORE:REF:ISMS-REF-EU-AI-ACT-IT-artificial-intelligence-act:framework:REF:eu-ai-act -->
**ISMS-REF-EU-AI-ACT — Riferimento ai requisiti del Regolamento sull'IA dell'UE**
**Requisiti di gestione del rischio e conformità per i sistemi di IA dell'UE (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento ai requisiti del Regolamento sull'IA dell'UE |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-REF-EU-AI-ACT |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | RSSI (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Semestrale (l'attuazione del Regolamento IA è in rapida evoluzione)
**Distribuzione**: Team di sviluppo IA/ML, Gestione prodotti, Legale, RSSI, RPD

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione.

- Questo documento NON fa parte del SGSI.
- Questo documento NON definisce requisiti obbligatori a meno che [Organizzazione] non sviluppi o utilizzi sistemi di IA che incidono su persone nell'UE.
- Questo documento NON sostituisce né estende alcuna politica SGSI.

**Determinazione dell'applicabilità**: Il Regolamento sull'IA dell'UE si applica SOLO SE [Organizzazione] è un fornitore (sviluppa o immette sistemi di IA sul mercato dell'UE), un utilizzatore (usa sistemi di IA sotto propria responsabilità nell'UE), un importatore o distributore di sistemi di IA nell'UE, oppure sviluppa/utilizza sistemi di IA i cui output incidono su persone nell'UE (applicazione extraterritoriale).

---

# Panoramica e applicabilità del Regolamento sull'IA dell'UE

## Cos'è il Regolamento sull'IA dell'UE?

Il **Regolamento (UE) 2024/1689** recante norme armonizzate sull'intelligenza artificiale (Regolamento sull'IA).

**Date chiave**:
- **Adozione**: 21 maggio 2024 (Parlamento europeo)
- **Entrata in vigore**: 1° agosto 2024
- **Attuazione graduale**: 2025-2027

**Scopo**: Stabilire norme armonizzate per lo sviluppo e l'utilizzo dell'IA nell'UE; approccio normativo basato sul rischio (proporzionato); proteggere i diritti fondamentali, la salute, la sicurezza e la democrazia; promuovere l'innovazione IA affidabile.

**Base giuridica**: Regolamento UE (direttamente applicabile in tutti gli Stati membri, nessuna trasposizione nazionale richiesta).

**Applicazione extraterritoriale**: Si applica a fornitori/utilizzatori al di fuori dell'UE se i sistemi di IA incidono su persone nell'UE.

## Definizioni chiave

**Sistema di IA** (Articolo 3(1)): Un sistema basato su macchine, progettato per operare con vari livelli di autonomia e che può mostrare adattabilità dopo il dispiegamento, che, per obiettivi espliciti o impliciti, deduce, dagli input ricevuti, come generare output quali previsioni, contenuti, raccomandazioni o decisioni che possono influenzare ambienti fisici o virtuali.

**Fornitore** (Articolo 3(3)): Persona fisica o giuridica, autorità pubblica, agenzia o altro organismo che sviluppa o fa sviluppare un sistema di IA o un modello di IA di uso generale e lo immette sul mercato o lo mette in servizio con il proprio nome o marchio.

**Utilizzatore** (Articolo 3(4)): Persona fisica o giuridica, autorità pubblica, agenzia o altro organismo che utilizza un sistema di IA sotto la propria responsabilità.

**Modello di IA di uso generale (GPAI)** (Articolo 3(44)): Un modello di IA che mostra significativa generalità ed è in grado di svolgere in modo competente un'ampia gamma di compiti distinti, indipendentemente dal modo in cui viene immesso sul mercato.

## Classificazione basata sul rischio

Il Regolamento sull'IA utilizza una **piramide del rischio a quattro livelli**:

```
                ┌─────────────────────┐
                │   INACCETTABILE     │
                │     VIETATO         │ ← Articolo 5
                └─────────────────────┘
                
           ┌─────────────────────────────┐
           │        AD ALTO RISCHIO      │ ← Allegato III + Art. 6
           │   (Requisiti severi)        │
           └─────────────────────────────┘
           
      ┌──────────────────────────────────────┐
      │          RISCHIO LIMITATO            │ ← Articolo 50
      │   (Obblighi di trasparenza)          │
      └──────────────────────────────────────┘
      
 ┌───────────────────────────────────────────────┐
 │              RISCHIO MINIMO                   │
 │    (Nessun obbligo — Codici volontari)        │
 └───────────────────────────────────────────────┘
```

## Calendario di attuazione graduale

| Categoria di requisiti | Data di applicazione | Stato |
|------------------------|---------------------|-------|
| **Pratiche di IA vietate** (Articolo 5) | 2 febbraio 2025 | 6 mesi dopo l'entrata in vigore |
| **Modelli di IA di uso generale** (Capitolo V) | 2 agosto 2025 | 12 mesi |
| **Sistemi di IA ad alto rischio** (Capitolo III, Sezione 2) | 2 agosto 2026 | 24 mesi |
| **IA ad alto rischio in prodotti regolamentati** | 2 agosto 2027 | 36 mesi |

**Periodo transitorio per i sistemi esistenti**: I sistemi di IA già immessi sul mercato o messi in servizio prima del 2 agosto 2026 possono continuare ad essere utilizzati fino al 2 agosto 2030 senza conformità (salvo modifiche sostanziali).

---

# Pratiche di IA inaccettabili (Articolo 5) — VIETATE

## Panoramica

**Data di applicazione**: 2 febbraio 2025
**Sanzione per violazione**: Fino a 35.000.000 € o 7% del fatturato mondiale annuo (il maggiore dei due)

## Pratiche vietate

| Pratica vietata | Descrizione |
|-----------------|-------------|
| **Art. 5(1)(a)** — Manipolazione subliminale | Sistemi di IA che utilizzano tecniche subliminali al di là della consapevolezza della persona per distorcerne il comportamento causando o rischiando di causare danni significativi |
| **Art. 5(1)(b)** — Sfruttamento delle vulnerabilità | Sistemi che sfruttano le vulnerabilità di gruppi specifici (età, disabilità, situazione socioeconomica) per distorcere il comportamento |
| **Art. 5(1)(c)** — Assegnazione di punteggi sociali | Sistemi che valutano o classificano persone fisiche in base al comportamento sociale portando a trattamenti discriminatori |
| **Art. 5(1)(d)** — Valutazione del rischio di recidiva | Sistemi che valutano il rischio di commissione di reati basandosi esclusivamente sulla profilazione o su tratti della personalità |
| **Art. 5(1)(e)** — Raccolta massiva di immagini facciali | Raccolta non mirata di immagini facciali da internet o CCTV per creare database di riconoscimento facciale |
| **Art. 5(1)(f)** — Riconoscimento delle emozioni sul lavoro/in ambito educativo | Sistemi per il riconoscimento delle emozioni in ambienti lavorativi o educativi (eccezione: ragioni mediche o di sicurezza) |
| **Art. 5(1)(g)** — Categorizzazione biometrica per attributi sensibili | Sistemi di categorizzazione biometrica che deducono attributi sensibili (razza, opinioni politiche, orientamento sessuale, ecc.) |
| **Art. 5(1)(h)** — Identificazione biometrica remota in tempo reale in spazi pubblici | Uso da parte delle forze dell'ordine di sistemi RBI in tempo reale in spazi accessibili al pubblico (con eccezioni limitate) |

## Requisiti di conformità per tutte le organizzazioni

1. **Inventariare i sistemi di IA**: Identificare tutti i sistemi di IA in sviluppo o utilizzo
2. **Valutazione dell'Articolo 5**: Verificare se i sistemi rientrano nelle pratiche vietate
3. **Cessazione immediata**: Interrompere sviluppo/utilizzo di IA vietata entro il 2 febbraio 2025
4. **Documentazione**: Documentare la valutazione e le decisioni
5. **Formazione**: Garantire che i team di sviluppo/acquisto siano consapevoli dei divieti

---

# Sistemi di IA ad alto rischio (Capitolo III, Sezione 2)

## Categorie di sistemi di IA ad alto rischio (Allegato III)

| Categoria | Casi d'uso |
|-----------|------------|
| **1. Identificazione e categorizzazione biometrica** | Identificazione biometrica remota, categorizzazione biometrica (attributi sensibili), riconoscimento delle emozioni |
| **2. Infrastrutture critiche** | Gestione e funzionamento di infrastrutture digitali critiche, traffico stradale, acqua, gas, riscaldamento, elettricità |
| **3. Istruzione e formazione professionale** | Determinazione dell'accesso/ammissione, valutazione degli studenti, rilevamento di imbroglio agli esami |
| **4. Occupazione** | Reclutamento, selezione, valutazione, promozione, allocazione delle attività, monitoraggio delle performance, risoluzione del rapporto |
| **5. Servizi privati/pubblici essenziali** | Scoring creditizio, valutazione dell'ammissibilità ad assistenza pubblica, prioritizzazione dei servizi di emergenza |
| **6. Attività di polizia** | Valutazione del rischio individuale (vittime, autori di reato, recidiva), poligrafi, rilevamento di deepfake, valutazione delle prove |
| **7. Migrazione, asilo e controllo delle frontiere** | Esame delle domande, rilevamento di documenti fraudolenti, valutazione dei rischi, poligrafo |
| **8. Amministrazione della giustizia e processi democratici** | Assistenza alle autorità giudiziarie in ricerca/interpretazione legale, influenza sui risultati elettorali |

## Obblighi del fornitore per i sistemi di IA ad alto rischio

**Articolo 9: Sistema di gestione del rischio**

Requisiti: Istituire, attuare, documentare e mantenere un sistema di gestione del rischio; processo iterativo e continuo per tutto il ciclo di vita; aggiornamenti sistematici regolari.

**Processo di gestione del rischio**: (1) Identificazione e analisi dei rischi noti e ragionevolmente prevedibili; (2) Stima e valutazione dei rischi nell'uso previsto e nell'uso improprio ragionevolmente prevedibile; (3) Valutazione di altri rischi basata sui dati di monitoraggio post-mercato; (4) Adozione di misure appropriate di gestione del rischio.

**Mappatura ISO 27001:2022**: Clausole 6.1.2; 6.1.3; A.5.7 | Standard specifico per l'IA: ISO/IEC 23894:2023

---

**Articolo 10: Dati e governance dei dati**

I dataset di addestramento, validazione e test devono soddisfare criteri di qualità: pertinenti, sufficientemente rappresentativi, privi di errori, completi ai fini previsti, con proprietà statistiche appropriate.

**Pratiche di governance dei dati**: Scelte di progettazione; processi di raccolta dei dati; operazioni di preparazione (annotazione, etichettatura, pulizia, arricchimento, aggregazione); valutazione dei bias dei dati e misure di mitigazione appropriate; identificazione delle lacune nei dati.

**Mappatura ISO 27001:2022**: A.5.12; A.5.13; A.5.14; A.8.11; Articolo 5(1)(d) RGPD

---

**Articolo 11: Documentazione tecnica**

Requisiti: Redigere la documentazione tecnica prima dell'immissione sul mercato; tenerla aggiornata; renderla disponibile alle autorità nazionali competenti su richiesta.

**Contenuto della documentazione tecnica** (Allegato IV): Descrizione generale del sistema di IA; descrizione dettagliata degli elementi e del processo di sviluppo; informazioni sul monitoraggio e controllo; descrizione del sistema di gestione del rischio; conformità ai requisiti ad alto rischio; procedura di valutazione della conformità; copia della dichiarazione di conformità UE.

**Mappatura ISO 27001:2022**: A.5.37; Clausola 7.5

---

**Articolo 12: Tenuta dei registri (registrazione)**

Requisiti: Registri generati automaticamente per tutto il ciclo di vita del sistema di IA; abilitare la **tracciabilità** del funzionamento del sistema; appropriati all'uso previsto e al livello di rischio.

**Requisiti di registrazione**: Timestamp di ogni evento; dati di input (database/file che causano l'azione); persone fisiche coinvolte (identificazione dove tecnicamente fattibile).

**Mappatura ISO 27001:2022**: A.8.15; A.8.16

---

**Articolo 13: Trasparenza e informazioni agli utilizzatori**

Requisiti: Progettare il sistema di IA per la trasparenza permettendo agli utilizzatori di interpretare l'output del sistema e usarlo in modo appropriato.

**Istruzioni per l'uso** (Allegato IV, Sezione 2): Identità e dati di contatto del fornitore; caratteristiche, capacità e limiti di prestazione; modifiche al sistema; misure di supervisione umana; risorse computazionali e hardware necessarie.

**Mappatura ISO 27001:2022**: A.5.37

---

**Articolo 14: Supervisione umana**

Requisiti: Progettare il sistema di IA per consentire un'efficace **supervisione da parte di persone fisiche**; prevenire o ridurre al minimo i rischi per salute, sicurezza, diritti fondamentali.

**Misure di supervisione umana**: Capacità di comprendere le capacità e i limiti del sistema di IA; consapevolezza della tendenza ai bias da automazione; capacità di interpretare correttamente l'output; facoltà di non utilizzare o ignorare l'output; possibilità di intervenire o interrompere il funzionamento del sistema (pulsante di arresto).

**Mappatura ISO 27001:2022**: A.5.37; A.6.3

---

**Articolo 15: Accuratezza, robustezza e sicurezza informatica**

Requisiti:
- **Accuratezza**: Livello appropriato per tutto il ciclo di vita
- **Robustezza**: Misure tecniche e di sicurezza informatica appropriate ai rischi
- **Resilienza**: Contro i tentativi di terzi di alterare l'uso/le prestazioni

**Misure di robustezza**: Soluzioni tecniche contro attacchi avversariali; attacchi di avvelenamento del modello (model poisoning); attacchi di avvelenamento dei dati (data poisoning); attacchi alla privacy (inversione del modello, inferenza di appartenenza).

**Mappatura ISO 27001:2022**: A.8.7; A.8.8; A.8.16; A.8.24

---

**Articolo 16: Sistema di gestione della qualità**

Requisiti: Istituire un sistema di gestione della qualità che garantisca la conformità al Regolamento sull'IA; attuazione degli Articoli 9-15; monitoraggio post-mercato (Articolo 72).

**Contenuto del sistema di gestione della qualità**: Strategia per la conformità normativa; tecniche, procedure e azioni sistematiche per progettazione, verifica, validazione, test; sistemi e procedure di gestione dei dati; sistema di gestione del rischio; sistema di monitoraggio post-mercato; quadro di responsabilità (ruoli e responsabilità).

**Mappatura ISO 27001:2022**: Clausole 4-10 (intero SGSI); complementare: ISO 9001:2015

---

**Articoli 43-51: Valutazione della conformità**

**Prima dell'immissione sul mercato** di un sistema di IA ad alto rischio, il fornitore deve effettuare una valutazione della conformità.

**Opzioni di valutazione**:
- **Opzione 1**: Controllo interno (Articolo 43 + Allegato VI) — valutazione propria del fornitore
- **Opzione 2**: Valutazione da parte di un organismo notificato (Articolo 43 + Allegato VII) — richiesta per identificazione biometrica/categorizzazione (Allegato III(1))

**Processo**: Preparazione della documentazione tecnica → Attuazione del sistema di gestione della qualità e del rischio → Valutazione interna o di terzi → Dichiarazione di conformità UE (Allegato V) → Apposizione della marcatura CE.

**Marcatura CE** (Articolo 48): I sistemi di IA ad alto rischio recano la marcatura CE; indica la conformità al Regolamento sull'IA.

---

**Articolo 72: Monitoraggio post-mercato**

Requisiti: Istituire e documentare un sistema di monitoraggio post-mercato; raccogliere, documentare e analizzare i dati sulle prestazioni per tutto il ciclo di vita.

**Mappatura ISO 27001:2022**: Clausola 9.1; A.8.16

## Obblighi dell'utilizzatore per i sistemi di IA ad alto rischio (Articolo 26)

Gli utilizzatori devono: usare il sistema in conformità alle istruzioni; assegnare la supervisione umana a persone fisiche competenti; monitorare il funzionamento; sospendere l'uso in caso di incidente grave; conservare i registri generati automaticamente; usare dati di input pertinenti e rappresentativi; condurre una valutazione dell'impatto sui diritti fondamentali (VDRF) — Articolo 27 — per determinati settori/usi.

---

# Sistemi di IA a rischio limitato (Articolo 50) — Obblighi di trasparenza

**Data di applicazione**: 2 agosto 2026
**Sanzione**: Fino a 7.500.000 € o 1,5% del fatturato mondiale annuo

| Requisito | Descrizione |
|-----------|-------------|
| **Art. 50(1)** — Sistemi che interagiscono con persone fisiche | Informare le persone fisiche che stanno interagendo con un sistema di IA (es. chatbot) |
| **Art. 50(2)** — Riconoscimento delle emozioni / categorizzazione biometrica | Informare le persone fisiche esposte al sistema |
| **Art. 50(3)** — Contenuti generati dall'IA (deepfake) | Rendere noto che il contenuto è stato generato o manipolato artificialmente |
| **Art. 50(4)** — Testo generato dall'IA | Rendere noto che gli output sono stati generati artificialmente (per sistemi che producono testo a fini di informazione pubblica) |

---

# Modelli di IA di uso generale (GPAI) — Capitolo V

**Esempi**: Modelli linguistici di grandi dimensioni (GPT-4, Claude, Gemini, LLaMA); modelli multimodali; modelli di generazione di immagini (DALL-E, Stable Diffusion).

**Data di applicazione**: 2 agosto 2025

## Obblighi dei fornitori di GPAI (Articolo 53)

Tutti i fornitori di GPAI devono:

1. **Documentazione tecnica** (Articolo 53(1)(a) + Allegato XI): Descrizione generale del modello (capacità, limitazioni); dati usati per l'addestramento; risorse computazionali; risultati della valutazione
2. **Informazioni per i fornitori a valle** (Articolo 53(1)(b)): Documentazione per consentire ai fornitori a valle di conformarsi al Regolamento sull'IA
3. **Politica sul diritto d'autore** (Articolo 53(1)(c)): Politica disponibile pubblicamente per il rispetto della Direttiva (UE) 2019/790
4. **Trasparenza** (Articolo 53(1)(d)): Sintesi accessibile al pubblico del contenuto usato per l'addestramento

## Modelli GPAI con rischio sistemico — Obblighi aggiuntivi (Articolo 54)

**Rischio sistemico** se: potenziale d'impatto elevato (valutato secondo le migliori pratiche) OPPURE quantità cumulativa di calcolo usata per l'addestramento ≥ 10^25 FLOPs.

**Obblighi aggiuntivi**:
- **Art. 54(1)(a)**: Valutazione del modello / red teaming per rischi sistemici
- **Art. 54(1)(b)**: Tracciamento, documentazione e segnalazione degli incidenti gravi all'Ufficio per l'IA dell'UE
- **Art. 54(1)(c)**: Garantire un adeguato livello di protezione della sicurezza informatica (protezione dei pesi del modello)
- **Art. 54(1)(d)**: Segnalare il consumo energetico durante l'addestramento

**Sanzione**: Fino a 15.000.000 € o 3% del fatturato mondiale annuo

---

# Requisiti organizzativi e governance

## Alfabetizzazione all'IA (Articolo 4)

I fornitori e gli utilizzatori devono garantire che il personale che gestisce i sistemi di IA abbia un livello sufficiente di alfabetizzazione all'IA.

**Attuazione**: Programmi di formazione per gli utenti dei sistemi di IA; formazione per ruolo (sviluppatori, utilizzatori, personale di supervisione); consapevolezza dei bias, dell'etica e dei diritti fondamentali.

**Mappatura ISO 27001:2022**: A.6.3

## Struttura di governance consigliata

| Ruolo | Responsabilità |
|-------|---------------|
| **Comitato di governance dell'IA** | Supervisione strategica dell'IA, approvazione delle politiche, propensione al rischio |
| **Chief AI Officer (CAIO)** | Leadership del programma IA, coordinamento della conformità |
| **RSSI** | Aspetti di sicurezza informatica dei sistemi di IA (Articolo 15) |
| **RPD (RPD)** | Conformità al RGPD per l'elaborazione IA di dati personali |
| **Legale/Conformità** | Conformità al Regolamento sull'IA, valutazioni del rischio, segnalazione esterna |
| **Proprietari del prodotto** | Responsabili di specifici sistemi di IA |
| **Team di sviluppo IA** | Attuazione dei requisiti tecnici (Articoli 9-15) |
| **Personale di supervisione umana** | Assegnato per Articolo 14 per i sistemi ad alto rischio |

## Inventario dei sistemi di IA

Mantenere un inventario di tutti i sistemi di IA sviluppati o utilizzati con: nome e versione del sistema, fornitore, scopo previsto, classificazione del rischio, stato di dispiegamento, obblighi normativi, responsabilità dell'utilizzatore assegnate.

**Mappatura ISO 27001:2022**: A.5.9

---

# Mappatura ISO 27001:2022 — Regolamento sull'IA dell'UE

## Matrice di mappatura dei controlli

| Requisito del Regolamento sull'IA | Articolo | Controllo ISO 27001:2022 | Lacuna |
|-----------------------------------|----------|--------------------------|--------|
| Valutazione delle pratiche vietate | Art. 5 | A.5.1; A.5.31 | Specifico del Regolamento sull'IA |
| Sistema di gestione del rischio | Art. 9 | Clausole 6.1.2-6.1.3 | Regolamento sull'IA: processo di rischio specifico per l'IA |
| Governance dei dati | Art. 10 | A.5.12-5.14 | **Specifico del Regolamento sull'IA**: qualità dei dati, mitigazione del bias |
| Documentazione tecnica | Art. 11 | A.5.37; Clausola 7.5 | Regolamento sull'IA: documentazione estesa del sistema di IA |
| Registrazione | Art. 12 | A.8.15-8.16 | Allineato |
| Trasparenza agli utilizzatori | Art. 13 | A.5.37 | Regolamento sull'IA: istruzioni per l'uso dettagliate |
| Supervisione umana | Art. 14 | A.5.37 | **Specifico del Regolamento sull'IA**: requisiti human-in-the-loop |
| Accuratezza, robustezza, sicurezza | Art. 15 | A.8.7-8.8; A.8.16 | Regolamento sull'IA: protezione contro attacchi avversariali |
| Sistema di gestione della qualità | Art. 16 | Clausole 4-10 | Complementare: ISO 9001 + ISO 27001 |
| Valutazione della conformità | Art. 43-51 | Clausole 9.2-9.3 | **Specifico del Regolamento sull'IA**: marcatura CE, organismi notificati |
| Monitoraggio post-mercato | Art. 72 | Clausola 9.1; A.8.16 | Regolamento sull'IA: monitoraggio continuo in uso reale |
| Obblighi dell'utilizzatore | Art. 26 | A.5.37 | Regolamento sull'IA: responsabilità specifiche dell'utilizzatore |
| Trasparenza (rischio limitato) | Art. 50 | A.5.1 | **Specifico del Regolamento sull'IA**: requisiti di comunicazione all'utente |
| Alfabetizzazione all'IA | Art. 4 | A.6.3 | Regolamento sull'IA: formazione specifica per l'IA |

## Lacune principali tra ISO 27001:2022 e il Regolamento sull'IA dell'UE

1. **Valutazione del rischio specifica per l'IA**: ISO 27001 — valutazione generale; Regolamento sull'IA — gestione dettagliata del rischio per l'IA (bias, discriminazione, sicurezza, diritti fondamentali)
2. **Governance dei dati per l'IA**: ISO 27001 — classificazione e protezione; Regolamento sull'IA — qualità, rappresentatività, mitigazione del bias dei dati di addestramento
3. **Requisiti di supervisione umana**: ISO 27001 — nessun requisito specifico; Regolamento sull'IA — supervisione umana obbligatoria per l'IA ad alto rischio (Articolo 14)
4. **Valutazione della conformità e marcatura CE**: ISO 27001 — certificazione; Regolamento sull'IA — valutazione della conformità, marcatura CE
5. **Trasparenza e spiegabilità**: ISO 27001 — nessun requisito di spiegabilità; Regolamento sull'IA — trasparenza agli utilizzatori e agli utenti finali
6. **Impatto sui diritti fondamentali**: ISO 27001 — nessuna valutazione dei diritti fondamentali; Regolamento sull'IA — VDRF per determinati utilizzatori (Articolo 27)

**Standard complementari da considerare**: ISO/IEC 42001:2023 (Sistema di gestione dell'IA — AIMS); ISO/IEC 23894:2023 (Gestione del rischio per l'IA); ISO/IEC TR 24028:2020 (Panoramica dell'affidabilità nell'IA).

---

# Lista di controllo per l'auto-valutazione della conformità al Regolamento sull'IA

## Inventario dei sistemi di IA

| Domanda | Stato |
|---------|-------|
| Abbiamo identificato tutti i sistemi di IA in uso o in sviluppo? | ⬜ Sì ⬜ No ⬜ In corso |
| Abbiamo classificato il livello di rischio di ogni sistema? | ⬜ Sì ⬜ No ⬜ Parziale |
| Abbiamo determinato il ruolo fornitore/utilizzatore per ogni sistema? | ⬜ Sì ⬜ No ⬜ Parziale |
| Sviluppiamo o utilizziamo modelli GPAI? | ⬜ Sì ⬜ No ⬜ Incerto |

## Pratiche vietate (Articolo 5)

| Requisito | Stato |
|-----------|-------|
| Valutati tutti i sistemi di IA rispetto ai divieti dell'Articolo 5 | ⬜ Sì ⬜ No |
| Confermata assenza di IA di manipolazione subliminale | ⬜ Sì ⬜ No ⬜ N/A |
| Confermata assenza di IA per l'assegnazione di punteggi sociali | ⬜ Sì ⬜ No ⬜ N/A |
| Confermata assenza di RBI in tempo reale (salvo eccezioni forze dell'ordine) | ⬜ Sì ⬜ No ⬜ N/A |
| Confermata assenza di riconoscimento emozioni sul lavoro/in ambito educativo (salvo sicurezza/medicina) | ⬜ Sì ⬜ No ⬜ N/A |
| Valutazione dell'Articolo 5 documentata | ⬜ Sì ⬜ No |

## Sistemi di IA ad alto rischio — Obblighi del fornitore

| Requisito | Stato |
|-----------|-------|
| Sistema di gestione del rischio istituito (Articolo 9) | ⬜ Sì ⬜ No ⬜ N/A |
| Misure di governance e qualità dei dati (Articolo 10) | ⬜ Sì ⬜ No ⬜ N/A |
| Documentazione tecnica preparata (Articolo 11, Allegato IV) | ⬜ Sì ⬜ No ⬜ N/A |
| Registrazione automatica implementata (Articolo 12) | ⬜ Sì ⬜ No ⬜ N/A |
| Istruzioni per l'uso fornite (Articolo 13) | ⬜ Sì ⬜ No ⬜ N/A |
| Misure di supervisione umana progettate (Articolo 14) | ⬜ Sì ⬜ No ⬜ N/A |
| Accuratezza, robustezza, sicurezza informatica affrontate (Articolo 15) | ⬜ Sì ⬜ No ⬜ N/A |
| Sistema di gestione della qualità attuato (Articolo 16) | ⬜ Sì ⬜ No ⬜ N/A |
| Valutazione della conformità condotta | ⬜ Sì ⬜ No ⬜ Pianificato |
| Sistema di monitoraggio post-mercato istituito (Articolo 72) | ⬜ Sì ⬜ No ⬜ N/A |

## Sistemi di IA a rischio limitato (Articolo 50)

| Requisito | Stato |
|-----------|-------|
| Il chatbot/assistente virtuale divulga l'interazione con l'IA | ⬜ Sì ⬜ No ⬜ N/A |
| Il riconoscimento delle emozioni/categorizzazione biometrica informa gli utenti | ⬜ Sì ⬜ No ⬜ N/A |
| Il contenuto deepfake viene reso noto | ⬜ Sì ⬜ No ⬜ N/A |
| Il testo generato dall'IA viene reso noto | ⬜ Sì ⬜ No ⬜ N/A |

## Modelli GPAI

| Requisito | Stato |
|-----------|-------|
| Documentazione tecnica preparata (Articolo 53, Allegato XI) | ⬜ Sì ⬜ No ⬜ N/A |
| Politica sul diritto d'autore documentata (Articolo 53(1)(c)) | ⬜ Sì ⬜ No ⬜ N/A |
| Sintesi del contenuto di addestramento pubblicata (Articolo 53(1)(d)) | ⬜ Sì ⬜ No ⬜ N/A |
| Valutato il rischio sistemico (≥ 10^25 FLOPs o altri criteri) | ⬜ Sì ⬜ No ⬜ N/A |
| **Se rischio sistemico**: Red teaming / valutazione del modello (Art. 54(1)(a)) | ⬜ Sì ⬜ No ⬜ N/A |
| **Se rischio sistemico**: Tracciamento degli incidenti gravi (Art. 54(1)(b)) | ⬜ Sì ⬜ No ⬜ N/A |
| **Se rischio sistemico**: Sicurezza informatica / protezione del modello (Art. 54(1)(c)) | ⬜ Sì ⬜ No ⬜ N/A |

## Requisiti organizzativi

| Requisito | Stato |
|-----------|-------|
| Struttura di governance dell'IA istituita | ⬜ Sì ⬜ No ⬜ In corso |
| Formazione sull'alfabetizzazione all'IA per il personale (Articolo 4) | ⬜ Sì ⬜ No ⬜ Pianificato |
| Inventario dei sistemi di IA mantenuto | ⬜ Sì ⬜ No ⬜ In corso |
| Ruoli e responsabilità assegnati | ⬜ Sì ⬜ No ⬜ Parziale |

---

**FINE DEL DOCUMENTO DI RIFERIMENTO TECNICO**

*Questo riferimento tecnico supporta i potenziali requisiti di conformità al Regolamento sull'IA dell'UE come determinato in ISMS-POL-00.*

*Per le organizzazioni che NON sviluppano o utilizzano sistemi di IA che incidono su persone nell'UE, questo documento è solo a scopo informativo e NON crea obblighi di conformità.*

<!-- QA_VERIFIED: 2026-04-03 -->
