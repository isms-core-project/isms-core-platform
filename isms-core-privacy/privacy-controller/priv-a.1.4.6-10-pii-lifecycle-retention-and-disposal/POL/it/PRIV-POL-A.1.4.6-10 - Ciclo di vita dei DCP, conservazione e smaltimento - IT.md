<!-- ISMS-CORE:POLICY:PRIV-POL-A.1.4.6-10-IT:privacy:POL:a.1.4.6-10 -->
**PRIV-POL-A.1.4.6-10 — Ciclo di vita dei DCP, conservazione e smaltimento**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Ciclo di vita dei DCP, conservazione e smaltimento |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | PRIV-POL-A.1.4.6-10 |
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

**Catena di approvazione** : Principale: RPD; Secondaria: Responsabile Legale/Conformità; Autorità finale: Direzione generale.

**Documenti correlati** :

- PRIV-POL-00 (Quadro di applicabilità normativa sulla privacy)
- PRIV-POL-01 (Quadro di governance e processo decisionale sulla privacy)
- PRIV-IMP-A.1.4.6-10-UG (Ciclo di vita dei DCP — Guida utente)
- PRIV-IMP-A.1.4.6-10-TG (Ciclo di vita dei DCP — Guida tecnica)
- PRIV-POL-A.1.4.2-5 (Minimizzazione dei dati — politica gemella)
- PRIV-POL-A.3.20-22 (Supporti fisici e sicurezza degli endpoint — esecuzione dello smaltimento)
- ISO/IEC 27701:2025 Controlli A.1.4.6, A.1.4.7, A.1.4.8, A.1.4.9, A.1.4.10
- RGPD Articolo 5(1)(e) (limitazione della conservazione); Articolo 17 (cancellazione); Articolo 32(1)(a) (sicurezza)
- LPD svizzera Articolo 6(4) (limitazione della conservazione); Articolo 7 (sicurezza delle trasmissioni)

**Applicabilità del ruolo** : Questa politica si applica a [Organizzazione] che agisce in qualità di **Titolare del trattamento unicamente**. I controlli A.1.4.6–A.1.4.10 sono specifici per il titolare del trattamento (Tabella A.1).

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la de-identificazione e la cancellazione dei DCP al termine del trattamento, la gestione dei file temporanei, i limiti di conservazione dei DCP, le procedure di smaltimento e i controlli di trasmissione — conformemente ai controlli da A.1.4.6 a A.1.4.10 di ISO/IEC 27701:2025.

**Perimetro** : Tutti i DCP detenuti da [Organizzazione] come titolare del trattamento dal momento in cui la finalità del trattamento è soddisfatta fino allo smaltimento confermato; tutti i file temporanei generati durante il trattamento dei DCP; qualsiasi trasmissione di DCP su reti dati.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27701:2025

**Controllo A.1.4.6 — De-identificazione e cancellazione dei DCP al termine del trattamento**
Il controllo A.1.4.6 richiede che [Organizzazione] cancelli i DCP o li renda non identificabili non appena non siano più necessari per la finalità per cui sono stati trattati.

**Controllo A.1.4.7 — File temporanei**
Il controllo A.1.4.7 richiede che [Organizzazione] smaltisca i file temporanei creati durante il trattamento dei DCP entro un periodo definito e documentato, utilizzando procedure documentate.

**Controllo A.1.4.8 — Conservazione**
Il controllo A.1.4.8 richiede che [Organizzazione] non conservi i DCP più a lungo del necessario per le finalità per cui vengono trattati.

**Controllo A.1.4.9 — Smaltimento**
Il controllo A.1.4.9 richiede che [Organizzazione] disponga di politiche, procedure e meccanismi documentati per lo smaltimento dei DCP.

**Controllo A.1.4.10 — Controlli di trasmissione dei DCP**
Il controllo A.1.4.10 richiede che [Organizzazione] applichi controlli appropriati ai DCP trasmessi su reti dati, progettati per garantire che i dati raggiungano la destinazione prevista.

## Quadro normativo

Questa politica opera all'interno del quadro normativo stabilito in PRIV-POL-00. I seguenti obblighi sono pertinenti:

**Obbligatorio (Livello 1)** (per PRIV-POL-00):

- **RGPD UE** : Articolo 5(1)(e) (limitazione della conservazione — non conservati più a lungo del necessario; conservazione più lunga per archiviazione/ricerca con garanzie appropriate); Articolo 17 (cancellazione — al termine della finalità, revoca del consenso, o richiesta di cancellazione accolta); Articolo 32(1)(a) (pseudonimizzazione e cifratura come misure di sicurezza, incluso in transito)
- **LPD svizzera** : Articolo 6(4) (conservazione — solo per il tempo necessario); Articolo 7 (sicurezza delle trasmissioni)
- **ISO/IEC 27701:2025** : Controlli A.1.4.6–A.1.4.10 (normativi)

---

