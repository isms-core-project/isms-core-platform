<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.15-16-18-IT:operational:OP-POL:a.5.15-16-18 -->
**ISMS-OP-POL-A.5.15-16-18 — Gestione delle identità e degli accessi**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Gestione delle identità e degli accessi |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.5.15-16-18 |
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

- Controlli ISO/IEC 27001:2022 A.5.15, A.5.16, A.5.18 — Controllo degli accessi, gestione delle identità, diritti di accesso

**Controlli Annex A correlati**:

| Controllo | Relazione con la gestione delle identità e degli accessi |
|-----------|----------------------------------------------------------|
| A.5.3 Separazione dei compiti | La matrice SoD è applicata attraverso i controlli degli accessi |
| A.5.10 Uso accettabile delle informazioni | L'uso accettabile dipende dagli accessi concessi |
| A.5.12–13 Classificazione ed etichettatura | La classificazione determina il livello di accesso richiesto |
| A.5.17 Informazioni di autenticazione | Gestione delle credenziali per le identità autenticate |
| A.5.19–23 Relazioni con i fornitori | Governance degli accessi di terzi |
| A.5.24–28 Gestione degli incidenti | Gestione degli incidenti di compromissione degli account |
| A.8.2 Diritti di accesso privilegiato | Gestione degli accessi privilegiati (PAM) |
| A.8.3 Restrizione dell'accesso alle informazioni | Applicazione tecnica delle regole di accesso |
| A.8.5 Autenticazione sicura | Meccanismi di autenticazione per la verifica dell'identità |
| A.8.11 Mascheramento dei dati | Controlli di mascheramento allineati alla classificazione degli accessi |

**Policy interne correlate**:

- Policy di classificazione e gestione delle informazioni
- Policy di autenticazione e accesso privilegiato
- Policy di gestione degli incidenti
- Policy di trasferimento delle informazioni
- Policy di sviluppo sicuro

---

# Policy di controllo degli accessi

## Scopo

Lo scopo di questa policy è garantire il corretto accesso alle informazioni e alle risorse corrette da parte delle persone autorizzate, e gestire l'intero ciclo di vita delle identità degli utenti.

Questa policy supporta la nLPD svizzera (revDSG) implementando misure tecniche e organizzative proporzionate al rischio per proteggere i dati personali (inclusi i dati personali degni di particolare protezione) attraverso i controlli degli accessi. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.
Tutti i sistemi e le applicazioni inclusi nell'ambito della dichiarazione di scopo ISO 27001.
L'accesso fisico è definito nella Policy di sicurezza fisica e ambientale.

## Principio

Il controllo degli accessi è concesso secondo il principio del privilegio minimo. Agli utenti viene fornito accesso esclusivamente alle informazioni necessarie per svolgere le proprie mansioni e il proprio ruolo.

L'accesso è negato per impostazione predefinita e concesso solo con approvazione documentata. Tutte le decisioni di accesso DEVONO essere basate sul rischio, tenendo conto della classificazione delle informazioni e della criticità del sistema.

---

## Accordi di riservatezza

Tutti i dipendenti e i collaboratori a cui viene concesso l'accesso a informazioni riservate DEVONO firmare un accordo di riservatezza o di non divulgazione prima di ricevere l'accesso agli strumenti di elaborazione delle informazioni.

## Accesso basato sul ruolo

L'accesso ai sistemi è basato sul ruolo. L'accesso è concesso dal proprietario del sistema o dei dati ed è formalmente approvato.

L'organizzazione DEVE implementare il controllo degli accessi basato sui ruoli (RBAC) come metodo preferito per l'assegnazione degli accessi. I ruoli DEVONO essere documentati e rivisti annualmente dai proprietari del sistema.

## Identificatore univoco

Agli utenti viene assegnato un nome utente o identificatore univoco secondo il principio di un utente, un ID, per garantire la responsabilità individuale. I nomi utente e gli identificatori NON devono essere condivisi tra utenti.

Gli account condivisi sono vietati, salvo dove tecnicamente inevitabile (sistemi legacy, account richiesti dal fornitore). Qualsiasi eccezione richiede l'approvazione scritta del RSSI con motivazione aziendale documentata, controlli compensativi (logging per utente individuale, revisione trimestrale) e formale accettazione del rischio. Gli account condivisi DEVONO essere inclusi nel registro degli account privilegiati.

## Autenticazione degli accessi

Gli utenti DEVONO essere positivamente identificati e autenticati prima di accedere a sistemi, servizi o informazioni.

L'autenticazione a più fattori (AMF) DEVE essere richiesta per:

- Tutti gli accessi remoti alle reti e ai servizi cloud dell'organizzazione.
- Tutti gli account privilegiati e di amministratore.
- Tutte le applicazioni esposte esternamente.
- Tutti i sistemi che trattano dati riservati o personali.

