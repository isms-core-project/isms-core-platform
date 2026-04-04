<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-IT:framework:POL:a.5.19-23 -->
**ISMS-POL-A.5.19-23 — Sicurezza dei fornitori e dei servizi cloud**
**Quadro di politica e implementazione completo**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza dei fornitori e dei servizi cloud |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.19-23 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Catena di approvazione**: RSSI → DSI → Responsabile Legale/Conformità → Direttore Acquisti → Direzione generale

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.5.19-23-S1 through S6; ISMS-IMP-A.5.19-23.S1-S4-UG/TG; ISMS-REF-A.5.23; ISO/IEC 27001:2022 Controlli A.5.19-23; ISO/IEC 27036; ISO/IEC 27017; ISO/IEC 27018

**Distribuzione**: Tutti i dipendenti, appaltatori, team acquisti, team legale, operazioni IT, amministratori cloud

---

## Riepilogo esecutivo

Il presente documento costituisce l'**indice principale** del quadro di sicurezza dei fornitori e dei servizi cloud di [Organizzazione], implementando i controlli ISO/IEC 27001:2022 da A.5.19 ad A.5.23.

**Scopo**: Stabilire requisiti obbligatori per gestire i rischi di sicurezza delle informazioni associati a fornitori esterni, impegni contrattuali, dipendenze della catena di approvvigionamento TIC, gestione continua delle relazioni con i fornitori e ciclo di vita dei servizi cloud.

**Perimetro**: Tutte le relazioni con i fornitori che comportano accesso a informazioni o sistemi organizzativi; tutti i servizi cloud (IaaS, PaaS, SaaS, servizi di sicurezza); tutti gli accordi contrattuali con fornitori di servizi esterni; tutti i prodotti TIC con dipendenze della catena di approvvigionamento.

**Principio critico**: «La fiducia nei fornitori deve essere verificata, non presunta». Questo quadro richiede la validazione basata su prove della postura di sicurezza dei fornitori tramite due diligence sistematica, impegni contrattuali con clausole eseguibili e monitoraggio continuo durante tutto il ciclo di vita della relazione.

**Componenti del quadro**:

- **Livello politica**: Documenti di governance che definiscono i requisiti (7 documenti di politica)
- **Livello di valutazione**: Specifiche di valutazione tecnica (documentazione markdown)
- **Livello di implementazione**: Classeur Excel generati da Python (4 classeur di valutazione)
- **Livello di validazione**: Script di quality assurance e normalizzazione
- **Livello di integrazione**: Cruscotti riepilogativi dei classeur individuali

**Allineamento normativo**: Questa politica risponde ai requisiti di conformità obbligatori indicati in ISMS-POL-00, inclusi: nLPD svizzera; RGPD dell'UE (art. 28 — accordi con i responsabili del trattamento); ISO/IEC 27001:2022; DORA (registro dei rischi TIC di terzi, valutazione del rischio di concentrazione, strategie di uscita ai sensi degli artt. 28-31); NIS2 (misure di sicurezza della catena di approvvigionamento, notifica degli incidenti entro 24 ore ai sensi degli artt. 21-23); Legge europea sull'IA; considerazioni giurisdizionali del CLOUD Act statunitense.

---

## Allineamento sui controlli

### A.5.19 — Sicurezza delle informazioni nelle relazioni con i fornitori

> *Devono essere definiti e concordati con i fornitori processi e procedure per gestire i rischi di sicurezza delle informazioni associati all'uso dei prodotti o servizi del fornitore.*

**Riferimento politica**: ISMS-POL-A.5.19-23-S1 (Fondamentali delle relazioni con i fornitori)

### A.5.20 — Considerazione della sicurezza nelle relazioni con i fornitori

> *Requisiti pertinenti di sicurezza devono essere stabiliti e concordati con ciascun fornitore che può accedere, elaborare, archiviare, comunicare o fornire componenti di infrastruttura IT per le informazioni dell'organizzazione.*

**Riferimento politica**: ISMS-POL-A.5.19-23-S2 (Requisiti degli accordi con i fornitori)

### A.5.21 — Gestione della sicurezza nella catena di approvvigionamento TIC

> *Devono essere definiti e concordati con i fornitori processi e procedure per gestire i rischi di sicurezza delle informazioni associati alla catena di approvvigionamento di prodotti e servizi TIC.*

