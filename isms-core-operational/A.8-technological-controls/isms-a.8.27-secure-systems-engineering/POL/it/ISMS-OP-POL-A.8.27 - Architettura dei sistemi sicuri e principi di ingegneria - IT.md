<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.27-IT:operational:OP-POL:a.8.27 -->
**ISMS-OP-POL-A.8.27 — Architettura dei sistemi sicuri e principi di ingegneria**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Architettura dei sistemi sicuri e principi di ingegneria |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.27 |
| **Autore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da definire] |
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

- ISO/IEC 27001:2022 Controllo A.8.27 — Architettura dei sistemi sicuri e principi di ingegneria
- ISO/IEC 27002:2022 Sezione 8.27 — Guida all'implementazione
- NIST SP 800-160 Vol. 1 Rev. 1 — Engineering Trustworthy Secure Systems
- NIST SP 800-207 — Zero Trust Architecture
- NIST SP 800-53 Rev 5 SA-8 — Security and Privacy Engineering Principles
- CIS Controls v8 — Salvaguardie 4.1, 16.1–16.14 (Sicurezza del software applicativo)

**Controlli Allegato A correlati**:

| Controllo | Relazione con l'architettura sicura dei sistemi |
|-----------|------------------------------------------------|
| A.5.8 Sicurezza delle informazioni nella gestione dei progetti | Requisiti di architettura di sicurezza integrati nella governance del progetto |
| A.8.25 Ciclo di vita dello sviluppo sicuro | I principi di architettura informano il framework del processo di sviluppo |
| A.8.26 Requisiti di sicurezza delle applicazioni | I requisiti di sicurezza derivano dai principi di architettura |
| A.8.28 Codifica sicura | Gli standard di codifica implementano i principi di architettura a livello di codice |
| A.8.29 Test di sicurezza nello sviluppo e nell'accettazione | I test validano che i principi di architettura siano correttamente implementati |
| A.8.31 Separazione degli ambienti di sviluppo, test e produzione | La segregazione degli ambienti è un principio fondamentale dell'architettura |
| A.8.9 Gestione della configurazione | Le configurazioni di base applicano gli standard di architettura sicura |
| A.8.20–22 Sicurezza della rete | L'architettura di rete implementa la segmentazione e la difesa in profondità |
| A.8.2–3–5 Autenticazione e accesso privilegiato | L'architettura di autenticazione implementa i principi Zero Trust |
| A.5.19–23 Fornitori e servizi cloud | I sistemi di terze parti soggetti a revisione dell'architettura |

**Politiche interne correlate**:

- Politica sul ciclo di vita dello sviluppo sicuro
- Politica di sicurezza della rete
- Politica di autenticazione e accesso privilegiato
- Politica di gestione della configurazione
- Politica di sicurezza delle informazioni nella gestione dei progetti
- Politica sull'uso della crittografia

---

# Politica sull'architettura dei sistemi sicuri e principi di ingegneria

## Scopo

Lo scopo di questa politica è stabilire le regole e i principi per l'ingegnerizzazione di sistemi informativi sicuri, garantendo che la sicurezza sia integrata nell'architettura del sistema fin dall'inizio anziché aggiunta dopo la distribuzione. Questa politica definisce i principi fondamentali di ingegneria sicura che devono essere applicati a tutte le attività di sviluppo, acquisizione, integrazione e modifica dei sistemi.

Questa politica supporta la nLPD svizzera (revDSG) implementando la protezione dei dati per impostazione predefinita e fin dalla progettazione (Art. 7) e misure tecniche e organizzative adeguate al rischio (Art. 8). La nLPD richiede che gli sviluppatori integrino la protezione e il rispetto della privacy degli interessati nella struttura stessa dei prodotti e dei servizi che trattano dati personali, e che il più alto livello di sicurezza sia attivato per impostazione predefinita senza l'intervento dell'utente. Laddove l'organizzazione tratta dati di persone nell'UE/SEE, si applicano anche i requisiti del GDPR (Art. 25 — protezione dei dati per impostazione predefinita e fin dalla progettazione; Art. 32 — sicurezza del trattamento).

## Ambito

Tutti i sistemi informativi progettati, sviluppati, acquisiti, integrati, gestiti e mantenuti dall'organizzazione, inclusi:

- Applicazioni, API e servizi sviluppati internamente.
- Architettura di infrastruttura e piattaforma (on-premises e cloud).
- Sistemi sviluppati o acquisiti da terze parti integrati nell'ambiente dell'organizzazione.
- Servizi cloud, piattaforme SaaS e servizi gestiti dove l'organizzazione definisce o influenza l'architettura.
- Tecnologie operative (OT) e sistemi di controllo industriale (ICS), ove applicabile.

Tutti i dipendenti, i collaboratori e gli utenti terzi coinvolti nella progettazione, nell'architettura, nello sviluppo e nell'ingegneria dei sistemi.

**Fuori ambito**: Dispositivi endpoint autonomi degli utenti finali gestiti dalla Politica di sicurezza degli endpoint (A.8.1-7-18-19), a meno che non facciano parte di un'architettura di sistema in fase di revisione. L'infrastruttura fisica è disciplinata dalla Politica di sicurezza fisica (A.7.x).

## Principio

I principi per l'ingegnerizzazione di sistemi sicuri devono essere stabiliti, documentati, mantenuti e applicati a qualsiasi attività di sviluppo di sistemi informativi. La sicurezza deve essere trattata come una proprietà fondamentale del design del sistema — non come un'aggiunta successiva o un componente aggiunto in un secondo momento.

Tutte le decisioni di architettura e ingegneria devono essere basate sul rischio, considerando il valore e la classificazione delle informazioni trattate, il panorama delle minacce rilevante per il sistema, i requisiti normativi e la propensione al rischio dell'organizzazione.

Laddove l'organizzazione non disponga di risorse dedicate all'architettura della sicurezza — situazione comune nelle piccole e medie organizzazioni — il RSSI svolgerà la funzione di Architetto della sicurezza e si dovrà ricorrere a una revisione specialistica esterna per i sistemi ad alto rischio.

---

## Principi di ingegneria sicura

L'organizzazione deve stabilire, documentare e mantenere un insieme di principi di ingegneria sicura che si applicano a tutte le attività di sviluppo e acquisizione dei sistemi. Questi principi devono essere revisionati annualmente e aggiornati per riflettere i cambiamenti nel panorama delle minacce, negli standard tecnologici e nei requisiti normativi.

### Principio 1: Sicurezza per progettazione (Security by Design)

La sicurezza deve essere integrata fin dalle prime fasi della concezione del sistema:

- I requisiti di sicurezza devono essere identificati durante lo sviluppo del concetto iniziale, insieme ai requisiti funzionali.
- L'architettura di sicurezza deve essere definita prima che inizi la progettazione dettagliata.
- I controlli di sicurezza devono essere progettati come componenti integrali del sistema, non come aggiunte dopo che la funzionalità principale è stata costruita.
- I compromessi sulla sicurezza devono essere esplicitamente documentati, con l'accettazione del rischio approvata dal RSSI prima di procedere.

