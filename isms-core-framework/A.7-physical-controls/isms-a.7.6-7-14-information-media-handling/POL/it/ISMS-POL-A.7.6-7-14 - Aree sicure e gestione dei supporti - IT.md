<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.6-7-14-IT:framework:POL:a.7.6-7-14 -->
**ISMS-POL-A.7.6-7-14 — Aree sicure e gestione dei supporti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Aree sicure e gestione dei supporti |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.7.6-7-14 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale

**Catena di approvazione**: Principale: RSSI; Secondario: Responsabile delle strutture; Autorità finale: Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.7.1-3; ISMS-POL-A.7.10; ISMS-POL-A.8.10; ISMS-IMP-A.7.6-7-14-S1–S3-UG/TG; ISO/IEC 27001:2022 Controlli A.7.6, A.7.7, A.7.14.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per il lavoro in aree sicure, le pratiche di scrivania libera e schermo libero, e lo smaltimento o il riutilizzo sicuro delle apparecchiature.

**Approccio a controlli combinati**: I Controlli A.7.6, A.7.7 e A.7.14 sono implementati insieme perché affrontano aspetti complementari della protezione fisica delle informazioni durante le attività lavorative e il ciclo di vita delle apparecchiature.

**Allineamento normativo**: nLPD svizzera (Art. 8, Art. 6); ISO/IEC 27001:2022; RGPD dell'UE, PCI DSS v4.0.1, FINMA, DORA (applicabilità condizionale).

---

# Allineamento sul controllo

**A.7.6 — Lavoro in aree sicure**: Le misure di sicurezza per il lavoro in aree sicure devono essere progettate e implementate.

**A.7.7 — Scrivania libera e schermo libero**: Devono essere definite e opportunamente applicate regole di scrivania libera per carta e supporti di archiviazione rimovibili e regole di schermo libero per le strutture di elaborazione delle informazioni.

**A.7.14 — Smaltimento o riutilizzo sicuro delle apparecchiature**: Gli elementi delle apparecchiature contenenti supporti di archiviazione devono essere verificati per garantire che tutti i dati sensibili e il software concesso in licenza siano stati rimossi o sovrascritti in modo sicuro prima dello smaltimento o del riutilizzo.

---

# Enunciati di politica

## Lavoro in aree sicure (A.7.6)

### Accesso e condotta

**Controlli di accesso**: L'accesso alle aree sicure DEVE essere concesso solo al personale autorizzato in base al ruolo lavorativo e al principio del need-to-know; i visitatori nelle aree sicure DEVONO essere sempre accompagnati; i diritti di accesso DEVONO essere rivisti trimestralmente e revocati quando non più necessari.

**Condotta nelle aree sicure**: Il personale DEVE essere a conoscenza delle attività nelle aree sicure solo in base al need-to-know; il personale NON DEVE lavorare da solo nelle aree sicure al di fuori dei normali orari lavorativi a meno che non esista un'eccezione approvata in ISMS-REG-EXCEPTIONS con controlli compensativi in atto; le aree sicure vuote DEVONO essere chiuse a chiave e ispezionate periodicamente; la fotografia, il video, l'audio o altre registrazioni DEVONO essere vietati a meno che non siano specificamente autorizzati.

**Accesso di terze parti**: Le terze parti DEVONO essere accompagnate nelle aree sicure; l'accesso di terze parti DEVE essere registrato e limitato nel tempo; le terze parti DEVONO firmare accordi di riservatezza prima dell'accesso; le apparecchiature di terze parti NON DEVONO essere portate nelle aree sicure a meno che non sia autorizzato dal Proprietario dell'area sicura o dal Team di sicurezza.

## Scrivania libera e schermo libero (A.7.7)

### Requisiti di scrivania libera

**Durante l'orario di lavoro**: I documenti sensibili DEVONO essere archiviati in modo sicuro quando non in uso immediato; i documenti in attesa di stampa DEVONO essere ritirati immediatamente.

**Fine giornata / Assenza prolungata**:

