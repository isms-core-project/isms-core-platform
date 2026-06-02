<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.1-IT:cloud:POL:a.1 -->
**CLD-PII-POL-A.1 — Generalità**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Responsabile del trattamento di DCP nel cloud pubblico — Applicabilità generale e obblighi |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-PII-POL-A.1 |
| **Autore del documento** | RSSI / Responsabile della Protezione dei Dati (RPD) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Data da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto Cloud** | 1.0 |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data da definire] | RSSI / RPD | Politica iniziale per l'implementazione di ISO/IEC 27018:2025 Ed. 3 |

**Ciclo di revisione** : Annuale (o in caso di significativi cambiamenti normativi o del modello di servizio)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :
- Principale: RSSI / Responsabile Sicurezza Cloud
- Secondaria: Responsabile della Protezione dei Dati (RPD)
- Autorità finale: Direzione generale

**Documenti correlati** :
- PRIV-POL-00 (Quadro di applicabilità normativa sulla privacy)
- ISMS-POL-A.5.34 (Privacy e protezione dei DCP — politica SGSI principale)
- CLD-PII-POL-A.2 (Consenso e scelta)
- CLD-PII-POL-A.3 (Legittimità e specificazione della finalità)
- CLD-PII-POL-A.10 (Accountability)
- CLD-PII-POL-A.11 (Sicurezza delle informazioni)
- CLD-PII-POL-A.12 (Conformità in materia di privacy)
- ISO/IEC 27018:2025 Annex A, Sezione A.1 (Generalità)
- ISO/IEC 27701:2025 (Sistema di gestione delle informazioni sulla privacy)
- ISO/IEC 27002:2022 (Controlli di sicurezza delle informazioni)
- RGPD Articolo 28 (Obblighi del responsabile del trattamento)
- LPD svizzera Articolo 9 (Impegni del responsabile del trattamento)

---

## Riepilogo esecutivo

Questa politica stabilisce il perimetro, l'applicabilità e gli obblighi generali di [Organizzazione] che agisce in qualità di **responsabile del trattamento di DCP nel cloud pubblico** conformemente a ISO/IEC 27018:2025 Annex A, Sezione A.1.

**Perimetro** : Tutti i servizi cloud forniti da [Organizzazione] nell'ambito dei quali [Organizzazione] tratta dati a carattere personale (DCP) per conto e su istruzione di un titolare del trattamento dei DCP. Questo si applica indipendentemente dal modello di servizio cloud (IaaS, PaaS, SaaS) o dal modello di distribuzione (pubblico, ibrido). Le distribuzioni ibride rientrano nel perimetro nella misura in cui la componente cloud pubblico coinvolge il trattamento di DCP per conto di un titolare del trattamento.

**Chiarimento dei ruoli** : ISO/IEC 27018:2025 si applica a [Organizzazione] nella sua veste di **responsabile del trattamento dei DCP** — un'entità che tratta DCP per conto e sotto l'autorità di un titolare del trattamento dei DCP. [Organizzazione] non determina le finalità e i mezzi di tale trattamento; tale responsabilità spetta al titolare del trattamento dei DCP.

**Nota sui controlli estesi** : I controlli dell'Annex A di ISO/IEC 27018:2025 sono informativi. [Organizzazione] li implementa nell'ambito della propria pratica di protezione dei dati nel cloud, indipendentemente dal loro status normativo ai sensi dello standard.

---

# Perimetro e applicabilità

## ISO/IEC 27018:2025 — Sezione A.1

**Sezione A.1 — Generalità**

La Sezione A.1 dell'Annex A di ISO/IEC 27018:2025 stabilisce l'applicabilità generale del set di controlli, definendo il ruolo del responsabile del trattamento di DCP nel cloud pubblico e gli obblighi fondamentali che sottendono tutti i controlli successivi nel set di controlli esteso dell'Annex A.

## Applicabilità

Questa politica e la suite di politiche CLD-PII-POL-A.X si applicano a:

- Tutti i servizi cloud pubblico di [Organizzazione] che trattano DCP per conto di clienti (titolari del trattamento dei DCP)
- Tutto il personale, i sistemi, i processi e i sub-responsabili del trattamento coinvolti in tale trattamento dei DCP
- Tutte le giurisdizioni in cui [Organizzazione] fornisce servizi cloud in cui vengono trattati DCP di interessati

## Quadro normativo

**Livello 1: Conformità obbligatoria** (per PRIV-POL-00):

- **RGPD UE** : Articolo 28 (obblighi del responsabile del trattamento — contratto scritto, trattamento solo su istruzione, sicurezza, sub-responsabili del trattamento, assistenza, restituzione/cancellazione, diritti di audit); Articolo 32 (sicurezza del trattamento)
- **LPD svizzera** : Articolo 9 (condizioni di ingaggio del responsabile del trattamento e obblighi di sicurezza dei dati associati)
- **ISO/IEC 27018:2025** : Set di controlli esteso dell'Annex A — implementato come impegno organizzativo

---

# Disposizioni della politica: Applicabilità generale (A.1)

## Ruolo di responsabile del trattamento dei DCP

[Organizzazione] DEVE agire esclusivamente come responsabile del trattamento dei DCP — trattando i DCP esclusivamente secondo le istruzioni documentate dei titolari del trattamento dei DCP. [Organizzazione] NON DEVE:

