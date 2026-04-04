<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.23-31-IT:privacy:POL:a.3.23-31 -->
**PRIV-POL-A.3.23-31 — Controlli tecnici di sicurezza per i DCP**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Controlli tecnici di sicurezza per i DCP |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | PRIV-POL-A.3.23-31 |
| **Autore del documento** | Responsabile della Protezione dei Dati (RPD) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto Privacy** | 1.0 |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data da definire] | RPD | Politica iniziale per la prima certificazione ISO/IEC 27701:2025 |

**Ciclo di revisione** : Annuale | **Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** : Principale: RPD; Secondaria: RSSI; Tecnica: Responsabile Sviluppo / Architettura IT; Autorità finale: Direzione generale.

**Documenti correlati** :
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.3.23-31-UG / TG
- ISMS-POL-A.8.2, A.8.5, A.8.13, A.8.15-16, A.8.24, A.8.25-31 (paralleli SGSI)
- ISO/IEC 27701:2025 Controlli A.3.23 – A.3.31
- RGPD Articolo 25 (Privacy by design e by default); Articolo 32 (Sicurezza del trattamento)
- LPD svizzera Articolo 7 (Misure tecniche proporzionate al rischio)

**Applicabilità del ruolo** : Questa politica si applica all'organizzazione che agisce sia come **Titolare del trattamento che come Responsabile del trattamento dei DCP**. I controlli A.3.23–A.3.31 sono controlli condivisi (Tabella A.3).

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di sicurezza tecnici applicati al trattamento dei DCP, coprendo autenticazione, backup, registrazione nei log, crittografia, sviluppo sicuro, sicurezza delle applicazioni, architettura dei sistemi, sviluppo esternalizzato e informazioni di test — conformemente ai controlli A.3.23–A.3.31 di ISO/IEC 27701:2025.

**Perimetro** : Tutti i controlli tecnici implementati per sistemi, applicazioni e infrastrutture che trattano DCP; tutte le attività di sviluppo di software e sistemi che coinvolgono il trattamento dei DCP; tutti gli ambienti di test che utilizzano o simulano DCP.

**Motivazione** : A.3.23–A.3.31 costituiscono il livello di assurance tecnica per il trattamento dei DCP. Estendono e specializzano il quadro dei controlli tecnici SGSI per i contesti DCP — garantendo che ogni dominio tecnico (autenticazione, backup, registrazione nei log, crittografia, sviluppo, architettura, esternalizzazione, test) affronti esplicitamente i DCP. Il RGPD Articoli 25 e 32 forniscono la base normativa per questo gruppo.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27701:2025

**A.3.23 — Autenticazione sicura** : [Organizzazione] DEVE implementare tecnologie e procedure di autenticazione sicura per i sistemi di trattamento dei DCP, calibrate alle restrizioni di accesso applicabili.

**A.3.24 — Backup delle informazioni** : [Organizzazione] DEVE mantenere copie di backup dei DCP e dei software/sistemi coinvolti nel loro trattamento, e testarle regolarmente.

**A.3.25 — Registrazione nei log** : [Organizzazione] DEVE produrre, archiviare, proteggere e analizzare log che registrano attività, eccezioni, guasti e altri eventi rilevanti relativi al trattamento dei DCP.

**A.3.26 — Utilizzo della crittografia** : [Organizzazione] DEVE definire e implementare regole per l'utilizzo efficace della crittografia nei contesti di trattamento dei DCP, inclusa la gestione delle chiavi.

**A.3.27 — Ciclo di vita dello sviluppo sicuro** : [Organizzazione] DEVE stabilire e applicare regole per lo sviluppo sicuro di software e sistemi coinvolti nel trattamento dei DCP.

**A.3.28 — Requisiti di sicurezza delle applicazioni** : [Organizzazione] DEVE identificare, specificare e approvare i requisiti di sicurezza relativi al trattamento dei DCP nello sviluppo o nell'acquisizione di applicazioni.

**A.3.29 — Principi di architettura e ingegneria sicura dei sistemi** : [Organizzazione] DEVE stabilire, documentare, mantenere e applicare principi per l'ingegneria di sistemi sicuri nel contesto del trattamento dei DCP.

**A.3.30 — Sviluppo esternalizzato** : [Organizzazione] DEVE dirigere, monitorare e rivedere le attività relative allo sviluppo esternalizzato di sistemi utilizzati per il trattamento dei DCP.

