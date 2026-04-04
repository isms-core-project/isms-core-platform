<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.4-IT:framework:POL:a.8.4 -->
**ISMS-POL-A.8.4 — Accesso al codice sorgente**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Accesso al codice sorgente |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.4 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DT/VP Engineering → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.4.1–3-UG/TG; ISMS-POL-A.8.25-26-29 (Ciclo di vita dello sviluppo sicuro); ISMS-POL-A.5.15-16-18 (IAM); ISO/IEC 27001:2022 Controllo A.8.4.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per il controllo dell'accesso al codice sorgente per proteggere la proprietà intellettuale e mantenere pratiche di sviluppo software sicure, conformemente al Controllo A.8.4 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutti i repository di codice sorgente (produzione, strumenti interni, infrastruttura-come-codice, contributi open source, archiviati); tutti gli artefatti di sviluppo; tutte le piattaforme di repository (GitHub, GitLab, Bitbucket, Azure DevOps, auto-ospitate); tutto il personale organizzativo, gli appaltatori e le terze parti con accesso al codice sorgente.

**Allineamento normativo**: nLPD svizzera (Art. 8); RGPD dell'UE (Art. 32); ISO/IEC 27001:2022; FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.4

> *L'accesso al codice sorgente, agli strumenti di sviluppo e alle librerie software deve essere gestito in modo appropriato.*

---

# Requisiti di controllo degli accessi

## Gestione dell'accesso ai repository

[Organizzazione] implementa il controllo degli accessi basato sui ruoli (RBAC) per tutti i repository di codice sorgente con il principio del minimo privilegio.

**Principi di controllo degli accessi**:

- Tutti i repository DEVONO implementare RBAC
- Le autorizzazioni predefinite dei repository DEVONO essere «nessun accesso»
- L'accesso DEVE essere concesso solo in base a necessità aziendali documentate e approvate dal proprietario del repository
- L'accesso ai repository DEVE essere rivisto trimestralmente
- L'accesso DEVE essere revocato automaticamente alla cessazione del rapporto di lavoro, al cambio di ruolo o alla scadenza del contratto

**Processo di revisione trimestrale degli accessi**: Revisioni condotte utilizzando il modulo standardizzato di revisione degli accessi (modello in ISMS-IMP-A.8.4.3); il proprietario del repository rivede l'accesso di ciascun utente e conferma se è ancora necessario, se il livello è appropriato e l'azione (mantenere/modificare/revocare); mancata risposta escalata al Development Manager dopo 10 giorni lavorativi; registrazioni delle revisioni conservate nella libreria delle prove SGSI.

**Approvazione delle richieste di accesso**: Tutte le richieste DEVONO includere: nome del richiedente e ruolo, nome del repository e classificazione, livello di accesso richiesto (lettura/scrittura/admin), giustificazione aziendale, durata prevista. Le richieste DEVONO essere approvate dal proprietario del repository (obbligatorio), dal team lead per l'accesso in scrittura o superiore, e dal RSSI o delegato per l'accesso admin ai repository di produzione.

**Deprovisioning**: La revoca DEVE essere verificata entro 24 ore dall'evento trigger tramite reportistica automatizzata.

## Classificazione dei repository e controlli

[Organizzazione] classifica tutti i repository di codice sorgente:

- **Repository di codice di produzione**: Codice direttamente distribuito a sistemi di produzione rivolti ai clienti o business-critical (massima protezione)
- **Repository di strumenti interni**: Codice per automazione interna e strumenti operativi (alta protezione)
- **Repository di contributi open source**: Codice pubblico o open source dove l'organizzazione contribuisce (protezione media)
- **Repository archiviati/deprecati**: Codice storico non più in sviluppo attivo (sola lettura)

**Controlli basati sulla classificazione**:

- I repository di codice di produzione DEVONO richiedere: revisione di almeno due persone per tutti i merge, protezione dei branch sui branch principali e di rilascio, scansione giornaliera dei segreti, revisioni trimestrali degli accessi
- I repository di strumenti interni DEVONO richiedere: revisione di almeno una persona per i merge al branch principale, protezione del branch principale, scansione settimanale dei segreti, revisioni trimestrali degli accessi

## Controllo degli accessi basato sui ruoli

**Ruoli e autorizzazioni**:

- **Sviluppatori**: Accesso in scrittura (clonazione/pull, creazione branch/commit, push su branch non protetti, richieste di pull). Non possono fare push su branch protetti, approvare proprie richieste di pull o modificare le impostazioni del repository.
- **Team di sicurezza**: Accesso in sola lettura per revisioni di sicurezza e audit.
- **Auditor**: Accesso in sola lettura limitato nel tempo durante il periodo di audit; scade automaticamente al termine dell'audit.
- **Appaltatori esterni**: Accesso in scrittura limitato nel tempo e per repository specifici; scade alla data di fine contratto.
- **Amministratori di repository**: Gestiscono le impostazioni del repository; l'accesso admin non concede automaticamente l'accesso in scrittura al codice.
- **Proprietari di repository**: Responsabilità ultima; approvano le richieste di accesso; conducono le revisioni degli accessi.
- **Account di servizio** (CI/CD, automazione, scanner): Creati con nomi descrittivi; accesso limitato ai repository specifici; autenticazione basata su token con scadenza; rivisti trimestralmente; documentati con proprietario e scopo.

**Criteri di revisione trimestrale degli account di servizio**: L'automazione/pipeline è ancora attiva? Il proprietario documentato è ancora responsabile? Il livello di accesso è ancora appropriato? La scadenza del token è impostata in modo appropriato (massimo 1 anno; 90 giorni raccomandati per account con privilegi elevati)?

**Applicazione del minimo privilegio**: Accesso in lettura solo per revisioni o riferimento; accesso in scrittura solo se si contribuisce al codice; accesso admin solo per responsabilità di gestione del repository.

## Protezione dei branch e revisione del codice

**Protezione del branch principale**:

- Commit diretti bloccati
- Richiesta di pull obbligatoria prima del merge
- Revisori minimi: 2 per la produzione, 1 per gli strumenti interni
- Chiudere le approvazioni di pull request obsolete quando vengono inviate nuove commit
- I controlli di stato DEVONO passare prima del merge
- Firma dei commit obbligatoria dove tecnicamente fattibile

**Requisiti delle richieste di pull**: Tutte le modifiche al codice sui branch protetti DEVONO essere inviate tramite richieste di pull; le richieste di pull NON DEVONO essere approvate dall'autore del codice; le richieste di pull DEVONO rimanere aperte per un periodo minimo: 4 ore per le modifiche al codice di produzione, 1 ora per le modifiche agli strumenti interni. **Revisione accelerata** (periodo di revisione ridotto): Le modifiche a basso rischio (solo documentazione, solo configurazione senza logica di codice) possono utilizzare un periodo di revisione di 1 ora se etichettate come «basso rischio» e limitate ai file di documentazione/configurazione.

## Gestione dei segreti

**Divieto dei segreti**: I repository di codice sorgente NON DEVONO contenere: password/credenziali, chiavi API/token, chiavi crittografiche private, stringhe di connessione al database con credenziali incorporate, chiavi SSH private, chiavi di cifratura, o qualsiasi altro materiale di autenticazione sensibile.

**Scansione dei segreti**: Tutti i repository DEVONO avere la scansione automatizzata dei segreti abilitata con: scansione pre-commit (impedisce ai segreti di entrare nel repository), scansione lato server (rileva i segreti già presenti), frequenza di scansione in tempo reale per le nuove commit e giornaliera per la scansione completa del repository.

**Rimedio dei segreti**: I segreti scoperti DEVONO essere rimediati entro 1 ora per i segreti dei repository di produzione e entro 24 ore per i segreti dei repository di strumenti interni. **Gestione delle eccezioni alla sequenza temporale** (scoperta fuori orario): L'ingegnere di turno viene contattato; il contatore di 1 ora inizia dall'acknowledgment dell'ingegnere; se non c'è acknowledgment entro 30 minuti, escalate al turno secondario.

## Autenticazione e AMF

**Requisiti**: L'accesso ai repository DEVE richiedere l'autenticazione. L'AMF DEVE essere obbligatoria per tutti gli account utente umani con accesso in scrittura o admin ai repository di produzione e per l'accesso web-based per tutti gli utenti. **Metodi AMF accettabili**: app di autenticazione, chiavi di sicurezza hardware (YubiKey), notifica push, codici SMS (meno preferiti). **Account di servizio**: Usano l'autenticazione basata su token con ambiti limitati invece dell'AMF.

## Registrazione e monitoraggio degli audit

