<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.31.2-IT:framework:POL:a.5.31.2 -->
**ISMS-POL-A.5.31.2 — Metodologia di applicabilità normativa**
**Requisiti legali, normativi, regolamentari e contrattuali**

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Requisiti legali, normativi, regolamentari e contrattuali: Metodologia di applicabilità normativa |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.31.2 |
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
| 1.0 | [Data] | RSSI/ISO | Quadro di politica iniziale per la prima certificazione ISO 27001:2022 |

---

# Introduzione e contesto del quadro

## Scopo di questa sezione di politica

Questa sezione di politica stabilisce la metodologia sistematica con cui [Organizzazione] identifica, valuta e categorizza i requisiti legali, normativi, regolamentari e contrattuali applicabili al suo programma di sicurezza delle informazioni.

La metodologia qui definita trasforma la conformità normativa da un'attività reattiva e ad hoc in un processo sistematico e ripetibile che produce determinazioni coerenti e difendibili dell'applicabilità normativa.

## Relazione con il quadro di conformità

ISMS-POL-A.5.31.1 (Riepilogo esecutivo e allineamento dei controlli) ha stabilito il quadro complessivo di conformità normativa e la struttura di governance. Questa sezione di politica (5.31.2) fornisce la **prima metodologia operativa** all'interno di quel quadro: il processo per determinare **quali normative si applicano** a [Organizzazione].

Gli output di questa metodologia popolano e mantengono direttamente **ISMS-POL-00 (Quadro di applicabilità normativa)** — il registro autorevole dei regolamenti applicabili.

---

# Processo di identificazione normativa

## Trigger di identificazione normativa

[Organizzazione] DEVE avviare valutazioni di identificazione e applicabilità normativa quando attivata dai seguenti eventi:

### Trigger di revisione periodica

**Revisione annuale completa** (Obbligatoria): Scansione completa del panorama normativo; revisione di tutte le voci in ISMS-POL-00; eseguita nel Q4 di ogni anno civile; responsabilità: Responsabile della Conformità in coordinamento con la Funzione legale.

**Scansione ambientale trimestrale** (Raccomandata): Scansione focalizzata sugli sviluppi normativi nelle giurisdizioni chiave; revisione degli avvisi di monitoraggio normativo accumulati durante il trimestre.

### Trigger di espansione

La valutazione dell'applicabilità DEVE essere avviata quando [Organizzazione]: entra in un nuovo mercato geografico; offre nuovi servizi o prodotti; acquisisce clienti in settori regolamentati; effettua fusioni e acquisizioni.

### Trigger contrattuali

Avviare la valutazione quando: i contratti con i clienti includono requisiti specifici di conformità; nuovi accordi con fornitori creano obblighi pass-through; si perseguono nuove certificazioni; si ricevono questionari di conformità dagli stakeholder.

### Trigger interni

Valutazione da avviare in seguito a: iniziative strategiche che richiedono mercati regolamentati; risultati della valutazione dei rischi che identificano l'esposizione normativa; identificazione di lacune di conformità; segnalazioni dei dipendenti.

### Trigger esterni

La valutazione DEVE essere avviata quando: vengono promulgate nuove leggi o normative; l'autorità normativa emette nuove regole o orientamenti; il settore riceve azioni di applicazione normativa; l'autorità normativa contatta direttamente [Organizzazione].

## Fonti di intelligence normativa

[Organizzazione] DEVE utilizzare le seguenti fonti per identificare i regolamenti potenzialmente applicabili:

**Database legali e servizi di ricerca**: Piattaforme commerciali di ricerca legale (es. LexisNexis, Westlaw); database legali governativi (es. EUR-Lex per l'UE, Raccolta sistematica del diritto federale svizzero); piattaforme di Regulatory Technology (RegTech).

**Associazioni di settore e organismi di standardizzazione**: Associazioni di settore specifiche; (ISC)², ISACA, IAPP; ISO, NIST, CIS; organismi di standardizzazione specifici del settore.

**Consulente legale**: Team legale interno; consulenti legali esterni; consulenti legali normativi specializzati.

**Reti di pari e comunità professionali**: Forum del settore; associazioni professionali; comunità di pratica della conformità.

**Canali di clienti e fornitori**: Requisiti dei contratti con i clienti; obblighi dei contratti con i fornitori; questionari di conformità per RFP/RFI.

## Criteri di screening iniziale

Prima di condurre la valutazione completa dell'applicabilità, [Organizzazione] DEVE applicare uno screening iniziale:

**Screening della rilevanza**: Il regolamento riguarda la sicurezza delle informazioni, la protezione dei dati, i servizi IT o gli asset informativi di [Organizzazione]?

**Screening giurisdizionale**: [Organizzazione] ha qualche connessione con la giurisdizione in cui si applica questo regolamento?

**Screening operativo**: Le operazioni attuali o pianificate di [Organizzazione] rientrano nel perimetro di questo regolamento?

**Matrice decisionale di screening**:

| Rilevanza | Giurisdizione | Operazioni | Decisione |
|-----------|--------------|------------|-----------|
| NON rilevante | Qualsiasi | Qualsiasi | **STOP** — Escluso |
| Rilevante | NESSUNA connessione | NON applicabile | **STOP** — Probabilmente non applicabile (documentare) |
| Rilevante | NESSUNA connessione | Potenzialmente applicabile | **PROCEDERE** — Valutazione completa |
| Rilevante | Connessione | NON applicabile | **PROCEDERE** — Valutazione completa |
| Rilevante | Connessione | Potenzialmente applicabile | **PROCEDERE** — Valutazione completa |

---

# Quadro dei criteri di applicabilità

Per i regolamenti che superano lo screening iniziale, [Organizzazione] DEVE condurre una valutazione strutturata dell'applicabilità utilizzando un **quadro tridimensionale**:

1. **Perimetro geografico**: Applicabilità basata su DOVE opera [Organizzazione]
2. **Perimetro operativo**: Applicabilità basata su COSA fa [Organizzazione]
3. **Perimetro contrattuale**: Applicabilità basata sugli ACCORDI stipulati da [Organizzazione]

## Valutazione del perimetro geografico

**Criterio G1 — Operazioni nella giurisdizione**: [Organizzazione] conduce operazioni nella giurisdizione in cui si applica questo regolamento? (uffici fisici, dipendenti, entità legali, licenze).

**Criterio G2 — Clienti o interessati nella giurisdizione**: [Organizzazione] serve clienti fisicamente situati nella giurisdizione, o elabora dati di individui nella giurisdizione?

**Criterio G3 — Targeting della giurisdizione**: [Organizzazione] prende di mira attivamente individui o entità nella giurisdizione? (sito web in lingua locale, prezzi in valuta locale, campagne di marketing mirate).

**Criterio G4 — Trattamento dei dati nella giurisdizione**: [Organizzazione] elabora dati nella giurisdizione, anche senza altra presenza? (server, fornitori terzi, backup/siti DRP).

**Criterio G5 — Applicazione extraterritoriale**: Il regolamento afferma esplicitamente di applicarsi oltre i confini della sua giurisdizione? (es. RGPD, CCPA).

**Punteggio**: SÌ=1 punto, NO=0 punti, INCERTO=0,5 punti; Punteggio geografico 0-5.

## Valutazione del perimetro operativo

**Criterio O1 — Allineamento del tipo di servizio**: [Organizzazione] fornisce tipi di servizi che rientrano nel perimetro del regolamento? (cloud, elaborazione pagamenti, salute, telecomunicazioni, infrastrutture critiche).

**Criterio O2 — Allineamento del settore industriale**: [Organizzazione] serve settori industriali regolamentati da questo regolamento? (finanziario, sanitario, governativo, infrastrutture critiche).

**Criterio O3 — Allineamento del tipo di dati**: [Organizzazione] elabora tipi di dati protetti o regolamentati da questo regolamento? (DCP, categorie speciali, dati di carte di pagamento, dati governativi, dati di minori).

**Criterio O4 — Caratteristiche organizzative**: [Organizzazione] soddisfa le soglie di applicabilità del regolamento basate su dimensioni, fatturato o altre caratteristiche?

**Criterio O5 — Operazioni specifiche coperte**: [Organizzazione] esegue operazioni o attività specifiche esplicitamente coperte dal regolamento? (e-commerce, trasferimenti transfrontalieri di dati, decisioni automatizzate, autenticazione biometrica).

**Punteggio**: SÌ=1 punto, NO=0 punti, INCERTO=0,5 punti; Punteggio operativo 0-5.

## Valutazione del perimetro contrattuale

**Criterio C1 — Requisiti contrattuali dei clienti**: I contratti con i clienti di [Organizzazione] richiedono esplicitamente la conformità a questo regolamento?

**Criterio C2 — Obblighi pass-through dei fornitori**: Gli accordi di [Organizzazione] con i fornitori creano obblighi su [Organizzazione] di conformarsi a questo regolamento?

**Criterio C3 — Requisiti di certificazione**: La conformità a questo regolamento è richiesta per le certificazioni che [Organizzazione] detiene o persegue?

**Criterio C4 — Impegni volontari**: [Organizzazione] ha assunto impegni pubblici o promesse volontarie di conformità? (politiche sulla privacy, materiali di marketing, codici di condotta).

**Punteggio**: SÌ=1 punto, NO=0 punti, INCERTO=0,5 punti; Punteggio contrattuale 0-4.

## Determinazione combinata dell'applicabilità

**APPLICABILE** (Aggiungere a ISMS-POL-00):

- Punteggio alto (4-5) in QUALSIASI dimensione, OPPURE
- Punteggi moderati (2-3) in DUE O PIÙ dimensioni, OPPURE
- Requisito contrattuale esplicito (C1 o C2 = SÌ), OPPURE
- Parere legale che conferma l'applicabilità

**CONDIZIONALMENTE APPLICABILE** (Aggiungere a ISMS-POL-00 come Livello 2):

- Punteggio moderato (2-3) in UNA sola dimensione
- Potenziale applicabilità futura (piani di espansione)
- Adozione volontaria per vantaggio competitivo

**NON APPLICABILE** (Non aggiungere a ISMS-POL-00):

- Punteggi bassi (0-1) in TUTTE le dimensioni
- Il regolamento esclude esplicitamente le operazioni di [Organizzazione]
- Parere legale che conferma la non applicabilità

---

# Quadro di categorizzazione a tre livelli

I regolamenti determinati applicabili DEVONO essere categorizzati in uno dei tre livelli all'interno di ISMS-POL-00:

## Livello 1: Conformità obbligatoria

**Definizione**: Regolamenti con **OBBLIGO LEGALE** o **REQUISITO CONTRATTUALE ESEGUIBILE**. La non conformità comporta conseguenze legali o contrattuali concrete.

**Criteri di assegnazione**: DEVE essere classificato come Livello 1 se soddisfa QUALSIASI dei seguenti:

- **Obbligo legale**: Legge o normativa giuridicamente vincolante per [Organizzazione] nelle giurisdizioni in cui opera; punteggio geografico alto (4-5) E il regolamento contiene requisiti obbligatori
- **Applicabilità contrattuale**: Il contratto con il cliente richiede esplicitamente la conformità con meccanismi di applicazione; accordo con il fornitore crea un obbligo pass-through eseguibile
- **Requisito di certificazione**: La conformità è richiesta per una certificazione che [Organizzazione] detiene

**Trattamento**: Conformità totale richiesta; approvazione esecutiva obbligatoria; estrazione obbligatoria dei requisiti; mappatura obbligatoria dei controlli; rimedio delle lacune ad alta priorità; raccolta continua delle prove; revisione annuale minima.

## Livello 2: Applicabilità condizionale

**Definizione**: Regolamenti che **POTREBBERO DIVENTARE APPLICABILI** in futuro o che sono **VOLONTARIAMENTE ADOTTATI** per ragioni strategiche.

**Criteri di assegnazione**: DEVE essere classificato come Livello 2 se soddisfa QUALSIASI dei seguenti:

- Potenziale applicabilità futura: [Organizzazione] sta valutando l'espansione; normativa proposta o in bozza
- Adozione volontaria: Best practice del settore; differenziatore competitivo; aspettative dei clienti
- Incertezza normativa: La valutazione dell'applicabilità è incerta; in attesa di chiarimento legale

**Trattamento**: Monitoraggio e prontezza; analisi delle lacune opzionale; revisione annuale o biennale; documentare la motivazione strategica per l'adozione volontaria.

## Livello 3: Riferimento informativo

**Definizione**: Normative e quadri utilizzati solo per **ORIENTAMENTO**, **BENCHMARK** o **BEST PRACTICE**. Non vi è alcun obbligo di conformità.

**Criteri di assegnazione**: DEVE essere classificato come Livello 3 se: nessun obbligo di conformità (legale o contrattuale); utile come riferimento (best practice del settore, benchmark, guida per la progettazione dei controlli).

**Trattamento**: Riferimento per la progettazione dei controlli; nessun requisito di prove; revisione biennale o secondo necessità.

## Albero decisionale per l'assegnazione del livello

```
INIZIO: Il regolamento ha superato lo screening iniziale
    ↓
Esiste un OBBLIGO LEGALE?
(Il regolamento è giuridicamente vincolante in una giurisdizione dove [Org.] opera)
    ├─ SÌ → LIVELLO 1
    └─ NO → Continua
        ↓
Esiste un REQUISITO CONTRATTUALE ESEGUIBILE?
(Il contratto con cliente/fornitore richiede la conformità con meccanismo di esecuzione)
    ├─ SÌ → LIVELLO 1
    └─ NO → Continua
        ↓
La conformità è RICHIESTA per una CERTIFICAZIONE che [Org.] detiene?
    ├─ SÌ → LIVELLO 1
    └─ NO → Continua
        ↓
Esiste una POTENZIALE APPLICABILITÀ FUTURA?
(Piani di espansione, traiettoria di crescita, normativa proposta)
    ├─ SÌ → LIVELLO 2
    └─ NO → Continua
        ↓
[Org.] sta ADOTTANDO VOLONTARIAMENTE per ragioni strategiche?
    ├─ SÌ → LIVELLO 2
    └─ NO → Continua
        ↓
È utile come ORIENTAMENTO/BENCHMARK?
    ├─ SÌ → LIVELLO 3
    └─ NO → NON AGGIUNGERE A POL-00
```

## Mobilità tra livelli

I regolamenti possono spostarsi tra i livelli con l'evoluzione delle circostanze: Livello 2 → Livello 1 ([Organizzazione] si espande nella giurisdizione); Livello 1 → Livello 2 ([Organizzazione] esce dalla giurisdizione); Livello 3 → Livello 2 ([Organizzazione] decide l'adozione volontaria); Qualsiasi livello → Rimosso (normativa abrogata o definitivamente non applicabile).

