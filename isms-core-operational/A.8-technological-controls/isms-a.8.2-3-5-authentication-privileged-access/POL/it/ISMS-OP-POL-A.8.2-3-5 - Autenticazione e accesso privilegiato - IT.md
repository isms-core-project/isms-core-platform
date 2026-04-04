<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.2-3-5-IT:operational:OP-POL:a.8.2-3-5 -->
**ISMS-OP-POL-A.8.2-3-5 — Autenticazione e accesso privilegiato**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Autenticazione e accesso privilegiato |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.2-3-5 |
| **Creatore del documento** | Responsabile della Sicurezza delle Informazioni (RSSI) |
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

- ISO/IEC 27001:2022 Controlli A.8.2, A.8.3, A.8.5 — Diritti di accesso privilegiato, restrizione dell'accesso alle informazioni, autenticazione sicura

**Controlli correlati dell'Annex A**:

| Controllo | Relazione con autenticazione e accesso privilegiato |
|-----------|-----------------------------------------------------|
| A.5.3 Separazione dei compiti | La separazione dei compiti è applicata tramite restrizioni di accesso e privilegi a livelli |
| A.5.15–18 Controllo degli accessi e gestione delle identità | Il ciclo di vita delle identità alimenta l'autenticazione; i diritti di accesso definiscono le restrizioni |
| A.5.17 Informazioni di autenticazione | Gestione delle credenziali per password, token e segreti |
| A.5.24–28 Gestione degli incidenti | La compromissione delle credenziali attiva la risposta agli incidenti |
| A.8.1 Dispositivi endpoint degli utenti | La sicurezza degli endpoint supporta l'autenticazione (trust del dispositivo, crittografia) |
| A.8.9 Gestione della configurazione | Le configurazioni di sistema applicano le baseline di autenticazione e accesso |
| A.8.15 Registrazione degli eventi | Gli eventi di autenticazione e le azioni privilegiate alimentano la registrazione centralizzata |
| A.8.16 Attività di monitoraggio | Monitoraggio in tempo reale degli errori di autenticazione e degli accessi privilegiati |
| A.8.20–22 Sicurezza della rete | La segmentazione della rete supporta l'applicazione delle zone di accesso |
| A.8.24 Uso della crittografia | Protezione crittografica di credenziali, token e sessioni |

**Politiche interne correlate**:

- Politica di gestione delle identità e degli accessi
- Politica di sicurezza degli endpoint
- Politica di sicurezza della rete
- Politica di uso della crittografia
- Politica di registrazione degli eventi
- Politica delle attività di monitoraggio (A.8.16)
- Politica di gestione degli incidenti

---

# Politica di autenticazione e accesso privilegiato

## Scopo

Lo scopo di questa politica è garantire che i meccanismi di autenticazione siano implementati proporzionalmente alla sensibilità delle informazioni e dei sistemi a cui si accede, che i diritti di accesso privilegiato siano limitati e gestiti secondo il principio del privilegio minimo, e che i controlli di accesso tecnici applichino i confini di accesso autorizzati.

Questa politica supporta la nLPD svizzera (revDSG) e l'Ordinanza sulla protezione dei dati (OPDo) implementando misure tecniche e organizzative adeguate al rischio per proteggere i dati personali (inclusi i dati personali degni di particolare protezione) tramite controlli di autenticazione e accesso. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR. L'autenticazione forte e la gestione degli accessi privilegiati sono misure tecniche chiave per dimostrare la conformità agli obblighi di protezione dei dati nell'ambito di entrambi i quadri normativi.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Tutti i meccanismi di autenticazione, gli account privilegiati e i controlli di accesso tecnici su sistemi, piattaforme e ambienti di proprietà o gestiti dall'organizzazione e rientranti nell'ambito definito dalla dichiarazione di ambito ISO 27001.

Ciò include gli ambienti on-premises, cloud, ibridi e SaaS.

## Principio

I controlli di autenticazione e accesso sono implementati sul principio della difesa in profondità. Gli utenti sono positivamente identificati e autenticati prima di ottenere l'accesso. L'accesso privilegiato è concesso solo con approvazione documentata ed è limitato al minimo necessario per il compito. L'accesso è negato per default e concesso solo su autorizzazione esplicita.

Tutte le decisioni di autenticazione e accesso DEVONO essere basate sul rischio, tenendo conto della classificazione delle informazioni e della criticità del sistema.

---

## Infrastruttura di gestione delle identità e degli accessi

La seguente tabella documenta lo stack tecnologico IAM dell'organizzazione. La selezione effettiva degli strumenti è specifica dell'organizzazione; gli esempi sono forniti a titolo orientativo:

| Funzione | Soluzione | Responsabile | Uso principale |
|----------|-----------|--------------|----------------|
| **Provider di identità (IdP)** | [ad es. Azure Active Directory (Entra ID), Okta, Google Workspace, JumpCloud] | IT Operations | Autenticazione centralizzata, SSO, gestione del ciclo di vita degli utenti |
| **Gestione degli accessi privilegiati (PAM)** | [ad es. CyberArk, Delinea (Thycotic), BeyondTrust, Azure AD PIM] | Sicurezza IT | Archiviazione sicura delle password, registrazione delle sessioni, accesso JIT, rotazione delle credenziali |
| **Autenticazione a più fattori (AMF)** | [ad es. Azure MFA, Okta Verify, Duo Security, YubiKey (FIDO2)] | IT Operations | Secondo fattore di autenticazione per tutti gli utenti |
| **Gestore password aziendale** | [ad es. 1Password Business, Bitwarden Teams, LastPass Enterprise] | Sicurezza IT | Archiviazione sicura delle credenziali condivise; transitorio fino al PAM per gli account di servizio |
| **Single Sign-On (SSO)** | [Integrato con IdP tramite SAML 2.0 / OIDC] | IT Operations | Autenticazione delle applicazioni tramite IdP centralizzato |
| **Registrazione delle sessioni** | [ad es. PAM nativo, CyberArk PSM, Teleport, Windows Defender for Identity] | Sicurezza IT | Registrare e verificare le sessioni privilegiate di Livello 0 |
| **Verifica delle credenziali compromesse** | [ad es. Azure AD Password Protection, API Have I Been Pwned, Enzoic] | Sicurezza IT | Impedire l'uso di password note come violate |
| **Governance delle identità** | [ad es. Azure AD Access Reviews, SailPoint, Saviynt, o flusso di lavoro manuale su foglio di calcolo] | Sicurezza IT | Campagne di certificazione degli accessi, reporting di conformità |

