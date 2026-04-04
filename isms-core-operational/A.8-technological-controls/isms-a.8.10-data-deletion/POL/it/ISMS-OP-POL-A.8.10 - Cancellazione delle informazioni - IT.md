<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.10-IT:operational:OP-POL:a.8.10 -->
**ISMS-OP-POL-A.8.10 — Cancellazione delle informazioni**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Cancellazione delle informazioni |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.10 |
| **Creatore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione esecutiva |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.10 — Cancellazione delle informazioni

**Controlli Allegato A correlati**:

| Controllo | Relazione con la cancellazione delle informazioni |
|-----------|--------------------------------------------------|
| A.5.9 Inventario delle informazioni e delle altre risorse associate | L'inventario delle risorse definisce l'ambito di cancellazione e la titolarità dei dati |
| A.5.10 Uso accettabile delle informazioni e delle altre risorse associate | Il ciclo di vita dell'uso accettabile include la cancellazione a fine vita |
| A.5.12–13 Classificazione e etichettatura delle informazioni | La classificazione determina il metodo di cancellazione e il livello di verifica |
| A.5.14 Trasferimento delle informazioni | Obblighi di cancellazione dopo il completamento del trasferimento |
| A.5.33 Protezione dei documenti | I calendari di conservazione dei documenti attivano la cancellazione alla scadenza |
| A.5.34 Privacy e protezione dei dati personali | Diritto di cancellazione degli interessati; obblighi di cancellazione dei dati personali |
| A.7.10 Supporti di memorizzazione | Sanificazione e smaltimento dei supporti fisici |
| A.7.14 Smaltimento sicuro o riutilizzo delle attrezzature | La dismissione delle attrezzature richiede la cancellazione dei dati |
| A.8.13 Backup delle informazioni | Le copie di backup sono incluse nell'ambito di cancellazione |
| A.8.24 Uso della crittografia | La cancellazione crittografica come metodo di cancellazione |

**Politiche interne correlate**:

- Politica di classificazione e gestione delle informazioni
- Politica di privacy e protezione dei dati personali
- Politica di protezione delle informazioni e gestione dei documenti
- Politica di backup
- Politica di gestione delle risorse
- Politica sull'uso della crittografia

---

# Politica di cancellazione delle informazioni

## Scopo

Lo scopo della presente politica è garantire che le informazioni memorizzate nei sistemi informativi, nei dispositivi o in qualsiasi altro supporto di memorizzazione vengano cancellate quando non sono più necessarie, utilizzando metodi appropriati alla sensibilità dei dati e al tipo di supporto, per prevenire esposizioni non necessarie e per conformarsi ai requisiti legali, normativi e contrattuali.

La presente politica supporta la nLPD svizzera (revDSG) Art. 6 cpv. 4 (proporzionalità e minimizzazione dei dati — i dati personali devono essere distrutti o resi anonimi non appena non sono più necessari allo scopo del trattamento) e Art. 8 (misure tecniche e organizzative per la sicurezza dei dati). Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche il GDPR Art. 5(1)(e) (limitazione della conservazione) e Art. 17 (diritto alla cancellazione).

## Ambito di applicazione

Tutti i dipendenti e gli utenti di terze parti.

Tutte le informazioni trattate, memorizzate o trasmesse su o in sistemi, dispositivi e supporti di proprietà, gestiti e controllati dall'organizzazione rientranti nell'ambito della dichiarazione di applicabilità ISO 27001.

Ciò include:

- Tutte le categorie di dati (dati personali, informazioni aziendali riservate, documenti finanziari, dati tecnici, comunicazioni, log)
- Tutte le ubicazioni di storage (in sede, cloud, terze parti, backup, disaster recovery)
- Tutti i tipi di supporti (magnetico, a stato solido, ottico, cartaceo, supporti rimovibili, dispositivi mobili)
- Tutte le fasi del ciclo di vita (uso attivo, archiviazione, backup, sviluppo/test, fine vita)

## Principio

Le informazioni non devono essere conservate più a lungo di quanto richiesto per il loro scopo aziendale, legale o normativo dichiarato. Quando i periodi di conservazione scadono, o quando si verifica un trigger di cancellazione valido, le informazioni devono essere cancellate utilizzando un metodo appropriato alla sensibilità dei dati e al tipo di supporto, con prove verificabili che la cancellazione sia stata eseguita.

Devono essere utilizzati solo metodi di cancellazione approvati dall'organizzazione. La cancellazione standard del sistema operativo (es. "elimina" o "svuota il cestino") è insufficiente per i dati riservati o personali, poiché tali metodi sono tipicamente recuperabili.

---

## Calendari di conservazione e trigger di cancellazione

### Calendario di conservazione

L'organizzazione deve mantenere un calendario di conservazione che definisca i periodi di conservazione per tutte le categorie di dati. I periodi di conservazione devono essere basati sul requisito applicabile più lungo tra:

- Obblighi legali e normativi (CO svizzero, nLPD, legislazione fiscale)
- Requisiti normativi (regolamenti specifici del settore)
- Obblighi contrattuali (accordi con clienti, fornitori, partner)
- Esigenza aziendale documentata (con approvazione del proprietario)