I sistemi non in grado di supportare l'AMF DEVONO essere documentati nel registro dei rischi con motivazione tecnica, controlli compensativi (ad es. segmentazione di rete, monitoraggio potenziato) e accettazione del rischio approvata dal RSSI, rivista annualmente.

## Revisione dei diritti di accesso

L'accesso degli utenti ai sistemi DEVE essere rivisto periodicamente per garantirne la pertinenza e l'adeguatezza:

| Tipo di account | Frequenza di revisione |
|----------------|------------------------|
| Account privilegiati / di amministratore | Trimestrale |
| Accesso di terzi / collaboratori | Trimestrale |
| Account di servizio | Trimestrale |
| Account utente standard | Annuale |

Gli account inattivi e dormienti DEVONO essere oggetto di indagine. Un account è considerato inattivo se non si è autenticato con successo nel periodo specificato. Gli account inattivi da più di 45 giorni DEVONO essere disabilitati. Gli account inattivi da più di 90 giorni DEVONO essere rimossi, salvo documentata motivazione aziendale.

Gli account di servizio sono esclusi dalla disabilitazione per inattività, ma DEVONO essere rivisti trimestralmente per verificare che siano ancora in uso attivo e ancora necessari. Gli account di servizio non utilizzati DEVONO essere disabilitati immediatamente alla scoperta.

## Account privilegiati / di amministratore

Gli account di amministratore NON devono essere forniti agli utenti per le attività ordinarie, inclusi a titolo non esaustivo portatili e dispositivi mobili.

Laddove fattibile, agli utenti privilegiati e di amministratore DEVONO essere assegnati account privilegiati specifici in aggiunta al loro account ordinario, per l'uso esclusivo nell'esecuzione di attività privilegiate e di amministrazione.

Gli account privilegiati e di amministratore DEVONO:

- Non essere account condivisi o generici.
- Essere chiaramente identificabili (convenzione di denominazione).
- Essere soggetti a logging e monitoraggio.
- Essere a tempo limitato ove fattibile (accesso just-in-time preferito).
- Essere registrati in un inventario mantenuto aggiornato.

## Account di servizio

Gli account di servizio (account non umani utilizzati da applicazioni, script o processi automatizzati) DEVONO essere gestiti secondo i seguenti requisiti:

- La creazione di account di servizio DEVE essere approvata dal proprietario del sistema e dal RSSI.
- Tutti gli account di servizio DEVONO essere documentati con finalità, sistema/applicazione, proprietario e data di revisione.
- Agli account di servizio DEVONO essere concesse solo le autorizzazioni minime necessarie per la propria funzione.
- Gli account di servizio NON devono essere utilizzati per il login interattivo da parte del personale.
- Le credenziali degli account di servizio DEVONO essere archiviate in una soluzione approvata di gestione dei segreti, non codificate in chiaro o in testo normale.
- L'attività degli account di servizio DEVE essere soggetta a logging e monitoraggio per comportamenti anomali.
- Gli account di servizio DEVONO essere rivisti trimestralmente secondo il calendario di revisione degli accessi.

## Password

L'accesso ai sistemi e alle informazioni è autenticato tramite password. L'organizzazione DEVE applicare i seguenti standard sulle password:

| Requisito | Standard |
|-----------|----------|
| Lunghezza minima | 12 caratteri |
| Complessità | Lunghezza privilegiata rispetto alla complessità; nessuna regola di composizione obbligatoria (ai sensi di NIST SP 800-63B) |
| Verifica | Le password DEVONO essere validate rispetto a database di credenziali compromesse/violate note |
| Rotazione | Solo basata su eventi — in caso di sospetta o confermata compromissione; la rotazione periodica forzata non è richiesta |
| Password iniziali | DEVONO essere cambiate al primo utilizzo |
| Password predefinite | Le password fornite dal fornitore e quelle predefinite DEVONO essere cambiate immediatamente dopo l'installazione |
| Condivisione | Le password NON devono essere generiche, condivise o impostate a livello di gruppo |
| Riservatezza | Le password DEVONO essere mantenute riservate e non scritte |
| Visualizzazione | Le password NON devono essere visualizzate durante l'inserimento |
| Codice | Le password NON devono essere inserite in script, codice o macro |
| Trasmissione | Le password DEVONO essere cifrate durante la trasmissione sulla rete |
| Archiviazione | Le password DEVONO essere archiviate utilizzando funzioni hash crittografiche approvate (bcrypt, scrypt, Argon2 o PBKDF2) e mai in chiaro o con cifratura reversibile |
| Blocco | I sistemi DEVONO bloccare gli utenti dopo 6 tentativi di accesso falliti |
| Timeout di sessione | Le sessioni di sistema inattive per 15 minuti DEVONO richiedere la ri-autenticazione (5 minuti per i sistemi che trattano dati personali sensibili o dati finanziari) |
| Gestori di password | È raccomandato l'utilizzo di gestori di password approvati dall'organizzazione |