**Punti di integrazione**: L'IdP DEVE essere integrato con il sistema HR per l'automazione delle procedure di inserimento/trasferimento/uscita. PAM, IdP e SIEM DEVONO essere integrati per il monitoraggio centralizzato. L'AMF DEVE essere applicata tramite policy di accesso condizionale dell'IdP. I log della registrazione delle sessioni DEVONO essere inoltrati al SIEM.

---

## Requisiti di autenticazione

### Standard per le password

L'accesso ai sistemi e alle informazioni viene autenticato tramite password o meccanismi più robusti. L'organizzazione DEVE applicare i seguenti standard per le password, allineati con NIST SP 800-63B:

| Requisito | Standard |
|-----------|----------|
| Lunghezza minima | 12 caratteri (14 per gli account privilegiati) |
| Complessità | Lunghezza anziché complessità; nessuna regola di composizione obbligatoria |
| Lunghezza massima | I sistemi DEVONO accettare almeno 64 caratteri |
| Supporto caratteri | Tutti i caratteri ASCII stampabili (incluso lo spazio) e Unicode DEVONO essere accettati |
| Verifica | Le password DEVONO essere convalidate rispetto ai database di credenziali compromesse/violate note all'impostazione/modifica e mensilmente in seguito |
| Rotazione | Solo a seguito di eventi — in caso di compromissione sospetta o confermata; la rotazione periodica forzata non è richiesta |
| Password iniziali | DEVONO essere cambiate al primo utilizzo |
| Password predefinite | Le password predefinite fornite dal fornitore DEVONO essere cambiate immediatamente al momento dell'installazione |
| Condivisione | Le password NON devono essere generiche, condivise o impostate a livello di gruppo |
| Riservatezza | Le password DEVONO essere mantenute riservate e non scritte |
| Visualizzazione | Le password NON devono essere visualizzate durante l'inserimento |
| Codice | Le password NON devono essere codificate o incluse in script, codice o macro |
| Trasmissione | Le password DEVONO essere crittografate quando trasmesse sulle reti |
| Archiviazione | Le password DEVONO essere archiviate utilizzando funzioni di hash crittografiche approvate (bcrypt, scrypt, Argon2 o PBKDF2) e mai in chiaro o con crittografia reversibile |
| Blocco | I sistemi DEVONO bloccare gli utenti dopo 6 tentativi di accesso falliti |
| Cronologia | DEVE essere mantenuta una cronologia delle password di almeno 24 password precedenti per impedirne il riutilizzo |
| Gestori password | L'uso di gestori password approvati dall'organizzazione è raccomandato |

**Opzioni di implementazione per la verifica delle credenziali compromesse**:

| Opzione | Implementazione | Note |
|---------|----------------|------|
| **Azure AD Password Protection** | Abilitare la lista globale di password vietate + lista personalizzata; applicare nel cloud e on-premises (tramite agenti DC) | Raccomandato per ambienti Microsoft |
| **API Have I Been Pwned (HIBP)** | Modello k-anonimato (vengono inviati solo i primi 5 caratteri dell'hash); verifica all'impostazione/modifica della password e scansione mensile | Open-source; richiede sforzo di integrazione |
| **Soluzione di terze parti** | Enzoic, Specops Password Policy o equivalente | Commerciale; include tipicamente l'applicazione di policy sulle password aggiuntive |

Le password trovate nei database delle violazioni DEVONO essere rifiutate all'impostazione/modifica e cambiate forzatamente se rilevate durante le scansioni mensili. Metrica di copertura della verifica: percentuale di eventi di impostazione/modifica della password convalidati rispetto ai database delle violazioni (obiettivo: 100%).

### Autenticazione a più fattori (AMF)

L'autenticazione a più fattori DEVE essere richiesta per:

- Tutti gli account privilegiati e amministrativi.
- Tutti gli accessi remoti alle reti e ai servizi cloud dell'organizzazione.
- Tutte le applicazioni esposte esternamente con autenticazione.
- Tutti gli accessi ai sistemi che trattano dati riservati o dati personali.
- Tutte le console di amministrazione della piattaforma cloud.

**Metodi AMF accettabili** (in ordine di preferenza):

| Metodo | Resistenza al phishing | Uso raccomandato |
|--------|------------------------|------------------|
| Chiavi di sicurezza hardware (FIDO2/WebAuthn) | Alta | Obbligatorio per il Livello 0; raccomandato per tutti gli account privilegiati |
| App di autenticazione (TOTP) | Media | Accettabile per Livello 1/2 e utenti standard |
| Notifiche push (con abbinamento numerico) | Media | Accettabile dove è abilitato l'abbinamento numerico |
| OTP tramite SMS/voce | Bassa | Solo dove gli altri metodi non sono tecnicamente fattibili (sistemi legacy) |

L'OTP basata su SMS dovrebbe essere progressivamente eliminata ove possibile a causa delle vulnerabilità note (SIM swapping, intercettazione). I sistemi che si affidano esclusivamente all'AMF basata su SMS DEVONO essere documentati nel registro dei rischi con un piano di migrazione.

**Obiettivi di copertura AMF**:

- Utenti privilegiati: 100% di registrazione AMF.
- Tutti gli utenti: >95% di registrazione AMF entro 12 mesi dall'adozione della politica.
- Accesso remoto: 100% di applicazione AMF.

I sistemi che non supportano l'AMF DEVONO essere documentati nel registro dei rischi con giustificazione tecnica, controlli compensativi (ad es. segmentazione della rete, monitoraggio potenziato, restrizione IP) e accettazione del rischio approvata dal RSSI con revisione annuale.

### Single Sign-On (SSO)

L'organizzazione DEVE implementare SSO centralizzato tramite il provider di identità utilizzando SAML 2.0 o OIDC con i seguenti obiettivi:

- Nuove applicazioni SaaS: integrazione SSO richiesta prima dell'approvazione all'acquisto.
- Applicazioni esistenti: integrazione SSO prioritizzata in base al livello di rischio seguente.
- Obiettivo: >80% di integrazione delle applicazioni SaaS entro 12 mesi; >90% entro 24 mesi.

**Livelli di priorità per l'integrazione SSO**:

| Priorità | Criteri | Tempistica |
|----------|---------|------------|
| **Priorità 1** | Tratta dati riservati; >50 utenti; rivolto a internet; console di infrastruttura cloud | 30 giorni |
| **Priorità 2** | Tratta dati interni; 20–50 utenti; applicazioni di accesso privilegiato | 90 giorni |
| **Priorità 3** | <20 utenti; esposizione limitata ai dati; utilizzo poco frequente | 180 giorni |
| **Priorità 4** | Applicazioni legacy con limitazioni SSO; app programmate per la dismissione; fornitori che non supportano SSO | 12 mesi (o eccezione documentata) |

DEVE essere mantenuto un inventario delle integrazioni SSO che elenca ogni applicazione, il suo stato SSO (integrata / in corso / eccezione), il livello di priorità e la data obiettivo. L'inventario DEVE essere revisionato trimestralmente.

Le applicazioni senza capacità SSO richiedono un'eccezione documentata con controlli compensativi (ad es. AMF individuale, monitoraggio potenziato, applicazione del gestore password).

### Registrazione degli eventi di autenticazione

Tutti gli eventi di autenticazione DEVONO essere registrati e inoltrati al SIEM del sistema di registrazione centralizzata:

- Tentativi di autenticazione riusciti e falliti.
- Registrazione AMF e modifiche al metodo.
- Modifiche e reset delle password.
- Blocchi e sblocchi degli account.
- Creazione e terminazione delle sessioni.

I log di autenticazione DEVONO essere conservati per un minimo di 12 mesi.

**Regole di avviso per il monitoraggio dell'autenticazione**:

| Regola di avviso | Soglia | Gravità | SLA di risposta |
|------------------|--------|---------|-----------------|
| Attacco brute force | ≥10 accessi falliti da un singolo IP in 5 minuti | Alta | 1 ora |
| Credential stuffing | ≥5 accessi falliti su più account da un singolo IP in 10 minuti | Alta | 1 ora |
| Viaggio impossibile | Accesso riuscito da posizioni a >500 km di distanza entro 1 ora | Alta | 1 ora |
| Account privilegiato — nuovo dispositivo | Accesso Livello 0/1 da dispositivo non visto negli ultimi 30 giorni | Media | 4 ore |
| Account privilegiato — posizione inattesa | Accesso Livello 0/1 da paese al di fuori della lista approvata | Critica | Immediata |
| Accesso interattivo account di servizio | Account di servizio utilizzato per accesso RDP/SSH/console | Alta | 2 ore |
| Tentativo di elusione AMF | Autenticazione senza AMF richiesta | Alta | 1 ora |
| Utilizzo account d'emergenza | Autenticazione dell'account d'emergenza/break-glass | Critica | Immediata; revisione entro 24 ore |
| Picco di blocchi account | ≥10 blocchi nell'intera infrastruttura in 1 ora | Media | Investigare entro lo stesso giorno lavorativo |

**Posizioni geografiche approvate**: Svizzera, [paesi aggiuntivi per le operazioni aziendali]. Gli accessi da paesi non approvati DEVONO attivare avvisi come da tabella sopra.

Le regole di avviso DEVONO essere revisionate e ottimizzate trimestralmente per ridurre i tassi di falsi positivi. Flusso di lavoro per le indagini: ricevere avviso → convalidare (vero/falso positivo) → arricchire con contesto → escalare se confermato → documentare il risultato.

### Requisiti del sistema di autenticazione

Il sistema di autenticazione principale DEVE:

- Non visualizzare gli identificatori del sistema o dell'applicazione fino al completamento con successo del processo di accesso.
- Visualizzare un avviso generale che indica che il sistema deve essere accessibile solo dagli utenti autorizzati.
- Non fornire messaggi di aiuto durante la procedura di accesso che potrebbero aiutare un utente non autorizzato.
- Convalidare le informazioni di accesso solo al completamento di tutti i dati inseriti. In caso di errore, il sistema NON deve indicare quale parte dei dati è corretta o errata.
- Proteggere contro i tentativi di accesso brute force.
- Registrare i tentativi non riusciti e riusciti.
- Generare un evento di sicurezza se viene rilevato un potenziale tentativo o una potenziale violazione riuscita dei controlli di accesso.
- Non visualizzare la password durante l'inserimento.
- Non trasmettere le password in chiaro su una rete.
- Terminare le sessioni inattive dopo un periodo di inattività definito.
- Limitare i tempi di connessione per fornire sicurezza aggiuntiva per le applicazioni ad alto rischio.

---

## Gestione degli accessi privilegiati

### Principi dell'accesso privilegiato

L'accesso privilegiato DEVE essere limitato in base a:

- **Privilegio minimo**: Accesso minimo necessario per svolgere le funzioni lavorative.
- **Need-to-know**: Accesso solo alle informazioni richieste per compiti specifici.
- **Separazione dei compiti**: Le funzioni critiche sono suddivise tra più individui.
- **Accesso a tempo limitato**: Provisioning Just-in-Time (JIT) laddove supportato.

### Classificazione degli account privilegiati — Modello di livelli amministrativi

L'organizzazione DEVE implementare l'amministrazione a livelli per limitare l'impatto delle credenziali compromesse:

| Livello | Ambito | Esempi | Requisiti |
|---------|--------|--------|-----------|
| **Livello 0** | Dominio/Enterprise | Domain Admin, Azure/M365 Global Admin, PKI, SIEM | AMF hardware (FIDO2); workstation amministrativa dedicata; registrazione delle sessioni obbligatoria |
| **Livello 1** | Server/Applicazione | Amministratori di server, DBA, amministratori di sottoscrizioni cloud | AMF obbligatoria; workstation amministrativa dedicata raccomandata |
| **Livello 2** | Workstation/Endpoint | Supporto desktop, help desk con diritti di amministratore locale | AMF obbligatoria; workstation standard accettabile |

**Requisiti di isolamento dei livelli**:

- Gli account di Livello 0 NON devono mai autenticarsi su sistemi di Livello 1 o Livello 2.
- Gli account di Livello 1 NON devono mai autenticarsi su sistemi di Livello 2.
- DEVONO essere utilizzate credenziali separate per livello (ad es. j.rossi.l0, j.rossi.l1).
- Le attività lavorative quotidiane (e-mail, navigazione web) NON devono essere eseguite su workstation amministrative dedicate.

**Applicazione dell'isolamento dei livelli**:

I controlli tecnici DEVONO applicare i confini dei livelli. Le seguenti sono opzioni di implementazione a seconda della piattaforma di identità dell'organizzazione:

*Accesso condizionale (Azure AD / Entra ID o equivalente):*

| Policy | Target | Applicazione |
|--------|--------|-------------|
| Richiedere AMF resistente al phishing per il Livello 0 | Account di Livello 0, tutte le app cloud | Solo FIDO2/WebAuthn; bloccare altri metodi AMF |
| Bloccare il Livello 0 dalle app non amministrative | Account di Livello 0 | Bloccare l'accesso a Office 365, SharePoint, OneDrive, Teams |
| Richiedere dispositivo conforme per l'accesso amministrativo | Account di Livello 0/1 | Richiedere dispositivo conforme o hybrid-joined |
| Bloccare l'autenticazione legacy | Tutti gli utenti | Bloccare IMAP, POP3, SMTP AUTH |
| Bloccare l'accesso da paesi non approvati | Tutti gli utenti (esclusi gli account d'emergenza) | Consentire: CH + paesi approvati; bloccare tutti gli altri |
| Richiedere AMF per tutti gli utenti | Tutti gli utenti, tutte le app cloud | Frequenza di accesso: 90 giorni |
| Bloccare gli accessi ad alto rischio | Tutti gli utenti (richiede Azure AD P2) | Bloccare gli accessi segnalati come ad alto rischio da Identity Protection |
| Timeout delle sessioni per le applicazioni sensibili | Finanza, HR, database clienti | Ri-autenticazione ogni 4 ore |

