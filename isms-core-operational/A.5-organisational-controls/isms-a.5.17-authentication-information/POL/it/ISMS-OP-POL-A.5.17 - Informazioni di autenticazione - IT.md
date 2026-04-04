<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.17-IT:operational:OP-POL:a.5.17 -->
**ISMS-OP-POL-A.5.17 — Informazioni di autenticazione**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Informazioni di autenticazione |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.5.17 |
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

- Controllo ISO/IEC 27001:2022 A.5.17 — Informazioni di autenticazione
- NIST SP 800-63B-4 — Linee guida per l'identità digitale: autenticazione e gestione degli autenticatori

**Controlli Annex A correlati**:

| Controllo | Relazione con le informazioni di autenticazione |
|-----------|--------------------------------------------------|
| A.5.15–18 Controllo degli accessi e gestione delle identità | Il ciclo di vita delle identità alimenta l'autenticazione; i diritti di accesso determinano l'ambito delle credenziali |
| A.5.24–28 Gestione degli incidenti | La compromissione delle credenziali attiva la risposta agli incidenti e il cambio forzato della password |
| A.8.2 Diritti di accesso privilegiato | Gli account privilegiati richiedono un'autenticazione più rigorosa (AMF, chiavi hardware) |
| A.8.3 Restrizione dell'accesso alle informazioni | L'autenticazione applica i limiti di accesso |
| A.8.5 Autenticazione sicura | Implementazione del meccanismo tecnico di autenticazione |
| A.8.15 Logging | Gli eventi di autenticazione alimentano il logging centralizzato |
| A.8.16 Attività di monitoraggio | Monitoraggio in tempo reale dei fallimenti di autenticazione e delle anomalie |
| A.8.24 Uso della crittografia | Protezione crittografica di credenziali, token e hash delle password |

**Policy interne correlate**:

- Policy di gestione delle identità e degli accessi
- Policy di autenticazione e accesso privilegiato
- Policy sull'uso della crittografia
- Policy di logging
- Policy sulle attività di monitoraggio (A.8.16)
- Policy di gestione degli incidenti

---

# Policy sulle informazioni di autenticazione

## Scopo

Lo scopo di questa policy è garantire che le informazioni di autenticazione siano allocate, gestite, protette e revocate in modo sicuro attraverso processi di ciclo di vita definiti, e che il personale sia istruito sulla gestione sicura delle credenziali di autenticazione.

Questa policy stabilisce i requisiti per gli standard sulle password, l'autenticazione a più fattori, la distribuzione delle credenziali e la protezione dei segreti di autenticazione, al fine di prevenire l'accesso non autorizzato ai sistemi e ai dati dell'organizzazione.

Questa policy supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative proporzionate al rischio per proteggere i dati personali (inclusi i dati personali degni di particolare protezione) attraverso i controlli di autenticazione. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR.

## Ambito di applicazione

Questa policy si applica a:

- Tutti i dipendenti, i collaboratori e gli utenti terzi con accesso ai sistemi dell'organizzazione.
- Tutte le informazioni di autenticazione incluse password, passphrase, PIN, chiavi crittografiche, token, template biometrici, chiavi API, certificati e altri segreti di autenticazione.
- Tutti i sistemi, le applicazioni, i servizi cloud, i dispositivi di rete e i database di proprietà o gestiti dall'organizzazione e inclusi nell'ambito della dichiarazione di scopo ISO 27001.
- Tutti i processi del ciclo di vita dell'autenticazione: allocazione, distribuzione, utilizzo, archiviazione, reset e revoca.

## Principio

Le informazioni di autenticazione DEVONO essere gestite secondo i principi di riservatezza, responsabilità individuale e difesa in profondità. Ogni utente DEVE essere positivamente identificato e autenticato prima di accedere a sistemi o dati. I meccanismi di autenticazione DEVONO essere commisurati alla sensibilità delle informazioni e dei sistemi a cui si accede.

Le sole password non sono sufficienti per gli accessi ad alto rischio. L'autenticazione a più fattori fornisce una protezione a strati contro la compromissione delle credenziali. I controlli di autenticazione DEVONO essere basati sul rischio, tenendo conto della classificazione delle informazioni e della criticità del sistema.

---

## Infrastruttura di autenticazione