## Provisioning degli account utente

La creazione, la modifica e la cancellazione degli account DEVONO essere eseguite da personale autorizzato e completamente documentate.

L'organizzazione DEVE implementare un processo di Joiner-Mover-Leaver (JML):

| Evento HR | Azione sull'accesso | Tempistica |
|-----------|---------------------|-----------|
| Nuova assunzione | Creazione dell'account con accesso basato sul ruolo | Accesso pronto entro la data di inizio |
| Cambio di ruolo | Accesso adeguato al nuovo ruolo; accesso precedente rimosso | Entro 2 giorni lavorativi |
| Cessazione (volontaria) | Tutti gli accessi revocati | Stesso giorno lavorativo |
| Cessazione (per giusta causa) | Tutti gli accessi revocati | Immediata (entro 1 ora) |
| Fine contratto | Accesso di collaboratori/fornitori rimosso | Alla data di scadenza del contratto |

I proprietari del sistema o dei dati DEVONO approvare l'accesso ai sistemi e alle informazioni. Una richiesta documentata DEVE indicare chiaramente l'accesso richiesto e DEVE essere mantenuto un registro delle autorizzazioni.

**Flusso di lavoro per le richieste di accesso:**

1. L'utente invia una richiesta tramite il service desk IT o lo strumento di gestione degli accessi, specificando il sistema, il ruolo e la motivazione aziendale.
2. Il responsabile di linea approva la necessità aziendale.
3. Il proprietario del sistema o dei dati approva il livello di accesso.
4. L'IT effettua il provisioning dell'accesso e registra l'autorizzazione.
5. Il richiedente conferma che l'accesso è operativo.

L'accesso di emergenza (break-glass) può essere concesso dall'IT con approvazione verbale del RSSI e DEVE essere formalmente documentato entro 1 giorno lavorativo.

Tutti gli utenti che richiedono il reset della password o modifiche alle credenziali di autenticazione DEVONO avere la propria identità verificata mediante almeno uno dei seguenti metodi:

- Verifica di un contatto secondario pre-registrato (email, telefono).
- Challenge-response con domande di sicurezza prestabilite.
- Verifica di persona con documento di identità con foto.
- Conferma dell'identità dell'utente da parte del responsabile o delle Risorse umane.

Il reset della password self-service tramite il provider di identità (con verifica AMF registrata) è accettabile e non richiede ulteriori verifiche dell'identità.

## Uscenti

I responsabili di linea e le Risorse umane DEVONO informare il team di provisioning degli account della data di uscita di un utente.

Quando un utente lascia l'organizzazione, tutti gli accessi DEVONO essere revocati nello stesso giorno lavorativo, come minimo alla principale tecnologia di autenticazione, e a tutti i sistemi e i dati registrati nell'elenco degli accessi basato sul ruolo.

Gli ID utente, le password e le credenziali di autenticazione degli uscenti NON devono essere riutilizzati.

## Autenticazione

Il sistema principale di autenticazione degli accessi DEVE:

- Non visualizzare identificatori di sistema o applicazione fino al completamento con successo del processo di accesso.
- Visualizzare un avviso generale che il sistema deve essere utilizzato solo da utenti autorizzati.
- Non fornire messaggi di aiuto durante la procedura di accesso che possano assistere un utente non autorizzato.
- Validare le informazioni di accesso solo al completamento di tutti i dati inseriti. In caso di errore, il sistema NON deve indicare quale parte dei dati sia corretta o errata.
- Proteggere da tentativi di accesso a forza bruta.
- Registrare i tentativi falliti e riusciti.
- Generare un evento di sicurezza se viene rilevato un possibile tentativo di violazione o una violazione dei controlli di accesso.
- Non visualizzare una password durante l'inserimento.
- Non trasmettere password in chiaro sulla rete.
- Terminare le sessioni inattive dopo un periodo definito di inattività, specialmente in luoghi ad alto rischio come aree pubbliche o esterne alla gestione della sicurezza dell'organizzazione o su dispositivi mobili.
- Limitare i tempi di connessione per fornire sicurezza aggiuntiva alle applicazioni ad alto rischio.

## Accesso remoto

L'accesso remoto alle reti dell'organizzazione, ai servizi cloud e alle applicazioni accessibili esternamente segue le stesse regole previste da questa policy, con il requisito aggiuntivo dell'autenticazione a più fattori.

Le connessioni remote DEVONO essere impostate per disconnettersi dopo un periodo definito di inattività.

DEVE essere mantenuto e rivisto trimestralmente un elenco degli utenti con accesso remoto ai sistemi di rete interni.

