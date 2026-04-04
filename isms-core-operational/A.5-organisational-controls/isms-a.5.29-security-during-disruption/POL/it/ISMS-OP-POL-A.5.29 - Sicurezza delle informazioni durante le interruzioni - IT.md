<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.29-IT:operational:OP-POL:a.5.29 -->
**ISMS-OP-POL-A.5.29 — Sicurezza delle informazioni durante le interruzioni**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza delle informazioni durante le interruzioni |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.5.29 |
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
| 1.0 | [Data] | RSSI | Policy operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Data prossima revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- Controllo ISO/IEC 27001:2022 A.5.29 — Sicurezza delle informazioni durante le interruzioni
- ISO/IEC 22301 — Sistemi di gestione della continuità operativa (riferimento informativo)
- NIST SP 800-34 Rev 1 — Guida alla pianificazione delle contingenze per i sistemi informativi federali (riferimento informativo)
- NIST SP 800-61 Rev 2 — Guida alla gestione degli incidenti di sicurezza informatica (riferimento informativo)

**Controlli Annex A correlati**:

| Controllo | Relazione con la sicurezza delle informazioni durante le interruzioni |
|-----------|----------------------------------------------------------------------|
| A.5.24–28 Ciclo di vita della gestione degli incidenti | Gli incidenti di sicurezza possono innescare o coincidere con interruzioni operative |
| A.5.30 Prontezza ICT per la continuità operativa | La pianificazione BC/DR fornisce il quadro operativo; A.5.29 fornisce la sovrapposizione di sicurezza |
| A.8.13 Backup delle informazioni | La protezione dei backup è un controllo di sicurezza non negoziabile durante le interruzioni |
| A.8.14 Ridondanza delle strutture di elaborazione delle informazioni | La sicurezza del sito di ripristino deve essere equivalente a quella del sito principale |
| A.5.15–16–18 Gestione delle identità e degli accessi | Procedure di accesso di emergenza e controllo degli accessi durante le interruzioni |
| A.8.15 Logging | La continuità del logging è obbligatoria anche durante le operazioni degradate |
| A.8.16 Attività di monitoraggio | Monitoraggio potenziato richiesto durante gli stati elevati e degradati |

**Policy interne correlate**:

- Policy di continuità operativa e disaster recovery
- Policy di gestione degli incidenti
- Policy di gestione delle identità e degli accessi
- Policy di logging
- Policy sulle attività di monitoraggio (A.8.16)
- Policy di gestione dei cambiamenti

---

# Policy sulla sicurezza delle informazioni durante le interruzioni

## Scopo

Questa policy stabilisce i requisiti per il mantenimento dei controlli di sicurezza delle informazioni durante eventi di interruzione. Le interruzioni — che si tratti di catastrofi naturali, guasti infrastrutturali, attacchi informatici, pandemie o interruzioni della catena di fornitura — creano condizioni in cui i controlli di sicurezza sono più probabilmente indeboliti, proprio quando l'esposizione alle minacce è massima.

**"La sicurezza non va in vacanza."** Quando le organizzazioni si concentrano sul ripristino, gli avversari sfruttano la ridotta vigilanza, il personale distratto e i controlli degradati. Questa policy garantisce che l'organizzazione mantenga una postura di sicurezza minima definita durante tutte le fasi dell'interruzione e del ripristino, e validi che i controlli di sicurezza completi siano ripristinati prima del ritorno alle normali operazioni.

Questa policy supporta la nLPD svizzera (revDSG) Art. 8 mantenendo misure tecniche e organizzative di sicurezza appropriate durante le condizioni avverse. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 32 per la sicurezza continuativa del trattamento.

## Ambito di applicazione

Questa policy si applica a:

- Tutti gli eventi di interruzione che influiscono sulla capacità dell'organizzazione di operare normalmente, inclusi catastrofi naturali, guasti infrastrutturali, incidenti informatici, pandemie, interruzioni della catena di fornitura e disordini civili.
- Tutti i sistemi informativi, le reti, le applicazioni e le strutture di elaborazione dei dati nell'ambito ISO 27001.
- Tutti i processi di business continuity e disaster recovery.
- Tutto il personale — dipendenti, collaboratori e utenti terzi — durante le fasi di interruzione e ripristino.

## Principio

**La sicurezza delle persone è la nostra prima priorità. Sempre.**

Una volta garantita la sicurezza e il benessere del personale, la continuità della sicurezza delle informazioni diventa la priorità immediata. L'organizzazione DEVE pianificare, implementare e mantenere processi per garantire il livello richiesto di sicurezza delle informazioni durante le situazioni avverse, inclusi controlli compensativi laddove le misure di sicurezza standard non possano essere mantenute.

Nessuna azione di ripristino, per quanto urgente, giustifica la rimozione permanente dei controlli di sicurezza fondamentali. Laddove sia necessario un allentamento temporaneo, questo DEVE essere documentato, limitato nel tempo, compensato e monitorato fino alla chiusura.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Interruzione** | Qualsiasi evento che interrompe o minaccia di interrompere le normali operazioni aziendali |
| **Livello di postura di sicurezza** | Stato definito di implementazione dei controlli di sicurezza (Normale, Elevato, Degradato, Emergenza, Ripristino) |
| **Baseline minima di sicurezza** | Controlli di sicurezza non negoziabili che DEVONO essere mantenuti indipendentemente dallo stato operativo |
| **Accesso break-glass** | Meccanismo di accesso privilegiato di emergenza attivato quando l'accesso normale non è disponibile |
| **Debito di sicurezza** | Controlli o attività di sicurezza differiti durante un'interruzione che richiedono successiva remediation |
| **Sito di ripristino** | Ubicazione alternativa (fisica o cloud) per la ripresa delle operazioni durante un'interruzione |
| **Controllo compensativo** | Misura di sicurezza alternativa implementata quando il controllo principale non è disponibile |
| **Crisis management team** | Team interfunzionale attivato per gestire la risposta organizzativa a una grave interruzione |

---

## Baseline minima di sicurezza

### Controlli non negoziabili

I seguenti controlli di sicurezza DEVONO essere mantenuti in qualsiasi momento, indipendentemente dallo stato di interruzione. Questi controlli non sono soggetti ad allentamento o eccezione:

