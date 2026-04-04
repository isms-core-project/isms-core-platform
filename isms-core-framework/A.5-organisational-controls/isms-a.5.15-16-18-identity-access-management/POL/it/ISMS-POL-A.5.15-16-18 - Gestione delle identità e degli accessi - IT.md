<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.15-16-18-IT:framework:POL:a.5.15-16-18 -->
**ISMS-POL-A.5.15-16-18 — Gestione delle identità e degli accessi**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Politica di gestione delle identità e degli accessi |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.15-16-18 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Politica iniziale per la prima certificazione ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Direttore dei Sistemi Informativi (DSI)
- Integrazione HR: Direttore delle Risorse Umane (DRH)
- Conformità: Responsabile Legale/Conformità
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-IMP-A.5.15-16-18.S1-UG/TG (Valutazione dell'inventario utenti e conformità del ciclo di vita)
- ISMS-IMP-A.5.15-16-18.S2-UG/TG (Valutazione della matrice dei diritti di accesso)
- ISMS-IMP-A.5.15-16-18.S3-UG/TG (Valutazione dei risultati della revisione degli accessi)
- ISMS-IMP-A.5.15-16-18.S4-UG/TG (Valutazione della definizione dei ruoli e conformità SdC)
- ISMS-POL-A.8.2-3-5 (Autenticazione e accesso privilegiato)
- ISO/IEC 27001:2022 Controlli A.5.15, A.5.16, A.5.18

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di gestione delle identità e degli accessi al fine di garantire un'appropriata governance degli accessi durante il ciclo di vita completo dell'identità, conformemente ai Controlli A.5.15, A.5.16 e A.5.18 della norma ISO/IEC 27001:2022.

**Scopo**: Definire i requisiti organizzativi per la governance della gestione delle identità e degli accessi. Questa politica stabilisce QUALI controlli IAM sono richiesti e CHI è responsabile. Le procedure di attuazione (COME) sono documentate separatamente in ISMS-IMP-A.5.15-16-18 (varianti UG/TG).

**Perimetro**: Questa politica si applica a tutte le identità utente (dipendenti, appaltatori, fornitori, account di servizio), a tutti i sistemi di identità e a tutti i tipi di accesso indipendentemente dal modello di dispiegamento o dalla tecnologia.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; FINMA, DORA, NIS2, PCI DSS v4.0.1 (applicabilità condizionale per ISMS-POL-00).

---

# Perimetro e allineamento sui controlli

## Controlli ISO/IEC 27001:2022

**A.5.15 — Controllo degli accessi**: Le regole per controllare l'accesso fisico e logico alle informazioni e agli altri asset associati devono essere stabilite e attuate in base ai requisiti aziendali e di sicurezza delle informazioni.

**A.5.16 — Gestione delle identità**: L'intero ciclo di vita delle identità deve essere gestito.

**A.5.18 — Diritti di accesso**: I diritti di accesso alle informazioni e agli altri asset associati devono essere assegnati, rivisti, modificati e rimossi conformemente alla politica specifica per argomento dell'organizzazione e alle regole per il controllo degli accessi.

## Perimetro della politica

| Categoria | Perimetro |
|-----------|-----------|
| **Tipi di utente** | Dipendenti, Appaltatori (a tempo limitato), Fornitori (esterni), Account di servizio (non umani), Condivisi (con approvazione), Emergenza (account di emergenza) |
| **Sistemi di identità** | Active Directory, Azure AD/Entra ID, Okta, Google Workspace, LDAP e qualsiasi sistema di identità utilizzato da [Organizzazione] |
| **Tipi di accesso** | Applicazione, sistema, dati, rete e accesso amministrativo/privilegiato |
| **Personale** | Team IAM, Team di sicurezza, Team HR, Operazioni IT, Responsabili, Proprietari dei sistemi, tutti i dipendenti |

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria**:

| Normativa | Requisiti IAM chiave |
|-----------|---------------------|
| **nLPD svizzera** | Art. 8 — Misure tecniche e organizzative per il controllo degli accessi |
| **RGPD dell'UE** | Art. 32 — Sicurezza del trattamento inclusi i controlli degli accessi |
| **ISO/IEC 27001:2022** | Controlli A.5.15, A.5.16, A.5.18 |

**Livello 2 — Applicabilità condizionale**: FINMA (Circolare 2023/1 Margine 50-62); DORA (Artt. 6, 28-30); NIS2 (Art. 21); PCI DSS v4.0.1 (Requisiti 7, 8).

---

# Enunciati di politica

## Requisiti di controllo degli accessi (A.5.15)

### Principi di controllo degli accessi

[Organizzazione] DEVE implementare i controlli degli accessi basati sui seguenti principi:

| Principio | Requisito |
|-----------|-----------|
| **Minimo privilegio** | Gli utenti ricevono l'accesso minimo richiesto per la funzione lavorativa |
| **Need-to-know** | Accesso limitato alla necessità aziendale documentata |
| **Separazione dei compiti** | Le responsabilità in conflitto sono separate per prevenire frodi/errori |
| **Difesa in profondità** | Più livelli di controllo degli accessi implementati |
| **Rifiuto per impostazione predefinita** | Accesso negato a meno che non venga esplicitamente concesso con approvazione |

### Classificazione degli accessi

[Organizzazione] DEVE classificare gli accessi in base a:

| Dimensione | Classificazioni |
|------------|----------------|
| **Tipo di utente** | Dipendente, Appaltatore (a tempo limitato), Fornitore (esterno), Account di servizio (non umano), Condiviso (eccezionale), Emergenza (account di emergenza) |
| **Criticità del sistema** | Critico, Alto, Medio, Basso |
| **Sensibilità dei dati** | Limitato, Riservato, Interno, Pubblico |
| **Livello di accesso** | Lettura, Scrittura, Amministratore, Privilegiato |

### Giustificazione aziendale e approvazione

Tutte le richieste di accesso DEVONO includere una giustificazione aziendale documentata con autorità di approvazione in base al tipo di accesso:

| Tipo di accesso | Autorità di approvazione |
|----------------|--------------------------|
| **Accesso utente standard** | Responsabile diretto |
| **Accesso a sistemi sensibili** | Proprietario del sistema + Responsabile |
| **Dati Riservati/Limitati** | Proprietario dei dati + RSSI |
| **Accesso privilegiato/amministratore** | RSSI + DSI |
| **Accesso fornitore terzo** | Sponsor aziendale + RSSI |
| **Account condiviso** (eccezionale) | RSSI con controlli compensativi |

### Separazione dei compiti

[Organizzazione] DEVE mantenere una matrice di Separazione dei compiti che identifica le combinazioni di ruoli incompatibili (documentata in ISMS-IMP-A.5.15-16-18.3 Appendice A o nel [Modulo SdC della Piattaforma GRC]). Le violazioni SdC richiedono eccezioni approvate dal RSSI con controlli compensativi (registrate nel registro delle eccezioni).

Il rilevamento delle violazioni SdC DEVE avvenire mensilmente (automatizzato tramite script di controllo SdC) con reportistica al Team di sicurezza. Le violazioni DEVONO essere rimediate entro 30 giorni lavorativi o registrate come eccezioni con approvazione del RSSI.

### Integrazione HR

Il controllo degli accessi DEVE integrarsi con gli eventi del ciclo di vita HR:

| Evento HR | Azione di accesso | Tempistica |
|-----------|-----------------|-----------|
| **Nuovo assunto** | Avviare il processo di inserimento | Accesso pronto entro la data di inizio |
| **Cambio di ruolo** | Avviare il processo di trasferimento | Entro 2 giorni lavorativi |
| **Cessazione** | Avviare il processo di uscita | Immediata (per causa) o stesso giorno lavorativo |
| **Fine contratto** | Rimuovere l'accesso dell'appaltatore | Alla data di fine contratto |

Il sistema HR è designato come fonte autoritativa per gli eventi del ciclo di vita dell'identità.

---

## Requisiti di gestione delle identità (A.5.16)

### Quadro del ciclo di vita dell'identità

[Organizzazione] DEVE gestire le identità attraverso processi standardizzati del ciclo di vita:

| Processo | Trigger | Tempistica | Responsabilità |
|---------|---------|-----------|----------------|
| **Inserimento (Joiner)** | Notifica HR di nuovo assunto/appaltatore | Accesso pronto entro la data di inizio | HR attiva, Team IAM crea, IT provisiona |
| **Trasferimento (Mover)** | Notifica HR di cambio di ruolo | Entro 2 giorni lavorativi | HR attiva, Responsabile approva, Team IAM aggiorna |
| **Uscita (Leaver)** | Notifica HR di cessazione | Immediata fino a stesso giorno lavorativo | HR attiva, Team IAM disabilita, IT verifica |

### Requisiti per tipo di account

| Tipo di account | Requisiti |
|----------------|----------|
| **Dipendente** | Permanente fino alla cessazione, responsabilità individuale |
| **Appaltatore/Fornitore** | A tempo limitato con scadenza obbligatoria (imposta dal sistema tramite data di scadenza account impostata al momento del provisioning), sponsor interno richiesto (rinnovato trimestralmente con approvazione dello sponsor o de-provisionato automaticamente) |
| **Account di servizio** | Proprietario documentato (mantenuto nel [sistema IAM/piattaforma GRC]), rotazione della password (trimestrale come minimo, verificata tramite scansione automatica o attestazione manuale), controlli privilegiati per A.8.2, non conformità segnalata nella valutazione IAM mensile |
| **Account condiviso** | Approvazione RSSI richiesta (documentata nel registro delle eccezioni), controlli compensativi obbligatori (registrazione dell'utilizzo individuale tramite [SIEM/sistema di audit], monitoraggio degli accessi privilegiati per A.8.2, revisione trimestrale dell'utilizzo da parte del RSSI), fortemente scoraggiato (obiettivo: zero account condivisi o eccezione formale approvata dal RSSI), approvazione a tempo limitato (rivalidazione annuale richiesta) |
| **Emergenza/Account di emergenza** | Dormiente fino allo scenario di emergenza, doppia autorizzazione, l'utilizzo attiva un avviso (testato semestralmente per le procedure BCP, utilizzo del test documentato) |

### Gestione degli account orfani

[Organizzazione] DEVE rilevare e rimediare gli account orfani:

- **Rilevamento**: Confronto mensile incrociato dei sistemi di identità con il sistema HR
- **Rimedio**: Sequenza investigazione, notifica, disabilitazione, eliminazione entro 30 giorni
- **Eccezioni**: Approvazione del RSSI richiesta con giustificazione documentata

---

## Requisiti dei diritti di accesso (A.5.18)

### Assegnazione dei diritti di accesso

[Organizzazione] DEVE assegnare i diritti di accesso attraverso: flusso di lavoro documentato di richiesta e approvazione; controllo degli accessi basato sui ruoli (RBAC) come metodo preferito; giustificazione aziendale documentata per tutte le concessioni di accesso; pista di audit mantenuta (richiedente, approvatore, timestamp, giustificazione).

**Tempistiche di provisioning**:

| Tipo di richiesta | SLA |
|------------------|-----|
| **Accesso standard** | Entro 2 giorni lavorativi |
| **Accesso sensibile** | Entro 5 giorni lavorativi |
| **Accesso di emergenza** | Entro 4 ore |

### Controllo degli accessi basato sui ruoli

[Organizzazione] DEVE implementare il RBAC: Catalogo dei ruoli mantenuto dal Team IAM nella [Piattaforma GRC/Sistema IAM]; Proprietà del ruolo: ogni ruolo assegnato a un proprietario aziendale; Ciclo di vita del ruolo: i nuovi ruoli richiedono l'approvazione del Team IAM, le modifiche ai ruoli richiedono l'approvazione del proprietario aziendale, i ruoli deprecati archiviati (non eliminati) per la pista di audit; obiettivo: ≥80% degli utenti assegnati tramite ruoli rispetto all'accesso diretto; revisione annuale dei ruoli da parte dei proprietari aziendali.

### Revisione e ricertificazione degli accessi

[Organizzazione] DEVE rivedere periodicamente i diritti di accesso:

| Classificazione | Frequenza | Revisore |
|----------------|-----------|---------|
| **Sistemi critici / Accesso privilegiato** | Trimestrale | RSSI + Team di sicurezza |
| **Sistemi ad alto rischio / Dati Riservati** | Semestrale | Proprietari di sistemi + Responsabili |
| **Sistemi standard / Dati interni** | Annuale | Responsabili |
| **Accesso di terze parti/Fornitori** | Trimestrale | Sponsor aziendale + RSSI |

Le revisioni degli accessi delle terze parti includono la convalida che l'accordo contrattuale rimanga attivo e l'accesso rimanga necessario per A.5.20.

I revisori DEVONO certificare che l'accesso è appropriato o richiederne la rimozione. L'accesso inappropriato DEVE essere rimosso entro 5 giorni lavorativi.

**Follow-up della revisione degli accessi**: Se l'accesso inappropriato non può essere rimosso entro 5 giorni lavorativi per vincoli tecnici: il Responsabile DEVE documentare la giustificazione e i controlli compensativi nella [piattaforma GRC]; approvazione del RSSI richiesta per le eccezioni >10 giorni lavorativi; rimozioni in sospeso escalate al DSI dopo 15 giorni lavorativi; non conformità prolungata (>30 giorni) segnalata come incidente di sicurezza per A.5.24-27.

### Rimozione degli accessi

[Organizzazione] DEVE rimuovere tempestivamente gli accessi:

| Trigger | Tempistica |
|---------|-----------|
| **Cessazione per causa** | Immediata (entro 1 ora) |
| **Cessazione volontaria** | Stesso giorno lavorativo |
| **Cambio di ruolo** | Entro 2 giorni lavorativi (rimuovere l'accesso al ruolo precedente) |
| **Risultato della revisione degli accessi** | Entro 5 giorni lavorativi |
| **Incidente di sicurezza** | Immediata |

### Prevenzione dell'accumulo di privilegi

[Organizzazione] DEVE rilevare e rimediare l'accumulo di privilegi attraverso:

**Metodologia di rilevamento**:

| Metodo di rilevamento | Frequenza | Strumento/Processo | Responsabile |
|----------------------|-----------|-------------------|-------------|
| **Analisi della varianza basata sui ruoli** | Trimestrale | [Sistema IAM/Piattaforma GRC] confronta l'accesso effettivo vs. i diritti del ruolo | Team IAM |
| **Audit del processo di trasferimento** | Mensile | Revisione dei cambi di ruolo per verificare la rimozione dell'accesso precedente | Team di sicurezza |
| **Revisione dei diritti di accesso** | Semestrale | Revisione del responsabile di tutte le concessioni di accesso diretto (non basate su ruoli) | Responsabili |
| **Audit degli accessi privilegiati** | Trimestrale | Analisi delle concessioni di accesso privilegiato rispetto alle esigenze documentate | RSSI |

**Trigger di rilevamento**: L'utente ha >20% di diritti di accesso in più rispetto alla definizione del ruolo; l'utente conserva l'accesso dal ruolo precedente >30 giorni dopo l'evento di trasferimento; l'utente ha >3 concessioni di accesso diretto al di fuori delle assegnazioni basate su ruoli; l'account di servizio ha accesso oltre l'ambito documentato.

**Processo di rimedio**: Accesso in eccesso identificato e registrato nella [piattaforma GRC/sistema IAM]; Responsabile notificato con 5 giorni lavorativi per giustificare o approvare la rimozione; Accesso ingiustificato rimosso entro 10 giorni lavorativi dall'identificazione; L'accumulo di privilegi ripetuto (>2 occorrenze) attiva la revisione del processo di miglioramento.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Direzione generale** | Efficacia complessiva del programma IAM, approvazione della politica, allocazione delle risorse |
| **RSSI** | Implementazione e conformità della politica IAM, approvazione delle eccezioni, revisione trimestrale delle metriche |
| **DSI** | Infrastruttura tecnica IAM, selezione della tecnologia, allocazione delle risorse IT |
| **DRH** | Sistema HR come fonte autoritativa dell'identità, trigger degli eventi inserimento/trasferimento/uscita |
| **Team di sicurezza** | Sviluppo della politica, monitoraggio della conformità, indagine sugli incidenti, valutazioni |
| **Team IAM** | Processi del ciclo di vita dell'identità, manutenzione del sistema di identità, rilevamento degli account orfani |
| **Team HR** | Notifiche inserimento/trasferimento/uscita, manutenzione dei dati accurati dei dipendenti |
| **Operazioni IT** | Provisioning/de-provisioning degli accessi, implementazione tecnica |
| **Responsabili** | Approvazione degli accessi per i diretti, revisioni degli accessi, notifica delle cessazioni |
| **Proprietari dei sistemi** | Definizione dei requisiti di accesso, revisioni degli accessi specifiche del sistema |
| **Audit interno** | Verifica dell'efficacia dei controlli IAM, test di conformità |
| **Tutto il personale** | Richiedere accesso solo con necessità aziendale, utilizzare l'accesso appropriatamente, segnalare attività sospette |

---

# Governance e conformità

## Quadro di valutazione

[Organizzazione] DEVE verificare l'efficacia dei controlli IAM attraverso:

| Valutazione | Frequenza | Responsabile | Ubicazione delle prove |
|------------|-----------|-------------|------------------------|
| Inventario utenti e conformità del ciclo di vita | Mensile | Team IAM | IAM-Workbook-[AAAA-MM] (automatizzato) |
| Matrice dei diritti di accesso | Mensile | Team IAM | [Piattaforma GRC/esportazione sistema IAM] |
| Risultati della revisione degli accessi | Trimestrale | Team di sicurezza | [Sistema di ticketing], riepilogo trimestrale al RSSI |
| Conformità dei ruoli e SdC | Trimestrale | Team IAM | IAM-SoD-Workbook-[AAAA-MM] (automatizzato) |
| Cruscotto di governance IAM | Mensile | Team di sicurezza | [Strumento Business Intelligence/SharePoint] |

**Metriche di governance IAM (Cruscotto mensile)**:

- Conteggio degli account orfani e tempistica media di rimedio (obiettivo: <10 account, <30 giorni per il rimedio)
- Tasso di completamento della revisione degli accessi per tipo (obiettivo: 100% entro il periodo di revisione)
- Tasso di conformità SLA di provisioning/de-provisioning (obiettivo: >95%)
- Tasso di adozione del RBAC (percentuale utenti assegnati tramite ruoli vs. accesso diretto, obiettivo: >80%)
- Conteggio delle violazioni SdC e stato di approvazione delle eccezioni (obiettivo: <5 violazioni aperte, tutte con eccezioni approvate dal RSSI)
- Tasso di conformità all'anzianità delle password degli account di servizio (obiettivo: >95% ruotate entro 90 giorni)
- Stato di rimedio delle lacune IAM (risultati aperti per anzianità e livello di rischio)

Metriche riviste mensilmente dal Team di sicurezza, trimestralmente dal RSSI, incorporate nella revisione della direzione per la Clausola 9.3.

## Gestione delle eccezioni

Le eccezioni alla politica IAM richiedono: giustificazione aziendale documentata; valutazione del rischio del Team di sicurezza; approvazione del RSSI con controlli compensativi; documentazione nel registro delle eccezioni; revisione annuale per la necessità continuata.

## Risposta agli incidenti

Gli incidenti correlati all'IAM (compromissione dell'account, sfruttamento di account orfani, escalation dei privilegi) DEVONO essere gestiti per ISMS-POL-A.5.24-27 (Gestione degli incidenti). Il de-provisioning di emergenza DEVE avvenire entro 1 ora per gli incidenti di sicurezza.

---

# Integrazione SGSI

## Dichiarazione di Applicabilità

| Controllo | Stato | Riferimento all'implementazione |
|-----------|-------|--------------------------------|
| **A.5.15 — Controllo degli accessi** | Applicabile | Sezione 2.1, ISMS-IMP-A.5.15-16-18.1-UG/TG |
| **A.5.16 — Gestione delle identità** | Applicabile | Sezione 2.2, ISMS-IMP-A.5.15-16-18.2-UG/TG |
| **A.5.18 — Diritti di accesso** | Applicabile | Sezione 2.3, ISMS-IMP-A.5.15-16-18.3/4 |

## Controlli correlati

- **A.8.2** (Diritti di accesso privilegiato): L'IAM definisce gli utenti privilegiati, A.8.2 implementa il PAM
- **A.8.5** (Autenticazione sicura): L'IAM crea le identità, A.8.5 le autentica
- **A.5.24-27** (Gestione degli incidenti): Gli incidenti di compromissione dell'account gestiti per il quadro degli incidenti

## Risorse di implementazione

| Documento | Scopo |
|---------|-------|
| **ISMS-IMP-A.5.15-16-18.1-UG/TG** | Governance del controllo degli accessi |
| **ISMS-IMP-A.5.15-16-18.2-UG/TG** | Processo del ciclo di vita dell'identità |
| **ISMS-IMP-A.5.15-16-18.3-UG/TG** | Definizione e assegnazione dei ruoli |
| **ISMS-IMP-A.5.15-16-18.4-UG/TG** | Processo di revisione degli accessi |
| **ISMS-IMP-A.5.15-16-18.5-UG/TG** | Procedure di valutazione IAM |

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Identità** | Rappresentazione digitale di un utente (persona, servizio, dispositivo) con identificativo univoco |
| **Controllo degli accessi** | Tecnica di sicurezza che regola chi può visualizzare o utilizzare le risorse |
| **RBAC** | Modello di controllo degli accessi in cui le autorizzazioni sono assegnate ai ruoli piuttosto che agli individui |
| **Minimo privilegio** | Principio che richiede l'accesso minimo necessario per la funzione lavorativa |
| **Separazione dei compiti (SdC)** | Pratica di dividere i compiti critici per prevenire frodi ed errori |
| **Inserimento (Joiner)** | Onboarding di nuovi utenti inclusa la creazione dell'account e il provisioning degli accessi |
| **Trasferimento (Mover)** | Gestione dei cambi di ruolo degli utenti incluso l'adeguamento degli accessi |
| **Uscita (Leaver)** | Offboarding inclusa la disabilitazione dell'account e la rimozione degli accessi |
| **Account orfano** | Account senza proprietario aziendale valido che richiede rimedio |
| **Accumulo di privilegi** | Accumulo di diritti di accesso eccessivi nel tempo durante i cambi di ruolo |
| **Account di servizio** | Account non umano utilizzato per i processi automatizzati |
| **Account di emergenza** | Account privilegiato di emergenza per scenari di emergenza |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data] |
| **Direttore dei Sistemi Informativi (DSI)** | [Nome] | [Data] |
| **Direttore delle Risorse Umane (DRH)** | [Nome] | [Data] |
| **Responsabile Legale/Conformità** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la gestione delle identità e degli accessi. Le procedure di attuazione sono documentate in ISMS-IMP-A.5.15-16-18 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