## Accesso remoto di terzi

L'accesso è concesso a terzi solo se esiste un contratto in vigore con un accordo di non divulgazione applicabile.

L'accesso DEVE essere concesso per un periodo specifico, a un sistema specifico, a un individuo specifico, e fornito previa ricezione di una richiesta di accesso formale, valida e autorizzata.

L'accesso DEVE essere revocato immediatamente al completamento del requisito o alla scadenza del contratto, a seconda di quale evento si verifichi prima.

DEVE essere mantenuto un elenco dei terzi e delle persone con accesso, rivisto trimestralmente.

## Monitoraggio e reportistica

L'accesso ai sistemi DEVE essere monitorato e reportato. Le azioni che direttamente o indirettamente influiscono o potrebbero influire sulla riservatezza, integrità o disponibilità dei dati DEVONO essere gestite tramite il processo di gestione degli incidenti.

## Mascheramento dei dati

L'organizzazione maschera i dati in conformità con gli obblighi legali e normativi, inclusi i requisiti della nLPD svizzera e del GDPR ove applicabile.

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa policy:

- **Inventario degli account utente** (account attivi per tipo: dipendente, collaboratore, di servizio, condiviso) — *mantenuto nel provider di identità o nello strumento di gestione degli accessi; esportazione trimestrale*
- **Registri del processo JML** (log del flusso di lavoro joiner/mover/leaver con timestamp) — *conservati per 12 mesi dalla data di uscita; audit semestrale*
- **Registri di completamento delle revisioni degli accessi** (trimestrale per i privilegiati, annuale per gli standard) — *firmati dai proprietari del sistema; conservati per 3 anni*
- **Log di remediation degli account orfani/dormienti** — *revisione mensile; account disabilitati documentati*
- **Registri di iscrizione AMF** per i sistemi — *rapporto di copertura generato trimestralmente; obiettivo 100% per i sistemi in ambito*
- **Registro degli account privilegiati e log di utilizzo** — *revisione trimestrale; utilizzo anomalo oggetto di indagine*
- **Registro degli account di servizio** (proprietario, finalità, sistema, data di revisione) — *revisione trimestrale*
- **Registro degli accessi di terzi** con date di scadenza del contratto — *revisione trimestrale; accesso revocato alla scadenza del contratto*
- **Evidenze di configurazione della policy sulle password** (screenshot di sistema o esportazioni di audit) — *acquisite annualmente o in caso di modifica*
- **Registri di richiesta e approvazione degli accessi** — *conservati per 12 mesi; campione verificato durante gli audit interni*

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa policy attraverso vari metodi, inclusi a titolo non esaustivo: rapporti di revisione degli accessi, tracce di audit JML, monitoraggio degli accessi privilegiati, audit interni ed esterni, e feedback al proprietario della policy.

## Deroghe

Qualsiasi deroga a questa policy DEVE essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con documentazione dell'accettazione del rischio, dei controlli compensativi e di una data di revisione definita. Le deroghe DEVONO essere segnalate al Team di revisione del management.

## Non conformità

Un dipendente ritenuto responsabile di aver violato questa policy potrà essere soggetto a misure disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa policy è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO tener conto delle variazioni agli standard di gestione delle identità e degli accessi, delle minacce emergenti, dei cambiamenti normativi e delle lezioni apprese dagli incidenti.

---

# Sezioni della norma ISO 27001 trattate

Policy di gestione delle identità e degli accessi — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.3 Separazione dei compiti |
| Clausola 6.2 Obiettivi per la sicurezza delle informazioni | 5.4 Responsabilità del management |
| Clausola 7.3 Consapevolezza | **5.15 Controllo degli accessi** |
| Clausola 7.5.3 Controllo delle informazioni documentate | **5.16 Gestione delle identità** |
| | 5.17 Informazioni di autenticazione |
| | **5.18 Diritti di accesso** |
| | 5.36 Conformità a policy, regole e standard |
| | 8.2 Diritti di accesso privilegiato |
| | 8.3 Restrizione dell'accesso alle informazioni |
| | 8.5 Autenticazione sicura |
| | 8.11 Mascheramento dei dati |

**Quadro normativo e legale**:

| Quadro di riferimento | Rilevanza |
|-----------------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative inclusi i controlli degli accessi |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento (controlli degli accessi come misura appropriata) |
| ISO/IEC 27001:2022 | Controlli Annex A 5.15, 5.16, 5.18 |
| ISO/IEC 27002:2022 | Sezioni 5.15, 5.16, 5.18 — Linee guida per l'implementazione |
| NIST SP 800-63B | Linee guida per l'identità digitale e l'autenticazione |
| CIS Controls v8 | Controlli 5 (Gestione degli account) e 6 (Gestione del controllo degli accessi) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