### Principio 2: Sicurezza per impostazione predefinita (Security by Default)

I sistemi devono essere sicuri nella loro configurazione predefinita:

- Le configurazioni predefinite devono implementare le impostazioni di sicurezza più restrittive appropriate allo scopo previsto del sistema.
- Gli utenti non devono essere tenuti ad intervenire per proteggere il sistema — la sicurezza deve essere attiva dal primo utilizzo.
- Le funzionalità di sicurezza opzionali devono essere abilitate per impostazione predefinita a meno che non esista una giustificazione aziendale documentata per disabilitarle.
- Il rifiuto predefinito (default-deny) deve essere applicato ai controlli degli accessi, alle comunicazioni di rete e alle funzionalità del sistema.
- Le interfacce amministrative devono essere disabilitate o limitate per impostazione predefinita.
- Le funzionalità dell'applicazione che richiedono privilegi elevati devono essere abilitate esplicitamente, non per impostazione predefinita (ad esempio, logging di debug, amministrazione remota).

**Privacy per impostazione predefinita (nLPD Art. 7)**:

- Le impostazioni predefinite devono minimizzare la raccolta di dati personali (minimizzazione dei dati).
- Le funzionalità per il miglioramento della privacy devono essere abilitate per impostazione predefinita (ad esempio, anonimizzazione dei dati, applicazione della limitazione dello scopo).
- I meccanismi di consenso degli utenti devono essere impostati per impostazione predefinita su opt-in, non opt-out.
- La conservazione dei dati deve essere impostata per impostazione predefinita sul periodo più breve, a meno che una giustificazione aziendale non richieda una conservazione più lunga.

### Principio 3: Difesa in profondità (Defence in Depth)

Devono essere implementati più livelli di controlli di sicurezza in modo che nessun singolo punto di guasto comporti una compromissione totale:

- Nessun singolo controllo deve essere l'unica protezione per le risorse critiche.
- I controlli devono essere implementati a più livelli dell'architettura: rete, piattaforma, applicazione e dati.
- Il guasto di un livello di controllo non deve comportare una compromissione completa del sistema.
- I controlli a livelli devono essere complementari — ogni livello affronta diversi vettori di attacco.

**Livelli di difesa in profondità**:

| Livello | Controlli di sicurezza |
|---------|------------------------|
| **Perimetro** | Firewall, web application firewall (WAF), protezione DDoS, gateway sicuri |
| **Rete** | Segmentazione, controllo degli accessi alla rete, IDS/IPS, comunicazioni interne cifrate |
| **Piattaforma** | Configurazioni rafforzate, gestione delle patch, protezione degli endpoint, avvio sicuro |
| **Applicazione** | Validazione degli input, codifica degli output, autenticazione, autorizzazione, gestione delle sessioni |
| **Dati** | Cifratura a riposo e in transito, controlli degli accessi, mascheratura dei dati, prevenzione della perdita di dati |
| **Identità** | Autenticazione a più fattori (AMF), gestione degli accessi privilegiati (PAM), governance delle identità |
| **Monitoraggio** | Registrazione centralizzata, analisi comportamentale, rilevamento delle minacce, risposta agli incidenti |

### Principio 4: Privilegio minimo

Tutti gli utenti, i processi e i sistemi devono operare con i privilegi minimi necessari per svolgere la loro funzione autorizzata:

- I diritti di accesso devono essere limitati a quanto necessario per il compito specifico.
- I privilegi elevati devono essere concessi solo quando necessario e revocati quando non più richiesti.
- Gli account di servizio devono avere autorizzazioni con ambito ristretto limitate a risorse e operazioni specifiche (non accesso completo al database, non amministratore di dominio).
- L'accesso amministrativo deve essere separato dall'accesso operativo quotidiano.

### Principio 5: Funzionalità minima

I sistemi devono fornire solo le funzionalità necessarie per il loro scopo previsto:

- I servizi, i protocolli e le funzionalità non necessari devono essere disabilitati o rimossi.
- La superficie di attacco deve essere minimizzata attraverso la riduzione delle funzionalità.
- Le porte, le interfacce e le funzionalità inutilizzate devono essere disabilitate.
- I contenuti di esempio predefiniti, le pagine di test e i moduli inutilizzati devono essere rimossi prima della distribuzione.

### Principio 6: Fallimento in modo sicuro (Fail Secure)

I sistemi devono fallire in uno stato sicuro che non esponga dati sensibili o funzionalità:

- I guasti del sistema devono risultare in un rifiuto dell'accesso per impostazione predefinita piuttosto che in una concessione dell'accesso.
- Le condizioni di errore non devono rivelare informazioni sensibili per la sicurezza (stack trace, percorsi interni, dettagli del database, numeri di versione).
- Il ripristino da un guasto deve richiedere una nuova autenticazione e autorizzazione.
- La degradazione controllata deve mantenere i controlli di sicurezza anche quando le prestazioni sono ridotte.
- Gli eventi di guasto devono essere registrati per il monitoraggio della sicurezza e l'investigazione degli incidenti.

**Esempi di fallimento in modo sicuro**:

Corretto (fallimento sicuro):

- Guasto della connessione al database: L'applicazione restituisce un errore generico, nega l'accesso.
- Servizio di autenticazione non disponibile: Il sistema nega il login, non bypassa l'autenticazione.
- Errore di elaborazione delle regole del firewall: Rifiuto predefinito, blocco del traffico.
- Chiave di cifratura non disponibile: Accesso ai dati negato fino al ripristino della chiave.

Non corretto (fallimento non sicuro — da evitare):

- Guasto della connessione al database: L'applicazione concede l'accesso presumendo che le credenziali siano valide.
- Servizio di autenticazione non disponibile: Il sistema consente il login con credenziali memorizzate nella cache senza verifica di scadenza.
- Errore di elaborazione delle regole del firewall: Apertura in caso di guasto (fail open), consentire tutto il traffico.
- Chiave di cifratura non disponibile: I dati vengono serviti non cifrati.

### Principio 7: Riduzione della complessità

I design dei sistemi devono privilegiare la semplicità — i sistemi complessi sono più difficili da proteggere, verificare e mantenere:

- I componenti devono avere interfacce ben definite con confini di sicurezza chiari.
- I sistemi devono essere progettati con moduli indipendenti e liberamente accoppiati che possono essere protetti, aggiornati e validati in modo indipendente.
- Le risorse condivise devono essere minimizzate per ridurre la superficie di attacco e prevenire flussi di informazioni non autorizzati tra i componenti.
- Le dipendenze tra i componenti devono essere ben definite e documentate.

**Gestione della complessità**:

La complessità deve essere gestita attraverso:

- **Design modulare**: Componenti con scopo unico e ben definito.
- **Limiti delle interfacce**: Interfacce esterne limitate al minimo necessario (documentare e giustificare ogni integrazione esterna).
- **Tracciamento delle dipendenze**: Mantenere una mappa delle dipendenze per i sistemi critici; obiettivo inferiore a 10 dipendenze esterne per i sistemi di Livello 1.
- **Complessità ciclomatica**: Le metriche di complessità del codice vengono tracciate durante lo sviluppo (obiettivo: inferiore a 10 per funzione per il codice critico per la sicurezza).

**Elementi scatenanti per la revisione della complessità**:

- Il sistema richiede più di 5 diversi meccanismi di autenticazione.
- Più di 15 integrazioni con sistemi esterni.
- Risorse condivise tra confini di fiducia senza isolamento.
- Il team di sviluppo non riesce a spiegare il flusso dei dati in meno di 15 minuti.

---

## Principi dell'architettura Zero Trust

L'organizzazione deve adottare i principi Zero Trust per tutti i nuovi sistemi e applicarli progressivamente ai sistemi esistenti:

**Non fidarsi mai, verificare sempre**:

- Nessuna fiducia implicita deve essere concessa in base alla posizione di rete, alla proprietà del dispositivo o all'autenticazione precedente.
- Ogni richiesta di accesso deve essere autenticata e autorizzata indipendentemente dalla provenienza — interna o esterna.
- La fiducia deve essere valutata continuamente, non presunta dopo la verifica iniziale.

**Presupporre una violazione**:

- I sistemi devono essere progettati presumendo che gli avversari possano già avere accesso alle reti interne.
- Il traffico della rete interna deve essere trattato come potenzialmente ostile.
- Il movimento laterale deve essere limitato attraverso la segmentazione e i controlli degli accessi.
- Le funzionalità di rilevamento devono presumere che i controlli perimetrali possano aver fallito.
- Endpoint Detection and Response (EDR) deve essere distribuito su tutti i dispositivi gestiti per rilevare l'attività post-compromissione.

**Verificare esplicitamente**:

- Le decisioni di accesso devono considerare tutti i punti dati disponibili: identità dell'utente, integrità del dispositivo, sensibilità dei dati, contesto di accesso (posizione, ora, comportamento) e indicatori di anomalie nelle richieste.
- Le decisioni di accesso devono essere registrate a fini di audit e indagine.

**Accesso con privilegio minimo**:

- Accesso JIT (Just-in-Time) per i privilegi elevati — concedere l'accesso solo quando necessario, revocare automaticamente al completamento del task.
- Accesso con il minimo indispensabile (JEA — Just-Enough-Access) per tutte le concessioni di accesso — nessuna autorizzazione ampia permanente.
- Politiche di accesso condizionale basate sul rischio applicate tramite il provider di identità.

**Approccio all'implementazione Zero Trust**:

| Fase | Attività | Calendario obiettivo |
|------|----------|---------------------|
| **Fase 1: Fondamenta** | Controllo degli accessi centrato sull'identità, AMF per tutti gli utenti, verifica dell'integrità del dispositivo | Entro 12 mesi dall'approvazione della politica |
| **Fase 2: Rete** | Micro-segmentazione per i sistemi critici, comunicazioni interne cifrate, controllo degli accessi alla rete | Entro 24 mesi |
| **Fase 3: Continuità** | Valutazione continua degli accessi, analisi comportamentale, risposta automatica alle anomalie | Entro 36 mesi |

**Tempistiche di implementazione Zero Trust**: Le tempistiche mostrate presuppongono un'organizzazione di medie dimensioni (50–200 dipendenti) con un debito tecnico moderato. Adattare in base a:

- **Organizzazioni piccole (<50 dipendenti)**: Le tempistiche possono essere del 50% più brevi con infrastruttura cloud-native.
- **Organizzazioni grandi (>200 dipendenti)**: Le tempistiche possono essere del 50% più lunghe a causa dei sistemi legacy e della complessità organizzativa.
- **Livello di debito tecnico**: Le organizzazioni con infrastruttura on-premises significativa richiedono tempistiche più lunghe per la Fase 2.

I progressi devono essere valutati annualmente rispetto alla roadmap specifica dell'organizzazione, non alle date di calendario assolute.

Non ci si aspetta che l'organizzazione raggiunga subito la piena maturità Zero Trust. Ogni fase deve essere pianificata, dotata di risorse e revisionata. I progressi devono essere comunicati annualmente alla Direzione generale.

---

## Documentazione dell'architettura di sicurezza

Tutti i sistemi classificati come ad alto rischio o a rischio medio devono avere un'architettura di sicurezza documentata. I sistemi a basso rischio devono avere, come minimo, una checklist di sicurezza completata.

### Requisiti di documentazione

**Sistemi ad alto rischio**:

| Documento | Contenuto | Responsabile |
|-----------|-----------|--------------|
| **Documento di architettura di sicurezza (DAS)** | Panoramica del sistema, confini di fiducia, flussi di dati, controlli di sicurezza per livello, punti di integrazione, contesto delle minacce | RSSI / Architetto della sicurezza |
| **Modello delle minacce** | Minacce identificate, vettori di attacco, valutazioni del rischio, mitigazioni, rischi residui | RSSI / Architetto della sicurezza |
| **Matrice di tracciabilità dei requisiti di sicurezza** | Requisiti di sicurezza mappati agli elementi di design e ai test case | Proprietario del sistema |
| **Architecture Decision Records (ADR)** | Decisioni di design rilevanti per la sicurezza con motivazione e alternative considerate | Proprietario del sistema / Responsabile sviluppo |

**Sistemi a rischio medio**:

| Documento | Contenuto | Responsabile |
|-----------|-----------|--------------|
| **Sintesi dell'architettura di sicurezza** | DAS abbreviato che copre i confini di fiducia, i flussi di dati e i controlli chiave | Proprietario del sistema |
| **Valutazione delle minacce** | Identificazione leggera delle minacce e pianificazione delle mitigazioni | RSSI |

**Sistemi a basso rischio**:

- Checklist di design della sicurezza (completata e approvata dal RSSI o suo delegato).

**Archiviazione della documentazione**: La documentazione dell'architettura di sicurezza deve essere archiviata in [Strumento di architettura / Confluence / SharePoint] con accesso limitato a: RSSI, Responsabile sviluppo, Proprietario del sistema e personale con documentata necessità di conoscere approvata dal RSSI. La documentazione deve essere sotto controllo di versione.

**Aggiornamento della documentazione**: La documentazione dell'architettura di sicurezza deve essere revisionata e aggiornata: quando vengono apportate modifiche significative al sistema, quando vengono identificate nuove minacce che riguardano il sistema, e almeno annualmente per i sistemi ad alto rischio.

---

## Processo di revisione dell'architettura