**Requisiti di registrazione**: I repository DEVONO registrare: eventi di accesso, accesso ai repository (clonazione, pull, navigazione), modifiche al codice (commit con autore/timestamp/messaggio), operazioni sui branch, attività delle richieste di pull, modifiche alle autorizzazioni, azioni amministrative, eventi di sicurezza.

**Conservazione dei log**: Minimo: eventi di accesso 1 anno; eventi di modifica del codice 3 anni; modifiche alle autorizzazioni 3 anni.

**Monitoraggio e avvisi**: I log DEVONO essere monitorati per: tentativi di autenticazione falliti multipli, accesso da ubicazioni geografiche insolite, accesso al di fuori dei normali orari lavorativi, operazioni di download in blocco, tentativi di elevazione delle autorizzazioni, push forzati su branch protetti.

## Backup e ripristino

**Requisiti di backup**: Frequenza: backup incrementali giornalieri e backup completi settimanali; conservazione: minimo 90 giorni per i repository attivi e 7 anni per i repository di produzione; ridondanza geografica. **Test di ripristino**: Test trimestrali per i repository di produzione; annuali per i repository di strumenti interni. L'RTO è di 4 ore per la produzione, 24 ore per la non produzione.

## Gestione dell'accesso di terze parti

**Requisiti**: Le terze parti DEVONO firmare NDA prima della concessione dell'accesso; accesso limitato ai repository specifici; accesso limitato nel tempo; revoca automatica alla scadenza del contratto; soggetti a requisiti di revisione del codice avanzati. **Monitoraggio**: L'accesso di terze parti DEVE essere monitorato mensilmente e documentato nel registro degli accessi di terze parti. **Revoca immediata**: Alla scadenza del contratto, alla risoluzione del contratto, all'incidente di sicurezza che coinvolge terze parti, o su richiesta del proprietario del repository.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Responsabilità complessiva; approvazione delle eccezioni; supervisione degli incidenti di sicurezza; revisione annuale della politica |
| **DT/VP Engineering** | Responsabilità per la selezione della piattaforma di sviluppo; approvazione delle classificazioni dei repository; conformità del team di sviluppo |
| **Responsabile della Sicurezza Informatica** | Manutenzione della politica; revisione e approvazione delle eccezioni; monitoraggio della sicurezza; coordinamento degli audit |
| **Proprietari di repository** | Assegnazione della classificazione del repository; approvazione delle richieste di accesso; revisioni degli accessi; segnalazione degli incidenti |
| **Team leader dello sviluppo** | Revisione delle richieste di accesso per i membri del team; applicazione del processo di revisione del codice |
| **Team di sicurezza** | Monitoraggio della sicurezza; gestione dello strumento di scansione dei segreti; audit e valutazioni di sicurezza |
| **Operazioni IT** | Manutenzione e disponibilità della piattaforma dei repository; implementazione del backup e del ripristino |
| **Sviluppatori e appaltatori** | Conformità ai requisiti; protezione delle credenziali; nessun archiviazione di segreti; partecipazione alla revisione del codice |

---

# Punteggio di conformità

**Punteggio complessivo della sicurezza del codice sorgente** (0-100%):

| Componente | Peso | Calcolo |
|-----------|------|---------|
| Conformità al controllo degli accessi dei repository | 35% | Repository con RBAC conforme + revisioni completate / totale |
| Conformità alla protezione dei branch | 35% | Repository con protezione dei branch obbligatoria abilitata / applicabili |
| Gestione dei segreti | 20% | Repository con scansione dei segreti abilitata + segreti rimediati nei tempi / totale |
| Accesso di terze parti | 10% | Account di terze parti con NDA valido + contratto corrente / totale |

**Obiettivi**: SGSI maturo ≥90% conformità complessiva; nuovo SGSI ≥70% entro 180 giorni.

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **Direttore della Tecnologia (DT)** | [Nome] | [Data] |
| **Responsabile Legale/Conformità** | [Nome] | [Data] |
| **Amministratore Delegato (AD)** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per il controllo dell'accesso al codice sorgente. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.4.1 (Controllo degli accessi ai repository), ISMS-IMP-A.8.4.2 (Protezione dei branch) e ISMS-IMP-A.8.4.3 (Valutazione dell'accesso al codice sorgente).*

<!-- QA_VERIFIED: 2026-04-03 -->