*Applicazione on-premises:*

- Restrizioni di accesso GPO: negare agli account di Livello 0 di accedere localmente ai sistemi di Livello 1/2; negare agli account di Livello 1 l'accesso alle workstation di Livello 2.
- Segmentazione della rete: Workstation amministrative di Livello 0 su VLAN dedicata; Livello 1 su VLAN separata; utenti standard su VLAN aziendale. Le regole del firewall limitano l'accesso cross-livello.

*Regole di avviso SIEM per le violazioni dei livelli:*

| Avviso | Gravità | Notifica |
|--------|---------|----------|
| Autenticazione del Livello 0 su sistema di Livello 1/2 | Critica | RSSI immediato |
| Autenticazione del Livello 1 su sistema di Livello 2 | Alta | Responsabile della sicurezza IT |
| Account privilegiato da posizione non approvata | Alta | Team di sicurezza IT |

**Workstation per accessi privilegiati (PAW)**:

| Livello | Requisito PAW |
|---------|---------------|
| **Livello 0** | PAW obbligatoria |
| **Livello 1** | PAW raccomandata; obbligatoria per la Fase 2 |
| **Livello 2** | Workstation standard accettabile |

*Baseline di configurazione PAW (Livello 0/1):*

- **Hardware**: Dispositivo fisico dedicato; crittografia completa del disco; TPM 2.0; Secure Boot abilitato.
- **Sistema operativo**: Hardened per CIS Benchmark Livello 2; aggiornamenti automatici; nessun software installato dall'utente (applicata la lista di applicazioni consentite).
- **Rete**: VLAN amministrativa dedicata; le regole del firewall limitano le connessioni ai soli target di gestione; nessuna navigazione internet generale.
- **Applicazioni**: Solo client RDP/SSH, client PAM e strumenti amministrativi. E-mail, browser web, suite Office e strumenti di collaborazione (Teams/Slack) sono vietati.
- **Controllo degli accessi**: Amministratore locale disabilitato; credenziali PAM obbligatorie; AMF applicata; blocco schermo dopo 10 minuti.
- **Monitoraggio**: Agente EDR installato; tutta l'attività inoltrata al SIEM; avvisi per software non autorizzato, connessioni o tentativi di navigazione.

**Distribuzione graduale**: Fase 1 (Anno 1): PAW di Livello 0 distribuite. Fase 2 (Anno 2): PAW di Livello 1 distribuite. DEVONO essere documentati controlli compensativi per qualsiasi periodo in cui le PAW non siano ancora in uso (ad es. monitoraggio potenziato, VM dedicate, account amministrativi con restrizioni su workstation standard).

**Monitoraggio dello stato di distribuzione**: L'attuale fase di distribuzione (pianificazione, pilota, applicazione parziale, applicazione completa) DEVE essere documentata per ogni livello con controlli compensativi per i livelli non ancora applicati e date obiettivo di completamento.

### Gestione degli account privilegiati

Tutti gli account privilegiati DEVONO essere:

- Non condivisi o generici (un utente, un account privilegiato per livello).
- Chiaramente identificabili (convenzione di nomenclatura documentata e applicata).
- Registrati e monitorati per attività anomale.
- A tempo limitato ove fattibile (accesso JIT preferito rispetto ai privilegi permanenti).
- Registrati in un inventario degli account privilegiati mantenuto aggiornato con proprietario, livello, scopo e data di revisione.

### Soluzione PAM (Gestione degli accessi privilegiati)

L'organizzazione DEVE implementare controlli di accesso privilegiato, che possono includere una soluzione PAM dedicata (vedere la tabella dell'infrastruttura IAM) o controlli manuali equivalenti:

| Capacità | Requisito | Approccio graduale per le PMI |
|----------|-----------|-------------------------------|
| **Archiviazione sicura delle password** | Le password privilegiate sono archiviate in un vault approvato, non in chiaro | Fase 1: Implementare per gli account di Livello 0; espandere al Livello 1/2 |
| **Registrazione delle sessioni** | Le sessioni di Livello 0 vengono registrate; la registrazione del Livello 1 è raccomandata | Fase 1: Livello 0 obbligatorio; Livello 1 man mano che il PAM viene esteso |
| **Accesso Just-in-Time** | Elevazione temporanea dei privilegi con revoca automatica | Fase 2: Implementare dove il PAM supporta i flussi di lavoro JIT |
| **Rotazione delle credenziali** | Le password degli account di servizio vengono ruotate secondo la pianificazione seguente | Fase 1: Rotazione manuale con evidenza documentata |

Laddove una soluzione PAM dedicata non sia ancora distribuita, DEVONO essere documentati controlli compensativi (ad es. rotazione manuale delle credenziali, gestore password condiviso con audit trail, registrazione alternativa delle sessioni tramite SIEM).

**Requisiti di rotazione delle credenziali**:

| Tipo di account | Frequenza di rotazione |
|-----------------|------------------------|
| Account di servizio (Livello 0) | Massimo 90 giorni |
| Account di servizio (Livello 1/2) | Massimo 180 giorni |
| Account d'emergenza | Dopo ogni utilizzo + massimo 365 giorni |
| Account amministrativi condivisi (sconsigliati) | 90 giorni; migrare ad account individuali con eccezione del RSSI |

Tutte le credenziali DEVONO essere ruotate immediatamente in caso di compromissione sospetta o confermata, indipendentemente dalla pianificazione.

### Gestione degli account di servizio

Gli account di servizio DEVONO essere gestiti attraverso un ciclo di vita definito:

1. **Richiesta e approvazione**: Il richiedente invia la richiesta tramite il sistema di ticketing. Il Responsabile della sicurezza IT approva entro 3 giorni lavorativi. Criteri di approvazione: giustificazione aziendale documentata, autorizzazioni minime definite, proprietario designato, livello designato.
2. **Creazione**: Convenzione di nomenclatura `svc-[sistema]-[scopo]` (ad es. `svc-erp-backup`). Password casuale di almeno 20 caratteri. Credenziali consegnate in modo sicuro tramite vault PAM o equivalente (mai tramite e-mail o chat).
3. **Inventario**: Tutti gli account di servizio registrati con: nome account, scopo, proprietario, livello, autorizzazioni, posizione delle credenziali (riferimento vault), data dell'ultima rotazione, data della prossima rotazione.
4. **Revisione degli accessi**: Attestazione trimestrale da parte dei proprietari delle applicazioni. Gli account inutilizzati (nessuna autenticazione negli ultimi 90 giorni) vengono disabilitati immediatamente ed eliminati dopo 90 giorni di conservazione.
5. **Rotazione delle credenziali**: Automatizzata tramite PAM dove supportato; rotazione manuale documentata nell'inventario dove PAM non è disponibile.
6. **Dismissione**: Quando il servizio viene dismesso, l'account di servizio viene disabilitato immediatamente, le credenziali vengono ruotate e l'account viene eliminato dopo 90 giorni di conservazione.

**Monitoraggio degli account di servizio**: Le regole di avviso SIEM DEVONO rilevare l'accesso interattivo da parte degli account di servizio, l'autenticazione da posizioni inattese e i tentativi di autenticazione falliti. DEVE essere eseguita una scansione di discovery trimestrale per identificare gli account di servizio non documentati.

### Accesso privilegiato Just-In-Time (JIT)

L'accesso JIT è preferito rispetto ai privilegi permanenti. Il seguente flusso di lavoro si applica in base agli strumenti disponibili:

**JIT basato su PAM** (preferito):

1. L'utente richiede l'elevazione dei privilegi tramite il portale PAM con giustificazione.
2. Approvazione: automatica per le attività pre-approvate; approvazione del manager/sicurezza IT per le altre.
3. Il PAM emette credenziali a tempo limitato (predefinito: 4 ore; massimo: 8 ore).
4. Sessione registrata (Livello 0 obbligatorio; Livello 1 raccomandato).
5. Privilegi automaticamente revocati alla scadenza.
6. Tutte le sessioni JIT registrate nell'audit trail PAM.

**Azure AD PIM** (per i ruoli cloud):

1. Ruolo idoneo assegnato (non attivo).
2. L'utente attiva il ruolo con giustificazione e AMF.
3. Approvazione richiesta per Global Admin e altri ruoli di Livello 0.
4. Attivazione a tempo limitato (predefinito: 4 ore; massimo: 8 ore).
5. Disattivazione automatica alla scadenza.
6. Tutte le attivazioni registrate nel log di audit di Azure AD.

**JIT manuale** (transitorio dove PAM/PIM non è distribuito):

1. L'utente richiede l'accesso tramite il sistema di ticketing con giustificazione.
2. La sicurezza IT approva e aggiunge l'appartenenza temporanea al gruppo.
3. Promemoria sul calendario impostato per il tempo di revoca.
4. IT Operations revoca manualmente l'accesso alla scadenza.
5. Il ticket viene chiuso con la conferma della revoca.