- Tutti i documenti sensibili DEVONO essere chiusi a chiave in cassetti o armadietti
- I supporti di archiviazione rimovibili (chiavette USB, unità esterne) DEVONO essere messi al sicuro
- Le card di accesso e le chiavi NON DEVONO essere lasciate sulle scrivanie
- I taccuini e i post-it con informazioni sensibili DEVONO essere messi al sicuro

**Requisiti specifici per classificazione**:

| Classificazione | Requisito di scrivania libera |
|----------------|-------------------------------|
| **RISERVATO** | Archiviazione chiusa a chiave obbligatoria quando incustodito |
| **INTERNO** | Archiviazione chiusa a chiave a fine giornata |
| **PUBBLICO** | Buona pratica ma non obbligatoria |

### Requisiti di schermo libero

**Blocco dello schermo**: Tutte le workstation aziendali DEVONO bloccarsi automaticamente dopo un massimo di 5 minuti di inattività; questa base si applica indipendentemente dalla classificazione dei dati e DEVE essere applicata tramite la politica di gestione degli endpoint; gli utenti DEVONO bloccare manualmente gli schermi (Win+L / Ctrl+Cmd+Q) quando lasciano la workstation.

**Visualizzazione delle informazioni**: Le informazioni sensibili NON DEVONO essere visualizzate dove possono essere viste da persone non autorizzate; gli schermi per la privacy DEVONO essere utilizzati negli open space e nelle aree pubbliche; le sessioni di proiezione e condivisione dello schermo DEVONO essere terminate immediatamente dopo l'uso.

**Verifica**: Audit casuali della scrivania libera DEVONO essere condotti mensilmente; la non conformità DEVE essere segnalata ai responsabili diretti; la non conformità ripetuta DEVE essere escalata alle HR. Le liste di controllo degli audit sono archiviate nella Piattaforma GRC — Modulo di conformità; i documenti di non conformità sono conservati per 12 mesi.

## Smaltimento o riutilizzo sicuro delle apparecchiature (A.7.14)

### Requisiti pre-smaltimento

Tutte le apparecchiature DEVONO essere valutate per dati sensibili e software concesso in licenza prima dello smaltimento; le apparecchiature contenenti supporti di archiviazione DEVONO essere identificate e gestite per questa politica; i registri di gestione degli asset DEVONO essere aggiornati per riflettere lo smaltimento.

### Metodi di smaltimento

**Distruzione fisica** (obbligatoria per i dati RISERVATI): I supporti di archiviazione DEVONO essere fisicamente distrutti (tritatura, smagnetizzazione, disintegrazione); la distruzione DEVE essere eseguita da fornitori di servizi approvati; DEVE essere ottenuto e conservato un certificato di distruzione; la distruzione DEVE essere testimoniata o verificata.

**Sovrascrittura sicura** (accettabile per i dati INTERNI): I dati DEVONO essere sovrascritti utilizzando strumenti di cancellazione sicura approvati definiti in ISMS-IMP-A.7.6-7-14.3; i supporti magnetici DEVONO utilizzare metodi di sovrascrittura approvati; i supporti SSD/flash DEVONO utilizzare la cancellazione crittografica; la verifica della cancellazione riuscita DEVE essere eseguita; per gli asset RISERVATI, DEVE essere registrata una revisione di secondo verificatore.

**Eliminazione standard** (accettabile solo per i dati PUBBLICI).

### Metodi di smaltimento per tipo di apparecchiatura

| Tipo di apparecchiatura | RISERVATO | INTERNO | PUBBLICO |
|------------------------|-----------|---------|---------|
| Dischi rigidi (HDD) | Distruzione fisica | Sovrascrittura a 3 passaggi o distruzione | Formattazione |
| Unità a stato solido (SSD) | Distruzione fisica | Cancellazione crittografica o distruzione | Cancellazione sicura |
| Dispositivi mobili | Distruzione fisica | Ripristino del sistema + verifica | Ripristino del sistema |
| USB/Supporti rimovibili | Distruzione fisica | Sovrascrittura sicura o distruzione | Formattazione |
| Stampanti/Fotocopiatrici | Rimozione + distruzione HDD | Rimozione + cancellazione sicura HDD | Cancellazione della memoria |
| Apparecchiature di rete | N/D (cancellazione config) | Cancellazione config + verifica | Ripristino config |