**Riferimento politica**: ISMS-POL-A.5.19-23-S3 (Sicurezza della catena di approvvigionamento TIC)

### A.5.22 — Monitoraggio, revisione e gestione dei cambiamenti dei servizi

> *L'organizzazione dovrebbe monitorare, rivedere, valutare e gestire regolarmente i cambiamenti nelle pratiche di sicurezza dei fornitori e nella consegna dei servizi.*

**Riferimento politica**: ISMS-POL-A.5.19-23-S4 (Monitoraggio dei fornitori e gestione dei cambiamenti)

### A.5.23 — Sicurezza delle informazioni per l'utilizzo dei servizi cloud

> *Devono essere stabiliti processi di acquisizione, utilizzo, gestione e uscita dai servizi cloud conformemente ai requisiti di sicurezza delle informazioni dell'organizzazione.*

**Riferimento politica**: ISMS-POL-A.5.19-23-S5 (Sicurezza dei servizi cloud)

---

## Struttura del quadro

### Architettura a cinque livelli

```
┌─────────────────────────────────────────────────────────────────┐
│ LIVELLO 1: POLITICA (7 documenti)                               │
│ ISMS-POL-A.5.19-23 (questo documento — indice principale)       │
│ ISMS-POL-A.5.19-23-S1: Fondamentali delle relazioni            │
│ ISMS-POL-A.5.19-23-S2: Requisiti degli accordi                 │
│ ISMS-POL-A.5.19-23-S3: Sicurezza della catena TIC              │
│ ISMS-POL-A.5.19-23-S4: Monitoraggio e gestione cambiamenti     │
│ ISMS-POL-A.5.19-23-S5: Sicurezza dei servizi cloud             │
│ ISMS-POL-A.5.19-23-S6: Metodologia di valutazione              │
├─────────────────────────────────────────────────────────────────┤
│ LIVELLO 2: SPECIFICHE DI VALUTAZIONE (Markdown)                 │
│ ISMS-IMP-A.5.19-23.S1: Inventario e classificazione            │
│ ISMS-IMP-A.5.19-23.S2: Due diligence fornitori                 │
│ ISMS-IMP-A.5.19-23.S3: Configurazione sicura                   │
│ ISMS-IMP-A.5.19-23.S4: Governance continua                     │
├─────────────────────────────────────────────────────────────────┤
│ LIVELLO 3: IMPLEMENTAZIONE (Script Python)                      │
│ generate_reg_a523_1_inventory.py                                │
│ generate_reg_a523_2_vendor_dd.py                                │
│ generate_reg_a523_3_secure_config.py                            │
│ generate_reg_a523_4_governance.py                               │
├─────────────────────────────────────────────────────────────────┤
│ LIVELLO 4: REVISIONE (Cruscotti integrati)                      │
│ Ogni classeur contiene la propria scheda Cruscotto              │
├─────────────────────────────────────────────────────────────────┤
│ LIVELLO 5: VALIDAZIONE (Approvazione e pista di audit)          │
│ Scheda di validazione in ogni classeur                          │
│ Registro delle prove per la tracciabilità                       │
└─────────────────────────────────────────────────────────────────┘
```

### Classeur di valutazione

| Classeur | Scopo | Parti interessate principali |
|---------|-------|------------------------------|
| **ISMS-IMP-A.5.19-23.S1** | Inventario e classificazione dei servizi cloud | Operazioni IT, Acquisti |
| **ISMS-IMP-A.5.19-23.S2** | Due diligence e contratti fornitori | Legale, Acquisti, Conformità |
| **ISMS-IMP-A.5.19-23.S3** | Configurazione e dispiegamento sicuri | Sicurezza IT, DevOps |
| **ISMS-IMP-A.5.19-23.S4** | Governance continua e gestione del rischio | Gestione del rischio, RSI |

---

## Requisiti del ciclo di vita dei fornitori

### Integrazione del ciclo di vita

```
SELEZIONE → INTEGRAZIONE → ESERCIZIO → USCITA
    │             │              │          │
 Due diligence  Contratto    Monitoraggio  Piano di
 Classif. S1   Clausole S2  Revisioni S4  uscita S5
 Valut. rischio Onboarding   Incidenti    Cancellaz.
                             Modifiche    dati
```

### Requisiti per fase

**Selezione**: Classificare il fornitore (S1 Livelli 1-4); eseguire la due diligence appropriata; completare la valutazione del rischio; ottenere l'approvazione necessaria.