**Obiettivi JIT**: Anno 1: 50% degli accessi di Livello 1 tramite JIT. Anno 2: 80% degli accessi di Livello 1 tramite JIT. Livello 0: accesso permanente per i ruoli di reperibilità; JIT per tutti gli altri.

### Revisioni degli accessi privilegiati

| Tipo di account | Frequenza di revisione |
|-----------------|------------------------|
| Account privilegiati di Livello 0 | Trimestrale (revisione del RSSI o del Responsabile della sicurezza IT) |
| Account privilegiati di Livello 1/2 | Trimestrale (revisione dei proprietari del sistema) |
| Account di servizio | Trimestrale (i proprietari del sistema verificano la necessità continuata) |

**Processo di revisione**:

- Campagne di revisione degli accessi avviate tramite strumento di governance delle identità o processo manuale.
- Revisori: Responsabili diretti per Livello 1/2; RSSI o Responsabile della sicurezza IT per Livello 0.
- Periodo di revisione: 10 giorni lavorativi per completare.
- Mancata risposta: Promemoria al giorno 5; escalation al manager del revisore al giorno 8; accesso sospeso al giorno 15 in assenza di risposta.
- Le richieste di revoca vengono elaborate entro 48 ore.

### Processo di campagna di certificazione degli accessi

Le revisioni trimestrali degli accessi DEVONO seguire una campagna strutturata:

**Settimana 1 — Preparazione della campagna**:
- Generare il rapporto sugli account privilegiati, il rapporto sugli account di servizio e il rapporto sulle appartenenze ai gruppi dal provider di identità e dal PAM.
- Distribuire ai revisori: account di Livello 0 al RSSI; account di Livello 1/2 ai proprietari del sistema; account di servizio ai proprietari delle applicazioni.

**Settimane 2–3 — Periodo di revisione (10 giorni lavorativi)**:
- I revisori attestano ogni account: Approvare / Revocare / Trasferire / Impossibile determinare.
- Promemoria: Giorno 5 (automatico), Giorno 8 (escalation al manager del revisore), Giorno 10 (avviso finale — la mancata risposta viene trattata come diniego implicito, accesso sospeso).

**Settimana 4 — Rimedio**:
- IT Operations elabora le revoche entro 48 ore.
- Viene generato un rapporto di riepilogo con le azioni intraprese.

**Post-campagna**: I risultati vengono presentati al RSSI alla prossima revisione trimestrale. I registri di certificazione vengono conservati per 3 anni.

