<!-- ISMS-CORE:POLICY:ISMS-POL-A.6.7-8-IT:framework:POL:a.6.7-8 -->
**ISMS-POL-A.6.7-8 — Lavoro da remoto e segnalazione degli eventi di sicurezza**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Lavoro da remoto e segnalazione degli eventi di sicurezza delle informazioni |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.6.7-8 |
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
- Secondario: Direttore delle Risorse Umane (DRH)
- Tecnico: Direttore IT / Direttore della Tecnologia (DT)
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-IMP-A.6.7-8.S1–S4 (Suite di orientamento all'implementazione e valutazione)
- ISO/IEC 27001:2022 Controlli A.6.7, A.6.8
- ISMS-POL-A.5.1-2-6.1-2 (Impiego sicuro e ruoli)
- ISMS-POL-A.6.3 (Sensibilizzazione e formazione)
- ISMS-POL-A.5.24-28 (Ciclo di vita della gestione degli incidenti)
- ISMS-POL-A.8.1-7-18-19 (Sicurezza degli endpoint)

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la sicurezza del lavoro da remoto e la segnalazione degli eventi di sicurezza delle informazioni, conformemente ai Controlli A.6.7 e A.6.8 della norma ISO/IEC 27001:2022.

**Perimetro**: Questa politica si applica a tutto il personale che lavora da remoto o al di fuori dei locali di [Organizzazione], a tutti i dispositivi utilizzati per il lavoro da remoto (aziendali e personali), a tutte le informazioni a cui si accede o che vengono elaborate da remoto, e a tutto il personale responsabile della segnalazione degli eventi di sicurezza indipendentemente dall'ubicazione di lavoro.

**Quadro di controlli combinati**: Questi due controlli sono implementati come un quadro unificato perché: i lavoratori da remoto sono in prima linea nel rilevamento degli eventi; il lavoro da remoto presenta minacce specifiche che richiedono una segnalazione specializzata; ISO 27002:2022 li collega esplicitamente; interessano la stessa popolazione di personale.

**Allineamento normativo**: nLPD svizzera (Art. 8); RGPD dell'UE (Artt. 32 e 33); ISO/IEC 27001:2022; NIS2, DORA, FINMA, PCI DSS v4.0.1 (applicabilità condizionale per ISMS-POL-00).

---

# Allineamento sul controllo e perimetro

## Controllo A.6.7 — Lavoro da remoto

> *Devono essere attuate misure di sicurezza quando il personale lavora da remoto per proteggere le informazioni a cui si accede, che vengono elaborate o archiviate al di fuori dei locali dell'organizzazione.*

**Obiettivo del controllo**: Garantire che il personale remoto disponga dei controlli di sicurezza necessari per salvaguardare la riservatezza, l'integrità e la disponibilità delle informazioni organizzative.

**Tipo di controllo**: Preventivo | **Categoria**: Controllo sulle persone

## Controllo A.6.8 — Segnalazione degli eventi di sicurezza delle informazioni

> *L'organizzazione deve fornire un meccanismo per consentire al personale di segnalare gli eventi di sicurezza delle informazioni osservati o sospettati attraverso canali appropriati in modo tempestivo.*

**Obiettivo del controllo**: Supportare la segnalazione tempestiva, coerente ed efficace degli eventi di sicurezza delle informazioni che possono essere identificati dal personale.

**Tipo di controllo**: Detective | **Categoria**: Controllo sulle persone

## Perimetro

**Questa politica si applica a**:

**Personale**: Tutti i dipendenti che lavorano da remoto; tutti gli appaltatori e consulenti che lavorano da locali non di [Organizzazione]; tutto il personale terzo con accesso remoto; tutto il personale in viaggio; tutto il personale che può osservare o segnalare eventi di sicurezza.

**Modalità di lavoro da remoto**: Lavoro da casa; spazi di co-working; locali di clienti o partner; lavoro in viaggio (hotel, aeroporti, spazi pubblici); qualsiasi lavoro svolto al di fuori dei locali controllati di [Organizzazione].

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria**:

| Normativa | Applicabilità | Requisiti chiave |
|-----------|---------------|-----------------|
| **nLPD svizzera** | Tutte le operazioni svizzere | Art. 8 — Misure tecniche e organizzative appropriate per la protezione dei dati negli ambienti remoti |
| **RGPD dell'UE** | Trattamento di dati personali UE | Art. 32 — La sicurezza del trattamento deve estendersi al lavoro da remoto; Art. 33 — Notifica delle violazioni entro 72 ore richiede il rilevamento tempestivo degli eventi |
| **ISO/IEC 27001:2022** | Ambito di certificazione | Controlli A.6.7 (Lavoro da remoto), A.6.8 (Segnalazione eventi) |

**Livello 2 — Applicabilità condizionale**: NIS2 (entità essenziale/importante UE); DORA (entità finanziaria UE); FINMA Circolare 2008/21 (istituto finanziario svizzero regolamentato); PCI DSS v4.0.1 (trattamento di dati di carte di pagamento).

---

# Requisiti per il lavoro da remoto (Controllo A.6.7)

## Autorizzazione al lavoro da remoto

[Organizzazione] DEVE stabilire un processo di autorizzazione formale per le modalità di lavoro da remoto.

**Requisiti di autorizzazione**:

| Requisito | Descrizione |
|-----------|-------------|
| **Approvazione formale** | Tutti i regolari accordi di lavoro da remoto DEVONO essere formalmente approvati prima dell'inizio |
| **Autorità di autorizzazione** | I responsabili diretti autorizzano il lavoro da remoto; la Sicurezza IT approva l'accesso tecnico |
| **Valutazione del rischio** | DEVE essere eseguita una valutazione del rischio per i ruoli che gestiscono dati sensibili da remoto |
| **Criteri di valutazione del rischio** | La valutazione DEVE considerare almeno: (a) Livello di classificazione dei dati a cui si accede da remoto; (b) Capacità di sicurezza fisica dell'ubicazione remota; (c) Postura di sicurezza della rete; (d) Conformità alla base di sicurezza del dispositivo; (e) Restrizioni normative o contrattuali |
| **Accordo documentato** | I lavoratori da remoto DEVONO riconoscere i requisiti di sicurezza del lavoro da remoto |
| **Revisione periodica** | Le autorizzazioni al lavoro da remoto DEVONO essere riviste almeno annualmente |

**Revoca dell'autorizzazione**: L'autorizzazione al lavoro da remoto DEVE essere revocata quando il rapporto di lavoro o il contratto termina; il ruolo cambia in uno non adatto al lavoro da remoto; i requisiti di sicurezza non vengono mantenuti; si verificano violazioni della politica.

## Requisiti di sicurezza fisica

I lavoratori da remoto DEVONO:

- Posizionare gli schermi per impedire la visualizzazione non autorizzata da parte di altri
- Utilizzare schermi per la privacy quando si lavora in spazi condivisi o pubblici
- Proteggere le apparecchiature di lavoro quando la postazione è incustodita
- Impedire l'accesso ai dispositivi di lavoro da parte di familiari, visitatori o altre persone non autorizzate
- Archiviare i documenti sensibili in modo sicuro quando non in uso attivo
- Smaltire i documenti sensibili con metodi approvati (tritatura)

**Requisiti sulla scrivania libera**: La politica sulla scrivania libera (per A.7.7) SI ESTENDE agli ambienti di lavoro da remoto. I materiali di lavoro devono essere protetti alla fine di ogni sessione di lavoro.

## Requisiti di sicurezza tecnica

**Requisiti di connessione sicura**:

| Requisito | Obbligatorio per |
|-----------|-----------------|
| **VPN o accesso Zero Trust** | Tutte le connessioni alle risorse interne |
| **Autenticazione a più fattori (AMF)** | Tutto l'accesso remoto ai sistemi organizzativi |
| **Comunicazioni cifrate** | Tutte le trasmissioni di dati (minimo TLS 1.2) |
| **DNS aziendale** | Risoluzione tramite DNS organizzativo quando connesso |

**Requisiti di sicurezza della rete**: I lavoratori da remoto DEVONO utilizzare solo reti wireless sicure e cifrate (minimo WPA2/WPA3); evitare il Wi-Fi pubblico non protetto per il lavoro organizzativo senza protezione VPN; non disabilitare o aggirare i controlli di sicurezza; segnalare preoccupazioni o anomalie di sicurezza della rete.

## Requisiti di gestione dei dati

**Conservazione dei dati per classificazione**:

| Classificazione dei dati | Conservazione remota consentita | Condizioni |
|--------------------------|--------------------------------|-----------|
| **Pubblico** | Sì | Sicurezza standard del dispositivo |
| **Interno** | Sì | Dispositivo cifrato, ubicazione sicura |
| **Riservato** | Condizionale | Solo dispositivi cifrati e approvati, giustificazione aziendale |
| **Limitato** | No (per impostazione predefinita) | Richiede approvazione esplicita del RSSI, controlli avanzati |

**Processo di autorizzazione condizionale**: La conservazione remota di dati Riservati richiede: (a) Giustificazione aziendale scritta del responsabile diretto; (b) Verifica dei controlli tecnici (cifratura del dispositivo, ubicazione di archiviazione sicura); (c) Approvazione del Responsabile della Sicurezza IT. I dati Limitati richiedono approvazione scritta del RSSI con controlli compensativi documentati.

## Sicurezza dei dispositivi

**Requisiti per i dispositivi aziendali**: Configurati per la base di sicurezza organizzativa (per A.8.9); cifratura completa del disco attivata; software di protezione endpoint aggiornato (per A.8.7); aggiornati per calendario organizzativo (per A.8.8); capacità di cancellazione remota attivata; registrati nell'inventario dei dispositivi (per A.5.9).

**Requisiti per i dispositivi personali (BYOD)**: Soddisfano i requisiti minimi di sicurezza definiti dalla Sicurezza IT; soluzione MDM/EMM organizzativa installata (se richiesta); separazione tra dati personali e di lavoro (containerizzazione); soggetti alla cancellazione remota dei dati organizzativi alla cessazione del rapporto.

**Dispositivi vietati**: Dispositivi jailbroken o con root; dispositivi con funzionalità di sicurezza disabilitate; dispositivi condivisi non sotto il controllo dell'utente; dispositivi con sistemi operativi a fine vita senza aggiornamenti di sicurezza.

---

# Requisiti di segnalazione degli eventi di sicurezza (Controllo A.6.8)

## Meccanismi di segnalazione

[Organizzazione] DEVE fornire meccanismi accessibili per la segnalazione degli eventi di sicurezza.

**Requisiti del canale di segnalazione**:

| Requisito | Descrizione |
|-----------|-------------|
| **Canali multipli** | DEVONO essere disponibili almeno due canali di segnalazione distinti |
| **Disponibilità 24/7** | Almeno un canale DEVE essere disponibile al di fuori degli orari lavorativi |
| **Accessibilità remota** | Tutti i canali DEVONO essere accessibili da ubicazioni remote |
| **Informazioni di contatto chiare** | I contatti per la segnalazione DEVONO essere pubblicati in modo prominente |
| **Conferma di ricezione** | Tutti i report DEVONO essere confermati entro termini definiti |

**Canali di segnalazione standard**: Email di sicurezza (indirizzo email dedicato); telefono/linea diretta (per questioni urgenti); sistema di ticketing (per eventi non urgenti); opzione anonima (meccanismo per la segnalazione anonima dove appropriato).

**Segnalazione anonima**: DEVE essere supportata attraverso: (a) Alias email dedicato che non richiede autenticazione; (b) Modulo web accessibile senza accesso; (c) Linea di terze parti se implementata. **Limitazioni**: la segnalazione anonima può precludere domande di follow-up e feedback dettagliato. I segnalatori sono incoraggiati a fornire informazioni di contatto dove si sentono a proprio agio, con garanzia di riservatezza.

## Tipi di eventi da segnalare

**Distinzione evento/incidente**:

| Termine | Definizione |
|---------|-------------|
| **Evento di sicurezza** | Occorrenza identificata che indica una *possibile* violazione della politica o un guasto dei controlli |
| **Incidente di sicurezza** | Evento valutato come avente una *significativa probabilità* di compromettere le operazioni o minacciare la sicurezza |

**Il personale segnala gli EVENTI. Il Team di Sicurezza IT valuta se gli eventi costituiscono INCIDENTI.**

**Categorie di eventi segnalabili**:

- **Phishing e ingegneria sociale**: Email sospette che richiedono credenziali; telefonate o messaggi di testo sospetti; tentativi di manipolazione per aggirare i controlli di sicurezza
- **Malware e compromissione del sistema**: Comportamento di sistema inaspettato; pop-up, messaggi o notifiche sospetti; sospetta infezione da malware (NUOVO in ISO 27002:2022); indicatori di ransomware
- **Accesso non autorizzato**: Tentativi di accesso sconosciuti ai propri account; dispositivi non familiari connessi ai propri account; blocchi account o modifiche di password inaspettati
- **Violazione e perdita di dati**: Email inviate per errore contenenti informazioni sensibili; accesso o esposizione non autorizzata di dati; dispositivi o documenti persi o rubati
- **Sicurezza fisica**: Dispositivi persi o rubati (laptop, telefoni, unità USB); accesso fisico non autorizzato; persone sospette in aree sicure
- **Violazioni della politica**: Aggiramento dei controlli di sicurezza osservato; modifiche ai sistemi non elaborate tramite il controllo dei cambiamenti (NUOVO in ISO 27002:2022)
- **Specifici del lavoro da remoto**: Sospetta compromissione della rete domestica; accesso non autorizzato al dispositivo di lavoro da parte di altri; problemi VPN o di accesso remoto che suggeriscono un attacco; attività sospetta durante il lavoro da luoghi pubblici; tentativi di accesso da dispositivi non approvati; richieste sospette di supporto IT per credenziali di accesso remoto; osservazione fisica di materiali di lavoro da parte di persone non autorizzate

## Procedure di segnalazione

**Tempestività della segnalazione**:

| Gravità dell'evento | Termine di segnalazione |
|--------------------|------------------------|
| **Critico** (attacco attivo, violazione dei dati, ransomware) | Immediatamente |
| **Alto** (dispositivo perso, compromissione delle credenziali) | Entro 1 ora |
| **Medio** (tentativo di phishing, attività sospetta) | Entro 4 ore |
| **Basso** (preoccupazione sulla politica, osservazione generale) | Entro 24 ore |

**Determinazione della gravità**: I segnalatori DEVONO segnalare in base alla loro migliore valutazione della gravità. In caso di incertezza, segnalare al livello di gravità superiore. Il Team di Sicurezza IT rivaluterà la gravità durante il triage iniziale. I segnalatori NON DEVONO ritardare la segnalazione per determinare la classificazione precisa.

**Responsabilità del segnalatore**: Il personale DEVE: segnalare tempestivamente; fornire informazioni accurate; conservare le prove potenziali (inoltrare le email di phishing come allegato preservando le intestazioni; fare screenshot dei messaggi di errore); NON tentare di investigare o verificare l'evento; NON tentare di testare o sfruttare presunte vulnerabilità; cooperare con qualsiasi indagine successiva.

## Cultura della non colpevolizzazione

[Organizzazione] DEVE favorire un ambiente non punitivo per la segnalazione degli eventi di sicurezza.

| Principio | Impegno |
|-----------|---------|
| **Protezione della buona fede** | Il personale che segnala eventi in buona fede NON deve subire conseguenze negative per l'atto di segnalazione |
| **Gestione degli errori onesti** | Gli errori onesti segnalati tempestivamente DEVONO essere gestiti in modo costruttivo, concentrandosi sull'apprendimento |
| **Nessuna ritorsione** | Le ritorsioni contro i segnalatori in buona fede sono vietate e soggette ad azioni disciplinari |
| **Riservatezza** | L'identità del segnalatore DEVE essere protetta nella misura del possibile |

**Eccezioni**: I principi della non colpevolizzazione NON proteggono: le violazioni deliberate della politica segnalate solo dopo la scoperta; l'attività dolosa camuffata da accidentale; la negligenza ripetuta dopo la formazione e gli avvertimenti; le false segnalazioni in mala fede.

## Risposta e feedback

**Tempistiche di risposta**:

| Tipo di risposta | Termine |
|-----------------|---------|
| **Conferma di ricezione** | Entro 4 ore lavorative |
| **Valutazione iniziale** | Entro 24 ore |
| **Aggiornamento di stato al segnalatore** | Entro 72 ore |
| **Notifica di chiusura** | Al momento della risoluzione |

---

# Ruoli e responsabilità

| Ruolo | Lavoro da remoto (A.6.7) | Segnalazione eventi (A.6.8) |
|-------|--------------------------|----------------------------|
| **Direzione generale** | Approvare la politica; fornire risorse | Promuovere la cultura della non colpevolizzazione; ricevere briefing sugli incidenti critici |
| **RSSI** | Definire i requisiti di sicurezza; autorizzare le eccezioni; rivedere la conformità | Definire i meccanismi di segnalazione; supervisionare la risposta; riferire alla direzione |
| **Team di Sicurezza IT** | Implementare i controlli tecnici; monitorare la conformità | Ricevere i report; valutare gli eventi; coordinare la risposta; fornire feedback |
| **Operazioni IT** | Provisioning dell'accesso remoto; manutenzione VPN/AMF; supporto dei dispositivi | Supportare i canali di segnalazione; implementare le azioni di contenimento |
| **HR** | Gestire gli accordi di lavoro da remoto; coordinare le cessazioni | Includere la segnalazione nell'onboarding; gestire gli incidenti relativi al personale |
| **Responsabili diretti** | Autorizzare il lavoro da remoto; garantire la conformità del team | Incoraggiare la segnalazione; escalare le preoccupazioni del team |
| **Tutto il personale** | Rispettare i requisiti del lavoro da remoto; proteggere i dispositivi e i dati | Segnalare gli eventi tempestivamente; conservare le prove; cooperare con le indagini |

---

# Governance e conformità

## Revisione della politica

| Aspetto | Requisito |
|---------|-----------|
| **Frequenza di revisione** | Annuale, o in caso di cambiamento significativo |
| **Autorità di revisione** | RSSI con approvazione della Direzione generale |
| **Revisioni attivate** | Incidente di sicurezza importante, cambiamento normativo, cambiamento tecnologico, ristrutturazione organizzativa |

## Non conformità

**Conseguenze della non conformità**: Le violazioni di questa politica possono comportare: revoca dei privilegi di lavoro da remoto; formazione aggiuntiva obbligatoria sulla sicurezza; azione disciplinare per politiche HR; risoluzione del rapporto di lavoro o contratto per violazioni gravi.

## Gestione delle eccezioni

Le eccezioni a questa politica richiedono: giustificazione aziendale documentata; valutazione del rischio dell'eccezione; controlli compensativi dove applicabile; approvazione del RSSI (o delegato); durata limitata con data di revisione; documentazione nel registro delle eccezioni.

**Autorità di eccezione**:

| Tipo di eccezione | Autorità di approvazione |
|------------------|--------------------------|
| Eccezioni standard (deviazioni minori) | Responsabile della Sicurezza IT |
| Eccezioni ad alto rischio (dati sensibili, durata estesa) | RSSI |
| Deroghe alla politica (requisiti fondamentali) | Direzione generale |

---

# Prove per questa politica

**Prove per la Fase 1**: Documento di politica (v1.0) con firme di approvazione; procedura di autorizzazione al lavoro da remoto documentata; documentazione del canale di segnalazione pubblicata; materiali formativi; registro delle eccezioni.

**Prove per la Fase 2**: Campioni di autorizzazione al lavoro da remoto; documenti di riconoscimento della politica; registrazioni di completamento della formazione; report di conformità tecnica (utilizzo VPN, iscrizione AMF, stato di cifratura del dispositivo); campioni di report di eventi di sicurezza; registrazioni di risposta tempestiva agli eventi segnalati; cruscotto delle metriche di conformità.

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

*Questa politica stabilisce i requisiti per il lavoro da remoto e la segnalazione degli eventi di sicurezza delle informazioni. Le procedure di attuazione sono documentate in ISMS-IMP-A.6.7-8 (UG/TG), da .S1 a .S4.*

<!-- QA_VERIFIED: 2026-04-03 -->