**A.3.31 — Informazioni di test** : [Organizzazione] DEVE selezionare, proteggere e gestire in modo appropriato le informazioni di test utilizzate nel contesto dei sistemi di trattamento dei DCP.

## Quadro normativo

**Obbligatorio (Livello 1)** (per PRIV-POL-00):
- **RGPD UE** : Articolo 25 (privacy by design e by default — controlli tecnici come requisito di progettazione); Articolo 32 (pseudonimizzazione, cifratura, ripristino della disponibilità, test regolare delle MTO)
- **LPD svizzera** : Articolo 7 (misure tecniche proporzionate al rischio)
- **ISO/IEC 27701:2025** : Controlli A.3.23–A.3.31 (normativi)

---

# A.3.23 — Autenticazione sicura per il trattamento dei DCP

[Organizzazione] DEVE implementare tecnologie e procedure di autenticazione sicura per l'accesso ai sistemi di trattamento dei DCP.

### Requisiti di autenticazione per i sistemi DCP

| Sensibilità dei DCP | Requisito minimo di autenticazione |
|--------------------|------------------------------------|
| DCP RISERVATI | Autenticazione a più fattori (AMF) per l'accesso remoto; politica di password forte per l'accesso interno |
| DCP LIMITATI (categoria speciale) | AMF richiesta per TUTTI gli accessi (interno e remoto) |
| Accesso amministrativo / privilegiato ai DCP | AMF richiesta; identità privilegiata separata da quella standard |

Le procedure di autenticazione DEVONO applicare le restrizioni di accesso allineate ai diritti di accesso definiti in PRIV-POL-A.3.8-10. I tentativi di autenticazione falliti DEVONO essere registrati nei log e innescare un blocco per le soglie definite in PRIV-IMP-A.3.23-31-TG. Le credenziali di autenticazione per i sistemi DCP DEVONO essere univoche per individuo; le credenziali condivise sono vietate.

---

# A.3.24 — Backup dei DCP e sistemi correlati

[Organizzazione] DEVE mantenere copie di backup dei DCP e dei software/sistemi correlati, e testare regolarmente l'integrità e la ripristinabilità di tali backup.

- Tutti i DCP trattati DEVONO essere coperti da un regime di backup con obiettivi di punto di ripristino (RPO) documentati
- I backup contenenti DCP DEVONO essere soggetti agli stessi controlli di classificazione e accesso dei DCP primari
- Le copie di backup DEVONO essere cifrate con lo stesso standard dei dati primari
- I backup fuori sede o cloud DEVONO essere soggetti a controlli di sicurezza equivalenti, inclusa cifratura in transito e a riposo
- Il ripristino dei backup DEVE essere testato al minimo annualmente; i risultati DEVONO essere documentati; i fallimenti dei test che coinvolgono DCP DEVONO essere escalati a RSSI e RPD

---

# A.3.25 — Registrazione nei log per il trattamento dei DCP

[Organizzazione] DEVE produrre, archiviare, proteggere e analizzare log che registrano attività, eccezioni, guasti e altri eventi rilevanti relativi al trattamento dei DCP.

### Eventi DCP che devono essere registrati nei log

- Accesso agli archivi dati DCP (lettura, scrittura, esportazione) da parte di utenti autenticati
- Tentativi di accesso falliti ai sistemi DCP
- Operazioni di dati in massa che coinvolgono DCP (esportazione, cancellazione, pseudonimizzazione, anonimizzazione)
- Modifiche ai diritti di accesso per i sistemi DCP
- Operazioni privilegiate sui sistemi di trattamento dei DCP
- Operazioni di adempimento dei diritti degli interessati
- Errori o eccezioni di sistema nei componenti di trattamento dei DCP

### Protezione dei log