Tutti i nuovi sistemi e le modifiche significative ai sistemi esistenti devono essere sottoposti a revisione dell'architettura di sicurezza prima dell'implementazione.

### Elementi scatenanti per la revisione

È richiesta una revisione dell'architettura di sicurezza quando:

- Viene sviluppato o acquisito un nuovo sistema.
- Si verifica un aggiornamento di versione principale o una migrazione di piattaforma.
- Le modifiche all'architettura riguardano i confini di sicurezza o le zone di fiducia.
- Vengono integrati nuovi servizi esterni o flussi di dati.
- I meccanismi di autenticazione o autorizzazione vengono modificati.
- La classificazione dei dati delle informazioni trattate aumenta.
- Un incidente di sicurezza rivela debolezze architetturali.

### Processo di revisione

| Fase | Attività | Responsabile |
|------|----------|--------------|
| 1. **Avvio** | Il Proprietario del sistema invia la richiesta di revisione dell'architettura con la documentazione del sistema | Proprietario del sistema |
| 2. **Modellazione delle minacce** | Condurre la modellazione delle minacce utilizzando la metodologia STRIDE (obbligatoria per alto rischio; raccomandata per rischio medio) | RSSI / Architetto della sicurezza |
| 3. **Validazione dei requisiti** | Verificare che i requisiti di sicurezza siano completi e allineati con i requisiti aziendali | RSSI |
| 4. **Revisione degli schemi** | Valutare l'architettura rispetto agli schemi sicuri approvati; identificare le deviazioni | RSSI / Architetto della sicurezza |
| 5. **Validazione della difesa in profondità** | Verificare che i controlli siano implementati in tutti i livelli dell'architettura rilevanti | RSSI |
| 6. **Valutazione del rischio** | Documentare i rischi residui e i piani di trattamento per i gap identificati | RSSI / Proprietario del sistema |
| 7. **Approvazione** | Il RSSI approva o restituisce con le modifiche richieste | RSSI |

**Criteri di approvazione**: L'architettura non deve essere approvata se:

- La modellazione delle minacce non è stata completata (sistemi ad alto rischio).
- Esistono rischi critici o alti senza piani di trattamento.
- La difesa in profondità è assente per i sistemi che trattano dati Riservato o Ristretto.
- Le deviazioni dagli schemi di architettura approvati non hanno controlli compensativi e approvazione di eccezione del RSSI.

**SLA di revisione**:

- Sistemi ad alto rischio (con modello delle minacce completo): 15 giorni lavorativi dalla presentazione completa.
- Sistemi a rischio medio (revisione sommaria): 10 giorni lavorativi.
- Sistemi a basso rischio (revisione della checklist): 5 giorni lavorativi.

Le presentazioni incomplete devono essere restituite entro 3 giorni lavorativi con i gap specifici identificati. Il conteggio riprende alla ricezione della documentazione completa.

### Checklist per la revisione dell'architettura (sistemi a rischio medio e alto)

**Identità e accessi**:

- [ ] Meccanismo di autenticazione documentato (SSO, AMF, chiavi API).
- [ ] Modello di autorizzazione definito (RBAC, ABAC).
- [ ] Separazione dell'accesso privilegiato implementata.
- [ ] Autorizzazioni degli account di servizio minimizzate.

**Protezione dei dati**:

- [ ] Classificazione dei dati identificata per tutti i dati trattati.
- [ ] Cifratura a riposo implementata per i dati Riservato/Ristretto.
- [ ] Cifratura in transito (TLS 1.2+) per tutte le comunicazioni di rete.
- [ ] Meccanismi di conservazione ed eliminazione dei dati definiti.

**Sicurezza della rete**:

- [ ] Segmentazione della rete adeguata al livello del sistema.
- [ ] Regole del firewall in entrata/uscita documentate e giustificate.
- [ ] Gateway API o WAF per le applicazioni accessibili da Internet.
- [ ] Comunicazioni interne cifrate dove si trattano dati sensibili.

**Difesa in profondità**:

- [ ] Almeno 3 livelli di controllo verificati (rete, piattaforma, applicazione, dati).
- [ ] Analisi dei singoli punti di guasto condotta.
- [ ] Controlli complementari confermati (diversi vettori di attacco affrontati).

**Monitoraggio e registrazione**:

- [ ] Registrazione degli eventi di sicurezza configurata.
- [ ] Inoltro dei log alla piattaforma di registrazione/SIEM centralizzata.
- [ ] Regole di allerta definite per gli eventi critici.
- [ ] Conservazione dei log conforme ai requisiti della politica.

**Resilienza**:

- [ ] Procedure di backup e ripristino documentate.
- [ ] RPO/RTO definiti e validati.
- [ ] Piano di disaster recovery esistente (sistemi di Livello 1).
- [ ] Ridondanza implementata per i componenti critici.

**Modellazione delle minacce** (solo alto rischio):

- [ ] Analisi STRIDE completata.
- [ ] Vettori di attacco documentati.
- [ ] Mitigazioni mappate a ciascuna minaccia.
- [ ] Rischi residui accettati dal RSSI.

**Conformità**:

- [ ] Requisiti nLPD/GDPR valutati (se si trattano dati personali).
- [ ] Normative specifiche del settore affrontate (se applicabile).
- [ ] Protezione dei dati per impostazione predefinita e fin dalla progettazione dimostrata.

### Revisione esterna dell'architettura di sicurezza

Le organizzazioni devono coinvolgere specialisti esterni di architettura della sicurezza quando:

| Elemento scatenante | Motivazione |
|--------------------|-------------|
| **Nuovo sistema ad alto rischio** sviluppato internamente senza precedente esperienza di architettura sicura | Validazione indipendente del modello delle minacce e delle decisioni di design |
| **Design di sistemi crittografici** (implementazioni personalizzate, gestione delle chiavi) | Richiede competenza specializzata in crittografia |
| **Sistema di elaborazione dei pagamenti** | Conformità PCI DSS e requisiti di sicurezza specializzati |
| **Implementazione Zero Trust** (design iniziale) | Architettura complessa che richiede competenza specializzata Zero Trust |
| **Incidente significativo** che ha rivelato una debolezza architetturale | Analisi indipendente della causa principale e guida alla remediation |
| **Integrazione post-acquisizione/fusione** | Valutazione di terze parti del security posture dell'architettura combinata |
| **Rilievo di audit normativo** relativo all'architettura | Validazione indipendente del design di remediation |

I revisori esterni devono essere selezionati in base a: certificazioni pertinenti del settore (CISSP, CCSP o equivalente), esperienza dimostrata con architetture simili e indipendenza dai fornitori di implementazione.

### Modellazione delle minacce

Dove è richiesta la modellazione delle minacce, la metodologia STRIDE deve essere utilizzata come approccio principale:

