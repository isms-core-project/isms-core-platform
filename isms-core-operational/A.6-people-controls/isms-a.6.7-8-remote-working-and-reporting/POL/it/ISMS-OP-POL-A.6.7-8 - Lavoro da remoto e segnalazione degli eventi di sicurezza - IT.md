<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.6.7-8-IT:operational:OP-POL:a.6.7-8 -->
**ISMS-OP-POL-A.6.7-8 — Lavoro da remoto e segnalazione degli eventi di sicurezza**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Lavoro da remoto e segnalazione degli eventi di sicurezza |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.6.7-8 |
| **Autore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
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

- ISO/IEC 27001:2022 Controllo A.6.7 — Lavoro da remoto
- ISO/IEC 27001:2022 Controllo A.6.8 — Segnalazione degli eventi di sicurezza delle informazioni
- ISO/IEC 27002:2022 Sezioni 6.7, 6.8 — Linee guida di attuazione

**Controlli correlati dell'Allegato A**:

| Controllo | Relazione con il lavoro da remoto e la segnalazione degli eventi |
|-----------|------------------------------------------------------------------|
| A.5.10 Uso accettabile delle informazioni e degli altri asset associati | Definisce l'uso accettabile dei dispositivi e delle informazioni nel contesto del lavoro da remoto |
| A.5.11 Restituzione degli asset | Restituzione delle attrezzature alla cessazione del lavoro da remoto o del rapporto di lavoro |
| A.5.14 Trasferimento delle informazioni | Requisiti di trasferimento sicuro per i dati inviati da postazioni remote |
| A.5.24-28 Ciclo di vita della gestione degli incidenti | Percorso di escalation quando gli eventi segnalati sono confermati come incidenti |
| A.6.3 Consapevolezza, formazione e addestramento sulla sicurezza delle informazioni | Formazione sulla sicurezza del lavoro da remoto e sulle procedure di segnalazione degli eventi |
| A.8.1 Dispositivi endpoint degli utenti | Baseline di sicurezza dei dispositivi per endpoint remoti e mobili |
| A.8.5 Autenticazione sicura | Requisiti AMF e di autenticazione per l'accesso remoto |

**Politiche interne correlate**:

- Politica di controllo degli accessi
- Politica di sicurezza degli endpoint
- Politica di gestione degli incidenti
- Politica di classificazione e gestione delle informazioni
- Politica di trasferimento delle informazioni
- Politica di uso accettabile e restituzione degli asset

---

# Politica sul lavoro da remoto e sulla segnalazione degli eventi di sicurezza

## Scopo

Questa politica stabilisce i requisiti dell'organizzazione per il lavoro da remoto sicuro e la tempestiva segnalazione degli eventi di sicurezza delle informazioni. Definisce le misure di sicurezza richieste quando il personale lavora al di fuori delle sedi dell'organizzazione e fornisce un meccanismo strutturato per consentire a tutto il personale di segnalare eventi di sicurezza osservati o sospetti attraverso i canali appropriati.

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative proporzionate al rischio per proteggere i dati personali (inclusi i dati personali degni di particolare protezione) negli ambienti di lavoro da remoto. Nei casi in cui l'organizzazione tratti dati di persone nell'UE/SEE, si applicano altresì i requisiti del RGPD.

Questi due controlli sono combinati perché i lavoratori da remoto sono la prima linea di rilevamento degli eventi, i lavoratori da remoto affrontano minacce non presenti negli ambienti d'ufficio, e ISO 27002:2022 richiede esplicitamente che le procedure di segnalazione degli incidenti siano accessibili dalle postazioni remote.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Tutti i dispositivi aziendali e personali utilizzati per accedere, elaborare o archiviare informazioni organizzative da remoto.

Tutte le modalità di lavoro da remoto incluso il lavoro da casa, gli spazi di coworking, le sedi dei clienti e il lavoro in trasferta.

Tutto il personale responsabile della segnalazione degli eventi di sicurezza, indipendentemente dalla sede di lavoro.

## Principio

Il lavoro da remoto DEVE essere formalmente autorizzato e soggetto a controlli di sicurezza proporzionati alla classificazione delle informazioni a cui si accede. Tutto il personale DEVE segnalare tempestivamente gli eventi di sicurezza delle informazioni osservati o sospetti attraverso i canali designati. L'organizzazione promuove una cultura senza colpa in cui la segnalazione in buona fede è protetta e incoraggiata.

---

# Parte 1 — Lavoro da remoto (A.6.7)

## Autorizzazione al lavoro da remoto

Tutte le modalità di lavoro da remoto regolari DEVONO essere formalmente approvate prima dell'inizio.

