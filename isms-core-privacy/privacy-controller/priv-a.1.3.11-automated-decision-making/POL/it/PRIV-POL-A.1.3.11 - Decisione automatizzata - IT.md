<!-- ISMS-CORE:POLICY:PRIV-POL-A.1.3.11-IT:privacy:POL:a.1.3.11 -->
**PRIV-POL-A.1.3.11 — Decisione automatizzata**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Decisione automatizzata |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | PRIV-POL-A.1.3.11 |
| **Autore del documento** | Responsabile della Protezione dei Dati (RPD) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Data da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto Privacy** | 1.0 |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data da definire] | RPD | Politica iniziale per la prima certificazione ISO/IEC 27701:2025 |

**Ciclo di revisione** : Annuale (o in caso di significativi cambiamenti normativi o organizzativi)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :

- Principale: Responsabile della Protezione dei Dati (RPD)
- Secondaria: Responsabile Legale/Conformità
- Autorità finale: Direzione generale

**Documenti correlati** :

- PRIV-POL-00 (Quadro di applicabilità normativa sulla privacy)
- PRIV-POL-01 (Quadro di governance e processo decisionale sulla privacy)
- PRIV-IMP-A.1.3.11-UG (Decisione automatizzata — Guida utente)
- PRIV-IMP-A.1.3.11-TG (Decisione automatizzata — Guida tecnica)
- PRIV-POL-A.1.3.5-10 (Diritti degli interessati — politica gemella: diritto alla revisione umana)
- PRIV-POL-A.1.3.2-4 (Trasparenza — politica gemella: obbligo di trasparenza per la DA)
- ISO/IEC 27701:2025 Controllo A.1.3.11
- ISO/IEC 27701:2025 Allegato B (Orientamenti di implementazione B.1.3.11)
- RGPD Articolo 22 (Decisione individuale automatizzata, compresa la profilazione); Considerando 71
- LPD svizzera Articolo 21 (Decisioni individuali automatizzate)

**Applicabilità del ruolo** : Questa politica si applica a [Organizzazione] che agisce in qualità di **Titolare del trattamento unicamente**. Il controllo A.1.3.11 è specifico per il titolare del trattamento (Tabella A.1).

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per identificare, documentare e affrontare gli obblighi nei confronti degli interessati derivanti da decisioni basate esclusivamente sul trattamento automatizzato dei DCP — conformemente al controllo A.1.3.11 di ISO/IEC 27701:2025.

**Perimetro** : Tutte le attività di trattamento in cui [Organizzazione], agendo come titolare del trattamento dei DCP, prende decisioni sugli individui basate esclusivamente sul trattamento automatizzato e che producono effetti giuridici o effetti significativi analoghi su quegli individui; tutte le attività di profilazione che alimentano tali decisioni.

---

# Perimetro e applicabilità

## Enunciato del controllo ISO/IEC 27701:2025

**Controllo A.1.3.11 — Decisione automatizzata**
Il controllo A.1.3.11 richiede che [Organizzazione] identifichi gli obblighi — inclusi gli obblighi legali — che ha nei confronti degli interessati in connessione con le decisioni prese esclusivamente attraverso il trattamento automatizzato dei loro DCP, e che dimostri come tali obblighi vengono affrontati.

## Cosa copre questa politica

- Attività di decisione automatizzata (DA) che producono effetti giuridici o effetti significativi analoghi sugli interessati
- Attività di profilazione che alimentano le decisioni automatizzate
- Obblighi nei confronti degli interessati derivanti da tale trattamento
- Capacità di dimostrare come [Organizzazione] affronta tali obblighi

## Cosa questa politica NON copre