### Requisiti di riutilizzo

**Riutilizzo interno**: Tutti i dati DEVONO essere cancellati in modo sicuro prima della riassegnazione; il software concesso in licenza DEVE essere trasferito o rimosso per i termini di licenza; i registri degli asset DEVONO essere aggiornati con il nuovo assegnatario.

**Riutilizzo esterno (Donazione/Vendita)**: Le apparecchiature RISERVATE NON DEVONO essere riutilizzate esternamente; le apparecchiature INTERNE DEVONO avere il supporto di archiviazione distrutto o cancellato in modo sicuro; tutti gli identificatori organizzativi DEVONO essere rimossi; le impostazioni predefinite di fabbrica DEVONO essere ripristinate.

### Custodia

**Detenzione interna**: I supporti/apparecchiature in attesa di cancellazione/distruzione DEVONO essere conservati in un'area di detenzione sicura designata con accesso limitato al personale di smaltimento autorizzato.

**Distruzione fuori sede**: Quando il supporto/le apparecchiature lasciano i locali di [Organizzazione] per la distruzione, la catena di custodia DEVE essere documentata includendo: data/ora di consegna, identificatori degli asset (numeri di serie), identità della parte cedente, identità della parte ricevente, riferimento di trasporto del fornitore. I certificati di distruzione DEVONO corrispondere ai numeri di serie registrati; le discrepanze DEVONO essere escalate immediatamente.

### Documentazione

**I documenti di smaltimento** DEVONO includere: etichetta dell'asset e numero di serie; livello di classificazione dei dati; metodo di smaltimento utilizzato; data dello smaltimento; persona che autorizza lo smaltimento; certificato di distruzione (ove applicabile); prove di verifica. **Conservazione**: I documenti di smaltimento DEVONO essere conservati per 7 anni.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità per le aree sicure e la gestione dei supporti |
|-------|-------------------------------------------------------------|
| **Direzione generale** | Approvare la politica, allocare risorse per le operazioni sicure |
| **RSSI** | Proprietà della politica, standard di smaltimento, supervisione della conformità |
| **Responsabile delle strutture** | Gestione delle aree sicure, audit della scrivania libera |
| **Operazioni IT** | Esecuzione dello smaltimento delle apparecchiature, verifica della cancellazione sicura |
| **Responsabili diretti** | Conformità del team alla scrivania/schermo libero, autorizzare lo smaltimento delle apparecchiature |
| **Tutto il personale** | Seguire le regole delle aree sicure, mantenere la scrivania/schermo libero, segnalare gli incidenti |

---

# Metriche di governance

- Tasso di superamento dell'audit della scrivania libera (obiettivo: >95%)
- Conformità al blocco dello schermo (obiettivo: 100%)
- Smaltimento con certificato (obiettivo: 100% per RISERVATO)
- Verifica della cancellazione sicura (obiettivo: 100%)
- Incidenti nelle aree sicure (obiettivo: 0)

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Area sicura** | Ubicazione fisicamente protetta con controlli di accesso dove vengono elaborate o archiviate informazioni sensibili |
| **Scrivania libera** | Pratica di rimozione di tutti i materiali sensibili dalle scrivanie quando non in uso |
| **Schermo libero** | Pratica di blocco o disconnessione degli schermi dei computer quando incustoditi |
| **Smaltimento sicuro** | Metodi di smaltimento delle apparecchiature che impediscono il recupero dei dati |
| **Cancellazione crittografica** | Distruzione delle chiavi di cifratura per rendere irrecuperabili i dati cifrati |
| **Smagnetizzazione** | Utilizzo di campi magnetici per cancellare dati dai supporti di archiviazione magnetici |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data da definire] |
| **Responsabile delle strutture** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per le aree sicure e la gestione dei supporti. Le procedure di attuazione sono documentate in ISMS-IMP-A.7.6-7-14 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