| Categoria di controllo | Requisito minimo | Motivazione |
|-----------------------|-----------------|-------------|
| **Controllo degli accessi** | Autenticazione richiesta per tutti gli accessi ai sistemi | Previene l'accesso non autorizzato in condizioni caotiche |
| **Cifratura dei dati** | Cifratura a riposo per i dati riservati e limitati | I dati rimangono protetti se i supporti vengono persi, rubati o esposti durante il ripristino |
| **Logging** | Il logging dei sistemi critici continua su tutti i sistemi Tier 1 e Tier 2 | Mantiene la traccia di audit per le indagini post-incidente e la conformità normativa |
| **Segmentazione di rete** | I confini di rete critici vengono mantenuti | Previene i movimenti laterali se un attaccante sfrutta l'interruzione |
| **Protezione dei backup** | I backup rimangono cifrati e con controllo degli accessi | Previene la compromissione dei backup come percorso alternativo al furto di dati |

### Controlli accettabili in modalità degradata

I seguenti controlli possono essere temporaneamente allentati durante un'interruzione, previa approvazione documentata del RSSI (o del suo sostituto designato), implementazione di controlli compensativi e inserimento nel Registro del debito di sicurezza:

| Categoria di controllo | Degradazione accettabile | Controllo compensativo richiesto | Durata massima |
|-----------------------|-------------------------|----------------------------------|----------------|
| **Autenticazione a più fattori** | Fattore singolo se l'infrastruttura AMF non è disponibile | Logging potenziato, limiti di tempo della sessione, restrizioni basate sull'IP | Durata dell'interruzione + 7 giorni |
| **Scansione delle vulnerabilità** | Scansione programmata posticipata | Revisione manuale delle patch critiche; applicare patch critiche/alte entro 72h/7gg | 30 giorni |
| **Monitoraggio della sicurezza** | Ambito di monitoraggio ridotto | Concentrarsi sui sistemi Tier 1 e Tier 2; revisione manuale potenziata | Durata dell'interruzione + 14 giorni |
| **Revisioni degli accessi** | Revisioni periodiche posticipate | Approvazione più rigorosa per le nuove richieste di accesso durante l'interruzione | 30 giorni |
| **Gestione delle patch** | Patching ritardato per vulnerabilità non critiche | Vulnerabilità critiche e alte ancora patchate entro 72h/7gg | 30 giorni per le non critiche |

**Tracciamento obbligatorio**: Qualsiasi allentamento dei controlli approvato DEVE creare immediatamente una voce a tempo limitato nel Registro del debito di sicurezza, includendo: proprietario, controlli compensativi in vigore, data di inizio, data target di chiusura ed evidenza della chiusura alla remediation.

### Mai accettabile

Le seguenti azioni sono vietate anche durante l'interruzione più grave. Non esistono eccezioni:

- **Disabilitazione del logging** sui sistemi critici — la traccia di audit non deve mai essere interrotta
- **Rimozione dei requisiti di autenticazione** — nessun accesso anonimo ad alcun sistema
- **Decifratura dei dati a riposo** senza re-cifratura — i dati devono rimanere protetti
- **Disabilitazione di firewall o IDS/IPS** sui confini di rete critici
- **Condivisione di credenziali privilegiate** senza responsabilità individuale — ogni azione deve essere attribuibile a una persona
- **Elusione della gestione dei cambiamenti** per i sistemi di produzione senza seguire la procedura di modifica di emergenza (con revisione post-implementazione obbligatoria entro 5 giorni lavorativi)

### Gestione dei cambiamenti di emergenza durante le interruzioni

**Regola standard**: Tutte le modifiche in produzione richiedono l'approvazione della gestione dei cambiamenti ai sensi della Policy di gestione dei cambiamenti.

**Eccezione per modifica di emergenza**: Durante la postura di sicurezza **Degradata** o di **Emergenza**, le modifiche di emergenza possono essere implementate con approvazione abbreviata, soggetta ai seguenti requisiti.

**Criteri per le modifiche di emergenza** (tutti devono essere soddisfatti):

1. La modifica è necessaria per ripristinare le operazioni aziendali critiche o mitigare un incidente di sicurezza attivo.
2. Il ritardo fino all'approvazione standard della modifica causerebbe un danno significativo.
3. La modifica è approvata verbalmente dal CIO o dal RSSI (o dal loro sostituto designato).
4. La modifica è registrata immediatamente in [Sistema di gestione dei cambiamenti / Ticket incidente].

**Procedura per le modifiche di emergenza**:

1. **Approvazione verbale**: Il richiedente della modifica contatta CIO/RSSI tramite piattaforma di comunicazione di crisi o telefono; descrive la modifica, la motivazione e il piano di rollback.
2. **Approvazione**: Il CIO o il RSSI fornisce l'approvazione verbale; l'approvazione viene registrata con timestamp e nome del responsabile.
3. **Implementazione**: La modifica viene implementata con monitoraggio potenziato.
4. **Documentazione**: Entro 4 ore dall'implementazione — viene creato un ticket di modifica in [Sistema di gestione dei cambiamenti] con i dettagli: cosa è cambiato, perché, chi ha approvato, piano di rollback, risultato effettivo.
5. **Revisione post-implementazione**: Entro 5 giorni lavorativi — riunione di revisione della modifica (CIO, RSSI, implementatore della modifica, proprietario del sistema interessato). Determinare se la modifica deve rimanere, essere annullata o perfezionata. Documentare le lezioni apprese e gli aggiornamenti necessari a policy/procedure.

**Restrizioni per le modifiche di emergenza**:

- Le modifiche di emergenza NON devono disabilitare i controlli di sicurezza dall'elenco "Mai accettabile" (logging, autenticazione, cifratura, firewall, stessa gestione dei cambiamenti).
- Le modifiche di emergenza che aggirano i controlli di sicurezza richiedono l'approvazione specifica del RSSI (non solo del CIO).
- Le modifiche di emergenza che aumentano il rischio (ad es. apertura di regole firewall, riduzione dei requisiti di autenticazione) richiedono controlli compensativi documentati prima dell'implementazione.

**Riferimento incrociato**: Procedura completa per le modifiche di emergenza documentata nella Policy di gestione dei cambiamenti.

---

## Postura di sicurezza a livelli

L'organizzazione DEVE operare a uno dei cinque livelli di postura di sicurezza definiti. Il livello di postura corrente determina quali controlli sono completamente attivi, quali possono essere degradati e quali misure aggiuntive sono richieste.

### Livelli di postura