# A.1.4.6 — De-identificazione e cancellazione al termine del trattamento

Quando i DCP non sono più necessari per le finalità di trattamento identificate, [Organizzazione] DEVE:

- **Cancellare** i DCP (distruzione irreversibile), OPPURE
- **De-identificare** i DCP in una forma che non consenta l'identificazione o la re-identificazione degli interessati (anonimizzazione — confermata dal RPD per PRIV-POL-A.1.4.2-5)

Questo obbligo si applica **non appena** la finalità non è più servita. Si applica a tutte le copie dei DCP: database primari, backup, archivi, log di trattamento e copie temporanee.

### Conservazione per obbligo legale contrario

Laddove un obbligo legale richieda la conservazione oltre la finalità del trattamento (es. registri fiscali, registri del lavoro, blocco legale), la conservazione DEVE essere:

- Limitata al periodo legalmente richiesto
- Limitata al perimetro minimo necessario (ove possibile, gli altri campi non richiesti dall'obbligo legale devono essere cancellati)
- Chiaramente registrata nel Calendario di conservazione con il riferimento alla disposizione legale

---

# A.1.4.7 — File temporanei

[Organizzazione] DEVE garantire che i file temporanei creati durante il trattamento dei DCP vengano smaltiti entro un periodo documentato e specificato.

### Tipi di file temporanei e periodi di smaltimento

| Tipo di file temporaneo | Conservazione massima | Metodo di smaltimento |
|------------------------|----------------------|----------------------|
| File di cache di trattamento (dati di sessione, risultati intermedi) | 24 ore dopo la fine della sessione o il completamento del trattamento | Eliminazione automatica |
| File di esportazione generati per richieste di accesso degli interessati | 72 ore dopo la trasmissione all'interessato | Cancellazione sicura |
| File di staging per elaborazione batch | 48 ore dopo il completamento del batch | Cancellazione sicura |
| File di debug / log di errori contenenti DCP | 30 giorni | Rotazione automatizzata con cancellazione sicura |
| Copie temporanee di sviluppo con DCP reali | Immediatamente dopo l'uso (per requisiti PRIV-POL-A.3.23-31 sui dati di test) | Cancellazione sicura approvata dal RPD con conferma |

I periodi di smaltimento specifici per altri tipi di file temporanei sono documentati in PRIV-IMP-A.1.4.6-10-TG. I meccanismi di eliminazione automatizzata sono preferiti alla cancellazione manuale.

---

# A.1.4.8 — Conservazione

[Organizzazione] NON DEVE conservare i DCP più a lungo del necessario per le finalità per cui vengono trattati.

### Calendario di conservazione

Il RPD mantiene un **Calendario di conservazione dei DCP** che specifica:

- Categoria di DCP o attività di trattamento
- Periodo di conservazione (da una data trigger definita: es. fine del contratto, ultimo utilizzo attivo, data di raccolta)
- Base legale o normativa per il periodo di conservazione (ove applicabile)
- Metodo di smaltimento alla scadenza

Il Calendario di conservazione è pubblicato internamente e fa parte del RAT. È rivisto al minimo annualmente e in caso di modifiche ai requisiti normativi o alle attività di trattamento.

### Blocchi legali

Laddove il Legale/Conformità identifichi un requisito di blocco legale, i DCP soggetti al blocco DEVONO essere conservati indipendentemente dalla loro data di smaltimento pianificata. I blocchi legali DEVONO essere:

- Autorizzati per iscritto dal Legale/Conformità o dalla Direzione generale
- Documentati nel Calendario di conservazione con la base del blocco e la data di fine prevista
- Rivisti al minimo trimestralmente; revocati tempestivamente una volta che la base del blocco non si applica più
- Applicati in modo ristretto al perimetro minimo di DCP necessario

I blocchi legali che non vengono formalmente rivisti e revocati diventano una fonte di conservazione illecita. Il RPD monitora tutti i blocchi legali attivi.

### Principi di conservazione

- I periodi di conservazione DEVONO essere basati su un'esigenza documentata (legale, contrattuale o operativa) — non sul principio di «conservare per ogni evenienza»
- Laddove più obblighi normativi creino diversi requisiti di conservazione per gli stessi dati, il periodo obbligatorio più lungo si applica per il perimetro legalmente richiesto; i dati in eccesso vengono cancellati al primo periodo applicabile
- I backup contenenti DCP DEVONO essere soggetti agli stessi limiti di conservazione dei dati primari — i calendari di conservazione dei backup DEVONO allinearsi ai periodi di conservazione dei DCP o disporre di un'eccezione documentata con controlli compensativi

---

# A.1.4.9 — Smaltimento

[Organizzazione] DEVE disporre di politiche, procedure e meccanismi documentati per lo smaltimento dei DCP.

### Requisiti di smaltimento

Lo smaltimento dei DCP DEVE essere:

- **Irreversibile**: I DCP smaltiti non possono essere recuperati con mezzi tecnici ordinari
- **Documentato**: Ogni azione di smaltimento è registrata (cosa è stato smaltito, quando, da chi, metodo)
- **Verificato**: Ove tecnicamente fattibile, lo smaltimento è confermato da verifica automatizzata o manuale
- **Conforme alla gestione della classificazione**: Lo smaltimento dei DCP RISERVATI utilizza il metodo più rigoroso per PRIV-POL-A.3.20-22

### Metodi di smaltimento

| Posizione dei dati | Metodo di smaltimento |
|-------------------|----------------------|
| Record di database | SQL DELETE o equivalente; o anonimizzazione in loco dove la cancellazione crea problemi di integrità dei dati (con approvazione RPD) |
| File system (elettronico) | Cancellazione crittografica (se cifrato) o standard di sovrascrittura approvato |
| Supporti di backup | Sovrascrittura per ciclo di backup allineata al calendario di conservazione; o distruzione fisica per supporti di backup scaduti |
| Documenti fisici | Triturazione trasversale (RISERVATO), triturazione trasversale + testimone (LIMITATO) |
| Archiviazione cloud | Cancellazione tramite API/console approvata; conferma della cancellazione dal fornitore ove disponibile |

Le procedure di smaltimento sono dettagliate in PRIV-IMP-A.1.4.6-10-TG.

### Trigger di smaltimento

Lo smaltimento dei DCP DEVE essere innescato da:

- La scadenza del periodo di conservazione per il Calendario di conservazione
- La cessazione della finalità del trattamento (quando non si applica alcun obbligo legale contrario)
- La richiesta di cancellazione di un interessato (per PRIV-POL-A.1.3.5-10) — entro il termine di risposta richiesto
- La revoca del consenso (per il trattamento basato sul consenso senza altra base)
- La fine del contratto o del rapporto di lavoro (per le categorie di DCP applicabili)

---

# A.1.4.10 — Controlli di trasmissione dei DCP

[Organizzazione] DEVE sottoporre i DCP trasmessi su reti dati a controlli appropriati per garantire che i dati raggiungano la destinazione prevista.

### Requisiti di controllo delle trasmissioni

- Tutti i DCP trasmessi su reti DEVONO essere cifrati in transito utilizzando gli standard TLS attuali (minimo TLS 1.2; TLS 1.3 preferito)
- I DCP trasmessi a terze parti DEVONO utilizzare metodi di trasferimento sicuro approvati per PRIV-POL-A.3.5-7 (regole di trasferimento)
- La trasmissione non cifrata di DCP RISERVATI o LIMITATI su reti pubbliche è vietata
- Deve essere ottenuta la conferma di consegna o la ricevuta di conferma per i trasferimenti di DCP LIMITATI (categoria speciale)
- I log di trasmissione DEVONO essere mantenuti per i trasferimenti di DCP RISERVATI e LIMITATI per PRIV-POL-A.3.25 (registrazione)

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Responsabile della Protezione dei Dati (RPD)** | Proprietario del Calendario di conservazione; approva le eccezioni di smaltimento; conferma l'anonimizzazione; monitora la conformità allo smaltimento; risponde alle richieste di cancellazione che coinvolgono conflitti di conservazione |
| **Proprietario dei dati** | Avvia lo smaltimento alla scadenza del periodo di conservazione nel proprio dominio; escalate i conflitti di smaltimento al RPD |
| **Team Sicurezza IT** | Implementa i meccanismi di smaltimento automatizzati; esegue l'allineamento della conservazione dei backup; mantiene i log di smaltimento; configura la cifratura delle trasmissioni |
| **Legale/Conformità** | Consulenza sui requisiti di blocco legale; identifica i periodi di conservazione legalmente obbligatori |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Calendario di conservazione dei DCP | Periodi di conservazione documentati per categoria di DCP, con base legale | In corso + 3 anni |
| Log di smaltimento | Registrazioni delle azioni di smaltimento dei DCP con data, metodo e perimetro | 5 anni |
| Conferma di eliminazione dei file temporanei | Conferma automatizzata o manuale dello smaltimento dei file temporanei | 3 anni dalla data di eliminazione |
| Configurazione della cifratura delle trasmissioni | Registrazioni di configurazione TLS per i sistemi che trasportano DCP | In corso + 3 anni |
| Registrazioni di revisione del Calendario di conservazione | Prove di revisione annuale | 3 anni dalla data della revisione |

---

# Considerazioni di audit

- Calendario di conservazione con periodi documentati e base legale per tutte le categorie di DCP
- Prove delle azioni di smaltimento nei periodi pianificati
- Nessun DCP conservato oltre il periodo di conservazione documentato senza una base legale documentata
- Meccanismi di eliminazione dei file temporanei configurati e verificati
- Applicazione di TLS per i DCP in transito (prove di configurazione)
- Log di smaltimento che mostrano il metodo e i tempi

---

<!-- QA_VERIFIED: 2026-04-03 -->