I log DEVONO essere: protetti contro la modifica e la cancellazione (archiviazione a prova di manomissione); classificati al minimo RISERVATO; accessibili solo al personale autorizzato; conservati per **minimo 12 mesi** come soglia operativa, con un **minimo di 3 anni** per i log che possono essere richiesti come prove di accountability RGPD (log di accesso per l'adempimento dei diritti, operazioni di cancellazione e anonimizzazione in massa, accesso privilegiato ai sistemi DCP). RSSI e RPD DEVONO concordare periodi di conservazione specifici per categoria di log in PRIV-IMP-A.3.23-31-TG.

I log DEVONO essere esaminati su base di eccezioni (alert per pattern di accesso DCP anomali), nell'ambito della revisione della conformità periodica, in risposta a un incidente di privacy, e nell'ambito della revisione dei diritti di accesso.

---

# A.3.26 — Crittografia per il trattamento dei DCP

[Organizzazione] DEVE definire e implementare regole per l'utilizzo efficace della crittografia nei contesti di trattamento dei DCP, inclusa la gestione delle chiavi crittografiche.

- **Cifratura a riposo** : Tutti i DCP RISERVATI e LIMITATI DEVONO essere cifrati a riposo con un algoritmo approvato (minimo AES-256 o equivalente per ISMS-POL-A.8.24)
- **Cifratura in transito** : Tutti i DCP trasmessi su reti DEVONO essere cifrati in transito con gli standard TLS attuali (minimo TLS 1.2; TLS 1.3 preferito)
- **Pseudonimizzazione** : Laddove i DCP vengano utilizzati per analisi, test, ricerca o finalità secondarie, la pseudonimizzazione DEVE essere applicata per ridurre il rischio di re-identificazione ove tecnicamente fattibile
- **Anonimizzazione** : Laddove venga applicata un'anonimizzazione irreversibile, il risultato non è più DCP — ma l'anonimizzazione deve essere robusta. Il RPD DEVE confermare, utilizzando una metodologia documentata, che la re-identificazione non è ragionevolmente possibile con qualsiasi mezzo ragionevolmente suscettibile di essere utilizzato, considerando i rischi di singolarizzazione (isolare un individuo in un dataset), collegabilità (collegare record per identificare un individuo) e inferenza (dedurre attributi di un individuo dai dati rimanenti). Un'anonimizzazione che non supera questa valutazione DEVE essere trattata come pseudonimizzazione, e i dati sottostanti continuano ad essere DCP

### Gestione delle chiavi

Le chiavi crittografiche che proteggono i DCP DEVONO essere gestite separatamente dai DCP che proteggono; l'accesso alle chiavi DEVE essere limitato; la rotazione delle chiavi DEVE avvenire agli intervalli definiti in PRIV-IMP-A.3.23-31-TG; la compromissione o la perdita di chiavi che proteggono DCP DEVE essere trattata come un incidente DCP per PRIV-POL-A.3.11-12.

---

# A.3.27 — Ciclo di vita dello sviluppo sicuro per i sistemi DCP

[Organizzazione] DEVE stabilire e applicare regole per lo sviluppo sicuro di software e sistemi relativi al trattamento dei DCP.

- **Privacy by Design** : I requisiti di privacy e protezione dei DCP DEVONO essere considerati fin dalla prima fase di progettazione di qualsiasi sistema destinato a trattare DCP; il retrofitting dei controlli di privacy non è un approccio accettabile
- **Privacy by Default** : I valori predefiniti del sistema DEVONO minimizzare la raccolta e il trattamento dei DCP; le impostazioni più protettive per la privacy DEVONO essere il valore predefinito
- **Minimizzazione dei DCP nella progettazione** : I sistemi DEVONO essere progettati per raccogliere e trattare solo i DCP minimi necessari per la finalità dichiarata; la raccolta di campi in eccesso DEVE essere identificata e rimossa durante la revisione della progettazione
- **Separazione dei DCP** : Ove tecnicamente fattibile, i DCP DEVONO essere isolati dai dati non-DCP nella progettazione del sistema

### Conformità RGPD Articolo 25

I sistemi che coinvolgono il trattamento dei DCP DEVONO essere documentati come conformi alla privacy by design prima del dispiegamento in produzione. Il processo DPIA (PRIV-POL-A.1.2.6-9) DEVE essere innescato per i sistemi di trattamento ad alto rischio durante la fase di progettazione, non dopo il dispiegamento.

---

# A.3.28 — Requisiti di sicurezza delle applicazioni per i DCP

[Organizzazione] DEVE identificare, specificare e approvare i requisiti di sicurezza relativi al trattamento dei DCP nello sviluppo o nell'acquisizione di applicazioni.

- I requisiti di sicurezza DCP DEVONO essere documentati prima dell'inizio dello sviluppo o dell'acquisizione
- I requisiti DEVONO coprire come minimo: autenticazione, controllo degli accessi, cifratura a riposo e in transito, registrazione nei log, conservazione/cancellazione dei dati
- I requisiti DEVONO essere approvati dal RPD (requisiti di privacy) e dal RSSI (requisiti di sicurezza) prima dell'inizio
- Per le applicazioni acquisite: i requisiti di sicurezza DEVONO essere inclusi nelle specifiche di procurement; la valutazione di sicurezza del fornitore DEVE affrontare i controlli di trattamento dei DCP

---

# A.3.29 — Principi di architettura e ingegneria sicura per i DCP

[Organizzazione] DEVE stabilire, documentare, mantenere e applicare principi per l'ingegneria di sistemi sicuri relativi al trattamento dei DCP.

I seguenti principi di architettura DEVONO essere applicati ai sistemi che coinvolgono DCP:

1. **Esposizione minima** : I DCP devono fluire attraverso il numero minimo di componenti di sistema necessari; l'esposizione inutile dei DCP a sistemi intermedi o log DEVE essere evitata
2. **Minimo privilegio nell'architettura** : I componenti di sistema accedono solo ai DCP di cui hanno bisogno; l'accesso da servizio a servizio ai DCP DEVE essere limitato e autenticato
3. **Separazione dei dati** : Ove fattibile, i DCP di diverse finalità DEVONO essere logicamente separati
4. **Auditabilità** : I sistemi che trattano DCP DEVONO essere progettati per produrre i log richiesti da A.3.25 senza strumentazione aggiuntiva
5. **Ripristinabilità** : L'architettura DEVE supportare i requisiti di backup e ripristino di A.3.24 per i DCP
6. **Percorsi di anonimizzazione e pseudonimizzazione** : L'architettura DEVE includere meccanismi tecnici per pseudonimizzare o anonimizzare i DCP per casi d'uso secondari senza richiedere l'accesso agli archivi DCP primari

---

# A.3.30 — Sviluppo esternalizzato di sistemi di trattamento dei DCP

[Organizzazione] DEVE dirigere, monitorare e rivedere le attività relative allo sviluppo esternalizzato di sistemi di trattamento dei DCP.

- Il partner di sviluppo DEVE essere trattato come un responsabile del trattamento dei DCP o un fornitore adiacente per PRIV-POL-A.3.8-10
- Un accordo che copra gli obblighi di sicurezza DCP DEVE essere in vigore prima dell'accesso allo sviluppo ai DCP
- I requisiti di sicurezza DCP (A.3.28) DEVONO essere comunicati e concordati prima dell'inizio dello sviluppo
- [Organizzazione] DEVE mantenere il diritto di esaminare gli artefatti di sviluppo (codice, documenti di progettazione) per la conformità DCP
- Il partner di sviluppo NON DEVE utilizzare DCP reali in ambienti di sviluppo o test senza esplicita approvazione del RPD

---

# A.3.31 — Informazioni di test per i DCP

[Organizzazione] DEVE selezionare, proteggere e gestire in modo appropriato le informazioni di test relative al trattamento dei DCP.

### Divieto di DCP reali negli ambienti di test

I DCP reali NON DEVONO essere utilizzati negli ambienti di test come pratica predefinita. Gli ambienti di test DEVONO utilizzare: dati generati sinteticamente che assomigliano ai DCP nella struttura ma non contengono dati personali reali, OPPURE dati irreversibilmente anonimizzati da dataset DCP reali (conferma di anonimizzazione del RPD richiesta).

### Eccezione: utilizzo di DCP reali nei test

Laddove l'utilizzo di DCP reali nei test sia operativamente necessario: approvazione scritta del RPD richiesta prima della copia nell'ambiente di test; perimetro limitato ai DCP minimi necessari, per la durata minima richiesta; i DCP reali DEVONO essere eliminati dall'ambiente di test immediatamente dopo la conclusione del test specifico, con conferma e documentazione; tutti gli accessi ai DCP reali nell'ambiente di test DEVONO essere registrati nei log.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità per A.3.23–A.3.31 |
|-------|----------------------------------|
| **RPD** | Approva i requisiti di sicurezza DCP per i nuovi sistemi (A.3.28); conferma le decisioni di anonimizzazione (A.3.26); approva le DPIA per i nuovi sistemi DCP (A.3.27); approva l'utilizzo di DCP reali nei test (A.3.31); esamina la conformità DCP dello sviluppo esternalizzato (A.3.30) |
| **RSSI** | Definisce gli standard di autenticazione (A.3.23); definisce gli standard di backup (A.3.24); gestisce l'infrastruttura di registrazione nei log (A.3.25); mantiene gli standard crittografici (A.3.26); è proprietario del quadro di sviluppo sicuro (A.3.27–A.3.30) |
| **Team Sicurezza IT** | Implementa autenticazione, backup, registrazione nei log e cifratura; monitora i log per le anomalie di accesso DCP; gestisce l'infrastruttura di gestione delle chiavi |
| **Team Sviluppo / DevOps** | Applica le regole di privacy by design e sviluppo sicuro; implementa i requisiti di sicurezza DCP nel codice; utilizza solo dati di test approvati (nessun DCP reale senza approvazione RPD) |
| **Architettura IT** | Mantiene i principi di architettura sicura per i DCP; esamina le nuove progettazioni di sistemi |
| **Acquisti / Legale** | Garantisce che i contratti di sviluppo esternalizzato includano gli obblighi di sicurezza DCP |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Configurazione di autenticazione dei sistemi DCP | Registrazioni di applicazione AMF e configurazioni di restrizione dell'accesso | In corso + 3 anni |
| Registrazioni di test di backup | Risultati di test di ripristino annuali per i backup DCP | 3 anni |
| Log di accesso DCP | Log di attività per l'accesso agli archivi dati DCP e ai sistemi | Minimo 12 mesi; più lungo per requisiti normativi o contrattuali |
| Documentazione degli standard crittografici | Algoritmi approvati, procedure di gestione delle chiavi, registrazioni di rotazione | In corso + 3 anni |
| Valutazioni Privacy by Design | Registrazioni di revisione della progettazione che confermano la conformità PbD | Durata di funzionamento del sistema + 3 anni |
| Documenti dei requisiti di sicurezza DCP | Requisiti approvati per le applicazioni DCP sviluppate o acquisite | Durata di funzionamento dell'applicazione + 3 anni |
| Registrazioni di approvazione di test con DCP reali | Approvazioni RPD per l'utilizzo di DCP reali nei test, con conferme di cancellazione | 3 anni |
| Accordi di sviluppo esternalizzato DCP | Accordi con partner di sviluppo che coprono gli obblighi di sicurezza DCP | Durata dell'accordo + 3 anni |

---

# Considerazioni di audit

**A.3.23 (Autenticazione)** : Prove di configurazione AMF per sistemi DCP RISERVATI/LIMITATI; allineamento delle restrizioni di accesso; registrazione nei log dei login falliti.

**A.3.24 (Backup)** : Politica di backup che copre i DCP; cifratura dei backup; registrazioni di test di ripristino annuali.

**A.3.25 (Registrazione nei log)** : Eventi DCP definiti registrati nei log; archiviazione a prova di manomissione; controlli degli accessi sui log; prove di analisi dei log.

**A.3.26 (Crittografia)** : Cifratura a riposo per DCP RISERVATI/LIMITATI; applicazione di TLS in transito; documentazione di gestione delle chiavi; prove di utilizzo della pseudonimizzazione.

**A.3.27 (Sviluppo sicuro)** : Prove di privacy by design nelle registrazioni di progettazione del sistema; innesco DPIA per sistemi ad alto rischio; revisione della minimizzazione dei dati nella progettazione.

**A.3.28 (Requisiti delle applicazioni)** : Requisiti di sicurezza DCP documentati e approvati RPD/RSSI; requisiti di sicurezza nelle specifiche di acquisizione.

**A.3.29 (Principi di architettura)** : Principi di architettura DCP documentati; prove di revisione della progettazione che applicano i principi ai nuovi sistemi.

**A.3.30 (Sviluppo esternalizzato)** : Accordi di sviluppo esternalizzato con clausole di sicurezza DCP; nessun DCP reale in ambienti di sviluppo esternalizzato senza approvazione RPD.

**A.3.31 (Informazioni di test)** : Utilizzo predefinito di dati di test sintetici o anonimizzati; registrazioni di approvazione RPD per qualsiasi utilizzo di DCP reali nei test; conferme di cancellazione dei DCP reali dopo i test.

---

<!-- QA_VERIFIED: 2026-04-03 -->