| Categoria STRIDE | Tipo di minaccia | Esempio |
|------------------|-----------------|---------|
| **Spoofing** | Impersonazione dell'identità | Furto di credenziali, session hijacking |
| **Tampering** | Modifica non autorizzata | Manipolazione dei dati, modifica della configurazione |
| **Repudiation** | Negazione delle azioni | Assenza di tracce di audit |
| **Information Disclosure** | Esposizione dei dati | Dati non cifrati, messaggi di errore dettagliati |
| **Denial of Service** | Interruzione della disponibilità | Esaurimento delle risorse, flooding |
| **Elevation of Privilege** | Acquisizione di accesso non autorizzato | Escalation dei privilegi, attacchi di iniezione |

I modelli delle minacce devono essere conservati per:

- **Sistemi attivi**: Ciclo di vita del sistema più 3 anni dopo la dismissione.
- **Incidenti gravi**: I modelli delle minacce per i sistemi coinvolti in incidenti di sicurezza devono essere conservati in modo permanente (minimo 7 anni).

I modelli delle minacce devono essere revisionati e aggiornati: ad ogni rilascio principale, quando l'architettura del sistema cambia significativamente, quando vengono identificate nuove informazioni sulle minacce rilevanti per il sistema, e almeno annualmente per i sistemi ad alto rischio.

---

## Criteri di sicurezza per la selezione delle tecnologie

Quando si selezionano nuove tecnologie, piattaforme, framework o componenti di terze parti, la sicurezza deve essere un criterio di selezione con peso uguale ai requisiti funzionali.

### Criteri di selezione

| Criterio | Requisito |
|----------|-----------|
| **Security posture del fornitore** | Il fornitore fornisce prove di pratiche di sviluppo sicuro (ad esempio, certificazione SOC 2, ISO 27001 o equivalente) |
| **Storico delle vulnerabilità** | Nessun modello di vulnerabilità critiche irrisolte; track record di rilascio di patch tempestive |
| **Impostazioni predefinite sicure** | La tecnologia viene fornita con una configurazione predefinita sicura; non richiede un'ampia fase di rafforzamento per raggiungere uno stato accettabile |
| **Supporto alla cifratura** | Supporta gli standard di cifratura correnti (TLS 1.2 minimo, TLS 1.3 preferito; AES-256 per i dati a riposo) |
| **Integrazione dell'autenticazione** | Supporta l'integrazione con il provider di identità dell'organizzazione (SAML, OIDC o equivalente) |
| **Registrazione e verificabilità** | Fornisce registrazione degli eventi di sicurezza compatibile con l'infrastruttura di registrazione dell'organizzazione |
| **Meccanismo di aggiornamento e patch** | Il fornitore fornisce aggiornamenti di sicurezza regolari con un processo di advisory chiaro |
| **Roadmap di fine vita** | Ciclo di supporto chiaro; nessuna tecnologia a fine vita o entro 12 mesi dalla fine del supporto deve essere selezionata |
| **Conformità normativa** | La tecnologia supporta la conformità con nLPD, GDPR (ove applicabile) e i requisiti ISO 27001 |

Le decisioni di selezione delle tecnologie per i sistemi ad alto rischio devono essere documentate con prove di valutazione della sicurezza e approvate dal RSSI prima dell'acquisizione.

---

## Configurazioni di sicurezza di base

L'organizzazione deve mantenere configurazioni di sicurezza di base per ciascun livello di sistema, definendo i controlli di sicurezza minimi richiesti.

### Classificazione dei livelli di sistema

| Livello | Descrizione | Sistemi di esempio |
|---------|-------------|-------------------|
| **Livello 1 — Critico** | Sistemi che trattano dati Riservato o Ristretto; accessibili da Internet; funzione aziendale principale | ERP, CRM con dati personali dei clienti, sistemi di pagamento, applicazioni web pubblicamente accessibili |
| **Livello 2 — Importante** | Sistemi che trattano dati Interno; esposizione esterna limitata; funzione aziendale di supporto | Strumenti di collaborazione interna, gestione dei progetti, reportistica interna |
| **Livello 3 — Standard** | Sistemi che trattano solo dati Pubblico; nessun dato personale; funzione non critica | Sito web di marketing (contenuto statico), wiki interni (non sensibili) |

**Riclassificazione del livello di sistema**:

Il livello del sistema deve essere revisionato e potenzialmente riclassificato quando:

- **La classificazione dei dati aumenta**: Il sistema inizia a trattare dati Riservato o Ristretto (ad esempio, Livello 3 riclassificato come Livello 1).
- **L'esposizione a Internet cambia**: Il sistema interno diventa accessibile da Internet (ad esempio, Livello 2 riclassificato come Livello 1).
- **La criticità aziendale aumenta**: Il sistema diventa critico per i ricavi o una funzione operativa principale (ad esempio, Livello 2 riclassificato come Livello 1).
- **Si verifica un incidente di sicurezza**: L'incidente rivela che il sistema è ad un rischio più elevato di quanto originariamente valutato.
- **L'ambito normativo si espande**: Il sistema inizia a trattare dati soggetti a normative (PCI DSS, GDPR).

La riclassificazione attiva requisiti di configurazione di sicurezza di base aggiornati e una revisione dell'architettura. Il Proprietario del sistema deve richiedere una revisione della riclassificazione al RSSI quando si verifica un elemento scatenante.

### Requisiti di base per livello

| Area di controllo | Livello 1 (Critico) | Livello 2 (Importante) | Livello 3 (Standard) |
|-------------------|---------------------|------------------------|----------------------|
| **Autenticazione** | AMF obbligatoria; integrazione SSO; timeout di sessione | AMF obbligatoria; integrazione SSO | Conformità alla politica sulle password |
| **Cifratura in transito** | TLS 1.3 richiesto (eccezione TLS 1.2 con approvazione del RSSI) | TLS 1.2 minimo | TLS 1.2 minimo |
| **Cifratura a riposo** | AES-256 obbligatoria | AES-256 per dati personali/sensibili | Richiesta per i sistemi che trattano dati personali (nomi, indirizzi e-mail) anche se non sensibili; non richiesta per dati veramente pubblici (contenuti di marketing, documentazione pubblicata) |
| **Segmentazione della rete** | Segmento dedicato; micro-segmentazione ove fattibile | Segmentato dalle reti non attendibili | Controlli di rete standard |
| **Registrazione** | Tutti gli eventi di sicurezza al SIEM centralizzato; allerta in tempo reale | Eventi di sicurezza alla registrazione centralizzata | Registrazione di base degli accessi |
| **Scansione delle vulnerabilità** | Continua o settimanale | Mensile | Trimestrale |
| **Test di penetrazione** | Annualmente + prima del rilascio iniziale + dopo modifiche significative | Ogni 2 anni | Decisione basata sul rischio |
| **Revisione dell'architettura** | Obbligatoria (revisione completa con modello delle minacce) | Obbligatoria (revisione sommaria) | Checklist di sicurezza |
| **Backup e ripristino** | RPO e RTO definiti per BIA; testati annualmente | Backup regolari; ripristino testato | Politica di backup standard |
| **Revisione degli accessi** | Trimestrale | Semestralmente | Annualmente |