**Metriche della campagna**: Tasso di completamento della revisione (obiettivo: 100%); tempo medio di revisione (obiettivo: ≤5 giorni lavorativi); tasso di revoca (intervallo sano: 5–15%; i tassi al di fuori di questo intervallo giustificano un'indagine).

### Accesso d'emergenza / Break-glass

L'organizzazione DEVE mantenere procedure di accesso d'emergenza per le situazioni in cui i normali canali di autenticazione non sono disponibili:

- Account d'emergenza protetti con credenziali sigillate (cassaforte fisica o busta sigillata della soluzione PAM).
- Richiesta di autorizzazione multi-persona per l'uso dell'account d'emergenza (doppio controllo — due persone necessarie per accedere alle credenziali).
- Tutto l'utilizzo degli account d'emergenza viene registrato, avvisato e revisionato entro 24 ore.
- Le credenziali vengono ruotate immediatamente dopo l'uso.
- Gli account d'emergenza DEVONO essere testati semestralmente (ad es. gennaio e luglio) per confermare che le credenziali funzionino e le procedure siano aggiornate.
- I registri dei test DEVONO documentare data, tester, conferma dell'autenticazione riuscita e rotazione delle credenziali post-test.

---

## Restrizione degli accessi

### Principi di applicazione

L'accesso alle informazioni e ad altri asset correlati DEVE essere limitato in conformità con questa politica e la Politica di gestione delle identità e degli accessi:

- **Accesso negato per default**: L'accesso è negato per default; richiesta autorizzazione esplicita.
- **Controllo degli accessi basato sui ruoli (RBAC)**: Accesso basato su ruoli lavorativi documentati.
- **Controllo degli accessi basato sugli attributi (ABAC)**: Accesso context-aware (posizione, conformità del dispositivo, punteggio di rischio) laddove supportato dal provider di identità.
- **Allineamento con la classificazione dei dati**: Le restrizioni di accesso corrispondono al livello di classificazione delle informazioni.

### Controlli di accesso tecnici

**Accesso al sistema operativo**:

- Autorizzazioni del file system applicate per classificazione dei dati.
- Comandi privilegiati limitati agli amministratori autorizzati.
- Diritti di amministratore locale rimossi dagli utenti standard (escalation dei privilegi gestita per le eccezioni).

**Accesso ai database**:

- Accesso diretto ai database limitato ai DBA autorizzati.
- Accesso delle applicazioni tramite account di servizio con privilegi minimi.
- Colonne sensibili crittografate o mascherate per gli accessi non privilegiati.

**Accesso alle applicazioni**:

- Controllo degli accessi basato sui ruoli all'interno delle applicazioni.
- Le funzioni sensibili richiedono ulteriore autenticazione (AMF step-up) laddove supportato.

**Accesso API**:

- Autenticazione API obbligatoria (OAuth 2.0 o chiavi API con rotazione secondo la pianificazione di rotazione delle credenziali).
- Rate limiting applicato su tutte le API.
- Le API sensibili richiedono ulteriore autorizzazione.

**Accesso alle risorse cloud**:

- Le policy IAM cloud seguono il privilegio minimo.
- L'accesso cross-account è limitato, registrato e revisionato trimestralmente.
- Autorizzazioni a livello di risorsa applicate.

### Timeout delle sessioni

Le sessioni di sistema DEVONO applicare i seguenti periodi di timeout:

| Classificazione | Timeout di inattività | Timeout assoluto |
|----------------|----------------------|------------------|
| Sistemi Riservati / Critici | 15 minuti | 8 ore |
| Sistemi che trattano dati personali degni di particolare protezione | 5 minuti | 4 ore |
| Console di amministrazione privilegiata | 10 minuti | 4 ore |
| Sistemi aziendali standard | 30 minuti | 12 ore |

Il timeout assoluto richiede la ri-autenticazione indipendentemente dall'attività.

### Restrizioni di accesso basate sulla rete

- La segmentazione della rete DEVE separare le zone di fiducia per supportare la restrizione degli accessi (dettagliata nella Politica di sicurezza della rete).
- Le regole del firewall DEVONO applicare i confini di accesso tra i segmenti di rete.
- Il controllo degli accessi di rete (NAC) o equivalente DEVE verificare la conformità degli endpoint prima di concedere l'accesso ove fattibile.

### Mascheratura dei dati

L'organizzazione maschera i dati in conformità con gli obblighi legali e normativi, inclusi i requisiti della nLPD svizzera e del GDPR ove applicabile. La mascheratura dei dati DEVE essere applicata a:

- Dati personali visualizzati in ambienti non di produzione.
- Campi di dati sensibili visibili agli utenti senza un legittimo bisogno di accesso completo.
- Dati presentati in rapporti, dashboard o log dove i valori completi non sono necessari.

### Verifica dei controlli di accesso

L'organizzazione DEVE verificare i controlli di accesso attraverso:

- Test di penetrazione annuali che includono tentativi di elusione del controllo degli accessi.
- Audit trimestrali delle autorizzazioni per i sistemi critici e gli account privilegiati.
- Scansione automatica della conformità per la deriva della configurazione ove fattibile.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Direzione generale** | Approvare la politica; allocare il budget per l'infrastruttura di autenticazione, la distribuzione AMF e il PAM; revisione trimestrale delle metriche di sicurezza |
| **RSSI** | Responsabilità generale per la sicurezza dell'autenticazione e degli accessi; approvare la strategia PAM e il Modello di livelli amministrativi; approvare le eccezioni (rischio medio/alto); revisione dei rapporti trimestrali |
| **Responsabile della sicurezza IT** | Gestione quotidiana dell'infrastruttura di autenticazione; monitoraggio degli avvisi di autenticazione e accesso privilegiato; conduzione delle campagne trimestrali di certificazione degli accessi; approvazione delle richieste di account di servizio; approvazione delle eccezioni a basso rischio |
| **IT Operations / Team IAM** | Gestire il provider di identità e l'infrastruttura SSO; elaborare le richieste di accesso privilegiato e JIT; mantenere la registrazione AMF; eseguire provisioning e deprovisioning; generare rapporti di certificazione degli accessi; mantenere l'inventario degli account di servizio; gestire la distribuzione PAW |
| **Amministratori di sistema** | Implementare i controlli di accesso sui sistemi gestiti; conformarsi ai requisiti del Modello di livelli amministrativi; utilizzare account privilegiati dedicati; segnalare anomalie nei controlli di accesso |
| **Tutti gli utenti** | Proteggere le credenziali di autenticazione; segnalare immediatamente la sospetta compromissione delle credenziali; completare la registrazione AMF entro il periodo richiesto; non condividere account o credenziali; non tentare di aggirare i controlli di accesso |

---

## Indicatori chiave di prestazione

Le seguenti metriche DEVONO essere monitorate per misurare l'efficacia dei controlli di autenticazione e accesso privilegiato:

| Metrica | Obiettivo | Frequenza |
|---------|-----------|-----------|
| Registrazione AMF (tutti gli utenti) | ≥95% | Mensile |
| Registrazione AMF (utenti privilegiati) | 100% | Mensile |
| Completamento della revisione degli accessi privilegiati | 100% | Trimestrale |
| Conformità alla politica sulle password | ≥98% | Mensile |
| Integrazione SSO delle applicazioni | ≥80% (Anno 1); ≥90% (Anno 2) | Trimestrale |
| Registrazione delle sessioni privilegiate (Livello 0) | 100% | Mensile |
| Conformità alla rotazione delle credenziali (account di servizio) | 100% nei tempi previsti | Trimestrale |
| Completamento del test degli account d'emergenza | 100% | Semestrale |
| Adozione dell'accesso JIT (Livello 1) | ≥50% (Anno 1); ≥80% (Anno 2) | Trimestrale |
| Completezza dell'inventario degli account di servizio | 100% | Trimestrale |
| Tasso di completamento della certificazione degli accessi | 100% | Trimestrale |
| Copertura delle policy di accesso condizionale | 100% delle policy definite applicate | Trimestrale |
| Verifica delle credenziali compromesse | 100% degli eventi di impostazione/modifica convalidati | Mensile |

Le metriche DEVONO essere riportate al RSSI trimestralmente. Le metriche al di sotto degli obiettivi DEVONO includere un piano di rimedio con responsabile e data obiettivo.

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

| N. | Prova | Responsabile | Frequenza |
|----|-------|--------------|-----------|
| 1 | **Prove della configurazione della politica sulle password** (impostazioni del provider di identità, configurazione della verifica delle violazioni) | IT Operations | *Acquisito annualmente o in seguito a modifica* |
| 2 | **Rapporti di registrazione AMF** (percentuale di copertura per tipo di utente: privilegiato, standard, remoto) | Sicurezza IT | *Mensile per privilegiati; trimestrale per tutti gli utenti* |
| 3 | **Inventario delle integrazioni SSO** (integrata vs. non integrata, registrazioni delle eccezioni) | IT Operations | *Revisionato trimestralmente* |
| 4 | **Inventario degli account privilegiati** (account, proprietario, livello, scopo, data dell'ultima revisione) | Sicurezza IT | *Revisionato trimestralmente* |
| 5 | **Registrazioni del completamento della revisione degli accessi privilegiati** (attestazione, revisore, data, azioni intraprese) | Sicurezza IT | *Trimestrale; conservate 3 anni* |
| 6 | **Campioni di registrazione delle sessioni** (sessioni di Livello 0; campione casuale revisionato per anomalie) | Sicurezza IT | *Revisionato trimestralmente* |
| 7 | **Registrazioni del test degli account d'emergenza** (data, tester, risultato, conferma della rotazione post-test) | Sicurezza IT | *Semestrale* |
| 8 | **Log di rotazione delle credenziali** (account di servizio, account d'emergenza, account condivisi) | IT Operations | *Per evento di rotazione; verificato semestralmente* |
| 9 | **Log degli eventi di autenticazione** (accessi riusciti/falliti, blocchi, indagini sulle anomalie) | Sicurezza IT | *Conservati 12 mesi; anomalie investigate entro 24 ore* |
| 10 | **Rapporti di test di penetrazione e audit delle autorizzazioni** (risultati dei controlli di accesso e stato del rimedio) | Sicurezza IT | *Test di penetrazione annuale; audit delle autorizzazioni trimestrale* |
| 11 | **Inventario degli account di servizio** (nome account, proprietario, livello, scopo, posizione delle credenziali, ultima/prossima rotazione) | Sicurezza IT | *Mantenuto continuamente; revisionato trimestralmente; conservato 3 anni* |
| 12 | **Log degli accessi JIT** (richieste, approvazioni, durata, conferma di revoca automatica) | Sicurezza IT | *Per evento; verificato trimestralmente; conservato 12 mesi* |
| 13 | **Registrazioni della campagna di certificazione degli accessi** (risultati della campagna, attestazioni dei revisori, revoche elaborate) | Sicurezza IT | *Trimestrale; conservate 3 anni* |
| 14 | **Documentazione della policy di accesso condizionale** (definizioni delle policy, stato di distribuzione, eccezioni) | IT Operations | *Revisionata trimestralmente; aggiornata in seguito a modifiche delle policy* |
| 15 | **Stato di distribuzione PAW** (inventario delle PAW, conformità della configurazione, monitoraggio della fase di distribuzione) | Sicurezza IT | *Revisionato trimestralmente; conservato 3 anni* |
| 16 | **Inventario delle integrazioni SSO** (applicazioni, stato SSO, livello di priorità, registrazioni delle eccezioni) | IT Operations | *Revisionato trimestralmente; conservato 3 anni* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, audit della configurazione del provider di identità, rapporti sulla copertura AMF, revisioni degli accessi privilegiati, test di penetrazione, audit interni ed esterni e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita. Le eccezioni devono essere riportate al team di revisione della direzione. Durata massima dell'eccezione: 12 mesi, rinnovabile con nuova approvazione.

## Non conformità

Un dipendente che risulti aver violato questa politica può essere soggetto ad azioni disciplinari, fino al licenziamento.

**Risposta progressiva** (nell'arco di 12 mesi continuativi):

| Occorrenza | Risposta | Tempistica | Responsabile |
|------------|----------|------------|--------------|
| Prima | Promemoria sulla consapevolezza e formazione mirata | Entro 5 giorni lavorativi | Sicurezza IT |
| Seconda (entro 90 giorni) | Notifica al manager + avvertimento documentato | Entro 3 giorni lavorativi | Sicurezza IT + HR |
| Terza (entro 12 mesi) | Restrizione dell'accesso in attesa di rimedio | Immediata | Sicurezza IT + Manager |
| Violazione intenzionale / critica | Azione disciplinare secondo le politiche HR | Escalation immediata | HR + RSSI |

**Violazioni critiche** che giustificano l'escalation immediata indipendentemente dalla cronologia precedente:

- Condivisione delle credenziali privilegiate.
- Aggiramento deliberato dei controlli di sicurezza.
- Violazioni dell'isolamento dei livelli.
- Utilizzo non autorizzato degli account d'emergenza.

**Fallimenti della simulazione di phishing** (nell'arco di 12 mesi continuativi):

- 1 fallimento: Formazione mirata sulla consapevolezza (entro 7 giorni).
- 2 fallimenti: Notifica al manager + formazione aggiuntiva (entro 5 giorni).
- 3+ fallimenti: Accesso privilegiato sospeso; accesso standard limitato fino a dimostrato miglioramento.

## Miglioramento continuo

Questa politica viene rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti agli standard di autenticazione (incluse le revisioni di NIST SP 800-63B), le minacce emergenti (credential stuffing, phishing, tecniche di elusione dell'AMF), i cambiamenti normativi e le lessons learned dagli incidenti.

---

# Aree dello standard ISO 27001 trattate

Politica di autenticazione e accesso privilegiato — Mapping dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.15 Controllo degli accessi |
| Clausola 7.3 Consapevolezza | 5.17 Informazioni di autenticazione |
| Clausola 7.5.3 Controllo delle informazioni documentate | 5.36 Conformità a politiche, regole e standard |
| | 6.3 Sensibilizzazione, educazione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | **8.2 Diritti di accesso privilegiato** |
| | **8.3 Restrizione dell'accesso alle informazioni** |
| | **8.5 Autenticazione sicura** |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|-----------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative inclusi i controlli di autenticazione e accesso |
| OPDo svizzero | Art. 1-3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (se applicabile) | Art. 32 — Sicurezza del trattamento (controlli di autenticazione come misura appropriata) |
| ISO/IEC 27001:2022 | Annex A Controlli 8.2, 8.3, 8.5 |
| ISO/IEC 27002:2022 | Sezioni 8.2, 8.3, 8.5 — Indicazioni di implementazione |
| NIST SP 800-63B | Linee guida per l'identità digitale e l'autenticazione (segreti memorizzati, AMF) |
| NIST CSF 2.0 | PR.AA (Identity Management, Authentication, and Access Control) |
| CIS Controls v8 | Controllo 5 (Account Management), Controllo 6 (Access Control Management) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