- **Autorità di approvazione**: Il responsabile diretto autorizza la modalità di lavoro da remoto; la Sicurezza informatica approva l'accesso tecnico.
- **Valutazione del rischio**: Una valutazione del rischio DEVE essere eseguita per i ruoli che gestiscono dati Riservati o Limitati da remoto. La valutazione DEVE esaminare almeno: (a) il livello di classificazione dei dati a cui si accede da remoto; (b) la capacità di sicurezza fisica della postazione remota; (c) la postura di sicurezza della rete presso il sito remoto; (d) la conformità alla baseline di sicurezza del dispositivo; e (e) eventuali restrizioni normative o contrattuali.
- **Conferma documentata**: I lavoratori da remoto DEVONO firmare una conferma attestante che comprendono e accettano i requisiti di sicurezza di questa politica.
- **Revisione annuale**: Tutte le autorizzazioni al lavoro da remoto DEVONO essere riesaminate almeno annualmente. Le revisioni devono confermare che l'autorizzazione rimanga appropriata, che i requisiti di sicurezza siano mantenuti, e che eventuali modifiche al ruolo, all'accesso ai dati o alla sede di lavoro siano recepite.

**Approvazione della sede**:
- **Sedi remote standard** (ufficio domestico in Svizzera, area di lavoro remota consolidata): È sufficiente l'approvazione del responsabile diretto.
- **Lavoro da remoto internazionale** (lavoro dall'estero): Richiede l'approvazione del RSSI + l'approvazione delle RU + la revisione legale (implicazioni fiscali, diritto del lavoro, residenza dei dati).
- **Lavoro da remoto temporaneo da sedi ad alto rischio** (spazi di coworking pubblici, caffè, trasferte): Richiede la consapevolezza del responsabile diretto; l'accesso ai dati Riservati da luoghi pubblici è vietato.

**Variazioni di sede**: Le variazioni permanenti della sede di lavoro da remoto (ad es., trasferimento in una nuova abitazione, trasferta prolungata) DEVONO essere comunicate al responsabile diretto e alla Sicurezza informatica entro **14 giorni**.

**Revoca**: L'autorizzazione al lavoro da remoto DEVE essere revocata quando il rapporto di lavoro o il contratto termina, il ruolo cambia in uno non adatto al lavoro da remoto, i requisiti di sicurezza non vengono mantenuti, si verificano violazioni della politica, o le esigenze aziendali richiedono la presenza in sede.

## Registrazione e responsabilità dei dispositivi mobili

I dispositivi mobili emessi o approvati per il lavoro da remoto DEVONO essere registrati nel registro degli asset e assegnati a una persona nominativa.

**Requisiti di registrazione dei dispositivi**:

- Tutti i dispositivi mobili (aziendali e BYOD approvati) DEVONO essere registrati nel registro degli asset con il proprietario assegnato, il tipo di dispositivo, il numero di serie e lo scopo.
- I proprietari assegnati DEVONO ricevere una copia di questa politica ed essere informati delle proprie responsabilità.
- I dispositivi DEVONO avere installati la crittografia appropriata, la protezione antivirus/endpoint e i controlli di accesso.

**Responsabilità del proprietario assegnato**:

- Garantire che le patch del sistema operativo e delle applicazioni vengano applicate tempestivamente.
- Garantire che la crittografia e la protezione endpoint rimangano abilitate e aggiornate.
- Non lasciare il dispositivo incustodito; proteggere fisicamente il dispositivo quando non è in uso.
- Accedere solo alle informazioni organizzative necessarie per il proprio ruolo, in linea con la Politica di controllo degli accessi.
- Non installare software o apportare modifiche che violerebbero le politiche di sicurezza delle informazioni dell'organizzazione, le normative o la legislazione applicabile.
- Non consentire ad altri, inclusi i familiari, di accedere o utilizzare il dispositivo assegnato.
- Non archiviare dati personali o dati personali degni di particolare protezione (ai sensi della nLPD) sul dispositivo salvo autorizzazione e registrazione nel registro degli asset.
- Restituire il dispositivo mobile quando non più necessario, su richiesta, o al momento della cessazione del rapporto di lavoro con l'organizzazione.

## Cancellazione remota e backup

- **Cancellazione remota**: Tutti i dispositivi mobili aziendali DEVONO avere la funzionalità di cancellazione remota abilitata prima che il dispositivo venga consegnato all'utente. Il blocco automatico DEVE essere abilitato (massimo 5 tentativi di autenticazione falliti).
- **Backup**: I dispositivi mobili non vengono sottoposti a backup predefinito nelle soluzioni di backup aziendali. Gli utenti DEVONO archiviare i file di lavoro in posizioni cloud o di rete approvate (ad es., SharePoint, OneDrive for Business, file server approvato). I dati di lavoro critici non DEVONO risiedere esclusivamente sull'archiviazione locale del dispositivo.

## Sicurezza fisica

I lavoratori da remoto DEVONO mantenere la sicurezza fisica appropriata alla classificazione delle informazioni trattate:

- **Posizionamento dello schermo**: Posizionare gli schermi per impedire la visualizzazione non autorizzata da parte di altri nella postazione di lavoro.
- **Schermi privacy**: Utilizzare schermi privacy quando si lavora in spazi condivisi o pubblici (aree di coworking, caffè, mezzi pubblici).
- **Sicurezza delle attrezzature**: Mettere in sicurezza le attrezzature di lavoro quando la postazione è incustodita. Non lasciare mai i dispositivi incustoditi in luoghi pubblici. Bloccare i dispositivi quando ci si allontana, anche brevemente.
- **Scrivania libera**: La politica della scrivania libera (A.7.7 — cfr. Politica sulla sicurezza fisica e ambientale) si estende agli ambienti di lavoro da remoto. I documenti sensibili non DEVONO essere lasciati visibili quando non sono in uso attivo. I materiali di lavoro DEVONO essere messi in sicurezza al termine di ogni sessione di lavoro.

  **Requisiti di scrivania libera per il lavoro da remoto**:
  - Documenti chiusi in cassetto, schedario o ufficio domestico sicuro quando non in uso.
  - Schermo bloccato quando ci si allontana (Windows+L, Ctrl+Cmd+Q).
  - Nessun materiale di lavoro lasciato su tavoli da cucina, aree del soggiorno o altri spazi familiari condivisi.
- **Smaltimento dei documenti**: I documenti sensibili DEVONO essere smaltiti utilizzando metodi approvati (distruzione con trita-documenti). Nei casi in cui un trita-documenti non sia disponibile presso la postazione remota, i documenti sensibili DEVONO essere riportati in ufficio per lo smaltimento sicuro.
- **Accesso di familiari e visitatori**: Impedire l'accesso ai dispositivi e ai documenti di lavoro da parte di familiari, visitatori o altre persone non autorizzate.

## Sicurezza tecnica

I seguenti controlli di sicurezza tecnica DEVONO essere applicati a tutti gli accessi remoti:

- **VPN o Zero Trust**: Tutte le connessioni alle risorse organizzative interne DEVONO utilizzare una VPN o un'architettura Zero Trust equivalente. Il tunneling diviso (split tunnelling) può essere consentito solo quando una valutazione del rischio dimostri un rischio residuo accettabile e tutte le risorse organizzative siano accessibili tramite il tunnel crittografato.

  **Implementazione corrente**: [Specificare: ad es., "Cisco AnyConnect VPN", "Palo Alto GlobalProtect", "Zero Trust tramite Cloudflare Access / Zscaler", o "Selezione in corso; nel frattempo: VPN obbligatoria"]

  **Requisiti VPN/Zero Trust**:
  - Applicare l'AMF prima di stabilire la connessione.
  - Applicare il controllo di conformità del dispositivo (crittografia, patch, protezione endpoint) prima dell'accesso.
  - Terminare le sessioni dopo un periodo di inattività definito (secondo i requisiti di timeout della sessione di seguito).
  - Registrare tutti i tentativi di connessione (riusciti e falliti).
- **Autenticazione a più fattori (AMF)**: L'AMF DEVE essere richiesta per tutti gli accessi remoti ai sistemi organizzativi. Questo include le connessioni VPN, i servizi cloud, le email e qualsiasi sistema contenente dati Interni, Riservati o Limitati.
- **Crittografia in transito**: Tutti i dati trasmessi tra endpoint remoti e sistemi organizzativi DEVONO essere crittografati utilizzando TLS 1.2 come minimo (TLS 1.3 preferito).
- **Sicurezza Wi-Fi**: I lavoratori da remoto DEVONO utilizzare solo reti wireless sicure e crittografate (WPA2 minimo, WPA3 preferito).

  **Utilizzo del Wi-Fi pubblico**:
  - **Vietato senza VPN**: Il Wi-Fi pubblico e non protetto (aeroporti, hotel, caffè) NON DEVE essere utilizzato per lavoro organizzativo senza protezione VPN.
  - **Con VPN**: Il Wi-Fi pubblico può essere utilizzato con connessione VPN attiva solo per l'accesso ai dati Interni.
  - **Dati Riservati**: L'accesso ai dati Riservati tramite Wi-Fi pubblico è sconsigliato anche con VPN; utilizzare un hotspot cellulare o una rete attendibile ove possibile.
  - **Attività vietate sul Wi-Fi pubblico** (anche con VPN): Transazioni finanziarie, variazioni di password per account critici (utilizzare rete dati cellulare o rete attendibile).

  **Sicurezza della rete domestica**: I lavoratori da remoto dovrebbero proteggere le proprie reti domestiche (cambiare la password predefinita del router, abilitare WPA3/WPA2, disabilitare WPS, applicare gli aggiornamenti del firmware del router).
- **Timeout della sessione**: Le sessioni di accesso remoto DEVONO essere configurate per disconnettersi dopo un periodo di inattività definito (massimo 15 minuti per i sistemi che gestiscono dati Riservati o Limitati; massimo 30 minuti per gli altri sistemi).

## Gestione dei dati

I lavoratori da remoto DEVONO gestire i dati secondo il loro livello di classificazione ai sensi della Politica di classificazione e gestione delle informazioni:

| Classificazione dei dati | Archiviazione remota consentita | Condizioni |
|--------------------------|---------------------------------|------------|
| **Pubblico** | Sì | Sicurezza standard del dispositivo |
| **Interno** | Sì | Dispositivo crittografato richiesto |
| **Riservato** | Condizionale | Dispositivo crittografato, posizione di archiviazione approvata, approvazione del responsabile diretto |
| **Limitato** | No (predefinito) | Richiede l'approvazione esplicita del RSSI con controlli compensativi documentati |

I lavoratori da remoto DEVONO seguire la Politica di trasferimento delle informazioni quando inviano o ricevono dati organizzativi da postazioni remote. I dati organizzativi non DEVONO essere trasferiti su storage cloud personale, account email personali o servizi di condivisione file non approvati.

## Requisiti per dispositivi aziendali e BYOD

### Dispositivi aziendali

I dispositivi emessi dall'azienda e utilizzati per il lavoro da remoto DEVONO:

- Essere configurati secondo la baseline di sicurezza organizzativa.
- Avere la crittografia completa del disco (FDE) abilitata.
- Avere installato e attivo un software di protezione endpoint aggiornato.
- Essere aggiornati con le patch secondo il programma di patching organizzativo.
- Avere la funzionalità di cancellazione remota abilitata.
- Essere registrati nell'inventario dei dispositivi.

### BYOD (Bring Your Own Device)

Non è nella politica dell'organizzazione consentire di default l'utilizzo di dispositivi mobili personali per il lavoro. È richiesta l'autorizzazione del team di gestione della sicurezza delle informazioni.

**Criteri di approvazione BYOD**:
- Giustificazione aziendale (necessità temporanea, requisito del ruolo, riduzione dei costi).
- Il dispositivo soddisfa i requisiti minimi di sicurezza (sistema operativo aggiornato, compatibile con MDM, non jailbroken/rooted).
- Classificazione dei dati: BYOD consentito solo per dati Interni e Pubblici; per i dati Riservati è richiesta l'approvazione di eccezione da parte del RSSI.
- Formazione dell'utente completata e conferma di responsabilità firmata.
- Soluzione MDM o di containerizzazione implementata prima della concessione dell'accesso.

Nei casi in cui un dispositivo personale sia autorizzato:

- Il dispositivo DEVE essere registrato nel registro degli asset.
- L'utente DEVE ricevere formazione e firmare una conferma di responsabilità.
- Si applicano tutte le politiche organizzative, inclusa questa politica e la Politica di controllo degli accessi.
- DEVE essere installata una soluzione MDM (gestione dei dispositivi mobili) o di containerizzazione per separare i dati personali da quelli organizzativi.
- L'organizzazione si riserva il diritto di cancellare da remoto i dati organizzativi dal dispositivo alla cessazione del rapporto di lavoro o dell'accesso, o in caso di smarrimento o furto.
- Nessun dato personale o dato personale degno di particolare protezione (ai sensi della nLPD) DEVE essere archiviato sul dispositivo al di fuori del container gestito.

### Dispositivi vietati

I seguenti dispositivi NON DEVONO essere utilizzati per lavoro organizzativo:

- Dispositivi sottoposti a jailbreak o root.
- Dispositivi con funzionalità di sicurezza disabilitate.
- Dispositivi condivisi non sotto il solo controllo dell'utente.
- Dispositivi che eseguono sistemi operativi a fine vita che non ricevono più aggiornamenti di sicurezza.
- Dispositivi che non possono soddisfare i requisiti minimi di sicurezza definiti dalla Sicurezza informatica.

## Cessazione del lavoro da remoto

Alla cessazione dell'autorizzazione al lavoro da remoto o del rapporto di lavoro:

- Le credenziali di accesso remoto DEVONO essere revocate immediatamente (lo stesso giorno).
- VPN e token di accesso remoto DEVONO essere disabilitati.
- Tutte le attrezzature organizzative DEVONO essere restituite ai sensi della Politica di restituzione degli asset (A.5.11).
- Tutti i dati organizzativi DEVONO essere rimossi dai dispositivi personali. Per i dispositivi BYOD, DEVE essere eseguita la cancellazione remota MDM del container organizzativo.
- La restituzione e la rimozione dei dati DEVONO essere verificate e documentate.

---

# Parte 2 — Segnalazione degli eventi di sicurezza (A.6.8)

## Canali di segnalazione

L'organizzazione DEVE fornire meccanismi accessibili a tutto il personale per segnalare eventi di sicurezza delle informazioni osservati o sospetti.

**Requisiti dei canali**:

- Devono essere disponibili almeno **due canali di segnalazione distinti**.
- Almeno **un canale** DEVE essere disponibile al di fuori degli orari lavorativi (24/7).
- Tutti i canali DEVONO essere accessibili da postazioni remote senza richiedere l'accesso ai sistemi interni (per consentire la segnalazione di eventi correlati agli accessi).

**Canali di segnalazione standard**:

| Canale | Scopo | Disponibilità |
|--------|-------|---------------|
| **Email di sicurezza** (ad es., security@[organizzazione].ch) | Eventi non urgenti, report dettagliati con allegati | 24/7 (monitorata durante l'orario lavorativo) |
| **Telefono / linea di assistenza** | Eventi urgenti, attacchi attivi, dispositivi smarriti/rubati | 24/7 (reperibilità al di fuori dell'orario) |
| **Sistema di ticketing** | Invio formale degli eventi, monitoraggio, follow-up | Orario lavorativo |
| **Opzione anonima** (modulo web o linea di assistenza di terze parti) | Segnalazioni in cui il segnalante desidera rimanere anonimo | 24/7 |

**Segnalazione anonima**:
- **Scopo**: Consente la segnalazione di presunte violazioni delle politiche, minacce interne o preoccupazioni sensibili nei casi in cui il segnalante tema ritorsioni.
- **Preservazione dell'anonimato**: Il canale anonimo è gestito da un fornitore terzo (se applicabile) o tramite un modulo web senza registrazione di dati identificativi. L'identità del segnalante non viene tracciata né registrata.
- **Limitazione del follow-up**: Poiché l'identità del segnalante è sconosciuta, il follow-up è limitato. I segnalanti anonimi sono incoraggiati a verificare le risposte nel portale/canale di segnalazione se il sistema supporta la comunicazione bidirezionale anonima.
- **Approccio alternativo**: I segnalanti possono anche rivolgersi alle RU o al Consulente legale con riservatezza (non anonimato completo) se è necessario un follow-up.

Le segnalazioni anonime ricevono la stessa priorità e indagine delle segnalazioni identificate.

**Pubblicazione**: I canali di segnalazione DEVONO essere pubblicati sulla intranet, inclusi nei materiali di onboarding dei dipendenti, citati nella formazione annuale sulla consapevolezza della sicurezza e visualizzati sulle schermate di accesso o sugli sfondi del desktop.

## Eventi segnalabili

**Distinzione evento / incidente**:

| Termine | Definizione |
|---------|-------------|
| **Evento di sicurezza** | Un'occorrenza identificata che indica una *possibile* violazione della politica di sicurezza o un guasto dei controlli |
| **Incidente di sicurezza** | Un evento di sicurezza che è stato valutato e confermato come avente un effetto negativo reale o potenziale sulla riservatezza, integrità o disponibilità delle informazioni |

**Il personale segnala gli EVENTI. Il Team di sicurezza informatica valuta se gli eventi costituiscono INCIDENTI.** In caso di dubbio, segnalare.

**Categorie di eventi segnalabili**:

**Phishing e ingegneria sociale**:

- Email sospette che richiedono credenziali, pagamenti o informazioni sensibili.
- Telefonate o messaggi di testo sospetti che si spacciano per colleghi o fornitori.
- Tentativi di manipolazione per aggirare i controlli di sicurezza o ottenere l'accesso.

**Malware e compromissione dei sistemi**:

- Comportamento imprevisto del sistema, degrado delle prestazioni o arresti anomali.
- Pop-up, messaggi o notifiche sospetti.
- Sospetta infezione da malware (inclusi gli indicatori di ransomware).
- Modifiche ai sistemi non elaborate tramite il controllo delle modifiche.

**Accesso non autorizzato**:

- Tentativi di accesso sconosciuti o imprevisti agli account.
- Dispositivi sconosciuti connessi agli account.
- Blocchi account o variazioni di password imprevisti.
- Modifiche sospette ai privilegi o nuovi account amministratore.

**Violazione e perdita di dati**:

- Email inviate per errore contenenti dati sensibili o personali.
- Accesso, esposizione o download non autorizzato di dati.
- Documenti o supporti contenenti dati organizzativi smarriti o rubati.
- Sospetta esfiltrazione di dati.

**Sicurezza fisica**:

- Dispositivi smarriti o rubati (laptop, telefoni, chiavette USB, badge di accesso).
- Accesso fisico non autorizzato ad aree protette (piggybacking).
- Attrezzature mancanti o danneggiate.

**Violazioni delle politiche**:

- Elusione osservata dei controlli di sicurezza.
- Violazioni note delle politiche di sicurezza da parte di altri.
- Installazioni software non approvate o variazioni di configurazione.

**Specifiche del lavoro da remoto**:

- Sospetta compromissione della rete domestica o del router.
- Accesso non autorizzato al dispositivo di lavoro da parte di familiari o altri.
- Guasti VPN o di accesso remoto che suggeriscono un attacco o una compromissione.
- Attività sospette mentre si lavora da luoghi pubblici.
- Furto o smarrimento del dispositivo durante una trasferta o presso un sito remoto.
- Richieste di supporto IT sospette che chiedono le credenziali di accesso remoto.
- Variazioni di configurazione del router domestico non avviate dall'utente.
- Osservazione fisica dei materiali di lavoro da parte di persone non autorizzate.

### Procedura in caso di dispositivo smarrito o rubato

In caso di smarrimento o furto di un dispositivo contenente dati organizzativi:

1. **Segnalare immediatamente** tramite telefono/linea di assistenza (gravità Critica — segnalare immediatamente).
2. **Fornire i dettagli**: tipo di dispositivo, numero di serie (se noto), ultima posizione nota, ora approssimativa dello smarrimento/furto, classificazione dei dati presenti sul dispositivo.
3. **Azioni della Sicurezza informatica**:
   - Avviare la cancellazione remota (se il dispositivo è acceso e connesso).
   - Revocare le credenziali VPN e di accesso remoto.
   - Monitorare eventuali attività sospette sugli account.
   - Documentare l'incidente per le indagini.
4. **Azioni dell'utente**:
   - Cambiare le password degli account a cui si è acceduto dal dispositivo smarrito (come indicato dalla Sicurezza informatica).
   - Presentare una denuncia alle forze dell'ordine (in caso di furto) e fornire il numero della denuncia alla Sicurezza informatica.
   - Non tentare di recuperare il dispositivo da soli (priorità alla sicurezza personale).
5. **Assicurazione / Sostituzione**: Contattare le RU per il processo di sostituzione del dispositivo.

**Conservazione delle prove**: Se il dispositivo viene successivamente ritrovato, non accenderlo né tentare di utilizzarlo. Riconsegnarlo alla Sicurezza informatica per l'analisi forense.

## Procedure di segnalazione

**Cosa includere in una segnalazione** (ove noto):

- Data e ora in cui l'evento è stato osservato o scoperto.
- Descrizione di quanto accaduto.
- Sistemi, applicazioni o dati potenzialmente interessati.
- Azioni già intraprese (se presenti).
- Informazioni di contatto per il follow-up (salvo segnalazione anonima).
- Eventuali prove a supporto (screenshot, intestazioni email, messaggi di errore).

**Tempestività della segnalazione**:

| Gravità dell'evento | Esempi | Tempistica di segnalazione |
|---------------------|--------|---------------------------|
| **Critica** | Attacco attivo, violazione dei dati confermata, ransomware, dispositivo con dati Limitati rubato | Immediatamente |
| **Alta** | Dispositivo smarrito/rubato, credenziali compromesse, sospetta infezione da malware | Entro 1 ora |
| **Media** | Tentativo di phishing (non cliccato), attività sospetta, violazione della politica osservata | Entro 4 ore |
| **Bassa** | Preoccupazione generica per la sicurezza, deviazione minore dalla politica, attività insolita ma non minacciosa | Entro 24 ore |

In caso di incertezza sulla gravità, segnalare al livello superiore. Il Team di sicurezza informatica rivaluterà durante il triage. Non ritardare la segnalazione per determinare la classificazione precisa.

**Responsabilità del segnalante**:

- Segnalare tempestivamente secondo le tempistiche sopra indicate.
- Fornire informazioni accurate al meglio delle proprie conoscenze.
- **Conservare le prove**: Inoltrare le email di phishing come allegati (non inoltrarle inline né cliccare sui link). Screenshot delle anomalie e annotare l'ora esatta e i sistemi interessati. Fotografare gli eventi di sicurezza fisica se è sicuro farlo.
- **Non** tentare di indagare, verificare o risolvere l'evento autonomamente.
- **Non** tentare di testare o sfruttare vulnerabilità sospette.
- Cooperare con qualsiasi indagine di follow-up del Team di sicurezza informatica.

## Cultura senza colpa

L'organizzazione promuove un ambiente non punitivo per la segnalazione degli eventi di sicurezza.

| Principio | Impegno |
|-----------|---------|
| **Protezione in buona fede** | Il personale che segnala eventi in buona fede non subirà conseguenze negative per l'atto di segnalazione |
| **Gestione degli errori onesti** | Gli errori onesti (ad es., clic su un link di phishing) segnalati tempestivamente saranno gestiti in modo costruttivo, concentrandosi sull'apprendimento e sulla prevenzione |
| **Nessuna ritorsione** | Le ritorsioni nei confronti dei segnalanti in buona fede sono vietate e saranno esse stesse soggette a provvedimenti disciplinari |
| **Riservatezza del segnalante** | L'identità del segnalante DEVE essere protetta nella misura del possibile e condivisa solo su base di necessità di sapere |

L'organizzazione DEVE riconoscere e incoraggiare il comportamento esemplare di segnalazione. Gli eventi segnalati DEVONO essere utilizzati come opportunità di apprendimento, non come fattori scatenanti di sanzioni.

**Eccezioni alla protezione senza colpa**:

- Violazioni deliberate delle politiche segnalate solo dopo la scoperta da parte di altri.
- Attività dolosa mascherata da accidentale.
- Negligenza reiterata dopo formazione e avvertimenti formali.
- Segnalazioni false fatte in malafede.

## Risposta e feedback

L'organizzazione DEVE rispondere a tutte le segnalazioni di eventi di sicurezza entro i tempi definiti:

| Tipo di risposta | Tempistica |
|------------------|------------|
| **Conferma di ricezione** (conferma che la segnalazione è stata ricevuta) | Entro 4 ore lavorative |
| **Valutazione iniziale** (evento classificato, priorità assegnata) | Entro 24 ore |
| **Aggiornamento di stato al segnalante** | Entro 72 ore |
| **Notifica di chiusura** | Al momento della risoluzione |

L'organizzazione DEVE:

- Confermare la ricezione di tutte le segnalazioni (incluse quelle anonime, ove esiste un canale di risposta).
- Fornire aggiornamenti di stato ai segnalanti sull'avanzamento e sull'esito delle loro segnalazioni.
- Comunicare le lezioni apprese dagli eventi attraverso aggiornamenti sulla consapevolezza (senza identificare i segnalanti).
- Escalare gli eventi al processo di gestione degli incidenti (ai sensi di A.5.24-28) quando l'evento è valutato come un incidente di sicurezza confermato, richiede risorse che vanno oltre la risposta iniziale, ha implicazioni per la notifica normativa, o interessa più sistemi o unità aziendali.

## Metriche di segnalazione

L'organizzazione DEVE monitorare le seguenti metriche di segnalazione degli eventi di sicurezza:

| Metrica | Obiettivo | Frequenza di revisione |
|---------|-----------|------------------------|
| **Conferma di ricezione entro 4 ore lavorative** | 100% | Mensile |
| **Valutazione iniziale entro 24 ore** | 100% | Mensile |
| **Andamento del volume delle segnalazioni** (aumento della consapevolezza o delle minacce) | Monitorato | Trimestrale |
| **Utilizzo dei canali di segnalazione** (email, telefono, ticketing, anonimo) | Utilizzo bilanciato tra i canali | Trimestrale |
| **Feedback dei segnalanti** (soddisfazione per la risposta e la comunicazione) | >80% soddisfatti | Annuale (sondaggio) |
| **Tasso di falsi positivi** (eventi rispetto a incidenti confermati) | Monitorato | Trimestrale |

Le metriche DEVONO essere riferite al RSSI mensilmente e al team di revisione della direzione trimestralmente.

**KPI di segnalazione degli eventi integrati nella formazione sulla consapevolezza**: La formazione annuale DEVE includere il volume delle segnalazioni e i casi di successo per rafforzare la cultura senza colpa.

---

## Formazione e consapevolezza sulla segnalazione

Tutto il personale DEVE ricevere formazione sulla segnalazione degli eventi di sicurezza:

**Formazione iniziale** (entro 30 giorni dall'assunzione o dal cambio di ruolo):
- Cos'è un evento di sicurezza rispetto a un incidente.
- Categorie di eventi segnalabili con esempi.
- Canali di segnalazione e quando utilizzare ciascuno.
- Tempistiche di segnalazione per gravità.
- Cultura senza colpa e protezione in buona fede.

**Formazione di aggiornamento annuale**:
- Panorama aggiornato delle minacce (recenti campagne di phishing, tattiche di ingegneria sociale).
- Casi di successo (eventi segnalati che hanno prevenuto incidenti).
- Metriche di segnalazione (che reinforzano il valore della segnalazione).

**Simulazione di phishing**: Simulazioni di phishing trimestrali con formazione immediata per gli utenti che cliccano; le simulazioni sono trattate come opportunità di apprendimento, non come misure punitive.

Il completamento della formazione è monitorato; obiettivo: **100% del personale** completa la formazione annuale.

---

## Verifica della conformità al lavoro da remoto

La conformità alla sicurezza del lavoro da remoto DEVE essere verificata tramite:

**Controlli di conformità trimestrali**:
- Log di utilizzo VPN/AMF (100% dei lavoratori da remoto che accedono tramite VPN con AMF).
- Stato di crittografia dei dispositivi (100% dei dispositivi registrati crittografati).
- Protezione endpoint aggiornata (100% dei dispositivi con antivirus/EDR aggiornato).
- Conformità alle patch (≥95% dei dispositivi aggiornati con patch del sistema operativo e patch critiche).

**Revisioni annuali del lavoro da remoto**:
- Revisione delle autorizzazioni al lavoro da remoto (confermare che le autorizzazioni siano aggiornate e appropriate).
- Audit dell'inventario dei dispositivi BYOD (verificare che tutti i dispositivi personali siano registrati e conformi).
- Lavoratori da remoto ad alto rischio (accesso ai dati Riservati) — aggiornamento della valutazione del rischio.

**Controlli a campione** (casuali o attivati):
- La Sicurezza informatica può condurre controlli di conformità da remoto (richiedere screenshot che mostrino la crittografia, la protezione endpoint, la connessione VPN).
- La non conformità attiva un piano di rimediazione o la revoca dei privilegi di lavoro da remoto.

Le metriche di conformità sono riferite al RSSI trimestralmente.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **Direzione generale** | Approvare la politica sul lavoro da remoto; fornire risorse; promuovere la cultura di segnalazione senza colpa; ricevere briefing sugli eventi di sicurezza critici |
| **RSSI** | Definire i requisiti di sicurezza del lavoro da remoto e i meccanismi di segnalazione degli eventi; autorizzare le eccezioni ad alto rischio; supervisionare la conformità; riferire alla direzione |
| **Team di sicurezza informatica** | Implementare e mantenere i controlli di accesso remoto; ricevere e valutare le segnalazioni degli eventi; coordinare la risposta; fornire feedback ai segnalanti; mantenere i canali di segnalazione |
| **Operazioni IT** | Predisporre l'accesso remoto (VPN, AMF, dispositivi); supportare l'infrastruttura dei canali di segnalazione; implementare le azioni di contenimento quando indicato |
| **RU** | Gestire gli accordi e le cessazioni del lavoro da remoto; includere la segnalazione degli eventi nell'onboarding; coordinare le questioni relative al personale |
| **Responsabili diretti** | Autorizzare il lavoro da remoto per i membri del team; garantire la conformità del team; incoraggiare la segnalazione degli eventi; escalare le preoccupazioni di sicurezza |
| **Tutto il personale** | Rispettare i requisiti del lavoro da remoto; mettere in sicurezza dispositivi e dati; segnalare tempestivamente gli eventi; conservare le prove; cooperare con le indagini |

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

| N. | Prova | Responsabile | Frequenza |
|----|-------|--------------|-----------|
| 1 | **Registri delle autorizzazioni al lavoro da remoto** (accordi approvati con valutazione del rischio ove applicabile) | RU / Responsabili diretti | *Per accordo; riesaminato annualmente; conservato per la durata + 2 anni* |
| 2 | **Registri di conferma della politica** da parte dei lavoratori da remoto | RU | *Per onboarding / rinnovo annuale; obiettivo: copertura del 100%* |
| 3 | **Inventario dei dispositivi** (dispositivi aziendali e BYOD approvati assegnati ai lavoratori da remoto) | Operazioni IT | *Aggiornato entro 5 giorni lavorativi dalla modifica; verificato annualmente* |
| 4 | **Rapporti di conformità tecnica** (utilizzo VPN, registrazione AMF, crittografia dispositivi, stato delle patch) | Sicurezza informatica | *Riesaminato mensilmente; dashboard aggiornato continuamente* |
| 5 | **Segnalazioni di eventi di sicurezza** ricevute tramite i canali designati | Sicurezza informatica | *Mantenuto continuamente; conservato per un minimo di 3 anni* |
| 6 | **Registri di risposta agli eventi** (conferma di ricezione, valutazione, aggiornamenti di stato, chiusura) con metriche sui tempi di risposta | Sicurezza informatica | *Per evento; conformità alle tempistiche di risposta riesaminata trimestralmente* |
| 7 | **Registri di formazione sulla consapevolezza della sicurezza** relativi alla sicurezza del lavoro da remoto e alla segnalazione degli eventi | RU / Sicurezza informatica | *Annuale; completamento monitorato; obiettivo: 100% dei lavoratori da remoto* |
| 8 | **Registri della disponibilità dei canali di segnalazione** (test e uptime di email, telefono, ticketing, canali anonimi) | Operazioni IT | *Testato trimestralmente; risultati documentati* |
| 9 | **Registri di restituzione delle attrezzature e rimozione dei dati** alla cessazione del lavoro da remoto | Operazioni IT / RU | *Per cessazione; verificato e firmato* |
| 10 | **Registro delle eccezioni** (eccezioni autorizzate a questa politica con giustificazione e controlli compensativi) | RSSI | *Aggiornato per eccezione; riesaminato trimestralmente; voci a tempo determinato rivalutate alla scadenza* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, l'analisi dei log di accesso remoto, i rapporti di conformità dei dispositivi, le metriche di segnalazione degli eventi (volume, tempestività, tempi di risposta), gli audit interni ed esterni, e il feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione a questa politica DEVE essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita. Le eccezioni DEVONO essere riferite al team di revisione della direzione.

## Non conformità

Un dipendente che abbia violato questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro. La non conformità ai requisiti del lavoro da remoto può comportare anche la revoca dei privilegi di lavoro da remoto. Il mancato rispetto dell'obbligo di segnalare gli eventi di sicurezza non gode della protezione senza colpa e può essere trattato come una violazione della politica.

## Miglioramento continuo

Questa politica è riesaminata e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare le modifiche alle modalità di lavoro da remoto, le minacce emergenti nei confronti dei lavoratori da remoto, le modifiche normative (in particolare nLPD e RGPD), gli sviluppi tecnologici, le tendenze nella segnalazione degli eventi e le lezioni apprese dagli incidenti.

---

# Aree della norma ISO 27001 trattate

Politica sul lavoro da remoto e sulla segnalazione degli eventi di sicurezza — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi della sicurezza delle informazioni | 5.36 Conformità alle politiche, norme e standard |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, formazione e addestramento sulla sicurezza delle informazioni |
| Clausola 8.1 Pianificazione e controllo operativi | 6.4 Processo disciplinare |
| | **6.7 Lavoro da remoto** |
| | **6.8 Segnalazione degli eventi di sicurezza delle informazioni** |
| | 7.9 Sicurezza degli asset fuori sede |
| | 8.1 Dispositivi endpoint degli utenti |

**Quadro normativo e giuridico**:

| Framework | Pertinenza |
|-----------|------------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la protezione dei dati negli ambienti di lavoro da remoto |
| CO svizzero Art. 328b | Il trattamento dei dati dei dipendenti è limitato ai dati necessari per il rapporto di lavoro |
| OPDo svizzera | Art. 1-3 — Requisiti minimi per la sicurezza dei dati |
| RGPD UE (ove applicabile) | Art. 32 — La sicurezza del trattamento deve estendersi al lavoro da remoto; Art. 33 — La notifica della violazione entro 72 ore richiede il rilevamento tempestivo degli eventi |
| ISO/IEC 27001:2022 | Allegato A Controlli 6.7, 6.8 |
| ISO/IEC 27002:2022 | Sezioni 6.7, 6.8 — Linee guida di attuazione |
| NIST SP 800-46 Rev 2 | Guida alla sicurezza del telelavoro aziendale, dell'accesso remoto e del BYOD |
| CIS Controls v8 | Controllo 4 (Configurazione sicura degli asset aziendali), Controllo 6 (Gestione del controllo degli accessi), Controllo 17 (Gestione della risposta agli incidenti) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