Le configurazioni di sicurezza di base devono essere revisionate annualmente dal RSSI e aggiornate per riflettere le minacce attuali, i cambiamenti tecnologici e i requisiti normativi.

---

## Schemi di architettura sicura

L'organizzazione deve mantenere un catalogo di schemi di architettura sicura approvati a cui i progettisti di sistemi devono fare riferimento quando costruiscono nuovi sistemi o modificano quelli esistenti.

**Categorie di schemi**:

| Categoria | Esempi |
|-----------|--------|
| **Autenticazione** | Integrazione SSO (SAML/OIDC), implementazione AMF, gestione delle chiavi API, autenticazione basata su certificati |
| **Autorizzazione** | Controllo degli accessi basato sui ruoli (RBAC), controllo degli accessi basato sugli attributi (ABAC), autorizzazione API (OAuth 2.0) |
| **Protezione dei dati** | Cifratura a riposo (AES-256), cifratura in transito (TLS 1.3), tokenizzazione per i dati personali, mascheratura dei dati |
| **Sicurezza della rete** | Architettura DMZ, micro-segmentazione, gateway API con WAF, VPN/ZTNA per l'accesso remoto |
| **Integrazione** | Schemi API sicuri (REST con OAuth 2.0), sicurezza delle code di messaggi, service mesh con mTLS |
| **Cloud** | Architettura della landing zone, isolamento dei carichi di lavoro, controlli di sicurezza cloud-native, integrazione CSPM |

Ogni schema approvato deve documentare:

- Motivazione della sicurezza e mitigazione delle minacce.
- Guida all'implementazione.
- Insidie comuni e anti-schemi da evitare.
- Criteri di test e validazione.

**Governance degli schemi**:

- Gli schemi approvati devono essere revisionati annualmente per verificarne la continua adeguatezza.
- Le deviazioni dagli schemi approvati richiedono l'approvazione del RSSI con giustificazione documentata e controlli compensativi.
- I nuovi schemi devono essere validati attraverso la modellazione delle minacce prima dell'aggiunta al catalogo.

**Esempio di schema approvato: Integrazione SSO con SAML 2.0**

**Motivazione della sicurezza**:

- Centralizza l'autenticazione, riducendo la proliferazione delle credenziali.
- Consente l'applicazione dell'AMF presso il provider di identità.
- Fornisce una traccia di audit degli accessi alle applicazioni.
- Supporta il provisioning just-in-time.

**Guida all'implementazione**:

1. Registrare l'applicazione presso il provider di identità (Azure AD, Okta, Google Workspace).
2. Configurare le asserzioni SAML per includere gli attributi richiesti (e-mail, gruppi, stato AMF).
3. Validare le firme e i certificati della risposta SAML.
4. Implementare la propagazione del logout (SLO — Single Logout).
5. Impostare il timeout della sessione allineato alla politica dell'organizzazione (massimo 4 ore).

**Insidie comuni**:

- Accettare asserzioni SAML non firmate.
- Non validare la scadenza del certificato.
- Fidarsi del contenuto dell'asserzione senza verifica della firma.
- Non implementare la propagazione del logout (l'utente rimane connesso all'applicazione dopo il logout dal provider di identità).

**Criteri di test**:

- Il login reindirizza al provider di identità.
- L'applicazione dell'AMF è visibile nel flusso di autenticazione.
- La risposta SAML non valida viene rifiutata.
- La sessione scade dopo il periodo di timeout.
- Il logout dal provider di identità disconnette l'utente dall'applicazione.

**Implementazione di riferimento**: [Link al repository del codice / wiki]

**Posizione del catalogo degli schemi**: [Strumento di architettura / Confluence / SharePoint] — accessibile a tutti gli architetti di sistema e agli sviluppatori.

### Anti-schemi di architettura comuni da evitare

| Anti-schema | Rischio | Alternativa |
|-------------|---------|-------------|
| **Database condiviso tra confini di fiducia** | Movimento laterale; escalation dei privilegi tramite SQL injection | Database per servizio o forte isolamento a livello di schema con credenziali separate |
| **Segreti hardcoded nella configurazione** | Esposizione delle credenziali nel controllo di versione | Sistema di gestione dei segreti (Vault, Key Vault, Secrets Manager) |
| **Bypass dell'autenticazione per servizi "interni"** | Presupposto che la rete interna sia attendibile | TLS mutuo o OAuth 2.0 per la comunicazione da servizio a servizio |
| **Registrazione di dati sensibili (password, token, dati personali)** | Violazione della conformità; minaccia interna | Redazione dei log o tokenizzazione prima della registrazione |
| **Account amministratore singolo condiviso tra servizi** | Nessuna responsabilità; proliferazione delle credenziali | Account amministratori specifici per servizio con privilegio minimo |
| **Endpoint di health check non autenticati che espongono i dettagli del sistema** | Divulgazione di informazioni | Health check autenticati o risposta minima (solo HTTP 200) |
| **Accesso diretto al database dal livello web** | Amplificazione SQL injection; nessuna difesa in profondità | Livello API/servizio tra web e database |
| **Fidarsi della validazione lato client** | Bypass banale | Validazione lato server; lato client solo come miglioramento dell'UX |

---

## Sistemi di terze parti e sistemi acquisiti

I principi di ingegneria sicura si applicano ai sistemi sviluppati da terze parti e acquisiti che vengono integrati nell'ambiente dell'organizzazione.

**Pre-acquisizione**:

- La documentazione dell'architettura di sicurezza deve essere revisionata prima dell'approvazione dell'acquisizione.
- La valutazione della sicurezza del fornitore deve essere condotta secondo la Politica sui fornitori e i servizi cloud (A.5.19-23).
- La compatibilità dell'architettura con gli standard di sicurezza dell'organizzazione deve essere verificata.

**Requisiti contrattuali**:

- Gli sviluppatori terzi devono essere contrattualmente tenuti a seguire i principi di ingegneria sicura dell'organizzazione.
- La revisione dell'architettura di sicurezza deve essere richiesta alla milestone di design.
- Devono essere fornite prove di pratiche di sviluppo sicuro.
- I risultati dei test di sicurezza devono essere forniti prima dell'accettazione.

**Post-acquisizione**:

- Revisione della sicurezza dell'integrazione prima della distribuzione nell'ambiente dell'organizzazione.
- Rivalutazione annuale dell'architettura per i servizi SaaS e gestiti.
- La non conformità del fornitore deve attivare l'escalation dei problemi secondo i termini del contratto.

**Elementi scatenanti per la revisione continua dei sistemi di terze parti**:

- Aggiornamenti di versione principale (ad esempio, da v2.x a v3.x).
- Modifiche all'ambito di trattamento dei dati del sistema di terze parti.
- Incidenti di sicurezza che riguardano il sistema di terze parti.
- Revisione annuale per le integrazioni di Livello 1.
- Ogni 2 anni per le integrazioni di Livello 2.
- Quando la certificazione SOC 2 o ISO 27001 del fornitore scade.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Ingegneria dei sistemi sicuri (ISS)** | La disciplina di integrazione delle considerazioni sulla sicurezza in tutte le fasi del ciclo di vita del sistema per produrre sistemi affidabili |
| **Security by Design** | Principio secondo cui la sicurezza è integrata nei sistemi fin dall'inizio anziché aggiunta dopo lo sviluppo |
| **Security by Default** | Principio secondo cui i sistemi sono configurati in modo sicuro fin dall'installazione senza richiedere azioni dell'utente per abilitare la sicurezza |
| **Difesa in profondità** | Approccio di sicurezza a livelli dove molteplici controlli proteggono le risorse in modo che la compromissione di un livello non comporti una compromissione totale |
| **Zero Trust** | Modello di sicurezza basato sul "non fidarsi mai, verificare sempre" — nessuna fiducia implicita viene concessa in base alla posizione di rete o all'autenticazione precedente |
| **Modello delle minacce** | Analisi strutturata delle minacce potenziali, dei vettori di attacco e delle contromisure per un sistema |
| **Architettura di sicurezza** | Artefatti di design che descrivono come i controlli di sicurezza sono posizionati e come si relazionano all'architettura complessiva del sistema |
| **Superficie di attacco** | La somma di tutti i punti dove un attaccante potrebbe potenzialmente entrare o estrarre dati da un sistema |
| **STRIDE** | Metodologia di modellazione delle minacce che categorizza le minacce come Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service ed Elevation of Privilege |
| **Configurazione di sicurezza di base** | L'insieme minimo di controlli di sicurezza richiesti per un determinato livello o classificazione di sistema |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità per l'architettura sicura |
|-------|------------------------------------------|
| **Direzione generale** | Approvare la politica di ingegneria sicura; allocare le risorse per le revisioni dell'architettura; accettare i rischi architetturali residui |
| **RSSI** | Titolarità della politica; definire e mantenere i principi di ingegneria sicura; condurre o commissionare le revisioni dell'architettura; approvare le eccezioni architetturali; supervisione della modellazione delle minacce |
| **Responsabile sviluppo** | Garantire che i team di sviluppo applichino i principi di ingegneria sicura; partecipare alle revisioni dell'architettura; mantenere l'allineamento agli standard tecnologici |
| **Proprietari dei sistemi** | Sottoporre i sistemi alla revisione dell'architettura; mantenere la documentazione dell'architettura di sicurezza; possedere i rischi specifici del sistema |
| **Sviluppatori / Ingegneri** | Applicare i principi di ingegneria sicura nel design e nell'implementazione del sistema; partecipare alla modellazione delle minacce; utilizzare gli schemi di architettura approvati |
| **IT Operations** | Implementare e mantenere le configurazioni di sicurezza di base; applicare gli standard di configurazione; supportare la revisione dell'architettura con informazioni sull'infrastruttura |
| **Fornitori terzi** | Conformarsi ai requisiti contrattuali di ingegneria sicura; fornire documentazione dell'architettura e prove dei test di sicurezza |

### Percorso di escalation

- Preoccupazioni di sicurezza architetturale: Lo sviluppatore/ingegnere notifica il RSSI. Il RSSI scala alla Direzione generale se sono necessarie risorse o modifiche organizzative.
- Deviazioni dagli schemi: Il richiedente presenta la richiesta di deviazione al RSSI. Il RSSI approva o rifiuta con motivazione documentata.
- Accettazione del rischio architetturale: Il Proprietario del sistema presenta la valutazione del rischio al RSSI. I rischi che superano la soglia di accettazione del RSSI vengono scalati alla Direzione generale.

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