**Integrazione**: Eseguire il contratto con le clausole di sicurezza richieste (S2); completare la lista di controllo di onboarding; configurare gli accessi con minimo privilegio; registrare nel registro dei fornitori.

**Esercizio**: Monitorare le performance e la conformità (S4); effettuare revisioni periodiche della sicurezza; gestire i cambiamenti tramite il processo formale; rispondere agli incidenti secondo le procedure.

**Uscita**: Eseguire la strategia di uscita pianificata (S5); garantire la restituzione/cancellazione dei dati con certificazione; revocare tutti gli accessi; archiviare la documentazione.

---

## Requisiti normativi specifici

### Registro dei rischi TIC di terzi (DORA)

Per le entità soggette a DORA, [Organizzazione] mantiene un registro dei rischi TIC di terzi contenente: tutti i fornitori di servizi TIC che supportano funzioni critiche o importanti; classificazione del rischio per fornitore; valutazione del rischio di concentrazione; revisione trimestrale e reporting normativo annuale.

### Sicurezza della catena di approvvigionamento (NIS2)

Per le entità coperte da NIS2, le misure di sicurezza della catena di approvvigionamento devono includere: politiche per l'acquisizione, lo sviluppo e la manutenzione dei sistemi TIC; requisiti di sicurezza per le relazioni con i fornitori; notifica degli incidenti che consenta la segnalazione normativa entro 24 ore.

### Accordi di trattamento dei dati (RGPD art. 28)

Tutti gli accordi con i responsabili del trattamento che elaborano dati personali devono soddisfare i requisiti dell'art. 28, inclusa la definizione dei ruoli di titolare/responsabile, misure tecniche e organizzative, requisiti sui sub-responsabili e diritti di audit.

---

## Struttura di governance

### Frequenza delle revisioni

| Livello fornitore | Valutazione sicurezza | Revisione performance | Revisione relazione |
|------------------|----------------------|-----------------------|---------------------|
| **Livello 1 (Critico)** | Annuale completa | SLA mensili | Governance trimestrale |
| **Livello 2 (Alto)** | Annuale standard | Trimestrale | Semestrale |
| **Livello 3 (Medio)** | Biennale | Semestrale | Annuale |
| **Livello 4 (Basso)** | Solo iniziale | Annuale | Al rinnovo |

### Metriche di governance del quadro

| Metrica | Obiettivo |
|---------|-----------|
| Copertura dell'inventario dei fornitori | 100% dei fornitori registrati |
| Completamento della due diligence (N1) | 100% prima dell'accesso |
| Completamento della revisione contrattuale (N1) | 100% dei contratti con clausole di sicurezza |
| Conformità al monitoraggio continuo | 100% secondo il calendario |
| Tasso di completamento delle valutazioni di sicurezza | 100% entro il ciclo annuale |
| Completamento dei test della strategia di uscita | 100% annuale per i servizi critici |

---

## Riferimenti a documenti correlati

| Sezione di politica | Controllo/i ISO | Riferimento documento |
|--------------------|-----------------|-----------------------|
| S1 – Fondamentali | A.5.19 | ISMS-POL-A.5.19-23-S1 |
| S2 – Accordi | A.5.20 | ISMS-POL-A.5.19-23-S2 |
| S3 – Catena TIC | A.5.21 | ISMS-POL-A.5.19-23-S3 |
| S4 – Monitoraggio | A.5.22 | ISMS-POL-A.5.19-23-S4 |
| S5 – Servizi cloud | A.5.23 | ISMS-POL-A.5.19-23-S5 |
| S6 – Metodologia | Tutte | ISMS-POL-A.5.19-23-S6 |
| Registro fornitori | Registro di riferimento | ISMS-REF-A.5.23 |

---

## Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Direttore dei Sistemi Informativi (DSI)** | [Nome] | [Data da definire] |
| **Responsabile Legale/Conformità** | [Nome] | [Data da definire] |
| **Direttore Acquisti** | [Nome] | [Data da definire] |
| **Amministratore Delegato (AD)** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questo documento è l'indice principale per il quadro di sicurezza dei fornitori e dei servizi cloud. Per i requisiti dettagliati fare riferimento alle sezioni S1-S6 e ai documenti di implementazione ISMS-IMP-A.5.19-23.S1-S4.*

<!-- QA_VERIFIED: 2026-04-03 -->