Laddove si applichino più requisiti agli stessi dati, prevale il periodo di conservazione applicabile più lungo, salvo che il Consulente legale non determini diversamente.

**Periodi di conservazione di riferimento per le PMI svizzere**:

| Categoria di dati | Conservazione minima | Base legale | Note |
|-------------------|---------------------|-------------|------|
| **Documenti contabili** (relazioni annuali, relazioni di revisione, bilanci) | 10 anni dalla fine dell'esercizio finanziario | CO svizzero Art. 958f | Devono essere conservati in forma scritta e firmata (relazioni annuali/di revisione) o elettronicamente con garanzia di integrità |
| **Giustificativi contabili** (fatture, ricevute, estratti conto, documenti IVA) | 10 anni dalla fine dell'esercizio finanziario | CO svizzero Art. 958f | Possono essere conservati elettronicamente per i requisiti Olico |
| **Contratti di lavoro e fascicoli HR** | 10 anni dalla fine del rapporto di lavoro | CO svizzero Art. 127–128 (termini di prescrizione); requisiti cantonali | Pretese salariali: prescrizione 5 anni (CO Art. 128); certificati di lavoro: prescrizione 10 anni (CO Art. 127) |
| **Registrazioni buste paga e assicurazione sociale** | 10 anni dalla fine dell'esercizio finanziario | CO svizzero Art. 958f; requisiti AVS/AI | Include estratti stipendiali, contributi previdenziali |
| **Documenti fiscali** | 10 anni dalla fine dell'esercizio finanziario | CO svizzero Art. 958f; diritto fiscale cantonale | Include documentazione fiscale aziendale e IVA |
| **Contratti con i clienti** | Durata + 10 anni | CO svizzero Art. 127 (prescrizione generale) | Prescrizione decennale per le pretese contrattuali |
| **Contratti con fornitori e venditori** | Durata + 10 anni | CO svizzero Art. 127 | Conservare per il termine di prescrizione dopo la fine del contratto |
| **Dati personali (generali)** | Solo per il tempo necessario allo scopo del trattamento | nLPD Art. 6 cpv. 4 | Devono essere cancellati o resi anonimi quando lo scopo è stato raggiunto |
| **Registrazioni del consenso degli interessati** | Durata del trattamento + 3 anni | nLPD Art. 6; buona pratica | Prova della base giuridica per il trattamento |
| **Log di sicurezza e piste di audit** | 12 mesi (online), fino a 3 anni (archivio) | Politica organizzativa; OPDo Art. 4 | Conservazione più lunga per i log di trattamento di dati sensibili |
| **Prove di audit del SGSI** | Minimo 3 anni | Ciclo di certificazione ISO 27001 | Conservare nell'intero ciclo di certificazione |
| **Registrazioni delle indagini sugli incidenti** | 3 anni dalla chiusura | Politica organizzativa | Più lunga se si prevede un contenzioso |

Questa tabella fornisce periodi minimi di riferimento. Il Responsabile dei documenti deve mantenere il calendario di conservazione autorevole, che deve essere rivisto annualmente dal Consulente legale e approvato dalla Direzione esecutiva.

### Trigger di cancellazione

La cancellazione deve essere avviata quando si verifica uno dei seguenti eventi:

| # | Evento trigger | Parte responsabile | Tempistica |
|---|---------------|-------------------|-----------|
| 1 | **Scadenza del periodo di conservazione** | Responsabile dei documenti / Proprietario del sistema | Entro 90 giorni dalla scadenza (automatizzato ove fattibile) |
| 2 | **Richiesta di cancellazione dell'interessato** (nLPD / GDPR Art. 17) | DPD / Consulente privacy | Entro 30 giorni dalla richiesta validata |
| 3 | **Risoluzione del contratto o dell'accordo di servizio** | Proprietario del sistema | Per i termini contrattuali (predefinito: 90 giorni) |
| 4 | **Completamento dello scopo del trattamento** | Proprietario dei dati | Entro 90 giorni dal completamento dello scopo |
| 5 | **Rilascio del blocco legale** | Consulente legale | Entro 90 giorni dal rilascio del blocco |
| 6 | **Dismissione delle risorse** | IT Operations | Prima che la risorsa lasci il controllo organizzativo |
| 7 | **Revoca del consenso** | DPD / Consulente privacy | Entro 30 giorni (salvo che si applichi un'altra base giuridica) |

Laddove la cancellazione automatizzata sia tecnicamente fattibile, deve essere implementata con misure di salvaguardia contro la cancellazione prematura (controlli dei blocchi legali, notifica al proprietario del business). Laddove l'automazione non sia fattibile, le procedure di cancellazione manuale devono essere documentate con punti di verifica definiti.

---

## Metodi di cancellazione

### Standard di sanificazione

I metodi di cancellazione devono essere allineati con NIST SP 800-88 Rev. 2 (Linee guida per la sanificazione dei supporti, settembre 2025), che definisce tre livelli di sanificazione, e IEEE 2883 per le tecniche di sanificazione specifiche per tipo di supporto.

| Livello di sanificazione | Descrizione | Quando utilizzare | Metodi di esempio |
|--------------------------|-------------|-------------------|--------------------|
| **Cancellazione (Clear)** | Tecniche logiche che rendono i dati inaccessibili attraverso le interfacce standard; il ripristino è possibile con strumenti specializzati | Supporti che rimangono sotto il controllo organizzativo; dati a bassa sensibilità (Pubblici, Interni) | Sovrascrittura standard, ripristino delle impostazioni del produttore, cancellazione sicura del sistema operativo |
| **Eliminazione (Purge)** | Tecniche fisiche o logiche che rendono i dati inaccessibili anche con strumenti di laboratorio specializzati | Supporti che lasciano il controllo organizzativo; dati sensibili (Riservati); riutilizzo dei supporti da parte di terze parti | Cancellazione crittografica, cancellazione a blocchi (flash/SSD), degaussing (supporti magnetici) |
| **Distruzione (Destroy)** | Distruzione fisica che rende i supporti inutilizzabili e il recupero dei dati non praticabile | Supporti a fine vita; dati di massima sensibilità; supporti senza valore futuro | Disintegrazione, polverizzazione, incenerimento, fusione, triturazione |

### Metodo di cancellazione per classificazione e supporto

| Classificazione dei dati | Supporti che rimangono in-house | Supporti che lasciano l'organizzazione | Supporti a fine vita |
|--------------------------|----------------------------------|----------------------------------------|----------------------|
| **Pubblico** | Cancellazione | Cancellazione | Distruzione (o riciclaggio se verificato cancellato) |
| **Interno** | Cancellazione | Eliminazione | Distruzione |
| **Riservato** | Eliminazione | Eliminazione | Distruzione |
| **Strettamente riservato** | Eliminazione | Distruzione | Distruzione |

### Documenti cartacei

| Classificazione dei dati | Metodo di smaltimento |
|--------------------------|-----------------------|
| **Pubblico** | Rifiuti generali o riciclaggio |
| **Interno** | Distruzione a taglio incrociato (DIN 66399 P-3 minimo) |
| **Riservato** | Distruzione a taglio incrociato (DIN 66399 P-4 minimo) o incenerimento testimoniato |
| **Strettamente riservato** | DIN 66399 P-5 minimo o distruzione certificata da terze parti con certificato |

### Cancellazione crittografica

La cancellazione crittografica può essere utilizzata come metodo valido a livello di Eliminazione (Purge) laddove i dati siano stati crittografati a riposo e la crittografia soddisfi gli standard organizzativi (per la Politica sull'uso della crittografia). Affinché la cancellazione crittografica costituisca una cancellazione ai sensi della presente politica:

- Tutti i dati target devono essere stati crittografati prima dell'archiviazione (la crittografia applicata retroattivamente non è sufficiente).
- L'algoritmo di crittografia deve soddisfare gli standard minimi approvati (AES-256 o equivalente).
- Deve esistere una mappatura documentata dati-chiave, che consenta l'identificazione di quali chiavi di crittografia proteggono quali dati.
- La distruzione delle chiavi deve essere eseguita attraverso un processo verificato (azzeramento delle chiavi HSM, cancellazione delle chiavi KMS con log di audit o equivalente).
- Le prove della distruzione delle chiavi devono essere conservate (log di audit, certificati HSM) per un minimo di 3 anni.
- Anche le copie di backup della chiave di crittografia devono essere distrutte — se esiste un backup, un escrow o uno storage esterno della chiave e non è possibile verificarne la distruzione, la cancellazione crittografica non deve essere accettata come unico metodo di cancellazione.

### Cancellazione dei backup

La cancellazione nei sistemi di produzione deve estendersi a tutte le copie di backup contenenti i dati cancellati, inclusi:

- Backup completi, incrementali e differenziali
- Snapshot e copie point-in-time
- Repliche di disaster recovery
- Backup a livello applicativo (esportazioni database, esportazioni VM)
- Servizi di backup nativi cloud con politiche di conservazione indipendenti

Laddove la cancellazione immediata dai backup non sia tecnicamente fattibile (es. nastri di backup immutabili, backup cloud con blocco della conservazione), l'organizzazione deve:

1. Documentare il calendario di conservazione dei backup indicando quando i dati saranno naturalmente sovrascritti o scaduti.
2. Ottenere l'approvazione del RSSI e del Proprietario dei dati per il periodo di conservazione esteso.
3. Applicare controlli di accesso per impedire il ripristino dei dati dal backup.
4. Tracciare la cancellazione in sospeso nel registro delle cancellazioni fino alla conferma del completamento.

---

## Cancellazione da parte di terze parti e cloud

### Requisiti contrattuali

Tutti i contratti con terze parti che trattano dati organizzativi devono includere obblighi di cancellazione che specificano:

- Tempistica massima di cancellazione dopo la risoluzione del contratto o su richiesta scritta (predefinito: 30 giorni)
- Standard di sanificazione appropriato alla sensibilità dei dati (con riferimento ai livelli NIST SP 800-88)
- Ambito di cancellazione che copre tutte le copie, inclusi backup, cache, log e repliche di disaster recovery
- Obbligo di fornire la verifica della cancellazione (certificato di distruzione o attestazione equivalente)
- Trasferimento degli obblighi di cancellazione ai sub-responsabili del trattamento
- Diritto di audit sulla conformità della cancellazione

### Valutazione del fornitore di servizi cloud

Prima di contrarre con un fornitore di servizi cloud, l'organizzazione deve valutare le capacità di cancellazione tra cui:

- Supporto API per la cancellazione dei dati e la verifica della cancellazione
- Propagazione della cancellazione a tutte le regioni, zone di disponibilità e repliche
- Garanzia di isolamento multi-tenant (la cancellazione non influisce sugli altri tenant; gli altri tenant non possono accedere ai dati residui)
- Capacità e tempistiche di cancellazione di backup e snapshot
- Controlli sulla remanenza dei dati dopo la cancellazione
- Certificazione o attestazione delle pratiche di cancellazione (SOC 2 Tipo II, ISO 27001 con A.8.10 nell'ambito)

### Verifica della cancellazione da parte di terze parti

L'organizzazione deve ottenere la verifica della cancellazione da terze parti attraverso uno o più dei seguenti metodi:

**Distruzione fisica dei supporti** — Certificati di distruzione che includono:
- Numeri seriali o identificatori delle risorse dei supporti
- Metodo di distruzione (con riferimento al livello NIST SP 800-88 o al livello di sicurezza DIN 66399)
- Data e luogo di distruzione
- Nome dell'emittente del certificato e accreditamento (es. NAID AAA, ISO 21964)

**Cancellazione logica da parte del fornitore di servizi** — Uno dei seguenti:
- Report SOC 2 Tipo II con test del controllo di cancellazione
- Report di audit indipendente che verifica le procedure di cancellazione
- Certificazione ISO 27001 con A.8.10 nell'ambito

**Cancellazione tramite API cloud/SaaS** — Prove registrate che includono:
- Timestamp della chiamata API e utente autenticato
- Identificatori delle risorse eliminate
- Risposta HTTP di successo (200/204)
- Conferma della cancellazione di backup/snapshot laddove il fornitore lo supporti

Per i dati Riservati e Strettamente riservati: sono richiesti certificati di fornitori di distruzione accreditati o report di audit indipendenti. I soli log API sono insufficienti.

### Escalation per il fallimento della cancellazione da parte di terze parti

| Tempistica | Azione | Responsabile |
|-----------|--------|-------------|
| T+0 giorni | Registrare il fallimento nel registro dei gap; avviare il follow-up con il contatto della terza parte | IT Operations |
| T+15 giorni | Escalation al responsabile dell'account della terza parte; copia al RSSI e al DPD | Proprietario del sistema |
| T+30 giorni | Escalation al contatto esecutivo della terza parte; avviare la revisione del contratto con il Consulente legale | RSSI |
| T+45 giorni | Esaminare i rimedi contrattuali (crediti di servizio, risoluzione per violazione sostanziale); considerare la migrazione dei dati verso un fornitore conforme | Direzione esecutiva |

Per i dati Riservati/Strettamente riservati, i tempi di escalation sono accelerati: T+7, T+15, T+21 giorni.

---

## Richieste di cancellazione degli interessati

### Accettazione ed elaborazione delle richieste

L'organizzazione deve accettare ed elaborare le richieste di cancellazione degli interessati in conformità con la nLPD svizzera Art. 6 cpv. 4 e, ove applicabile, il GDPR Art. 17 (diritto alla cancellazione / diritto all'oblio).

**Processo di gestione delle richieste**:

| Fase | Azione | Tempistica | Responsabile |
|------|--------|-----------|-------------|
| 1 | Ricevere la richiesta (e-mail, modulo web, posta, di persona) | — | DPD / Consulente privacy |
| 2 | Registrare la richiesta nel registro delle richieste degli interessati | Entro 24 ore | DPD / Consulente privacy |
| 3 | Verificare l'identità dell'interessato | Entro 5 giorni lavorativi | DPD / Consulente privacy |
| 4 | Identificare tutti i sistemi, i database e i backup contenenti i dati personali dell'interessato | Entro 10 giorni lavorativi | IT Operations / Proprietari dei sistemi |
| 5 | Valutare se sussiste l'obbligo di cancellazione o se esiste un'eccezione legale | Entro 15 giorni lavorativi | DPD + Consulente legale |
| 6 | Eseguire la cancellazione o emettere un diniego motivato | Entro 25 giorni lavorativi | IT Operations / DPD |
| 7 | Confermare il completamento all'interessato per iscritto | Entro 30 giorni dalla richiesta | DPD / Consulente privacy |

### Eccezioni legali alla cancellazione

La cancellazione può essere rifiutata laddove il trattamento sia necessario per:

- Conformarsi a un obbligo legale di conservazione (es. CO svizzero Art. 958f documenti contabili, obblighi fiscali)
- Accertamento, esercizio o difesa di diritti in sede giudiziaria
- Finalità di archiviazione nel pubblico interesse, ricerca scientifica o storica
- Motivi di interesse pubblico nel settore della sanità pubblica
- Esercizio del diritto di libertà di espressione e di informazione

Laddove la cancellazione venga negata sulla base di un'eccezione legale:

1. Documentare la base giuridica specifica su cui ci si fonda.
2. Fornire all'interessato una spiegazione scritta che includa l'eccezione invocata e i diritti di reclamo (diritto di presentare un reclamo all'IFPDT o all'autorità di vigilanza competente).
3. Applicare la limitazione del trattamento ove possibile (dati conservati ma non trattati attivamente).
4. Stabilire una data di revisione per rivalutare se l'eccezione sia ancora applicabile.

### Notifica a terze parti

Laddove i dati personali oggetto di una richiesta di cancellazione siano stati comunicati a terze parti, l'organizzazione deve notificare a tali terze parti la richiesta di cancellazione ai sensi del GDPR Art. 19 e degli obblighi nLPD, salvo che ciò si riveli impossibile o comporti uno sforzo sproporzionato.

---

## Gestione dei blocchi legali

### Trigger dei blocchi legali

La cancellazione deve essere sospesa quando i dati sono soggetti a un blocco legale per uno dei seguenti motivi:

- Contenzioso (instaurato, minacciato o ragionevolmente previsto)
- Indagine governativa o ispezione regolamentare
- Indagine interna che richiede la conservazione forense (frode, illecito, violazione dei dati)
- Audit esterno che richiede la conservazione di dati specifici

### Istituzione e rilascio

Solo il Consulente legale (o il Responsabile legale/compliance designato) può istituire o rilasciare un blocco legale.

**Processo di emissione**:

1. Il Consulente legale emette una formale comunicazione di blocco che documenta: nome/numero del caso, ambito (sistemi, intervalli di date, custodi, categorie di dati), data di entrata in vigore, obblighi di conservazione.
2. I custodi interessati vengono notificati entro 24 ore e devono confermare la ricezione entro 2 giorni lavorativi.
3. IT Operations sospende la cancellazione automatizzata per i sistemi interessati entro 48 ore e conferma la sospensione per iscritto.
4. Il Consulente legale mantiene il Registro dei blocchi legali con: ID del blocco, nome del caso, data di emissione, ambito, sistemi interessati, custodi, stato delle conferme, date di revisione.

### Revisione trimestrale

I blocchi legali devono essere rivisti almeno trimestralmente dal Consulente legale. Ogni revisione deve produrre una valutazione documentata che includa:

- Identificatore del blocco e data di istituzione
- Stato attuale del contenzioso/dell'indagine
- Determinazione della necessità continuata con base giuridica
- Adeguamento dell'ambito se applicabile (restringimento a categorie di dati specifiche)
- Data di rilascio anticipata del blocco o condizione trigger
- Nome del revisore e data di revisione

### Rilascio del blocco e cancellazione post-blocco

Al rilascio del blocco:

1. Il Consulente legale emette una formale comunicazione di rilascio del blocco.
2. I custodi e IT Operations vengono notificati entro 24 ore.
3. IT Operations riabilita i normali calendari di cancellazione.
4. I dati conservati oltre il normale periodo di conservazione esclusivamente a causa del blocco legale devono essere cancellati entro 90 giorni dal rilascio del blocco, salvo che esista una giustificazione aziendale approvata.

### Conflitto con le richieste di cancellazione

Quando una richiesta di cancellazione dell'interessato è in conflitto con un blocco legale attivo:

- Il blocco legale prevale.
- Deve essere applicata la limitazione del trattamento (dati conservati ma non utilizzati attivamente).
- La cancellazione deve essere eseguita entro 30 giorni dal rilascio del blocco.
- L'interessato deve essere informato che la richiesta è stata registrata ma non può essere soddisfatta al momento, citando l'eccezione legale applicabile, senza divulgare dettagli che potrebbero pregiudicare i procedimenti legali.

---

## Verifica e prove

### Pista di audit delle cancellazioni

L'organizzazione deve mantenere piste di audit delle cancellazioni che includano:

| Campo | Descrizione |
|-------|-------------|
| **Timestamp della cancellazione** | Data e ora in cui è stata eseguita la cancellazione |
| **Categoria dei dati** | Tipo e classificazione dei dati cancellati |
| **Metodo di cancellazione** | Metodo di sanificazione applicato (Cancellazione / Eliminazione / Distruzione / Cancellazione crittografica) |
| **Identificatore del supporto** | Nome del sistema, numero seriale del dispositivo o ubicazione dello storage |
| **Trigger di cancellazione** | Evento che ha avviato la cancellazione (scadenza della conservazione, richiesta dell'interessato, dismissione, ecc.) |
| **Parte responsabile** | Persona o sistema che ha eseguito la cancellazione |
| **Risultato della verifica** | Conferma che la cancellazione è avvenuta con successo |

### Conservazione dei log di cancellazione

I log di cancellazione devono essere conservati per un minimo di 3 anni o il requisito normativo applicabile, a seconda di quale sia il periodo più lungo. I log di cancellazione non devono contenere i dati cancellati stessi — solo i metadati sull'evento di cancellazione.

### Metodi di verifica

L'efficacia della cancellazione deve essere verificata attraverso:

- **Verifica automatizzata**: Conferma generata dal sistema della cancellazione avvenuta con successo (risposta API, output del tool, voce del log)
- **Campionamento periodico**: Campionamento trimestrale dei registri di cancellazione per verificare completezza e accuratezza (minimo 10% delle cancellazioni per trimestre)
- **Attestazione di terze parti**: Certificati di distruzione per supporti fisici e fornitori di servizi esterni
- **Spot check**: Spot check annuale di sistemi selezionati casualmente per confermare l'assenza di dati oltre il loro periodo di conservazione

---

## Gestione delle eccezioni

### Richieste di eccezione

Le eccezioni alle procedure standard di cancellazione richiedono una richiesta documentata che includa:

- Categoria e classificazione dei dati
- Giustificazione aziendale per l'eccezione
- Valutazione del rischio (qual è il rischio di conservare i dati oltre il periodo normale?)
- Controlli compensativi per mitigare il rischio di conservazione
- Data di scadenza proposta (le eccezioni non devono essere a tempo indeterminato)

### Autorità di approvazione

| Classificazione dei dati | Durata dell'eccezione | Approvatori |
|--------------------------|----------------------|-------------|
| Interno | Fino a 12 mesi | Proprietario del sistema + RSSI |
| Riservato | Fino a 6 mesi | RSSI + DPD |
| Strettamente riservato | Qualsiasi durata | RSSI + DPD + Consulente legale + Direzione esecutiva |

### Eccezioni vietate

Le seguenti eccezioni non devono essere concesse:

- Conservazione a tempo indeterminato senza una data di scadenza specifica o un trigger di revisione
- Eccezioni per eludere richieste legittime di cancellazione degli interessati
- Eccezioni per aggirare le limitazioni normative alla conservazione
- Eccezioni generali per intere categorie di dati senza giustificazione specifica e documentata

### Registro delle eccezioni

Tutte le eccezioni approvate devono essere registrate nel registro delle eccezioni con proprietario, data di approvazione, data di scadenza, controlli compensativi e calendario di revisione. Le eccezioni devono essere riviste trimestralmente e scadono automaticamente salvo rinnovo attraverso il processo di approvazione.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Cancellazione delle informazioni** | Il processo di rimozione dei dati dai supporti di memorizzazione in modo tale che non possano essere recuperati con mezzi normali o, a seconda del livello di sanificazione, specializzati |
| **Sanificazione dei dati** | Tutti i metodi per rendere i dati inaccessibili, inclusa la cancellazione logica, l'eliminazione fisica e la distruzione |
| **Cancellazione (Clear)** | Sanificazione logica che protegge dal recupero dei dati tramite strumenti standard del sistema operativo o semplici tecniche non invasive |
| **Eliminazione (Purge)** | Sanificazione fisica o logica che protegge dal recupero dei dati tramite tecniche di attacco di livello laboratorio |
| **Distruzione (Destroy)** | Distruzione fisica che rende i supporti inutilizzabili e il recupero dei dati non praticabile con qualsiasi tecnica nota |
| **Cancellazione crittografica** | Metodo di cancellazione che rende i dati crittografati irrecuperabili distruggendo in modo sicuro le chiavi di crittografia |
| **Periodo di conservazione** | Arco temporale definito durante il quale i dati devono essere conservati prima che la cancellazione sia consentita o richiesta |
| **Trigger di cancellazione** | Evento o condizione che avvia il processo di cancellazione (es. scadenza della conservazione, richiesta di cancellazione) |
| **Blocco legale** | Sospensione della cancellazione per conservare i dati ai fini di contenzioso, indagine, ispezione normativa o audit |
| **Richiesta di cancellazione dell'interessato** | Richiesta di un interessato che esercita il proprio diritto alla cancellazione ai sensi della nLPD o del GDPR Art. 17 |
| **Certificato di distruzione** | Attestazione di terze parti che i supporti fisici sono stati distrutti secondo uno standard specifico |
| **Remanenza dei dati** | Dati residui che rimangono sui supporti di memorizzazione dopo i tentativi di cancellazione; il rischio che i metodi di sanificazione cercano di eliminare |
| **Proprietario dei dati** | Individuo o ruolo responsabile della definizione dello scopo aziendale, del periodo di conservazione e dei requisiti di cancellazione per una categoria di dati |
| **Responsabile dei documenti** | Ruolo responsabile del mantenimento del calendario di conservazione organizzativo e della supervisione dei processi di smaltimento |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **RSSI** | Titolarità della politica; approvazione dei metodi di cancellazione; approvazione delle eccezioni; monitoraggio della conformità e metriche; punto di escalation per le mancate cancellazioni |
| **DPD / Consulente privacy** | Gestione delle richieste di cancellazione degli interessati; conformità alla privacy; revisione del calendario di conservazione per i dati personali; approvazione delle eccezioni (Riservato+) |
| **Consulente legale** | Gestione dei blocchi legali (istituzione, revisione, rilascio); termini contrattuali con terze parti (clausole di cancellazione); interpretazione normativa; valutazione delle eccezioni alla cancellazione |
| **Responsabile dei documenti** | Manutenzione e revisione annuale del calendario di conservazione; supervisione dello smaltimento; gestione del registro delle cancellazioni; monitoraggio e reportistica di conformità |
| **IT Operations** | Esecuzione della cancellazione; gestione e manutenzione degli strumenti di cancellazione; cancellazione dei backup; registrazione e verifica; coordinamento della cancellazione con terze parti |
| **Proprietari di sistema** | Implementazione della cancellazione specifica del sistema; coordinamento con IT Operations; richieste di eccezione; valutazione della fattibilità della cancellazione automatizzata |
| **Proprietari dei dati** | Definizione del periodo di conservazione per le categorie di dati di loro competenza; approvazione della cancellazione dei dati critici per il business; decisioni di classificazione |
| **Tutto il personale** | Gestire i dati secondo i requisiti di classificazione e conservazione; non conservare i dati oltre i periodi autorizzati; segnalare sospetti fallimenti della cancellazione |

---

## Prove

Le seguenti prove dimostrano la conformità alla presente politica:

| # | Prova | Responsabile | Frequenza | Conservazione |
|---|-------|-------------|-----------|---------------|
| 1 | **Calendario di conservazione** (versione aggiornata, approvata dal Consulente legale e dalla Direzione esecutiva) | Responsabile dei documenti | *Rivisto annualmente; sotto controllo delle versioni* | Versioni attuali e superate (7 anni) |
| 2 | **Log di esecuzione della cancellazione** (timestamp, categorie di dati, metodi, risultati di verifica) | IT Operations | *Continuo; rivisto trimestralmente* | 3 anni |
| 3 | **Certificati di distruzione di terze parti** (supporti fisici, certificati di fornitori accreditati) | IT Operations | *Per evento di distruzione* | 3 anni dalla data di distruzione |
| 4 | **Registro delle richieste di cancellazione degli interessati** (richieste ricevute, valutazione, esito, data di completamento) | DPD / Consulente privacy | *Per richiesta; registro rivisto trimestralmente* | 3 anni dalla chiusura della richiesta |
| 5 | **Registro dei blocchi legali** (blocchi attivi, ambito, revisioni trimestrali, registrazioni di rilascio) | Consulente legale | *Blocchi attivi rivisti trimestralmente; registro mantenuto continuamente* | 3 anni dal rilascio del blocco |
| 6 | **Registro delle eccezioni** (eccezioni approvate con giustificazione, controlli compensativi, date di scadenza) | RSSI | *Rivisto trimestralmente; presentato alla revisione della direzione* | Vita dell'eccezione + 3 anni |
| 7 | **Inventario dei dati** con periodi di conservazione e ambito di cancellazione per categoria di dati | Responsabile dei documenti | *Rivisto annualmente; snapshot trimestrali* | Corrente + snapshot trimestrali (3 anni) |
| 8 | **Report di conformità trimestrale** (metriche di cancellazione: tasso di cancellazione puntuale, elementi in scaduto, eccezioni, tempi di risposta alle richieste degli interessati) | RSSI / Responsabile dei documenti | *Trimestrale; presentato alla revisione della direzione* | 3 anni |
| 9 | **Log di cancellazione tramite API cloud/SaaS** (registrazioni delle chiamate API, identificatori delle risorse, conferme di successo) | IT Operations | *Per evento di cancellazione* | 3 anni |
| 10 | **Registrazioni di revisione dei contratti di terze parti** (clausole di cancellazione, valutazioni delle capacità di cancellazione dei fornitori) | Consulente legale / RSSI | *Per contratto; rivisto al rinnovo del contratto* | Durata del contratto + 3 anni |
| 11 | **Registrazioni della configurazione della cancellazione automatizzata** (politiche di conservazione configurate nei sistemi, stato dell'integrazione dei blocchi legali) | IT Operations | *Rivisto semestralmente* | Configurazione attuale + 3 anni |
| 12 | **Risultati del campionamento per la verifica della cancellazione** (registrazioni del campionamento trimestrale, risultati degli spot check) | Sicurezza delle informazioni | *Campionamento trimestrale; spot check annuale* | 3 anni |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità alla presente politica tramite vari metodi, inclusi tra gli altri: audit dei log di cancellazione, revisioni della conformità al calendario di conservazione, monitoraggio dei tempi di risposta alle richieste degli interessati, revisioni della verifica della cancellazione da parte di terze parti, revisioni del registro delle eccezioni, audit interni ed esterni e feedback al proprietario della politica.

**Metriche chiave di conformità**:

| # | Metrica | Obiettivo | Frequenza di misurazione |
|---|---------|-----------|--------------------------|
| 1 | Tasso di cancellazione puntuale (cancellazioni eseguite entro 90 giorni dalla scadenza della conservazione) | ≥ 95% | Trimestrale |
| 2 | Richieste di cancellazione degli interessati completate entro 30 giorni | 100% | Per richiesta; riportato trimestralmente |
| 3 | Certificati di cancellazione di terze parti ottenuti per dati Riservati+ | 100% | Per evento; riportato trimestralmente |
| 4 | Blocchi legali rivisti nel ciclo trimestrale | 100% | Trimestrale |
| 5 | Registro delle eccezioni rivisto e aggiornato (nessuna eccezione scaduta e non rivista) | 100% | Trimestrale |
| 6 | Copertura del calendario di conservazione (percentuale di categorie di dati con conservazione definita) | 100% | Annuale |
| 7 | Completamento della cancellazione dei backup (dati cancellati da tutte le copie di backup entro i tempi documentati) | ≥ 90% | Trimestrale |

Le metriche che violano gli obiettivi devono essere segnalate al RSSI per un'attenzione immediata e riportate alla successiva Revisione della direzione.

## Eccezioni

Qualsiasi eccezione alla presente politica deve essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita. Le eccezioni devono essere segnalate al Team di revisione della direzione. Le eccezioni relative alla conservazione richiedono l'approvazione del Consulente legale.

## Non conformità

Un dipendente che risulti aver violato la presente politica può essere soggetto a provvedimenti disciplinari, fino al licenziamento. Il mancato rispetto dei requisiti legali in materia di cancellazione dei dati personali può inoltre esporre l'organizzazione a sanzioni normative (nLPD Art. 60–66; GDPR Art. 83 ove applicabile).

## Miglioramento continuo

La presente politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono tener conto di modifiche ai regolamenti sulla protezione dei dati (nLPD, GDPR, requisiti cantonali), agli standard di sanificazione dei supporti (NIST SP 800-88, IEEE 2883), alle capacità di cancellazione dei fornitori di servizi cloud, alle tecnologie di storage emergenti, ai risultati degli audit e alle lezioni apprese dai fallimenti della cancellazione o dai reclami degli interessati.

---

# Aree della norma ISO 27001 trattate

Politica di cancellazione delle informazioni — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.9 Inventario delle informazioni e delle altre risorse associate |
| Clausola 7.3 Consapevolezza | 5.12 Classificazione delle informazioni |
| Clausola 7.5.3 Controllo delle informazioni documentate | 5.33 Protezione dei documenti |
| | 5.34 Privacy e protezione dei dati personali |
| | 5.36 Conformità a politiche, regole e standard |
| | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 7.10 Supporti di memorizzazione |
| | 7.14 Smaltimento sicuro o riutilizzo delle attrezzature |
| | **8.10 Cancellazione delle informazioni** |
| | 8.13 Backup delle informazioni |
| | 8.24 Uso della crittografia |

**Quadro normativo e legale**:

| Quadro | Rilevanza |
|--------|-----------|
| nLPD svizzera (revDSG) | Art. 6 — Principi (proporzionalità, limitazione delle finalità, limitazione della conservazione); Art. 8 — Sicurezza dei dati (misure tecniche e organizzative); Art. 25 — Diritto di accesso (include i diritti di cancellazione); Art. 24 — Notifica delle violazioni |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| CO svizzero (Codice delle obbligazioni) | Art. 957–958f — Obblighi di contabilità e conservazione dei documenti (10 anni); Art. 127–128 — Termini di prescrizione per le pretese |
| GDPR UE (ove applicabile) | Art. 5(1)(e) — Limitazione della conservazione; Art. 17 — Diritto alla cancellazione; Art. 19 — Obbligo di notifica in merito alla cancellazione; Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Allegato A Controllo 8.10 — Cancellazione delle informazioni |
| ISO/IEC 27002:2022 | Sezione 8.10 — Guida all'implementazione per la cancellazione delle informazioni |
| NIST SP 800-88 Rev. 2 | Linee guida per la sanificazione dei supporti (Cancellazione, Eliminazione, Distruzione; cancellazione crittografica) |
| IEEE 2883 | Standard per la sanificazione dello storage (tecniche di sanificazione specifiche per tipo di supporto) |
| NIST SP 800-53 Rev 5 | MP-6 (Sanificazione dei supporti), SI-12 (Gestione e conservazione delle informazioni) |
| DIN 66399 | Classificazione dei livelli di sicurezza per la distruzione di carta e supporti |

**Quadri condizionali** (applicabili laddove le attività aziendali ne determinino l'applicabilità):

| Quadro | Condizione |
|--------|-----------|
| PCI DSS v4.0 | Applicabile se vengono trattati dati delle carte di pagamento; richiede la cancellazione sicura dei dati dei titolari di carta quando non più necessari |
| Circolari FINMA | Applicabile se l'organizzazione è un istituto finanziario svizzero vigilato |
| HIPAA Security Rule | Applicabile se vengono trattate informazioni sanitarie protette statunitensi |

---

<!-- QA_VERIFIED: 2026-04-03 -->