| # | Prova | Responsabile | Frequenza |
|---|-------|--------------|-----------|
| 1 | **Principi di ingegneria sicura documentati** (questa politica e tutti i documenti di standard di supporto) | RSSI | *Rivisti annualmente; aggiornati in caso di cambiamenti nel panorama delle minacce o normativi* |
| 2 | **Documentazione dell'architettura di sicurezza** (DAS, modelli delle minacce, tracciabilità dei requisiti di sicurezza) per sistemi ad alto rischio e a rischio medio | RSSI / Proprietario del sistema | *Per sistema; aggiornata in caso di modifica significativa; revisionata annualmente per l'alto rischio* |
| 3 | **Registri di revisione dell'architettura** (richieste di revisione, risultati, approvazione o rifiuto con motivazione) | RSSI | *Per revisione; conservati 3 anni* |
| 4 | **Report dei modelli delle minacce** (analisi STRIDE, valutazioni del rischio, mitigazioni, rischi residui) | RSSI | *Per sistema; conservati per il ciclo di vita del sistema + 3 anni; in modo permanente per i sistemi coinvolti in incidenti gravi (minimo 7 anni)* |
| 5 | **Catalogo degli schemi di architettura approvati** (schemi documentati con motivazione della sicurezza) | RSSI / Responsabile sviluppo | *Mantenuto continuamente; rivisto annualmente* |
| 6 | **Configurazioni di sicurezza di base** (per livello di sistema, con controlli minimi documentati) | RSSI / IT Operations | *Riviste annualmente; aggiornate in caso di cambiamenti tecnologici o delle minacce* |
| 7 | **Valutazioni di sicurezza per la selezione delle tecnologie** (registrazioni delle valutazioni di sicurezza per nuovi acquisti tecnologici) | RSSI | *Per acquisizione; conservate 3 anni* |
| 8 | **Registro delle eccezioni architetturali** (deviazioni dagli schemi o principi con approvazione del RSSI, controlli compensativi e date di scadenza) | RSSI | *Rivisto trimestralmente; conservato 3 anni dopo la chiusura* |
| 9 | **Valutazioni dell'architettura di terze parti** (revisioni dell'architettura di sicurezza dei fornitori, revisioni della sicurezza dell'integrazione) | RSSI | *Per incarico; conservate per la durata del contratto + 2 anni* |
| 10 | **Progressi nell'implementazione Zero Trust** (valutazione della maturità, roadmap, prove di completamento delle fasi) | RSSI | *Valutati annualmente; comunicati alla Direzione generale* |
| 11 | **Registri di validazione della difesa in profondità** (analisi dei livelli di controllo che confermano i controlli a livelli nell'architettura) | RSSI / IT Operations | *Semestralmente per i sistemi di Livello 1; annualmente per il Livello 2* |
| 12 | **Registri di formazione** (completamento della formazione su architettura e ingegneria sicura per il personale rilevante) | RSSI / HR | *Tracciati per individuo; revisionati annualmente; obiettivo: 100% completamento* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, tracciamento del completamento delle revisioni dell'architettura, analisi dell'adozione degli schemi, audit di conformità alle configurazioni di sicurezza di base, valutazioni della copertura dei modelli delle minacce, audit interni ed esterni e feedback al proprietario della politica.

Le seguenti metriche devono essere tracciate e comunicate al RSSI trimestralmente:

| Metrica | Obiettivo | Soglia critica |
|---------|-----------|----------------|
| Nuovi sistemi ad alto rischio con revisione dell'architettura completata | 100% | <100% |
| Nuovi sistemi a rischio medio con revisione dell'architettura completata | 100% | <80% |
| Completamento della revisione dell'architettura entro l'SLA (basato sul rischio: 5/10/15 giorni lavorativi) | 90% | <70% |
| Tasso di adozione degli schemi di architettura approvati per i nuovi sistemi | 80% | <60% |
| Eccezioni architetturali attive | Minimizzate; tendenza decrescente | >5 contemporanee o qualsiasi >12 mesi |
| Conformità alle configurazioni di sicurezza di base (sistemi di Livello 1) | 100% | <90% |
| Modelli delle minacce aggiornati per i sistemi ad alto rischio | 100% | <80% |

**Requisiti di reportistica**:
- **Report trimestrale del RSSI**: Stato delle revisioni dell'architettura, adozione degli schemi, stato del registro delle eccezioni, conformità alle configurazioni di base.
- **Report annuale alla Direzione generale**: Progressi nella maturità Zero Trust, efficacia del programma di architettura, rischi chiave e requisiti di risorse.
- **Revisione annuale della direzione**: Valutazione completa del programma di ingegneria sicura incluse le tendenze delle metriche, i risultati significativi e le raccomandazioni di miglioramento.

Le metriche che superano le soglie critiche devono essere scalate al RSSI per un'attenzione immediata e comunicate alla prossima Revisione della direzione.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata dal RSSI in anticipo, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita. Le eccezioni architetturali devono essere limitate nel tempo (massimo 12 mesi) e revisionate trimestralmente. Le eccezioni devono essere comunicate al Team di revisione della direzione. Le eccezioni permanenti ai principi fondamentali di ingegneria sicura e le eccezioni che eliminano la difesa in profondità non sono consentite.

## Non conformità

Un dipendente che si constata abbia violato questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro. I sistemi distribuiti in produzione senza la revisione dell'architettura richiesta possono essere sospesi dalla produzione in attesa di revisione e remediation.

## Allineamento SOC 2

Questa politica supporta la conformità ai criteri SOC 2 Trust Services:

| Criterio SOC 2 | Copertura |
|----------------|-----------|
| **CC3.1** (Specificazione degli obiettivi) | Obiettivi di sicurezza nel design del sistema |
| **CC5.2** (Controlli generali sulla tecnologia) | Controlli architetturali; le modifiche all'architettura richiedono l'approvazione del controllo delle modifiche secondo la Politica di gestione della configurazione (A.8.9) |
| **CC6.1** (Sicurezza degli accessi logici) | Architettura di autenticazione, privilegio minimo, Zero Trust |
| **CC6.6** (Protezione dalle minacce esterne) | Difesa in profondità, controlli perimetrali |
| **CC7.1** (Rilevamento delle vulnerabilità) | Scansione delle vulnerabilità nei requisiti delle configurazioni di base |
| **CC7.2** (Rilevamento delle anomalie) | Livello di monitoraggio nella difesa in profondità; riferimento incrociato alla Politica sulle attività di monitoraggio (A.8.16) |
| **CC9.2** (Gestione del rischio dei fornitori) | Revisione dell'architettura di terze parti; riferimento incrociato alla Politica sui fornitori e i servizi cloud (A.5.19-23) |

**Requisiti di prove SOC 2**:

- Registri di revisione dell'architettura (Prova n. 3).
- Modelli delle minacce (Prova n. 4).
- Catalogo degli schemi approvati (Prova n. 5).
- Configurazioni di sicurezza di base (Prova n. 6).
- Matrice di tracciabilità dei requisiti di sicurezza per i sistemi ad alto rischio.
- Prove dell'approvazione del RSSI per le eccezioni architetturali (Prova n. 8).

## Miglioramento continuo

Questa politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti agli standard di ingegneria sicura (NIST SP 800-160, NIST SP 800-207), l'evoluzione del panorama delle minacce e delle tecniche di attacco, nuovi schemi di architettura e standard tecnologici, modifiche normative (nLPD, GDPR), lezioni apprese dagli incidenti di sicurezza e dalle revisioni dell'architettura, e risultati degli audit. Le non conformità relative a questa politica devono essere registrate e gestite attraverso il processo di azione correttiva del SGSI (Clausola 10.2) con analisi della causa principale e remediation tracciata.

---

# Aree della norma ISO 27001 trattate

Politica sull'architettura dei sistemi sicuri e principi di ingegneria — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.1 Azioni per affrontare rischi e opportunità | 5.8 Sicurezza delle informazioni nella gestione dei progetti |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 8.25 Ciclo di vita dello sviluppo sicuro |
| Clausola 8.1 Pianificazione e controllo operativo | 8.26 Requisiti di sicurezza delle applicazioni |
| Clausola 9.1 Monitoraggio, misurazione, analisi e valutazione | **8.27 Architettura dei sistemi sicuri e principi di ingegneria** |
| Clausola 10.2 Non conformità e azione correttiva | 8.28 Codifica sicura |
| | 8.29 Test di sicurezza nello sviluppo e nell'accettazione |
| | 8.31 Separazione degli ambienti di sviluppo, test e produzione |
| | 8.9 Gestione della configurazione |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|------------------|-----------|
| nLPD svizzera (revDSG) | Art. 7 — Protezione dei dati per impostazione predefinita e fin dalla progettazione; Art. 8 — Misure tecniche e organizzative adeguate al rischio |
| OPDo svizzera | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 25 — Protezione dei dati per impostazione predefinita e fin dalla progettazione; Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Controllo Allegato A 8.27 — Architettura dei sistemi sicuri e principi di ingegneria |
| ISO/IEC 27002:2022 | Sezione 8.27 — Guida all'implementazione dell'architettura dei sistemi sicuri |
| NIST SP 800-160 Vol. 1 Rev. 1 | Engineering Trustworthy Secure Systems — principi fondamentali di ingegneria della sicurezza dei sistemi |
| NIST SP 800-207 | Zero Trust Architecture — architettura di riferimento per l'implementazione Zero Trust |
| NIST SP 800-53 Rev 5 | SA-8 (Principi di ingegneria della sicurezza e della privacy) — 28 principi di ingegneria della sicurezza |
| CIS Controls v8 | Controllo 4 (Configurazione sicura), Controllo 16 (Sicurezza del software applicativo) — salvaguardie a supporto dell'architettura sicura |

---

<!-- QA_VERIFIED: 2026-04-03 -->