- L'implementazione tecnica dei sistemi DA (vedere PRIV-IMP-A.1.3.11-TG)
- La governance generale di AI/ML al di là degli obblighi di privacy
- I sistemi di supporto alle decisioni con intervento umano in cui un essere umano prende la decisione finale (non soggetti alle restrizioni dell'Articolo 22, anche se gli obblighi di trasparenza si applicano comunque)

## Quadro normativo

Questa politica opera all'interno del quadro normativo stabilito in PRIV-POL-00. I seguenti obblighi sono pertinenti:

**Obbligatorio (Livello 1)** (per PRIV-POL-00):

- **RGPD UE** : Articolo 22 (diritto di non essere sottoposto a una decisione basata esclusivamente su un trattamento automatizzato che produce effetti significativi; eccezioni: contratto, legge, consenso esplicito — con garanzie); Articolo 13(2)(f) / 14(2)(g) (trasparenza sull'esistenza della DA, la logica, il significato, le conseguenze); Considerando 71 (contesto della profilazione e garanzie)
- **LPD svizzera** : Articolo 21 (diritto alla spiegazione per le decisioni automatizzate; diritto di richiedere una revisione umana)
- **ISO/IEC 27701:2025** : Controllo A.1.3.11 (normativo)

---

# Disposizioni della politica

## Identificazione della decisione automatizzata

[Organizzazione] DEVE identificare e documentare tutte le attività di trattamento in cui:

- Le decisioni vengono prese sulla base esclusivamente del trattamento automatizzato dei DCP (senza un significativo coinvolgimento umano), E
- Tali decisioni producono effetti giuridici o effetti significativi analoghi sugli interessati

Esempi di effetti significativi: rifiuto del credito, rigetto automatico di candidature di lavoro, determinazione dei premi assicurativi, prezzi personalizzati con impatto finanziario materiale, esclusione automatizzata dai servizi.

**Fuori perimetro** (anche se gli obblighi di trasparenza possono comunque applicarsi):
- Strumenti di supporto alle decisioni in cui un essere umano esamina e prende la decisione finale — purché la revisione sia significativa, cioè il revisore disponga delle informazioni e della capacità di ignorare la decisione automatizzata
- Filtraggio automatizzato che fornisce opzioni ma non prende la decisione finale

Il RPD mantiene un **Registro DA** che elenca tutte le attività di decisione automatizzata nel perimetro.

## Identificazione degli obblighi

Per ogni attività DA, [Organizzazione] DEVE identificare e documentare gli obblighi nei confronti degli interessati, tra cui:

- Il diritto di non essere soggetti alla decisione (Articolo 22(1)), salvo che si applichi un'eccezione
- Eccezioni applicabili: necessaria per l'esecuzione di un contratto (Articolo 22(2)(a)), autorizzata dalla legge dell'UE o di uno Stato membro (Articolo 22(2)(b)), o consenso esplicito (Articolo 22(2)(c))
- Laddove si applichi un'eccezione: garanzie richieste (diritto di ottenere l'intervento umano, diritto di esprimere il proprio punto di vista, diritto di contestare la decisione)
- Obblighi di trasparenza: gli interessati devono essere informati dell'esistenza della DA, della logica coinvolta e del significato e delle conseguenze previste

## Garanzie per le DA nel perimetro

Laddove la DA produca effetti significativi e venga invocata un'eccezione all'Articolo 22, [Organizzazione] DEVE implementare:

1. **Diritto alla revisione umana** : Un meccanismo che consenta agli interessati di richiedere l'intervento umano — sia (a) prima che la decisione venga applicata, sia (b) nell'ambito della contestazione di una decisione già comunicata. Il revisore deve disporre delle informazioni e dell'autorità per ignorare la decisione automatizzata; una revisione di facciata non soddisfa questa garanzia
2. **Espressione del punto di vista** : Un meccanismo che consenta agli interessati di esprimere il proprio punto di vista sulla decisione automatizzata
3. **Contestazione** : Un meccanismo che consenta agli interessati di contestare la decisione automatizzata

Queste garanzie DEVONO essere comunicate agli interessati nell'informativa sulla privacy e al momento della comunicazione della decisione automatizzata.

## Trasparenza

Per ogni attività DA nel perimetro, le informazioni di trasparenza fornite agli interessati (per PRIV-POL-A.1.3.2-4) DEVONO includere:

- L'esistenza della decisione automatizzata
- Informazioni significative sulla logica coinvolta (a un livello comprensibile agli interessati — non divulgazione di algoritmi proprietari)
- Il significato e le conseguenze previste di tale trattamento per l'interessato

## DCP di categoria speciale nelle DA

Le DA che trattano DCP di categoria speciale richiedono una condizione dell'Articolo 9(2) in aggiunta a un'eccezione dell'Articolo 22. Tale trattamento richiede l'approvazione esplicita del RPD e, nella maggior parte dei casi, una DPIA (per PRIV-POL-A.1.2.6-9).

## Capacità di dimostrazione

[Organizzazione] DEVE essere in grado di dimostrare in qualsiasi momento come affronta i propri obblighi per ogni attività DA — alle autorità di controllo, agli interessati e ai revisori di certificazione. Il Registro DA e la documentazione associata (inclusa la DPIA ove condotta) costituiscono le principali prove di dimostrazione.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Responsabile della Protezione dei Dati (RPD)** | Mantiene il Registro DA; approva le nuove attività DA; esamina l'identificazione degli obblighi; approva la progettazione delle garanzie; DPIA per i trattamenti DA |
| **Legale/Conformità** | Consulenza sulle eccezioni applicabili all'Articolo 22; revisione della base giuridica per le DA; consulenza sull'adeguatezza delle garanzie dell'Articolo 22 |
| **Team Sviluppo / Data Science** | Identificano le attività DA nei sistemi che costruiscono; notificano il RPD prima di dispiegare le DA; implementano i meccanismi di revisione umana e contestazione |
| **Direzione Prodotto** | Garantisce che le attività DA siano segnalate al RPD durante la progettazione del prodotto; supporta l'implementazione delle garanzie |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Registro DA | Tutte le attività DA con base giuridica, eccezione invocata, garanzie, trasparenza | In corso + 3 anni |
| DPIA per le DA | Laddove le DA comportino un trattamento ad alto rischio | Durata della DA + 3 anni |
| Prove di implementazione delle garanzie | Registrazioni tecniche del meccanismo di revisione umana, processo di contestazione | In corso + 3 anni |
| Registro dei diritti degli interessati | Richieste di revisione umana, espressione del punto di vista, o contestazione | 5 anni |

---

# Considerazioni di audit

I revisori che verificano la conformità al controllo A.1.3.11 devono aspettarsi di trovare:

- Registro DA che identifica tutte le attività di decisione automatizzata nel perimetro
- Per ogni attività: eccezione all'Articolo 22(1) invocata documentata e garanzie in atto
- Informazioni di trasparenza nell'informativa sulla privacy che coprono l'esistenza della DA, la logica e le conseguenze
- Meccanismi di revisione umana, espressione del punto di vista e contestazione operativi e accessibili
- DPIA condotta per le attività DA ad alto rischio

---

<!-- QA_VERIFIED: 2026-04-03 -->