---

# Requisiti di documentazione e approvazione

## Documentazione della valutazione dell'applicabilità

Per ogni regolamento valutato (sia esso determinato applicabile o meno), [Organizzazione] DEVE creare e mantenere una documentazione completa includendo:

- Identificazione completa del regolamento (nome, giurisdizione, autorità emittente, data di entrata in vigore, fonte)
- Sintesi della valutazione tridimensionale con punteggi e motivazioni
- Determinazione complessiva (Applicabile/Condizionalmente applicabile/Non applicabile)
- Assegnazione del livello con motivazione dettagliata
- Prove di supporto (testo normativo, pareri legali, estratti contrattuali)
- Metadati di valutazione (valutatore, data, revisore, approvatore, prossima data di revisione)

## Flusso di approvazione

**Fase 1 — Valutazione iniziale** (Responsabile della Conformità): Completare la valutazione tridimensionale; redigere la determinazione (entro 10 giorni lavorativi dall'evento trigger).

**Fase 2 — Revisione tra pari** (Obbligatoria per Livello 1): Secondo professionista di Conformità/Legale (entro 5 giorni lavorativi).

**Fase 3 — Revisione legale** (Obbligatoria per Livello 1): Consulente legale interno o esterno (entro 10 giorni lavorativi).

**Fase 4 — Revisione del Responsabile SGSI** (Tutti i livelli): Valutare le implicazioni per il SGSI (entro 5 giorni lavorativi).

**Fase 5 — Approvazione esecutiva** (Obbligatoria solo per Livello 1): Direzione generale (entro 10 giorni lavorativi).

**Matrice dell'autorità di approvazione**:

| Livello | Resp. Conformità | Consulente legale | Resp. SGSI | Dir. Gen. |
|---------|-----------------|------------------|-----------|-----------|
| **Livello 1** | Valuta (R) | Rivede e approva (A) | Rivede e approva (A) | **Approva** (A) |
| **Livello 2** | Valuta (R) | Rivede (C) | **Approva** (A) | Informata (I) |
| **Livello 3** | Valuta (R) | Opzionale (C) | **Approva** (A) | Informata (I) |

## Aggiunta a ISMS-POL-00

Dopo l'approvazione finale, il Responsabile SGSI DEVE aggiungere il regolamento a ISMS-POL-00 nella sezione del livello appropriato con: ID del regolamento; nome del regolamento; giurisdizione; autorità emittente; data di entrata in vigore; livello; motivazione dell'applicabilità; link alla valutazione completa; data dell'ultima revisione; prossima data di revisione; parte responsabile.

L'aggiunta di normative del Livello 1 o 2 attiva i processi downstream: Estrazione dei requisiti (POL-5.31.3); Mappatura dei controlli (POL-5.31.3); Pianificazione delle prove (POL-5.31.4).

---

# Frequenza di revisione e trigger di aggiornamento

## Calendario di revisione periodica

**Revisione annuale completa** (Obbligatoria): TUTTI i regolamenti in ISMS-POL-00; Q4 di ogni anno; documentare data di revisione e risultato («Nessun cambiamento», «Livello modificato», «Rimosso», ecc.).

**Frequenza specifica per livello**: Livello 1 — annuale minima (semestrali per normative in rapida evoluzione); Livello 2 — annuale; Livello 3 — biennale.

## Trigger di revisione guidati dagli eventi

La valutazione dell'applicabilità DEVE essere rivista quando attivata da:

**Cambiamenti organizzativi**: Espansione o contrazione geografica (entro 30 giorni); cambiamenti operativi (durante la fase di pianificazione); ristrutturazione organizzativa (come parte della due diligence di M&A; entro 60 giorni dal closing della transazione); cambiamenti di soglia (quando le soglie normative vengono superate).

**Cambiamenti normativi**: Regolamento emendato (il processo di monitoraggio dei cambiamenti per POL-5.31.4 rileva l'emendamento); normativa abrogata o sostituita; orientamento o interpretazione normativa emessa.

**Cambiamenti contrattuali**: Nuovo contratto con il cliente (durante la due diligence pre-contratto); rinnovo o modifica del contratto; scadenza del contratto (quando l'applicabilità era dovuta al contratto); nuovo accordo con il fornitore.

**Cambiamenti di certificazione**: Nuova certificazione perseguita; standard di certificazione aggiornato.

## Escalation per le controversie sull'applicabilità

**Controversie interne**: Discussione → Decisione del Responsabile della Conformità → Revisione del Consulente legale → Escalation esecutiva → Consulente esterno per questioni legali complesse.

**Sfide esterne** (autorità normativa, cliente, auditor): Raccogliere prove → Revisione del Consulente legale → Parere legale esterno → Risoluzione → Documenta.

**Posizione predefinita**: Se rimane il dubbio — Predefinire «Applicabile» e livello superiore per ridurre il rischio di non conformità; rivalutare quando sarà disponibile ulteriore chiarezza.

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Applicabilità** | Determinazione che un regolamento si applica a [Organizzazione] in base a criteri geografici, operativi o contrattuali |
| **Obbligo contrattuale** | Requisito imposto da un contratto (cliente, fornitore, partner) che crea un obbligo di conformità eseguibile |
| **Perimetro geografico** | Applicabilità basata su dove opera [Organizzazione], dove si trovano i clienti, o disposizioni extraterritoriali |
| **Obbligo legale** | Requisito imposto da legge o normativa giuridicamente vincolante e applicabile |
| **Perimetro operativo** | Applicabilità basata su quali servizi fornisce [Organizzazione], quali dati elabora o quali operazioni conduce |
| **Regolamento** | Termine generale che comprende leggi, statuti, normative, direttive, requisiti contrattuali e standard |
| **Quadro a tre livelli** | Sistema di categorizzazione che classifica i regolamenti come Livello 1 (Obbligatorio), Livello 2 (Condizionale) o Livello 3 (Informativo) |
| **Evento trigger** | Circostanza che avvia l'identificazione normativa o la rivalutazione dell'applicabilità |

---

# Registro di approvazione

| Ruolo | Nome | Firma | Data |
|-------|------|-------|------|
| **Responsabile della Conformità** | [Nome] | ___________ | __________ |
| **Consulente legale** | [Nome] | ___________ | __________ |
| **Responsabile SGSI** | [Nome] | ___________ | __________ |
| **Direzione generale** | [Nome] | ___________ | __________ |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce la metodologia sistematica di [Organizzazione] per la determinazione dell'applicabilità normativa, alimentando ISMS-POL-00 e consentendo la downstream estrazione dei requisiti e la mappatura dei controlli.*

<!-- QA_VERIFIED: 2026-04-03 -->