- Determinare le finalità o i mezzi del trattamento dei DCP al di là dell'erogazione tecnica del servizio
- Trattare DCP per finalità proprie di [Organizzazione] di natura commerciale, analitica o operativa senza esplicita autorizzazione del titolare del trattamento
- Trasferire, vendere o altrimenti sfruttare DCP trattati per conto di un titolare del trattamento

## Requisito contrattuale

[Organizzazione] DEVE trattare DCP solo laddove sia in vigore un contratto scritto con il titolare del trattamento dei DCP. Tale contratto DEVE disciplinare, come minimo, il perimetro del trattamento, gli obblighi di sicurezza, la notifica delle violazioni, le disposizioni relative ai sub-responsabili del trattamento, la restituzione/cancellazione dei dati e i diritti di audit — in conformità con CLD-PII-POL-A.11 (§11.11 — Requisiti contrattuali).

## Documentazione dei controlli

[Organizzazione] DEVE documentare come ciascun controllo applicabile dell'Annex A di ISO/IEC 27018:2025 viene affrontato nell'ambito dei propri servizi. Tale documentazione DEVE essere resa disponibile ai titolari del trattamento dei DCP su richiesta e incorporata negli accordi di servizio laddove contrattualmente richiesto.

## Trattamento su istruzione

[Organizzazione] DEVE trattare i DCP solo in conformità con le istruzioni documentate e aggiornate del titolare del trattamento dei DCP. Laddove [Organizzazione] sia legalmente tenuta dalla legge applicabile a trattare DCP al di là delle istruzioni del titolare del trattamento, [Organizzazione] DEVE informare il titolare del trattamento dei DCP di tale obbligo prima del trattamento, a meno che non le sia legalmente vietato farlo.

## Gestione dei sub-responsabili del trattamento

[Organizzazione] DEVE ingaggiare sub-responsabili del trattamento solo con il previo consenso scritto del titolare del trattamento dei DCP. Tutti i sub-responsabili del trattamento DEVONO essere vincolati da obblighi di protezione dei dati equivalenti. [Organizzazione] rimane responsabile nei confronti del titolare del trattamento per la conformità dei sub-responsabili del trattamento. Le disposizioni relative ai sub-responsabili del trattamento sono disciplinate in dettaglio da CLD-PII-POL-A.11 (§11.12 — Obblighi dei sub-responsabili del trattamento).

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI / Responsabile Sicurezza Cloud** | Mantiene la suite di politiche CLD-PII-POL-A.X; garantisce che i controlli tecnici soddisfino i requisiti dell'Annex A di ISO 27018:2025; riferisce sulla conformità del responsabile del trattamento di DCP nel cloud |
| **Responsabile della Protezione dei Dati (RPD)** | Fornisce consulenza sulla conformità normativa delle attività del responsabile del trattamento; esamina gli accordi di trattamento; coordina le questioni DCP con i titolari del trattamento |
| **Responsabile Legale/Conformità** | Esamina le condizioni degli accordi di trattamento; fornisce consulenza sugli obblighi di legge applicabili; valuta i cambiamenti normativi che incidono sugli obblighi del responsabile del trattamento |
| **Erogazione del servizio cloud** | Gestisce i servizi nell'ambito delle istruzioni documentate dei titolari del trattamento; escalate le richieste fuori perimetro a RSSI e RPD |
| **Tutto il personale** | Tratta i DCP solo come autorizzato; segnala immediatamente le violazioni sospette della politica a RSSI e RPD |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Registro degli accordi di trattamento | Elenco di tutti gli accordi attivi con i titolari del trattamento dei DCP con perimetro, stato e data di revisione | In corso + 3 anni dalla fine del contratto |
| Documentazione di implementazione dei controlli | Documentazione di come ciascun controllo CLD-PII-POL-A.X è implementato per servizio | Versione attuale + versioni precedenti per 3 anni dalla supersessione |
| Registro dei sub-responsabili del trattamento | Elenco dei sub-responsabili del trattamento approvati con registrazioni del consenso dei titolari del trattamento | In corso + 3 anni dalla fine dell'impegno |
| Registrazioni delle istruzioni | Registrazioni delle istruzioni di trattamento documentate dei titolari del trattamento e di eventuali deviazioni | Durata del contratto + 3 anni |

> **Base di conservazione** : I periodi di 3 anni si allineano ai termini di prescrizione applicabili ai sensi del diritto UE e svizzero per le controversie relative agli accordi di trattamento. Periodi più lunghi possono applicarsi laddove i requisiti di audit regolatorio o le condizioni contrattuali lo specifichino.

---

# Considerazioni di audit

Gli auditor che verificano la conformità a CLD-PII-POL-A.1 devono aspettarsi di trovare:

- Un registro degli accordi di trattamento che dimostri contratti scritti con tutti i titolari del trattamento dei DCP
- Documentazione che mappa ciascun controllo dell'Annex A di ISO/IEC 27018:2025 all'implementazione del servizio
- Un registro dei sub-responsabili del trattamento con registrazioni del consenso dei titolari del trattamento per ciascun sub-responsabile del trattamento
- Prove che il trattamento viene effettuato solo in conformità con le istruzioni documentate dei titolari del trattamento

---

<!-- QA_VERIFIED: 2026-04-04 -->