| Livello | Stato di interruzione | Postura di sicurezza | Esempi di trigger |
|---------|----------------------|----------------------|-------------------|
| **Normale** | Nessuna interruzione | Controlli di sicurezza completi operativi | Operazioni quotidiane |
| **Elevato** | Lieve interruzione | Monitoraggio potenziato, patching accelerato | Guasto singolo di sistema, evento di sicurezza minore, allerta meteo |
| **Degradato** | Interruzione moderata | Controlli fondamentali mantenuti, controlli non critici differiti secondo la tabella della modalità degradata | Failover del data center, interruzione regionale, incidente informatico significativo |
| **Emergenza** | Grave interruzione | Solo baseline minima, modalità di sopravvivenza | Disastro multi-sito, grande attacco ransomware, lockdown pandemico |
| **Ripristino** | Ritorno alla normalità | Ripristino graduale con validazione della sicurezza ad ogni fase | Recupero post-disastro, ricostruzione del sistema |

### Autorità per le transizioni

Le transizioni tra livelli di postura DEVONO essere formalmente autorizzate. L'autorizzazione verbale è consentita nelle situazioni urgenti, seguita da conferma scritta entro 4 ore.

| Transizione | Autorità richiesta | Documentazione |
|------------|-------------------|----------------|
| Normale → Elevato | RSSI o IT Security Manager | Ticket incidente o email di notifica |
| Elevato → Degradato | RSSI + CIO (congiuntamente) | Notifica formale alla Direzione generale |
| Degradato → Emergenza | Direzione generale (AD o delegato) | Documento di dichiarazione di emergenza |
| Qualsiasi livello → Ripristino | RSSI | Registro della transizione di fase |
| Ripristino → Normale | RSSI (confermato dalla Direzione generale) | Checklist di completamento della fase e firma della validazione della sicurezza |

Ogni transizione DEVE essere registrata con: data/ora, persona autorizzante, motivazione, stato corrente, stato target e eventuali controlli interessati.

### Comunicazione del livello di postura di sicurezza

Tutto il personale DEVE essere informato del livello di postura di sicurezza corrente e dei requisiti associati.

**Canali di comunicazione**:

| Canale | Formato del messaggio | Destinatari |
|--------|----------------------|-------------|
| **Email** | Annuncio formale del livello di postura dal RSSI o AD | Tutti i dipendenti |
| **Banner intranet** | Banner visibile in cima alla homepage dell'intranet: "POSTURA DI SICUREZZA ATTUALE: [LIVELLO] — [Breve descrizione]" | Tutti i dipendenti (ogni volta che accedono all'intranet) |
| **Piattaforma di collaborazione** (es. Slack/Teams) | Messaggio in evidenza nel canale #generale o #sicurezza | Tutti i dipendenti |
| **Crisis management team** | Notifica diretta tramite piattaforma di comunicazione di crisi | Team di crisi, team di sicurezza, management |

**Convenzione del banner intranet**:

| Postura | Colore banner | Testo |
|---------|---------------|-------|
| **Normale** | Verde | "POSTURA DI SICUREZZA: NORMALE — Tutti i sistemi operativi" |
| **Elevata** | Giallo | "POSTURA DI SICUREZZA: ELEVATA — Lieve interruzione; monitoraggio potenziato in corso" |
| **Degradata** | Arancione | "POSTURA DI SICUREZZA: DEGRADATA — Interruzione moderata; controlli fondamentali attivi; seguire le procedure aggiornate" |
| **Emergenza** | Rosso | "POSTURA DI SICUREZZA: EMERGENZA — Grave interruzione; solo baseline minima; attendere ulteriori istruzioni" |
| **Ripristino** | Blu | "POSTURA DI SICUREZZA: RIPRISTINO — Ritorno alla normalità; validare i controlli di sicurezza prima di riprendere le operazioni standard" |

**Tempistica delle comunicazioni**:

- Transizioni del livello di postura: comunicazione immediata (entro 1 ora dall'autorizzazione).
- Aggiornamenti di stato durante interruzioni prolungate: quotidiani (minimo) o più frequentemente al variare della situazione.
- Ritorno alla normalità: annuncio formale di "cessato allarme" dopo la firma di validazione post-interruzione.

La consegna delle comunicazioni DEVE essere verificata (email inviata, banner intranet attivo, messaggio pubblicato sulla piattaforma di collaborazione). La mancata ricezione attiva l'escalation verso metodi di comunicazione alternativi.

---

## Requisiti di sicurezza del piano BC/DR

Tutti i piani di business continuity e disaster recovery DEVONO includere requisiti di sicurezza revisionati e approvati dal RSSI. La sicurezza non è un pensiero secondario nella pianificazione della continuità — è un requisito di progettazione.

### Considerazioni di sicurezza nei piani BC/DR

I piani BC/DR DEVONO trattare le seguenti quattro aree:

**1. Controllo degli accessi durante il ripristino**

- Chi ha accesso ai sistemi e ai dati di ripristino (ruoli nominati, non accesso generale).
- Come viene autenticato l'accesso quando i normali sistemi di identità non sono disponibili.
- Come viene revocato l'accesso temporaneo al completamento del ripristino.
- Controlli sugli account di accesso di emergenza (si veda Accesso break-glass di seguito).

**2. Protezione dei dati durante il ripristino**

- Requisiti di cifratura per i dati in transito verso il sito di ripristino.
- Requisiti di cifratura per i supporti di ripristino (fisici e digitali).
- Procedure di catena di custodia per gli spostamenti fisici dei dati.
- Applicazione della classificazione dei dati nell'ambiente di ripristino.

**3. Sicurezza delle comunicazioni**

- Canali di comunicazione sicuri per il crisis management team (si veda Piattaforma di comunicazione di crisi di seguito).
- Canali di comunicazione alternativi se i sistemi principali sono compromessi (ad es. telefono fuori banda, gruppi di messaggistica pre-accordati).
- Autenticazione delle comunicazioni di crisi per prevenire il social engineering durante la confusione.
- Limiti di condivisione delle informazioni — cosa può essere condiviso esternamente e chi approva le comunicazioni esterne.

### Piattaforma di comunicazione di crisi

**Piattaforma principale**: [Specificare lo strumento — es. Microsoft Teams (con E2EE), Signal, Wickr, Zoom cifrato, WhatsApp Business]

**Configurazione**:

- Cifratura end-to-end abilitata (verificare che E2EE sia attiva).
- Gruppo di chat del crisis management team pre-configurato con tutto il personale autorizzato.
- Nome del gruppo di chat: **"Crisis Management Team — Sicuro"**.
- Accesso limitato al personale pre-approvato (nessuna aggiunta ad-hoc senza approvazione del RSSI durante la crisi).

**Piattaforma di backup** (se la principale non è disponibile): [Specificare l'alternativa — es. email cifrata (PGP/S/MIME), ponte telefonico pre-accordato, gruppo SMS fuori banda]

**Autenticazione durante la crisi**:

- Tutti i partecipanti alle comunicazioni di crisi DEVONO autenticarsi utilizzando le proprie credenziali aziendali.
- Durante la postura di Emergenza, se l'infrastruttura AMF non è disponibile, i partecipanti DEVONO utilizzare frasi di autenticazione pre-condivise per verificare l'identità (ruotate mensilmente, distribuite tramite elenco contatti offline).

**Verifica fuori banda**: Per le decisioni critiche (ad es. autorizzazione della postura di Emergenza, approvazione dell'attivazione break-glass), è richiesta la conferma verbale tramite chiamata telefonica per prevenire attacchi di impersonificazione. I numeri di telefono vengono verificati e aggiornati trimestralmente nell'elenco contatti offline.

**Test**: La piattaforma di comunicazione di crisi viene testata trimestralmente. I test includono la verifica della connettività, il controllo dello stato della cifratura, l'autenticazione dei partecipanti e la conferma della consegna dei messaggi. La documentazione dei test viene conservata per 3 anni.

**4. Sicurezza dei terzi**

- Controlli degli accessi dei fornitori durante le operazioni di ripristino.
- Requisiti di sicurezza per i collaboratori durante le operazioni di emergenza.
- Verifica della sicurezza dei servizi cloud durante il failover.
- Sicurezza della catena di fornitura per gli acquisti di emergenza.

### Revisione della sicurezza del piano BC/DR

- Il RSSI o il suo sostituto designato DEVE revisionare e approvare le sezioni di sicurezza di tutti i piani BC/DR prima della loro approvazione.
- La revisione della sicurezza DEVE avvenire dopo ogni aggiornamento a un piano BC/DR.
- Almeno uno scenario di test specifico per la sicurezza DEVE essere incluso nei test annuali BC/DR.
- Le deviazioni di sicurezza osservate durante i test DEVONO essere documentate e affrontate entro 30 giorni.

---

## Sicurezza del sito di ripristino

I siti di ripristino — che si tratti di siti in standby caldo, tiepido, freddo o di ambienti cloud di disaster recovery — DEVONO mantenere controlli di sicurezza equivalenti al sito principale. Un ambiente di ripristino con sicurezza inferiore al sito principale crea una lacuna sfruttabile.

| Controllo | Requisito |
|----------|-----------|
| **Sicurezza fisica** | Equivalente al sito principale per il livello di criticità dei dati gestiti |
| **Sicurezza di rete** | Stesse regole di segmentazione, policy firewall e monitoraggio |
| **Controllo degli accessi** | Stesso modello di autenticazione e autorizzazione; nessun percorso di accesso più debole |
| **Protezione dei dati** | Stessi standard di cifratura (a riposo e in transito) e applicazione della classificazione |
| **Logging** | Capacità di logging equivalente; i log DEVONO alimentare lo stesso [SIEM] o sistema di monitoraggio |
| **Hardening** | Stesse baseline di configurazione applicate all'infrastruttura di ripristino |

### Definizione e configurazione del sito di ripristino

**Sito di ripristino principale**: [Specificare il tipo e l'ubicazione]

| Opzione | Descrizione | Configurazione |
|---------|-------------|----------------|
| **Disaster recovery cloud** (più comune per PMI) | [es. AWS, Azure, Google Cloud] in [es. eu-central-1 (Francoforte), West Europe (Paesi Bassi)] | Standby caldo (sempre disponibile), standby tiepido (avvio entro X ore) o standby freddo (deployment manuale). Trigger di failover: automatico (guasto del controllo di integrità) o manuale (dichiarato da CIO + RSSI) |
| **Colocation / data center secondario** | [Nome struttura, città] | Collegamento WAN dedicato o VPN cifrata al sito principale |
| **Work-from-anywhere** (pandemia/indisponibilità dell'ufficio) | Accesso VPN, AMF, cifratura endpoint, guida alla rete domestica sicura | Solo funzioni amministrative/di knowledge worker; dipendente dal cloud/colo per il ripristino dell'infrastruttura |

**Configurazione corrente**: [Specificare quale/i opzione/i è/sono implementata/e]

**Verifica dell'equivalenza della sicurezza**:

| Controllo di sicurezza | Metodo di verifica |
|-----------------------|--------------------|
| **Sicurezza fisica** | Revisione annuale dei rapporti di audit del fornitore (SOC 2 Type II o ISO 27001); ispezione in loco se struttura fisica |
| **Segmentazione di rete** | Configurazione del sito di ripristino confrontata con la baseline del sito principale |
| **Controllo degli accessi** | Test di autenticazione (inclusa AMF) ai sistemi di ripristino |
| **Cifratura** | Scansione della configurazione; verifica del certificato |
| **Logging** | Verifica dell'inoltro dei log a [SIEM] durante il test DR |
| **Protezione dei backup** | Test di ripristino dai backup del sito di ripristino |

**Test di failover**: Test annuale di failover al sito di ripristino. La validazione della sicurezza durante il test DEVE confermare che l'autenticazione funziona (inclusa AMF), la segmentazione di rete è applicata, il logging è attivo e viene inoltrato a [SIEM], la cifratura è verificata e i controlli degli accessi corrispondono al sito principale. I risultati di sicurezza vengono documentati e rimediati entro 30 giorni.

La sicurezza del sito di ripristino DEVE essere verificata:

- Al provisioning iniziale, prima che il sito sia dichiarato operativo.
- Annualmente, nell'ambito del programma di test BC/DR.
- Dopo qualsiasi modifica significativa all'infrastruttura di ripristino.

---

## Procedure di accesso di emergenza

### Accesso break-glass

L'organizzazione DEVE mantenere account di accesso di emergenza pre-configurati ("account break-glass") per gli scenari in cui i normali sistemi di autenticazione o accesso non sono disponibili.

**Requisiti degli account break-glass**:

| Requisito | Specifica |
|-----------|-----------|
| **Stato dell'account** | Dormiente (disabilitato) fino alla dichiarazione dell'emergenza |
| **Autorità di attivazione** | RSSI, CIO o AD (catena di autorità documentata con sostituti designati) |
| **Autenticazione** | Autenticazione robusta — credenziali archiviate in modo sicuro secondo la specifica di Archiviazione delle credenziali break-glass di seguito |
| **Ambito** | Pre-definito, limitato ai soli sistemi essenziali per il ripristino |
| **Logging** | Tutte le azioni registrate con traccia di audit a prova di manomissione |
| **Durata** | A tempo limitato — default 24 ore, rinnovabile con ri-approvazione |
| **Disattivazione** | Disattivazione formale con rotazione delle credenziali e revisione completa dell'attività |

### Processo di attivazione break-glass

1. **Emergenza dichiarata** da un'autorità autorizzata (si veda la tabella delle Autorità per le transizioni).
2. **Richiesta di attivazione documentata** — anche se inizialmente verbale, registrazione scritta entro 4 ore.
3. **Attivazione a due persone** — per i sistemi critici, il break-glass richiede un minimo di due persone autorizzate (doppio controllo).
4. **RSSI e team di sicurezza notificati** immediatamente all'attivazione.
5. **Monitoraggio potenziato abilitato** — tutta l'attività dell'account break-glass monitorata in tempo reale ove possibile.
6. **Limite di tempo applicato** — 24 ore default; il rinnovo richiede ri-approvazione esplicita con motivazione.
7. **Disattivazione e revisione** — alla risoluzione dell'emergenza: disabilitare l'account, ruotare le credenziali, revisionare tutte le azioni eseguite, documentare i risultati.

### Archiviazione e accesso alle credenziali break-glass

**Metodo di archiviazione**: [Specificare il metodo scelto dall'organizzazione tra i seguenti]

**Opzione 1 — Cassaforte fisica** (metodo principale per ambienti ad alta sicurezza):

- **Ubicazione**: [Nome edificio], [Piano], [Numero stanza] — stanza fisicamente protetta con accesso limitato.
- **Autorizzazione all'accesso**: AD, RSSI, CIO (ciascuno ha la combinazione o la chiave della cassaforte; due sono necessari per l'accesso).
- **Contenuto**: Buste sigillate antimanomissione contenenti nomi utente e password iniziali degli account break-glass, credenziali VPN del sito di ripristino, password root per i sistemi critici (Tier 0) e chiavi di recupero della cifratura.
- **Integrità delle buste**: Sigilli antimanomissione; l'apertura della busta attiva la rotazione obbligatoria delle credenziali.
- **Verifica**: Verifica trimestrale che la cassaforte sia accessibile e le buste integre (solo ispezione esterna; nessuna apertura).

**Opzione 2 — Vault di emergenza del gestore di password**:

- **Strumento**: [es. 1Password Emergency Kit, Bitwarden Emergency Access, LastPass Emergency Access].
- **Configurazione**: Vault di emergenza separato dal vault aziendale standard.
- **Accesso**: Accesso di emergenza concesso al personale designato (AD, RSSI, CIO) con accesso a tempo differito (es. periodo di attesa di 12 ore prima che venga concesso l'accesso).
- **Bypass AMF**: Vault di emergenza accessibile con codici di recupero archiviati offline (schede stampate in buste sigillate, conservate secondo l'Opzione 1).
- **Test**: Test trimestrale del flusso di lavoro di accesso di emergenza (verifica del ritardo temporale, conferma dell'accesso, recupero delle credenziali).

**Opzione 3 — Split-knowledge / secret sharing** (avanzato):

- **Metodo**: Secret Sharing di Shamir o simile divisione crittografica.
- **Configurazione**: Password break-glass divisa in 3 parti; qualsiasi 2 delle 3 necessarie per ricostruire.
- **Detentori delle parti**: AD (Parte 1), RSSI (Parte 2), CIO (Parte 3).
- **Archiviazione**: Ogni detentore di parte archivia la propria parte in una cassaforte personale o busta sigillata (cassaforte domestica, cassetta di sicurezza bancaria).
- **Test**: Test annuale del processo di ricostruzione.

**Metodo corrente**: [Specificare quale/i opzione/i l'organizzazione utilizza]

**Accesso di backup** (se il metodo principale non funziona): Se la cassaforte non è accessibile (edificio distrutto) → Vault di emergenza del gestore di password (accessibile via cloud). Se il gestore di password non è accessibile (interruzione del servizio) → Cassaforte fisica o split-knowledge.

### Test del break-glass

Gli account e le procedure break-glass DEVONO essere testati almeno annualmente per verificare che:

- Le credenziali siano accessibili e funzionanti.
- Il processo di attivazione sia compreso da tutto il personale autorizzato.
- Il logging catturi tutte le azioni eseguite.
- Il processo di disattivazione funzioni correttamente.

I risultati dei test DEVONO essere documentati. I test falliti attivano la remediation immediata.

---

## Disponibilità del personale

L'organizzazione DEVE garantire che il personale con responsabilità di sicurezza sia disponibile durante gli eventi di interruzione. Le interruzioni si verificano spesso al di fuori dell'orario di lavoro e possono impedire il normale accesso al luogo di lavoro.

**Requisiti di continuità del team di sicurezza**:

- I ruoli chiave di sicurezza DEVONO avere sostituti designati documentati in un piano di successione.
- Le informazioni di contatto del personale di sicurezza DEVONO essere mantenute offline — elenchi contatti stampati e/o USB cifrata — accessibili quando email, intranet e altri sistemi digitali non sono disponibili.
- Ove possibile, il personale di sicurezza dovrebbe essere geograficamente distribuito per evitare che un guasto a un singolo sito disabiliti l'intero team di sicurezza.
- La formazione incrociata DEVE garantire che almeno due persone possano svolgere ciascuna funzione di sicurezza critica (attivazione break-glass, revisione dei log, revoca degli accessi di emergenza, valutazione della postura di sicurezza).
- DEVE essere stabilita una rotazione di reperibilità per una copertura 24/7 quando l'organizzazione opera a livelli di postura Elevato, Degradato o di Emergenza.

### Elenco contatti accessibile offline

**Approccio a più livelli per la resilienza**:

**Livello 1 — Schede plastificate stampate**:

- Schede plastificate da portafoglio fornite a tutti i membri del crisis management team e al personale di sicurezza.
- Contenuto: Nomi, numeri di cellulare, indirizzi email personali (per il contatto fuori banda), ruolo.
- Aggiornate trimestralmente; le vecchie schede vengono distrutte (triturate). Distribuzione: Consegna di persona; il personale firma la ricevuta.

**Livello 2 — Chiavetta USB cifrata**:

- Chiavetta USB conservata nella cassaforte break-glass insieme alle credenziali.
- Contenuto: Elenco contatti completo (tutto il personale di sicurezza, team di crisi esteso, contatti di emergenza dei fornitori).
- File cifrato (es. VeraCrypt, BitLocker To Go) con password nota a AD/RSSI/CIO.
- Aggiornata trimestralmente.

**Livello 3 — Archiviazione cloud sicura** (accessibile se Internet è disponibile):

- Elenco contatti archiviato in [repository documenti sicuro] con accesso limitato al crisis management team.
- Aggiornato regolarmente (in tempo reale quando si verificano cambiamenti del personale).

**Test**: Verifica trimestrale — 3 persone casuali contattate utilizzando le informazioni dalle schede plastificate (verifica che i numeri di telefono funzionino), chiavetta USB testata (password di cifratura verificata, file aperto), accesso all'archiviazione cloud verificato. Risultati dei test documentati; i guasti attivano l'aggiornamento immediato.

### Copertura di reperibilità del team di sicurezza

**Trigger di attivazione**: Attivato automaticamente quando la postura di sicurezza passa a **Elevata**, **Degradata** o di **Emergenza**.

**Modello di copertura**:

| Postura | Copertura |
|---------|-----------|
| **Normale** | Nessuna reperibilità dedicata (solo supporto negli orari di ufficio) |
| **Elevata** | Copertura 16x7 (07:00–23:00 CET, 7 giorni/settimana) |
| **Degradata / Emergenza** | Copertura 24x7 |

**Turni di rotazione**:

| Ruolo | Responsabilità di copertura |
|-------|----------------------------|
| **Reperibile principale** | IT Security Analyst o IT Security Manager (rotazione settimanale) |
| **Reperibile di backup** | RSSI o membro designato del team di sicurezza |
| **Escalation** | RSSI (raggiungibile 24x7 durante postura Degradata/Emergenza) |

**SLA di risposta**:

| Gravità | Elevata | Degradata / Emergenza |
|---------|---------|----------------------|
| **Critico** (attivazione break-glass, violazione confermata) | 30 minuti | 15 minuti |
| **Alto** (guasto del controllo di sicurezza, attività sospetta) | 2 ore | 1 ora |
| **Medio** (avviso non critico, advisory) | 4 ore | 2 ore |

**Percorso di escalation**: Reperibile principale → Reperibile di backup (se il principale non è raggiungibile dopo 30 min per Critico, 1 ora per Alto) → RSSI → Direzione generale.

**Test**: Test mensile di reperibilità durante il normale orario di lavoro (verifica delle informazioni di contatto e dei tempi di risposta). Test trimestrale fuori orario (orario casuale; verifica che il percorso di escalation funzioni).

---

## Validazione della sicurezza post-interruzione

Prima di tornare al livello di postura Normale, l'organizzazione DEVE validare che i controlli di sicurezza completi siano stati ripristinati. La transizione da Ripristino a Normale non è completa fino alla firma della validazione della sicurezza da parte del RSSI.

### Validazione in quattro fasi

| Fase | Tempistica | Attività di validazione |
|------|-----------|------------------------|
| **Immediata** | 0–24 ore post-interruzione | Verificare che i controlli non negoziabili siano operativi; disabilitare tutti gli account break-glass; revisionare i log per anomalie durante l'interruzione; confermare che non si siano verificati accessi non autorizzati |
| **Breve termine** | 1–7 giorni | Validazione completa dei controlli di sicurezza; scansione delle vulnerabilità di tutti i sistemi Tier 1 e Tier 2; revisione degli accessi (verifica che non rimangano permessi di emergenza); analisi iniziale degli incidenti |
| **Medio termine** | 1–4 settimane | Remediation del debito di sicurezza (applicare patch differite, ripristinare i controlli differiti); ricertificazione completa degli accessi; test dei controlli per verificarne l'efficacia; aggiornamento del piano BC/DR con le lezioni apprese |
| **Lungo termine** | 1–3 mesi | Implementazione delle lezioni apprese; aggiornamenti di policy e procedure; aggiornamenti della formazione; analisi delle tendenze della postura di sicurezza durante l'interruzione |

### Tracciamento del debito di sicurezza

Tutti gli allentamenti dei controlli di sicurezza approvati durante un'interruzione DEVONO essere tracciati nel Registro del debito di sicurezza fino alla remediation completa.

**Sistema**: [Specificare lo strumento — es. piattaforma GRC (Vanta, Drata, ServiceNow GRC), Jira, Asana, registro Excel archiviato in posizione sicura]

**Titolarità**: Il RSSI mantiene il registro; i proprietari assegnati rimediato i singoli elementi del debito.

**Formato del Registro del debito di sicurezza**:

| Campo | Descrizione |
|-------|-------------|
| **ID debito** | Identificatore univoco (es. DEBT-2025-001) |
| **Controllo allentato** | Quale controllo di sicurezza è stato degradato o differito |
| **Motivazione aziendale** | Perché era necessario l'allentamento? (collegato a un evento di interruzione specifico) |
| **Controllo compensativo** | Misura di sicurezza alternativa implementata |
| **Data di apertura** | Quando l'allentamento è stato approvato |
| **Postura di sicurezza all'apertura** | Elevata / Degradata / Emergenza |
| **Approvatore** | RSSI o delegato autorizzato |
| **Proprietario** | Persona responsabile della remediation |
| **Data target di chiusura** | Quando il controllo completo deve essere ripristinato |
| **Stato corrente** | Aperto / In corso / Chiuso |
| **Note di avanzamento** | Aggiornamenti sulle azioni di remediation |
| **Data di chiusura** | Quando il controllo è stato completamente ripristinato |
| **Verifica della chiusura** | Verifica da parte del RSSI o del team di sicurezza del ripristino del controllo |

**Ciclo di vita del debito**:

1. **Apertura**: Allentamento del controllo approvato durante l'interruzione → inserimento immediato nel registro.
2. **Tracciamento**: Revisione settimanale durante l'interruzione attiva; quindicinale durante la postura di Ripristino.
3. **Escalation**: Secondo le soglie di seguito.
4. **Chiusura**: Controllo completamente ripristinato → il team di sicurezza verifica → Debito contrassegnato come Chiuso.

**Integrazione con la postura di sicurezza**: La transizione Ripristino → Normale richiede che il Registro del debito di sicurezza sia vuoto o che abbia un'approvazione documentata della Direzione generale per gli elementi rimanenti.

**Reportistica**: Lo stato del debito di sicurezza viene segnalato in ogni revisione del management SGSI durante e dopo l'interruzione. Metriche: debiti aperti totali, età media, debiti scaduti, tasso di chiusura.

**Soglie di escalation**:

- Il debito di sicurezza più vecchio di **30 giorni** DEVE essere escalato al RSSI con un piano di remediation e una data target rivista.
- Il debito di sicurezza più vecchio di **90 giorni** DEVE essere escalato alla Direzione generale per una decisione: approvare una remediation accelerata con risorse aggiuntive, o accettare formalmente il rischio residuo con accettazione del rischio documentata.
- Il debito di sicurezza che non può essere rimediato DEVE essere convertito in una voce permanente del Registro dei rischi con controlli compensativi e revisione annuale.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità per la sicurezza delle informazioni durante le interruzioni |
|-------|---------------------------------------------------------------------------|
| **AD / Direzione generale** | Approvare i livelli di postura di sicurezza; autorizzare la modalità di Emergenza; allocare risorse per la sicurezza durante il ripristino; prendere decisioni di accettazione del rischio per il debito di sicurezza superiore a 90 giorni |
| **RSSI** | Titolare della policy; definire i requisiti di sicurezza per i piani BC/DR; approvare le transizioni della postura di sicurezza; autorizzare l'attivazione break-glass; possedere la validazione della sicurezza post-interruzione; punto di escalation per il debito di sicurezza |
| **Coordinatore BC/DR** | Integrare i requisiti di sicurezza nei piani BC/DR; coordinarsi con il RSSI sulla revisione della sicurezza del piano; includere scenari di sicurezza nei test BC/DR |
| **CIO** | Garantire che il ripristino IT sia allineato ai requisiti di sicurezza; co-autorizzare la transizione da Elevato a Degradato; autorizzare l'attivazione break-glass |
| **Team di sicurezza / Sicurezza IT** | Monitorare la sicurezza durante le interruzioni; attivare e disattivare le procedure di emergenza; validare la sicurezza del sito di ripristino; condurre scansioni delle vulnerabilità e revisioni degli accessi post-interruzione |
| **Crisis management team** | Includere le considerazioni di sicurezza in tutte le decisioni di crisi; mantenere la comunicazione con il RSSI durante tutta l'interruzione (si veda la composizione di seguito) |
| **Operazioni IT** | Implementare i controlli di sicurezza negli ambienti di ripristino; mantenere il logging durante il ripristino; segnalare le anomalie di sicurezza durante il ripristino |
| **Tutto il personale** | Seguire le procedure di sicurezza durante le interruzioni; segnalare le preoccupazioni di sicurezza attraverso i canali stabiliti; non aggirare i controlli di sicurezza senza autorizzazione |

### Composizione del crisis management team

**Scopo**: Coordinare la risposta organizzativa alle gravi interruzioni che influiscono sulle operazioni aziendali e sulla sicurezza delle informazioni.

**Trigger di attivazione**: Transizione della postura di sicurezza a **Degradata** o di **Emergenza**; incidente di gravità P0 (Critico) o P1 (Alto) con impatto aziendale esteso; o dichiarazione da parte del AD, CIO o RSSI che è necessaria la gestione della crisi.

**Membri del team principale**:

| Ruolo | Responsabilità durante la crisi |
|-------|--------------------------------|
| **AD** (Team Leader) | Leadership complessiva della crisi; comunicazione esterna; decisioni strategiche; autorizzare la postura di Emergenza |
| **CIO** | Coordinamento del ripristino IT; allocazione delle risorse; autorità decisionale sulla tecnologia |
| **RSSI** | Continuità della sicurezza delle informazioni; gestione della postura di sicurezza; autorizzazione break-glass; validazione post-interruzione |
| **CFO** | Valutazione dell'impatto finanziario; autorizzazione del budget per il ripristino; coordinamento assicurativo |
| **Direttore HR** | Sicurezza del personale; comunicazione ai dipendenti; continuità della forza lavoro |
| **Consulente legale** | Notifica normativa; gestione delle responsabilità; questioni contrattuali; obblighi legali per le violazioni di dati |
| **Comunicazione / PR** (se applicabile) | Comunicazioni esterne; gestione dei media; notifica ai clienti |

**Team esteso** (attivato secondo necessità): Coordinatore BC/DR, IT Operations Manager, Security Team Lead, Responsabile strutture, fornitori chiave.

**Autorità decisionale**:

| Tipo di decisione | Autorità |
|------------------|---------|
| Transizioni del livello di postura di sicurezza | Accordo di AD + CIO + RSSI richiesto |
| Decisioni di accettazione del rischio, comunicazione esterna, allocazione delle risorse oltre il budget | Autorità finale del AD |
| Allentamenti dei controlli di sicurezza, attivazione break-glass, approvazione del debito di sicurezza | Autorità finale del RSSI |
| Priorità di ripristino tecnologico, sequenza di ripristino del sistema | Autorità finale del CIO |

**Cadenza delle riunioni durante la crisi**:

| Postura | Frequenza |
|---------|-----------|
| **Degradata** | Chiamata giornaliera del crisis management team (30 minuti) fino all'inizio del ripristino |
| **Emergenza** | Due volte al giorno (mattina e sera) più ad-hoc secondo necessità |
| **Ripristino** | Ogni 2–3 giorni fino al ritorno alla Normale |

I verbali delle riunioni vengono documentati (anche se brevi) per la revisione post-incidente. Le azioni correttive vengono tracciate con proprietario e data target.

**Post-crisi**: Sessione formale di lezioni apprese entro 30 giorni dal ritorno alla postura Normale. Le lezioni apprese informano gli aggiornamenti della policy, dei piani BC/DR e della formazione.

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa policy:

| # | Evidenza | Proprietario | Frequenza |
|---|---------|--------------|-----------|
| 1 | **Piani BC/DR con approvazione della sicurezza del RSSI** (revisione firmata che conferma l'adeguatezza delle sezioni di sicurezza) | Coordinatore BC/DR / RSSI | *Revisione annuale; aggiornamento dopo test e incidenti; conservare versione corrente + 2 precedenti* |
| 2 | **Documentazione della baseline minima di sicurezza** (definizione dei controlli non negoziabili e soglie della modalità degradata) | RSSI | *Revisione annuale; aggiornamento ad ogni modifica della policy; conservare 3 anni* |
| 3 | **Inventario degli account break-glass** (elenco account, ambito, ubicazione di archiviazione delle credenziali, autorità di attivazione) | Team di sicurezza | *Mantenuto continuamente; revisione trimestrale; conservare 3 anni* |
| 4 | **Risultati dei test break-glass** (test annuale che documenta accessibilità delle credenziali, processo di attivazione, logging, disattivazione) | Team di sicurezza | *Annuale come minimo; conservare 3 anni* |
| 5 | **Registri delle transizioni della postura di sicurezza** (data, autorità, motivazione, controlli interessati) — se si sono verificate interruzioni | RSSI | *Per evento; conservare 5 anni* |
| 6 | **Registro del debito di sicurezza** (tutti gli allentamenti durante l'interruzione con proprietario, controlli compensativi, data target, chiusura) | RSSI | *Per evento; revisione mensile durante il debito attivo; conservare 3 anni* |
| 7 | **Rapporti di validazione della sicurezza post-interruzione** (completamento della checklist a quattro fasi con firma) — se si sono verificate interruzioni | RSSI / Team di sicurezza | *Per evento di interruzione; conservare 5 anni* |
| 8 | **Valutazione della sicurezza del sito di ripristino** (verifica annuale dell'equivalenza della sicurezza con il sito principale) | Team di sicurezza | *Annuale; conservare 3 anni* |
| 9 | **Elenco contatti del personale di sicurezza e piano di successione** (accessibile offline, testato trimestralmente) | RSSI | *Revisione trimestrale; aggiornamento ad ogni modifica* |
| 10 | **Registri dei test BC/DR con scenari specifici di sicurezza** (ambito del test, risultati di sicurezza, azioni di remediation) | Coordinatore BC/DR / Team di sicurezza | *Annuale come minimo; conservare 3 anni* |

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa policy attraverso vari metodi, inclusi a titolo non esaustivo: revisioni della sicurezza dei piani BC/DR, test degli account break-glass, registri delle transizioni della postura di sicurezza, stato del Registro del debito di sicurezza, valutazioni del sito di ripristino, audit interni ed esterni, e feedback al proprietario della policy.

**Metriche di governance** (segnalate alla Direzione generale almeno annualmente):

| Metrica | Obiettivo |
|---------|----------|
| Piani BC/DR con approvazione della sicurezza del RSSI corrente | 100% |
| Test degli account break-glass completati nei tempi previsti | 100% |
| Incidenti di sicurezza durante eventi di interruzione | Tracciamento delle tendenze (obiettivo: decrescente) |
| Elementi del debito di sicurezza aperti oltre 90 giorni | 0 |
| Valutazioni della sicurezza del sito di ripristino senza risultati critici/alti | 100% |

## Deroghe

Qualsiasi deroga a questa policy DEVE essere approvata e registrata preventivamente dal RSSI, con documentazione dell'accettazione del rischio, dei controlli compensativi e di una data di revisione definita (durata massima di interruzione + 7 giorni per le eccezioni di ripristino; massimo 12 mesi per le eccezioni permanenti). Le deroghe DEVONO essere segnalate al Team di revisione del management.

Le deroghe non sono consentite per i controlli non negoziabili (controllo degli accessi, cifratura dei dati, logging, segmentazione di rete, protezione dei backup). Le eccezioni che eliminano la capacità di traccia di audit non sono consentite.

## Non conformità

Un dipendente ritenuto responsabile di aver violato questa policy potrà essere soggetto a misure disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa policy è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO tener conto delle lezioni apprese da interruzioni reali, dei risultati dei test BC/DR, dei cambiamenti nel panorama delle minacce, degli aggiornamenti normativi, dei risultati degli audit e delle best practice emergenti per la sicurezza in condizioni avverse.

---

# Sezioni della norma ISO 27001 trattate

Policy sulla sicurezza delle informazioni durante le interruzioni — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.4 Responsabilità del management |
| Clausola 6.2 Obiettivi per la sicurezza delle informazioni | **5.29 Sicurezza delle informazioni durante le interruzioni** |
| Clausola 7.3 Consapevolezza | 5.30 Prontezza ICT per la continuità operativa |
| Clausola 8.1 Pianificazione e controllo operativi | 5.36 Conformità a policy, regole e standard |
| | 6.3 Sensibilizzazione, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 8.13 Backup delle informazioni |
| | 8.14 Ridondanza delle strutture di elaborazione delle informazioni |

**Quadro normativo e legale**:

| Quadro di riferimento | Rilevanza |
|-----------------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Mantenere misure tecniche e organizzative di sicurezza appropriate, anche durante le interruzioni |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento, inclusa la capacità di garantire la riservatezza, l'integrità, la disponibilità e la resilienza continuative dei sistemi e dei servizi di trattamento |
| ISO/IEC 27001:2022 | Controllo Annex A 5.29 — Sicurezza delle informazioni durante le interruzioni |
| ISO/IEC 27002:2022 | Sezione 5.29 — Linee guida per l'implementazione |
| ISO/IEC 22301 | Sistemi di gestione della continuità operativa (riferimento informativo) |
| NIST SP 800-34 Rev 1 | Guida alla pianificazione delle contingenze — approccio in tre fasi (notifica/attivazione, ripristino, ricostruzione) (riferimento informativo) |
| CIS Controls v8 | Controllo 17 (Gestione della risposta agli incidenti), Controllo 11 (Recupero dei dati) |
| DORA (condizionale) | Art. 11 — Gestione della continuità operativa ICT inclusi i requisiti di sicurezza durante le interruzioni |
| NIS2 (condizionale) | Art. 21 — Misure di continuità operativa e gestione delle crisi |
| FINMA (condizionale) | Circolare 2023/1 — Resilienza operativa per gli istituti finanziari regolamentati svizzeri |

---

<!-- QA_VERIFIED: 2026-04-03 -->