> **Specifica dei sistemi**: L'organizzazione utilizza i seguenti sistemi per implementare i controlli di autenticazione. I riferimenti segnaposto (ad es. [Provider di identità]) nel presente documento si riferiscono ai sistemi elencati di seguito.
>
> | Funzione | Sistema/Strumento | Proprietario |
> |----------|-------------------|--------------|
> | **Provider di identità (IdP)** | [es. Microsoft Entra ID, Okta, Google Workspace Identity] | Operazioni IT / Team IAM |
> | **Gestore di password** | [es. 1Password Business, Bitwarden Enterprise, KeePass + sync centralizzato] | Sicurezza IT |
> | **Piattaforma AMF** | [es. AMF integrata nell'IdP, Duo Security, gestione YubiKey] | Operazioni IT |
> | **Gestione degli accessi privilegiati (PAM)** | [es. CyberArk, Delinea Secret Server, HashiCorp Vault] | Sicurezza IT |
> | **Servizio di verifica violazioni** | [es. Have I Been Pwned API (modello k-anonimato), Enzoic, Microsoft Password Protection] | Operazioni IT |
> | **SIEM / Gestione log** | [es. Microsoft Sentinel, Splunk, Elastic SIEM] | Sicurezza IT |

---

## Allocazione delle informazioni di autenticazione

### Verifica dell'identità

Prima di emettere credenziali di autenticazione nuove o sostitutive, l'identità del richiedente DEVE essere verificata tramite almeno uno dei seguenti metodi:

- Verifica di un contatto secondario pre-registrato (email, numero di cellulare).
- Verifica di persona con documento di identità con foto.
- Conferma dell'identità dell'utente da parte del responsabile o delle Risorse umane.
- Processo self-service verificato con AMF tramite il provider di identità [Provider di identità].

Il metodo di verifica utilizzato DEVE essere documentato a fini di audit.

### Distribuzione sicura

Le informazioni di autenticazione DEVONO essere distribuite attraverso canali sicuri. I metodi non sicuri quali email non cifrate o messaggistica in testo normale NON devono essere utilizzati per la distribuzione delle credenziali.

| Tipo di autenticazione | Metodo di distribuzione |
|------------------------|-------------------------|
| **Password iniziali** | Canale sicuro (email cifrata, busta sigillata o auto-registrazione tramite provider di identità); separato dal nome utente; cambio forzato al primo utilizzo |
| **Token / chiavi hardware** | Consegna di persona con verifica dell'identità e ricevuta firmata |
| **Certificati** | Processo di iscrizione sicuro ai certificati; email verificata o flusso di lavoro tramite provider di identità |
| **Chiavi API** | Canale cifrato; periodo di validità limitato; emissione registrata; archiviate nel vault dei segreti |

### Autenticazione temporanea

Le credenziali di autenticazione temporanee (password iniziali, token di reset, codici monouso):

- DEVONO avere una validità massima di 24 ore.
- DEVONO richiedere il cambio al primo utilizzo.
- DEVONO essere generate con sufficiente casualità e lunghezza per resistere ai tentativi di indovinazione.
- DEVONO essere invalidate dopo l'utilizzo con successo.

### Gestione delle credenziali predefinite

Le password fornite dal fornitore e quelle predefinite DEVONO essere cambiate immediatamente dopo l'installazione, prima che qualsiasi sistema venga collegato alla rete di produzione.

Gli account predefiniti DEVONO essere disabilitati o rinominati ove tecnicamente fattibile.

Laddove le credenziali predefinite non possano essere cambiate (dipendenza da firmware del fornitore, limitazione del sistema), si DEVONO applicare i seguenti controlli compensativi:

- Password robusta univoca impostata per ogni dispositivo (non quella predefinita del fornitore).
- Segmentazione di rete che limita l'accesso al dispositivo.
- AMF applicata ove supportata.
- Monitoraggio e alerting potenziati sull'account.
- Credenziale archiviata nel vault approvato [Gestore di password].
- Eccezione documentata con approvazione del RSSI e revisione annuale.

---

## Requisiti sulle password

### Standard sulle password (allineati a NIST SP 800-63B)

L'organizzazione DEVE applicare i seguenti standard sulle password, allineati a NIST SP 800-63B-4:

| Requisito | Standard |
|-----------|----------|
| **Lunghezza minima** | 12 caratteri (15 caratteri laddove la password sia l'unico fattore di autenticazione senza AMF) |
| **Lunghezza massima** | I sistemi DEVONO accettare almeno 64 caratteri per supportare le passphrase |
| **Supporto caratteri** | DEVONO essere accettati tutti i caratteri ASCII stampabili (incluso lo spazio) e Unicode |
| **Regole di complessità** | Nessuna regola di composizione obbligatoria (nessun mix richiesto di maiuscole, minuscole, numeri, simboli); la lunghezza è il fattore principale di robustezza |
| **Verifica violazioni** | Le password DEVONO essere validate rispetto a database di credenziali compromesse/violate note (ad es. Have I Been Pwned API, o corpus di violazioni equivalente integrato in [Provider di identità]) alla creazione e periodicamente. **Frequenza di verifica**: Alla creazione della password (obbligatoria), ad ogni autenticazione ove tecnicamente fattibile (verifica in tempo reale tramite integrazione IdP), e verifica batch di tutti gli hash delle password archiviati trimestralmente (verifica offline rispetto a corpus di violazioni aggiornato). |
| **Rotazione** | Solo basata su eventi — in caso di sospetta o confermata compromissione, scoperta di credenziale condivisa o cambio di ruolo del personale che influisce sull'ambito di accesso; la rotazione periodica forzata non è richiesta |
| **Password iniziali** | DEVONO essere cambiate al primo utilizzo |
| **Password predefinite** | Password fornite dal fornitore e predefinite cambiate immediatamente dopo l'installazione |
| **Riutilizzo** | DEVE essere mantenuta una cronologia di almeno 24 password precedenti per prevenire il riutilizzo |
| **Condivisione** | Le password NON devono essere generiche, condivise o impostate a livello di gruppo |
| **Blocco** | I sistemi DEVONO bloccare gli utenti dopo 6 tentativi di accesso falliti; durata del blocco minimo 15 minuti o fino a reset manuale |
| **Gestori di password** | È raccomandato e supportato l'utilizzo di gestori di password approvati dall'organizzazione [Gestore di password]; i sistemi DEVONO consentire l'incolla nei campi password |

**Standard sulle password per gli account privilegiati**:

Gli account privilegiati (amministratore, account Tier 0/1) DEVONO applicare:

- Minimo 16 caratteri (o 24 caratteri per gli account di servizio).
- Blocco dopo 3 tentativi falliti.
- Verifica violazioni alla creazione e ad ogni autenticazione ove tecnicamente fattibile.
- Archiviazione nel vault delle credenziali approvato [Gestore di password].

**Motivazione della rotazione basata su eventi**: NIST SP 800-63B-4 stabilisce che la rotazione periodica obbligatoria delle password porta a password più deboli (schemi prevedibili, modifiche incrementali minime) senza benefici misurabili per la sicurezza. La rotazione basata su eventi combinata con la verifica delle violazioni e l'AMF fornisce una protezione più robusta.

### Pratiche vietate sulle password

Il personale NON deve:

- Condividere le password con altre persone, incluso il personale di supporto IT.
- Scrivere le password in luoghi non protetti (post-it, file non cifrati, taccuini).
- Archiviare le password in file di testo normale, documenti, fogli di calcolo o nel salvataggio automatico del browser senza un gestore di password approvato.
- Utilizzare la stessa password su più sistemi o servizi.
- Includere password in script, codice, macro o file di configurazione.
- Trasmettere password tramite canali non cifrati (corpo dell'email, messaggistica istantanea, SMS).

### Archiviazione delle password

I sistemi DEVONO archiviare le password utilizzando hashing crittografico unidirezionale approvato con salt univoco per ogni password:

- **Algoritmi approvati**: bcrypt, Argon2id, scrypt o PBKDF2 (con conteggio di iterazioni appropriato alla capacità hardware attuale).
- **L'archiviazione in chiaro è vietata** in tutte le circostanze.
- **La cifratura reversibile delle password è vietata.**
- I database delle password DEVONO essere protetti con cifratura a riposo e l'accesso DEVE essere limitato agli account di servizio autorizzati.

---

## Autenticazione a più fattori

### Requisiti AMF

L'autenticazione a più fattori DEVE essere richiesta per i seguenti tipi di accesso:

| Tipo di accesso | Requisito AMF |
|----------------|---------------|
| **Accesso remoto** (VPN, servizi cloud, applicazioni accessibili esternamente) | Obbligatoria |
| **Account privilegiati / di amministratore** | Obbligatoria |
| **Sistemi critici e infrastrutture** | Obbligatoria |
| **Sistemi che trattano dati personali** (ambito nLPD / GDPR) | Obbligatoria |
| **Email** (accesso esterno) | Obbligatoria |
| **Console amministrative della piattaforma cloud** | Obbligatoria |
| **Accesso interno standard** (in sede, rete fidata) | Basato sul rischio; implementazione determinata dalla classificazione del sistema e registrata nella policy di accesso condizionale di [Provider di identità] |

**Obiettivi di copertura AMF**:

- Utenti privilegiati: 100% di iscrizione AMF dalla data di entrata in vigore della policy.
- Tutti gli utenti (accesso remoto): 100% di applicazione AMF.
- Tutti gli utenti (tutti gli accessi): iscrizione AMF >=95% entro 12 mesi dall'adozione della policy.

### Tipi di fattori AMF

I fattori di autenticazione accettabili DEVONO essere scelti da almeno due categorie diverse:

| Categoria del fattore | Esempi | Note |
|-----------------------|--------|------|
| **Qualcosa che conosci** | Password, passphrase, PIN | Ai sensi degli standard sulle password sopra |
| **Qualcosa che possiedi** | Chiave di sicurezza hardware (FIDO2/WebAuthn), app di autenticazione (TOTP), smart card | Registrata all'utente individuale; chiavi hardware preferite per l'accesso privilegiato |
| **Qualcosa che sei** | Impronta digitale, riconoscimento facciale, scansione dell'iride | Template biometrico archiviato in modo sicuro; utilizzato come fattore di sblocco locale |

### Preferenza del metodo AMF

I metodi AMF DEVONO essere selezionati con preferenza per la resistenza al phishing:

| Metodo | Resistenza al phishing | Utilizzo raccomandato |
|--------|------------------------|----------------------|
| **Chiavi di sicurezza hardware** (FIDO2/WebAuthn) | Alta — legata crittograficamente all'origine | Richiesta per gli account con i privilegi più elevati; raccomandata per tutti gli utenti |
| **Passkey** (legate al dispositivo, non esportabili) | Alta — legate all'origine, verificate dall'utente | Accettabili per tutti i tipi di accesso; preferite rispetto al TOTP |
| **App di autenticazione** (TOTP) | Media — i codici possono essere oggetto di phishing in tempo reale | Accettabili per l'accesso standard e a privilegi moderati |
| **Notifiche push** (con abbinamento di numeri) | Media — richiede l'abbinamento di numeri per mitigare gli attacchi di fatigue | Accettabili dove l'abbinamento di numeri è applicato |
| **OTP via SMS / chiamata vocale** | Bassa — vulnerabile al SIM swapping e all'intercettazione | Solo dove nessun altro metodo è tecnicamente fattibile; eccezione documentata richiesta |

L'OTP via SMS DEVE essere documentata nel registro dei rischi con un piano di migrazione verso un metodo più robusto. I nuovi sistemi implementati NON devono implementare l'AMF basata su SMS come unico secondo fattore.

**Roadmap di migrazione all'autenticazione resistente al phishing**:

L'organizzazione DEVE pianificare ed eseguire la migrazione verso l'autenticazione resistente al phishing (FIDO2/WebAuthn passkey) come metodo AMF principale. FIDO2 utilizza la crittografia a chiave pubblica legata all'origine del servizio legittimo, impedendo il credential phishing anche se gli utenti vengono ingannati da siti fraudolenti.

| Fase | Tempistica | Ambito | Obiettivo |
|------|-----------|--------|-----------|
| **Fase 1 — Pilota** | Mesi 1-3 | Team IT, team sicurezza, RSSI | 100% del gruppo pilota con chiavi hardware FIDO2 |
| **Fase 2 — Utenti privilegiati** | Mesi 3-6 | Tutti gli account privilegiati/admin, dirigenti | 100% degli account privilegiati su FIDO2/passkey |
| **Fase 3 — Utenti ad alto rischio** | Mesi 6-12 | Utenti con accesso a dati Riservati, lavoratori remoti | >=80% degli utenti ad alto rischio migrati |
| **Fase 4 — Rollout generale** | Mesi 12-24 | Tutti gli utenti | >=90% di tutti gli utenti con AMF resistente al phishing; AMF via SMS/voce eliminata |

**Tracciamento della migrazione**: Avanzamento segnalato trimestralmente al RSSI con: utenti migrati (numero e %), utenti ancora su SMS/TOTP, blocchi (sistemi legacy, resistenza degli utenti), stato dell'inventario delle chiavi hardware.

### Processo di recupero AMF

Laddove un utente perda l'accesso al proprio dispositivo AMF (telefono perso, chiave hardware rotta, ripristino delle impostazioni di fabbrica):

1. **Contatto helpdesk**: L'utente contatta l'Helpdesk IT con verifica dell'identità (stessa procedura del reset assistito dell'helpdesk).
2. **Accesso temporaneo**: L'helpdesk emette un codice di bypass a tempo limitato (validità massima 24 ore, monouso) per consentire l'accesso immediato durante la ri-iscrizione AMF.
3. **Ri-iscrizione AMF**: L'utente si ri-iscrive all'AMF entro 24 ore tramite il portale self-service di [Provider di identità]. Se la ri-iscrizione non viene completata entro 24 ore, l'accesso viene sospeso fino al completamento dell'iscrizione.
4. **Chiave hardware persa**: Segnalata come incidente di sicurezza (possibile compromissione fisica). La chiave precedente viene immediatamente deregistrata. La chiave sostitutiva viene emessa con consegna di persona e verifica dell'identità.
5. **Metodo AMF di backup**: Gli utenti sono incoraggiati a registrare un metodo AMF di backup (ad es. seconda chiave hardware conservata in modo sicuro, app di autenticazione di backup). Gli utenti privilegiati DEVONO registrare almeno due metodi AMF indipendenti.
6. **Logging**: Tutti gli eventi di recupero AMF vengono registrati in [SIEM] con utente, timestamp, metodo di verifica e metodo di recupero utilizzato. I modelli anomali (ad es. lo stesso utente che recupera l'AMF più volte) vengono esaminati entro 24 ore.

### Requisiti per l'autenticazione biometrica

Laddove venga utilizzata l'autenticazione biometrica (impronta digitale, riconoscimento facciale, scansione dell'iride):

- **Archiviazione dei template**: I template biometrici DEVONO essere archiviati localmente sul dispositivo (non centralizzati) ove tecnicamente fattibile. Se è richiesta l'archiviazione centralizzata, i template DEVONO essere cifrati a riposo con AES-256.
- **Rilevamento della vivacità**: I sistemi biometrici DEVONO implementare il rilevamento della vivacità per prevenire attacchi replay (ad es. fotografie, impronte digitali in silicone).
- **Fallback**: DEVE essere sempre disponibile un metodo di autenticazione di fallback non biometrico (la biometria non deve essere l'unico fattore di autenticazione).
- **Consenso**: Il personale DEVE fornire il consenso informato prima dell'iscrizione biometrica, in conformità con i requisiti della nLPD svizzera per il trattamento di dati personali degni di particolare protezione.
- **Revoca**: I template biometrici DEVONO essere cancellati alla cessazione del rapporto di lavoro o quando l'individuo ritira il consenso.
- **Precisione**: I sistemi biometrici DEVONO essere configurati con un tasso di falsa accettazione (FAR) appropriato al livello di rischio (raccomandato: FAR <= 1:50.000 per l'accesso standard, FAR <= 1:1.000.000 per l'accesso privilegiato).

### Sistemi non in grado di supportare l'AMF

I sistemi che non possono supportare l'AMF DEVONO essere documentati nel registro dei rischi con:

- Motivazione tecnica della limitazione.
- Controlli compensativi (segmentazione di rete, restrizione IP, monitoraggio potenziato, timeout di sessione ridotto).
- Accettazione del rischio approvata dal RSSI.
- Revisione annuale e piano di migrazione ove fattibile.

---

## Protezione delle informazioni di autenticazione

### Responsabilità degli utenti

Tutto il personale DEVE:

- Mantenere riservate le informazioni di autenticazione e non divulgarle ad altre persone.
- Utilizzare password o passphrase robuste e univoche per ogni sistema.
- Utilizzare il gestore di password approvato dall'organizzazione [Gestore di password] per l'archiviazione sicura delle credenziali.
- Segnalare immediatamente al service desk IT e al team di sicurezza la sospetta o confermata compromissione delle credenziali.

### Risposta alla compromissione delle credenziali

Quando la compromissione delle credenziali è sospetta o confermata:

1. **Reset immediato della password**: L'utente interessato reimposta la password tramite il processo self-service di [Provider di identità] (verificato con AMF) o tramite procedura assistita dall'helpdesk. Per gli account privilegiati: la Sicurezza IT impone il reset immediato della password.
2. **Verifica AMF**: Verificare che i fattori AMF non siano stati manomessi (nessun dispositivo non autorizzato registrato). In caso di dispositivi AMF sospetti, rimuovere tutte le registrazioni AMF e ri-iscriversi da un dispositivo fidato.
3. **Terminazione delle sessioni**: Tutte le sessioni attive per l'account interessato vengono terminate immediatamente tramite la console di amministrazione di [Provider di identità].
4. **Valutazione dell'ambito della violazione**: La Sicurezza IT indaga: A cosa si è acceduto con le credenziali compromesse? Sono stati interessati altri account (riutilizzo delle credenziali)? Sono stati esfiltrati dati?
5. **Verifica violazioni**: Verificare l'hash della password compromessa rispetto al corpus di violazioni. Se trovato in un database di violazioni esterno, valutare l'ambito dell'esposizione.
6. **Notifica**: Se la compromissione ha comportato l'accesso a dati personali, valutare gli obblighi di notifica della violazione ai sensi di A.5.24-28 Gestione degli incidenti e della legge applicabile sulla protezione dei dati.
7. **Causa profonda**: Determinare come le credenziali sono state compromesse (phishing, malware, social engineering, forza bruta, violazione di un servizio esterno). Implementare la remediation mirata (ad es. formazione di sensibilizzazione sul phishing se il phishing era il vettore).
8. **Documentazione**: Incidente registrato in [Sistema ITSM] con: account interessato, vettore di compromissione, ambito di accesso durante la finestra di compromissione, azioni di remediation, causa profonda, misure preventive.
- Non consentire ad altri di utilizzare le proprie credenziali o autenticarsi al proprio posto.
- Completare l'iscrizione AMF entro il termine richiesto.
- Non tentare di aggirare i controlli di autenticazione.

### Requisiti di sistema

Il sistema principale di autenticazione degli accessi DEVE:

- Non visualizzare identificatori di sistema o applicazione fino al completamento con successo del processo di accesso.
- Visualizzare un avviso generale che il sistema deve essere utilizzato solo da utenti autorizzati.
- Non fornire messaggi di aiuto durante la procedura di accesso che possano assistere un utente non autorizzato.
- Validare le informazioni di accesso solo al completamento di tutti i dati inseriti; in caso di errore, il sistema NON deve indicare quale parte dei dati sia corretta o errata.
- Proteggere da tentativi di accesso a forza bruta (limitazione del rate, ritardo progressivo, CAPTCHA o blocco dell'account).
- Registrare tutti i tentativi di autenticazione riusciti e falliti.
- Generare un evento di sicurezza se viene rilevato un possibile tentativo di violazione o una violazione dei controlli di accesso.
- Non visualizzare una password durante l'inserimento (mascherare l'input).
- Non trasmettere password in chiaro sulla rete.
- Terminare le sessioni inattive dopo un periodo definito di inattività.
- Limitare i tempi di connessione per fornire sicurezza aggiuntiva alle applicazioni ad alto rischio.

**Requisiti di timeout di sessione**:

| Classificazione del sistema | Timeout di inattività | Timeout assoluto |
|-----------------------------|----------------------|-----------------|
| Sistemi riservati / critici | 15 minuti | 8 ore |
| Sistemi che trattano dati personali sensibili | 5 minuti | 4 ore |
| Console di amministrazione privilegiata | 10 minuti | 4 ore |
| Sistemi aziendali standard | 30 minuti | 12 ore |

Il timeout assoluto richiede la ri-autenticazione indipendentemente dall'attività.

### Informazioni di autenticazione condivise

Le informazioni di autenticazione condivise sono sconsigliabili e DEVONO essere evitate ove possibile. Laddove siano necessarie credenziali condivise (sistemi legacy, account richiesti dal fornitore):

- L'approvazione del RSSI è obbligatoria con motivazione aziendale documentata.
- Le credenziali DEVONO essere archiviate nel vault delle credenziali approvato [Gestore di password], non in documenti di testo normale, email o chat.
- DEVE essere assegnato un custode nominato per ogni credenziale condivisa.
- DEVE essere mantenuto un log di check-out con identificazione dell'utente e timestamp.
- Per gli account condivisi privilegiati è raccomandata la registrazione delle sessioni ove tecnicamente fattibile.
- La responsabilità individuale DEVE essere mantenuta attraverso il logging di audit.
- L'accesso e l'utilizzo DEVONO essere rivisti trimestralmente; è richiesta la ri-autorizzazione annuale.
- Gli account condivisi DEVONO essere inclusi nel registro degli account privilegiati e nel processo di revisione degli accessi.

---

## Reset e recupero della password

### Reset della password self-service

Laddove sia implementato il reset della password self-service tramite [Provider di identità]:

- La verifica basata su AMF (push tramite app, FIDO2 o token hardware) DEVE essere richiesta prima che sia consentito un reset della password.
- Le domande di sicurezza basate sulla conoscenza NON devono essere utilizzate come unico metodo di verifica a causa della loro suscettibilità al social engineering.
- I token di reset DEVONO essere a tempo limitato (validità massima 1 ora) e monouso.
- Tutte le attività di reset DEVONO essere registrate, incluso il metodo di verifica utilizzato.
- L'utente DEVE essere notificato del cambio password tramite un contatto secondario registrato (email o cellulare).
- Il processo di reset NON deve rivelare se esiste un account (per prevenire l'enumerazione degli account).

### Reset della password assistito dall'helpdesk

I reset della password assistiti dall'helpdesk DEVONO seguire questa procedura:

1. **Verifica dell'identità**: L'helpdesk DEVE verificare l'identità del chiamante utilizzando almeno un metodo di verifica pre-registrato (email secondaria, numero di cellulare registrato, conferma del responsabile o verifica di persona con documento di identità con foto).
2. **Generare una password temporanea**: DEVE essere generata una password temporanea casuale che soddisfi i requisiti minimi di lunghezza.
3. **Comunicare in modo sicuro**: La password temporanea DEVE essere comunicata tramite un canale sicuro (non email non cifrata); ove possibile, utilizzare il link di reset sicuro del provider di identità.
4. **Forzare il cambio**: La password temporanea DEVE scadere al primo utilizzo, richiedendo all'utente di impostare immediatamente una nuova password.
5. **Documentare**: La richiesta di reset, il metodo di verifica utilizzato e il timestamp DEVONO essere registrati nel sistema di gestione dei servizi IT.

Il personale dell'helpdesk NON deve avere accesso per visualizzare le password degli utenti dopo l'emissione.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Direzione generale** | Approvare la policy; allocare il budget per l'infrastruttura di autenticazione (AMF, gestore di password, provider di identità); rivedere le metriche di sicurezza trimestralmente |
| **RSSI** | Titolarità e responsabilità della policy; approvare la strategia AMF e la roadmap di autenticazione resistente al phishing; approvare le eccezioni (rischio medio/alto); rivedere i rapporti di conformità trimestrali |
| **IT Security Manager** | Gestione quotidiana della sicurezza dell'autenticazione; monitoraggio degli avvisi e delle anomalie di autenticazione; condurre revisioni trimestrali della copertura AMF; approvare le eccezioni a basso rischio |
| **Operazioni IT / Team IAM** | Gestire il [Provider di identità] e l'infrastruttura di autenticazione; elaborare l'emissione e i reset delle credenziali; mantenere l'iscrizione AMF; configurare le impostazioni della policy sulle password; integrare la verifica delle violazioni |
| **Helpdesk** | Eseguire i reset delle password assistiti dall'helpdesk secondo la procedura documentata; verificare l'identità dell'utente prima dei cambi di credenziali; escalare le richieste di reset sospette alla Sicurezza IT |
| **Proprietari di sistema** | Garantire che i sistemi di propria competenza rispettino i requisiti di autenticazione; implementare l'AMF dove richiesto; segnalare le lacune nei controlli di autenticazione |
| **Tutto il personale** | Proteggere le credenziali di autenticazione; completare l'iscrizione AMF entro il termine richiesto; segnalare immediatamente la sospetta compromissione delle credenziali; non condividere account o credenziali; rispettare gli standard sulle password |

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa policy:

| # | Evidenza | Proprietario | Frequenza |
|---|---------|--------------|-----------|
| 1 | **Evidenza di configurazione della policy sulle password** (impostazioni di [Provider di identità]: lunghezza minima, verifica violazioni, blocco, cronologia) | Operazioni IT | Acquisita annualmente e in caso di modifica |
| 2 | **Rapporti di iscrizione AMF** (percentuale di copertura per tipo di utente: privilegiato, standard, remoto) | Sicurezza IT | Mensile per i privilegiati; trimestrale per tutti gli utenti |
| 3 | **Distribuzione dei metodi AMF** (FIDO2, TOTP, push, SMS — avanzamento della migrazione verso metodi resistenti al phishing) | Sicurezza IT | Trimestrale |
| 4 | **Evidenza di configurazione della verifica violazioni** (integrazione con database di credenziali compromesse, frequenza di verifica) | Operazioni IT | Annualmente e in caso di modifica |
| 5 | **Risultati della scansione delle credenziali predefinite** (nessuna credenziale predefinita o del fornitore in produzione) | Sicurezza IT | Trimestrale |
| 6 | **Log degli eventi di autenticazione** (login riusciti/falliti, blocchi, indagini su anomalie, avvisi di spostamento impossibile) | Sicurezza IT | Conservati 12 mesi; anomalie esaminate entro 24 ore |

**Esempi di anomalie di autenticazione** (indicatori che attivano l'indagine):

| Tipo di anomalia | Metodo di rilevamento | Risposta |
|-----------------|----------------------|----------|
| **Spostamento impossibile** | Login da due luoghi geograficamente distanti in un tempo di spostamento impossibile | Blocco della seconda sessione; notifica all'utente; indagine |
| **Forza bruta** | > 10 tentativi di login falliti in 5 minuti dalla stessa sorgente | Blocco dell'IP sorgente; notifica alla Sicurezza IT |
| **Credential stuffing** | Più account bersaglio con login falliti dallo stesso intervallo IP | Blocco dell'intervallo IP; revisione degli account interessati; notifica alla Sicurezza IT |
| **AMF fatigue** | > 3 notifiche push AMF rifiutate in 10 minuti | Blocco dell'account; contatto con l'utente tramite canale secondario per verifica |
| **Orari insoliti** | Login al di fuori del normale orario di lavoro per i lavoratori non a turni | Registrazione e revisione; avviso se combinato con altre anomalie |
| **Nuovo dispositivo/luogo** | Primo login da dispositivo o luogo non riconosciuto | Autenticazione step-up (ulteriore challenge AMF); notifica all'utente |
| **Escalation dei privilegi** | Utente con privilegi elevati concessi senza richiesta di modifica approvata | Indagine immediata; ripristino in caso di non autorizzazione |
| 7 | **Registri di reset della password** (self-service e assistiti dall'helpdesk; metodo di verifica dell'identità documentato) | Operazioni IT | Per evento; audit semestrale |
| 8 | **Registro delle credenziali condivise** (account, custode, posizione nel vault, ultima revisione, data di ri-autorizzazione) | Sicurezza IT | Revisione trimestrale |
| 9 | **Registro delle eccezioni** (sistemi senza AMF, limitazioni di password legacy, AMF solo via SMS — con controlli compensativi e approvazione del RSSI) | Sicurezza IT | Revisione trimestrale; ogni eccezione max 12 mesi |
| 10 | **Registri di completamento della formazione di sensibilizzazione sull'autenticazione** | HR / Sicurezza IT | Annualmente |

### Requisiti di formazione sull'autenticazione

Tutto il personale DEVE completare la formazione di sensibilizzazione sull'autenticazione come segue:

| Modulo di formazione | Destinatari | Frequenza | Contenuto |
|---------------------|-------------|-----------|-----------|
| **Sensibilizzazione sulla sicurezza — basi dell'autenticazione** | Tutto il personale | Annuale (parte della sensibilizzazione obbligatoria sulla sicurezza) | Igiene delle password, iscrizione AMF, riconoscimento del phishing, segnalazione delle credenziali |
| **Onboarding al gestore di password** | Tutto il personale | All'onboarding + in caso di cambio dello strumento | Configurazione di [Gestore di password], creazione del vault, estensione del browser, app mobile, accesso di emergenza |
| **Formazione sull'accesso privilegiato** | Utenti privilegiati (admin, DBA, team sicurezza) | Annuale + all'assegnazione del ruolo | Utilizzo dello strumento PAM, check-out/check-in del vault delle credenziali, consapevolezza della registrazione delle sessioni, gestione delle chiavi hardware AMF |
| **Simulazione di phishing** | Tutto il personale | Trimestrale | Campagne simulate di phishing per testare la consapevolezza sulla raccolta delle credenziali; risultati segnalati al RSSI; ri-formazione mirata per il personale che fallisce |
| **Gestione degli account di servizio** | Proprietari di sistema, DevOps, Operazioni IT | Annuale | Ciclo di vita degli account di servizio, archiviazione delle credenziali (no hardcoding), procedure di rotazione, dismissione |

**Misurazione dell'efficacia della formazione**: Tasso di clic nella simulazione di phishing tracciato trimestralmente (obiettivo: < 5%). Il personale che fallisce due simulazioni di phishing in 12 mesi riceve un coaching obbligatorio di sicurezza individuale.

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni DEVE verificare la conformità a questa policy attraverso vari metodi, inclusi a titolo non esaustivo: audit della configurazione del provider di identità, rapporti di copertura AMF, verifica della configurazione della verifica violazioni, analisi dei log di autenticazione, penetration testing, audit interni ed esterni, e feedback al proprietario della policy.

**Indicatori chiave di prestazione**:

| Metrica | Obiettivo | Frequenza |
|---------|----------|-----------|
| Iscrizione AMF (tutti gli utenti) | >=95% | Mensile |
| Iscrizione AMF (utenti privilegiati) | 100% | Mensile |
| Conformità alla policy sulle password | >=98% | Mensile |
| Rilevamenti di credenziali predefinite in produzione | 0 | Trimestrale |
| Copertura password verificate per violazioni | 100% delle nuove password | Mensile |
| Indagine sulle anomalie di autenticazione (entro 24 ore) | 100% | Continua |
| Riduzione dell'AMF via SMS (anno su anno) | Trend decrescente | Annuale |
| Adozione del gestore di password (a livello organizzativo) | >=80% degli utenti con vault attivo | Trimestrale |
| Rapporto di password univoche nel gestore di password | >=90% password univoche nei vault | Trimestrale |
| Conformità alla rotazione delle credenziali degli account di servizio | 100% entro il periodo di rotazione definito | Trimestrale |

Le metriche DEVONO essere segnalate al RSSI trimestralmente. Le metriche che non raggiungono l'obiettivo DEVONO includere un piano di remediation con proprietario e data target.

## Deroghe

Qualsiasi deroga a questa policy DEVE essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con documentazione dell'accettazione del rischio, dei controlli compensativi e di una data di revisione definita. Le deroghe DEVONO essere segnalate al Team di revisione del management. Durata massima dell'eccezione: 12 mesi, rinnovabile con ri-approvazione.

**Eccezioni consentite** (con controlli compensativi):

- Sistemi legacy non in grado di soddisfare i requisiti di lunghezza delle password (controllo compensativo: segmentazione di rete, monitoraggio potenziato, accesso limitato).
- Sistemi non compatibili con l'AMF (controllo compensativo: restrizione IP, logging potenziato, timeout di sessione ridotto, accesso solo tramite VPN).
- Account di servizio che richiedono policy di autenticazione diverse (controllo compensativo: vaulting delle credenziali, rotazione automatizzata, monitoraggio potenziato).

### Autenticazione degli account di servizio

Gli account di servizio (account non interattivi utilizzati per la comunicazione da applicazione ad applicazione, le attività pianificate e l'automazione) DEVONO rispettare i seguenti requisiti:

| Requisito | Standard |
|-----------|----------|
| **Convenzione di denominazione** | Prefisso `svc-` seguito dal nome dell'applicazione/funzione (ad es. `svc-backup-agent`, `svc-crm-integration`) |
| **Lunghezza della password** | Minimo 24 caratteri, generata casualmente |
| **Archiviazione delle credenziali** | Vault dei segreti approvato [PAM / Gestore di password] — non in script, file di configurazione o codice sorgente |
| **Rotazione** | Rotazione automatizzata ogni 90 giorni ove tecnicamente fattibile; rotazione manuale ogni 180 giorni con motivazione documentata |
| **Login interattivo** | Vietato — gli account di servizio NON devono essere utilizzati per il login interattivo. I controlli tecnici (GPO/policy IdP) DEVONO impedire il login interattivo ove supportato. |
| **Titolarità** | Proprietario umano nominato (proprietario del sistema o responsabile dell'applicazione) responsabile della gestione del ciclo di vita |
| **Revisione** | Revisione trimestrale di tutti gli account di servizio: ancora necessari? proprietario ancora valido? credenziali ruotate? permessi ancora appropriati? |
| **Dismissione** | Disabilitato entro 5 giorni lavorativi dalla dismissione dell'applicazione; credenziali ruotate immediatamente |

**Inventario degli account di servizio**: Mantenuto in [PAM / Sistema di gestione degli asset] con: nome account, finalità, proprietario, data di creazione, data dell'ultima rotazione, data della prossima rotazione, applicazione associata, ambito delle autorizzazioni.
- Sistemi dove SMS è l'unico metodo AMF disponibile (controllo compensativo: restrizione IP, monitoraggio delle anomalie, piano di migrazione documentato).

**Non consentite come eccezioni**:

- Eliminare l'AMF per l'accesso privilegiato.
- Consentire la condivisione delle password senza responsabilità.
- Consentire credenziali predefinite negli ambienti di produzione.
- Disabilitare il logging dell'autenticazione.

## Non conformità

Un dipendente ritenuto responsabile di aver violato questa policy potrà essere soggetto a misure disciplinari, fino alla risoluzione del rapporto di lavoro.

**Risposta progressiva** (nel periodo di 12 mesi):

| Occorrenza | Risposta | Tempistica | Proprietario |
|-----------|---------|-----------|--------------|
| Prima | Promemoria di sensibilizzazione e formazione mirata | Entro 5 giorni lavorativi | Sicurezza IT |
| Seconda (entro 90 giorni) | Notifica al responsabile + avviso documentato | Entro 3 giorni lavorativi | Sicurezza IT + HR |
| Terza (entro 12 mesi) | Restrizione dell'accesso in attesa di remediation | Immediata | Sicurezza IT + Responsabile |
| Violazione grave / critica | Misure disciplinari ai sensi delle policy HR | Escalation immediata | HR + RSSI |

**Violazioni critiche** che giustificano l'escalation immediata indipendentemente dalla storia precedente:

- Condivisione di credenziali privilegiate.
- Aggirare deliberatamente i controlli di autenticazione.
- Archiviare credenziali in chiaro in posizioni condivise.
- Utilizzare credenziali predefinite o del fornitore in produzione dopo la notifica.

## Miglioramento continuo

Questa policy è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO tener conto delle variazioni agli standard di autenticazione (incluse le revisioni di NIST SP 800-63B), delle minacce emergenti (credential stuffing, phishing, tecniche di bypass dell'AMF come gli attacchi adversary-in-the-middle e di AMF fatigue), dei progressi nell'autenticazione resistente al phishing (FIDO2/WebAuthn, passkey), dei cambiamenti normativi e delle lezioni apprese dagli incidenti.

---

# Sezioni della norma ISO 27001 trattate

Policy sulle informazioni di autenticazione — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.4 Responsabilità del management |
| Clausola 6.2 Obiettivi per la sicurezza delle informazioni | **5.17 Informazioni di autenticazione** |
| Clausola 7.3 Consapevolezza | 5.15 Controllo degli accessi |
| Clausola 7.5.3 Controllo delle informazioni documentate | 5.16 Gestione delle identità |
| | 5.18 Diritti di accesso |
| | 5.36 Conformità a policy, regole e standard |
| | 6.3 Sensibilizzazione, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 8.2 Diritti di accesso privilegiato |
| | 8.5 Autenticazione sicura |
| | 8.24 Uso della crittografia |

**Quadro normativo e legale**:

| Quadro di riferimento | Rilevanza |
|-----------------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative inclusi i controlli di autenticazione per la protezione dei dati |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento (controlli di autenticazione come misura tecnica appropriata) |
| ISO/IEC 27001:2022 | Controllo Annex A 5.17 — Informazioni di autenticazione |
| ISO/IEC 27002:2022 | Sezione 5.17 — Linee guida per l'implementazione delle informazioni di autenticazione |
| NIST SP 800-63B-4 | Linee guida per l'identità digitale — segreti memorizzati, autenticazione a più fattori, requisiti del verificatore |
| CIS Controls v8 | Controllo 5 (Gestione degli account), Controllo 6 (Gestione del controllo degli accessi) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
