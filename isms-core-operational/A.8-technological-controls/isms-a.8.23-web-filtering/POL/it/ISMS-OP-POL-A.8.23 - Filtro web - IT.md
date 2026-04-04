<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.23-IT:operational:OP-POL:a.8.23 -->
**ISMS-OP-POL-A.8.23 — Filtro web**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Filtro web |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.23 |
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

- ISO/IEC 27001:2022 Controllo A.8.23 — Filtro web

**Controlli correlati dell'Annex A**:

| Controllo | Relazione con il filtro web |
|-----------|------------------------------|
| A.5.7 Intelligence sulle minacce | I feed di intelligence sulle minacce informano le liste di blocco del filtro web e la categorizzazione degli URL |
| A.5.10 Uso accettabile delle informazioni | La politica di uso accettabile definisce l'utilizzo del web consentito e vietato |
| A.8.7 Protezione contro il malware | Il filtro web previene la consegna di malware tramite download drive-by e siti web malevoli |
| A.8.16 Attività di monitoraggio | I log del filtro web alimentano il monitoraggio della sicurezza e il rilevamento delle anomalie |
| A.8.20 Sicurezza della rete | Il filtro web è un controllo di sicurezza a livello di rete |
| A.8.21 Sicurezza dei servizi di rete | Il Gateway web sicuro (SWG) è un servizio di sicurezza della rete gestito |
| A.8.22 Segregazione delle reti | Il filtro web applicato ai confini dei segmenti di rete |
| A.8.24 Uso della crittografia | Considerazioni sull'ispezione TLS per il traffico web crittografato |

**Politiche interne correlate**:

- Politica di uso accettabile
- Politica di sicurezza della rete
- Politica di sicurezza degli endpoint
- Politica delle attività di monitoraggio (A.8.16)
- Politica di protezione contro il malware
- Politica sulla privacy e protezione dei dati personali

---

# Politica di filtro web

## Scopo

Lo scopo di questa politica è gestire l'accesso ai siti web esterni per ridurre l'esposizione a contenuti malevoli, prevenire la perdita di dati tramite canali web e applicare i requisiti di uso accettabile. Il filtro web protegge i sistemi organizzativi dal malware consegnato tramite download drive-by, siti di phishing e altre minacce veicolate dal web.

Il filtro web è un controllo chiave identificato attraverso la valutazione del rischio per la sicurezza delle informazioni dell'organizzazione. Le decisioni sull'ambito del filtraggio e sulle categorie contenute in questa politica sono direttamente informate dal piano di trattamento del rischio, affrontando rischi tra cui: infezione da malware tramite minacce veicolate dal web, furto di credenziali tramite phishing, perdita di dati tramite servizi web non autorizzati e danno reputazionale da accesso a contenuti inappropriati.

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 implementando il filtro web come misura tecnica per proteggere i dati personali dalla compromissione tramite vettori di attacco web. Il filtro web che monitora l'attività di navigazione dei dipendenti DEVE essere conforme al diritto del lavoro svizzero (CO svizzero Art. 328/328b) e al divieto di sorveglianza comportamentale (OLL3 Art. 26). Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 32.

## Ambito di applicazione

Questa politica si applica a:

- Tutto il traffico web (HTTP/HTTPS) originante da dispositivi e reti gestiti dall'organizzazione.
- Tutti i dipendenti, i collaboratori e gli utenti terzi che accedono a Internet tramite l'infrastruttura dell'organizzazione.
- Tutti gli ambienti: rete aziendale, lavoratori remoti (tramite VPN o proxy cloud) e reti ospiti (ambito limitato).
- Tutti i metodi di accesso web: browser, applicazioni che effettuano chiamate HTTP/HTTPS e connessioni API a servizi esterni.

Fuori ambito:
- Filtraggio della posta elettronica (disciplinato dalle politiche di sicurezza degli endpoint e di protezione contro il malware).
- Controlli a livello applicativo per piattaforme SaaS specifiche (disciplinati dalla politica sui servizi cloud, A.5.19-23).

## Principio

L'accesso ai siti web esterni DEVE essere gestito per ridurre l'esposizione a contenuti malevoli. Il filtro web DEVE operare secondo un approccio basato sul rischio: bloccare automaticamente le minacce note, limitare le categorie discrezionali per policy e consentire l'accesso aziendale legittimo senza attrito inutile. Il filtraggio DEVE essere applicato in modo coerente indipendentemente dalla posizione o dal dispositivo dell'utente.

---

## Architettura del filtro web

### Approccio al filtraggio

L'organizzazione DEVE implementare il filtro web utilizzando una o più delle seguenti tecnologie:

| Livello | Tecnologia | Scopo |
|---------|-----------|-------|
| **Filtraggio DNS** | Servizio di filtraggio a livello DNS (ad es. Cisco Umbrella, Cloudflare Gateway, DNSFilter o equivalente) | Prima linea di difesa; blocca la risoluzione di domini malevoli e vietati prima che la connessione venga stabilita |
| **Filtraggio URL** | Gateway web sicuro (SWG) o proxy con database di categorizzazione URL | Ispeziona il percorso URL completo; applica policy basate su categorie; fornisce un controllo granulare |
| **Ispezione TLS** | SWG o proxy che eseguono la decrittografia e l'ispezione SSL/TLS | Ispeziona il traffico web crittografato per le minacce nascoste in HTTPS (si applica a categorie selezionate — vedere la sezione Ispezione TLS) |
| **Isolamento del browser** (opzionale) | Remote Browser Isolation (RBI) per siti ad alto rischio o non categorizzati | Esegue il rendering del contenuto web in una sandbox cloud; solo l'output visivo sicuro viene trasmesso all'utente |

### Modello di distribuzione

| Ambiente | Metodo di filtraggio |
|----------|---------------------|
| **Rete aziendale** | SWG/proxy o filtraggio DNS applicato al perimetro di rete |
| **Lavoratori remoti** | SWG cloud o agente di filtraggio DNS su endpoint gestiti; policy coerente indipendentemente dalla rete |
| **Dispositivi BYOD** | Filtraggio DNS (leggero, rispettoso della privacy); l'ispezione TLS **non** DEVE essere eseguita sui dispositivi personali |
| **Rete ospiti** | Filtraggio DNS solo per le categorie malware/phishing; filtraggio delle categorie discrezionali non applicato |

Il filtraggio DNS DEVE essere applicato su tutti i dispositivi gestiti come baseline. Le query DNS dirette verso resolver esterni (incluso DNS over HTTPS (DoH) e DNS over TLS (DoT) verso resolver non approvati) DEVONO essere bloccate al firewall per impedire l'elusione del filtro.

### Disponibilità e prestazioni (SOC 2: A1.1)

La piattaforma di filtro web DEVE soddisfare i seguenti obiettivi di livello di servizio:

| SLO | Obiettivo | Misurazione |
|-----|-----------|-------------|
| **Disponibilità** | ≥99,9% di uptime (misurato mensilmente) | Dashboard di monitoraggio della piattaforma |
| **Latenza** | ≤50ms di latenza aggiuntiva per richiesta web (p95) | Test di prestazioni periodici |
| **Failover** | Failover automatico al percorso di filtraggio secondario o fail-open entro 5 minuti | Test di failover annuale |
| **Capacità** | Piattaforma dimensionata per il traffico di picco + 30% di margine | Revisione trimestrale della capacità |

Se la piattaforma di filtraggio subisce un degrado prolungato che supera le soglie SLO, IT Operations DEVE implementare la procedura documentata di risposta agli incidenti. Il fail-open (consentire traffico non filtrato) è consentito solo come misura temporanea durante un guasto della piattaforma e DEVE essere registrato, segnalato al RSSI e rimediato entro 4 ore.

### Gestione delle modifiche per le regole di filtraggio (SOC 2: CC8.1)

Le modifiche alla configurazione del filtro web (policy delle categorie, liste di blocco/consentiti, impostazioni di ispezione TLS, architettura di distribuzione) DEVONO seguire il processo di gestione delle modifiche dell'organizzazione:

1. **Richiesta**: Richiesta di modifica inviata con giustificazione, ambito e valutazione del rischio.
2. **Revisione**: La sicurezza IT esamina la modifica per le implicazioni di sicurezza; il Consulente per la protezione dei dati esamina l'impatto sulla privacy se il monitoraggio dei dipendenti è interessato.
3. **Test**: Le modifiche vengono testate in un ambiente di staging o in una distribuzione limitata ove fattibile.
4. **Approvazione**: Le modifiche standard sono approvate dal responsabile della sicurezza IT; le modifiche significative (nuovi blocchi di categoria, modifiche all'ambito dell'ispezione TLS) sono approvate dal RSSI.
5. **Implementazione**: Modifica distribuita da IT Operations durante la finestra di manutenzione approvata.
6. **Verifica**: Verifica post-implementazione che la modifica funzioni come previsto.
7. **Documentazione**: Modifica registrata nel log delle modifiche con gli stati di configurazione prima e dopo.

Le modifiche d'emergenza (ad es. blocco di una campagna di phishing attiva) possono bypassare l'approvazione standard ma DEVONO essere documentate retrospettivamente entro 24 ore.

### Gestione dei fornitori (SOC 2: CC9.2)

Laddove il filtro web sia fornito da un servizio di terze parti (SWG cloud, provider di filtraggio DNS):

- Il fornitore DEVE essere incluso nel programma di gestione dei rischi dei fornitori dell'organizzazione.
- Il rapporto SOC 2 Tipo II o la certificazione ISO 27001 DEVONO essere revisionati annualmente.
- La conformità agli SLA (disponibilità, latenza, tasso di rilevamento delle minacce, tempo di risposta del supporto) DEVE essere monitorata rispetto alle soglie contrattuali.
- Gli accordi sul trattamento dei dati DEVONO riguardare: la gestione dei dati di navigazione dei dipendenti, la residenza dei dati, i periodi di conservazione e la notifica degli incidenti.
- Il rischio di dipendenza dal fornitore DEVE essere valutato; l'organizzazione DEVE mantenere la capacità di migrare a un provider alternativo entro un periodo di tempo ragionevole.

---

## Categorizzazione URL e regole di filtraggio

### Blocco obbligatorio — Categorie di minacce alla sicurezza

Le seguenti categorie DEVONO essere bloccate per tutti gli utenti senza eccezioni:

| N. | Categoria | Motivazione |
|----|-----------|-------------|
| 1 | **Distribuzione malware** | Siti che ospitano o distribuiscono attivamente malware, exploit kit o download drive-by |
| 2 | **Phishing e frode** | Siti progettati per raccogliere credenziali, informazioni finanziarie o dati personali |
| 3 | **Command and Control (C2)** | Infrastruttura botnet e APT nota |
| 4 | **Ransomware** | Siti di distribuzione, pagamento e comunicazione ransomware |
| 5 | **Spyware e adware** | Siti che distribuiscono software indesiderato o strumenti di tracciamento |
| 6 | **Cryptomining** | Siti che eseguono script di mining di criptovalute non autorizzati |
| 7 | **Exploit kit** | Siti che ospitano framework di exploitation di browser e plugin |
| 8 | **DNS dinamico (malevolo)** | Frequentemente utilizzato per infrastrutture malevole; bloccare i provider DNS dinamici noti come malevoli |
| 9 | **Contenuti illegali** | Contenuti vietati dalla legge svizzera o applicabile |
| 10 | **Materiale di abuso sui minori** | Obbligo legale obbligatorio di blocco |

### Blocco obbligatorio — Categorie di policy

Le seguenti categorie DEVONO essere bloccate a meno che non esista un'eccezione approvata:

| N. | Categoria | Motivazione |
|----|-----------|-------------|
| 11 | **Elusione del proxy e anonimizzatori** | Proxy web, servizi VPN e nodi Tor utilizzati per aggirare i controlli di filtraggio |
| 12 | **Strumenti e risorse di hacking** | Database di exploit, tutorial di hacking e distribuzione di strumenti di attacco (eccezione: team di sicurezza con giustificazione documentata) |
| 13 | **Condivisione file peer-to-peer** | Rischio di perdita di dati e vettore di malware |
| 14 | **Violazione del copyright / pirateria** | Rischio di proprietà intellettuale e legale |

### Restrizione discrezionale — Categorie monitorate

Le seguenti categorie possono essere limitate, monitorate o consentite in base alla policy organizzativa:

| N. | Categoria | Policy predefinita | Note |
|----|-----------|-------------------|------|
| 15 | **Archiviazione cloud personale** (Dropbox, Google Drive personale, ecc.) | Limitare | Rischio di perdita di dati; archiviazione cloud aziendale consentita |
| 16 | **Webmail personale** (Gmail, Outlook personale, ecc.) | Limitare | Rischio di perdita di dati; e-mail aziendale consentita |
| 17 | **Social media** | Consentire con monitoraggio | Esistono casi d'uso aziendali; limitare i caricamenti ove fattibile |
| 18 | **Streaming media / video** | Consentire con limiti di banda | Gestione della larghezza di banda; limitare durante le ore di picco se necessario |
| 19 | **Gaming** | Bloccare durante l'orario lavorativo | Produttività; consentire fuori orario se desiderato |
| 20 | **Contenuti per adulti** | Bloccare | Appropriatezza sul luogo di lavoro |
| 21 | **Gioco d'azzardo** | Bloccare | Appropriatezza sul luogo di lavoro e rischio legale |

### Consentito — Categorie business-critical

Le seguenti categorie NON devono essere filtrate o limitate:

| Categoria | Esempi |
|-----------|--------|
| **Business e finanza** | Portali bancari, portali di settore, servizi professionali |
| **Governo e legale** | Siti normativi, portali governativi, database giuridici |
| **Tecnologia e IT** | Fornitori di software, documentazione, risorse per sviluppatori |
| **Istruzione e formazione** | Piattaforme e-learning, sviluppo professionale, risorse accademiche |
| **Notizie e media** | Principali testate giornalistiche, pubblicazioni di settore |
| **Motori di ricerca** | Google, Bing, DuckDuckGo |
| **Applicazioni SaaS aziendali** | Applicazioni cloud approvate per il registro SaaS dell'organizzazione |

### Siti web non categorizzati

I siti web non categorizzati dalla soluzione di filtraggio DEVONO essere gestiti come segue:

- **Predefinito**: Consentire con registrazione (per le organizzazioni con minore propensione al rischio: limitare con opzione di override da parte dell'utente).
- Tutti gli accessi a siti non categorizzati DEVONO essere registrati per revisione della sicurezza.
- Se è distribuito l'isolamento del browser, i siti non categorizzati dovrebbero essere visualizzati tramite isolamento per default.

---

## Ispezione TLS

### Scopo

Circa l'80% del traffico web è crittografato (HTTPS). Senza l'ispezione TLS, le minacce nascoste nel traffico crittografato non possono essere rilevate dalla soluzione di filtro web. L'ispezione TLS decrittografa, ispeziona e ri-crittografa il traffico HTTPS al SWG/proxy.

### Requisiti

| Requisito | Specifica |
|-----------|-----------|
| **Distribuzione** | L'ispezione TLS DEVE essere abilitata sul SWG/proxy per il traffico dai dispositivi gestiti dall'organizzazione |
| **Certificato** | Un certificato CA radice privato DEVE essere distribuito su tutti gli endpoint gestiti tramite MDM, Group Policy o equivalente |
| **Firefox** | Firefox utilizza il proprio archivio certificati; il CA radice privato DEVE essere distribuito separatamente tramite la policy enterprise di Firefox |
| **Prestazioni** | Il SWG/proxy DEVE essere dimensionato per il carico di lavoro dell'ispezione TLS; il protocollo QUIC (UDP 443) DEVE essere bloccato per forzare l'ispezione HTTPS basata su TCP |

### Esclusioni per la privacy — Categorie da esonerare dall'ispezione TLS

Le seguenti categorie DEVONO essere **escluse** dall'ispezione TLS per proteggere la privacy ed evitare problemi tecnici:

| N. | Categoria | Motivo |
|----|-----------|--------|
| 1 | **Finanza / bancario** | Sensibilità delle credenziali; considerazioni normative |
| 2 | **Sanità** | Privacy dei dati sanitari (dati personali degni di particolare protezione ai sensi della nLPD) |
| 3 | **Portali governativi** | Sensibilità normativa |
| 4 | **Applicazioni con certificate pinning** | Incompatibilità tecnica (ad es. alcune API, applicazioni finanziarie) |
| 5 | **Dispositivi personali (BYOD)** | Nessuna base giuridica per l'ispezione TLS sui dispositivi personali |

### Requisiti legali per l'ispezione TLS

- I dipendenti DEVONO essere informati in anticipo che il traffico web crittografato può essere decrittografato e ispezionato per scopi di sicurezza.
- La politica di uso accettabile DEVE documentare l'ispezione TLS e il suo scopo.
- I dati dell'ispezione TLS DEVONO essere trattati solo per scopi di sicurezza (rilevamento malware, prevenzione della perdita di dati, applicazione delle policy) — non per il monitoraggio comportamentale.
- Il traffico BYOD e della rete ospiti **non** DEVE essere soggetto all'ispezione TLS.

---

## Integrazione dell'intelligence sulle minacce

### Aggiornamenti delle liste di blocco

Le liste di blocco del filtro web DEVONO essere aggiornate utilizzando l'intelligence sulle minacce da più fonti:

| Tipo di fonte | Esempi | Frequenza di aggiornamento |
|---------------|--------|---------------------------|
| **Fornita dal fornitore** | Database di categorizzazione URL del fornitore della soluzione di filtraggio | In tempo reale o giornaliero (automatico) |
| **Feed di intelligence sulle minacce** | ISAC di settore, agenzie informatiche governative (NCSC.ch, MELANI), feed commerciali | Automatico dove supportato; revisione manuale settimanale |
| **Intelligence interna** | IOC dalle indagini sugli incidenti, segnalazioni di phishing dei dipendenti, ricerca del team di sicurezza | Ad hoc; aggiunti entro 4 ore dall'identificazione |
| **Feed della community** | Intelligence sulle minacce open-source (MISP, abuse.ch, PhishTank, URLhaus) | Automatico dove supportato |

### Phishing e ingegneria sociale

- Gli URL di phishing segnalati dai dipendenti DEVONO essere valutati e aggiunti alla lista di blocco entro **4 ore** durante l'orario lavorativo.
- Gli URL delle simulazioni di phishing DEVONO essere esclusi dal filtro web durante le campagne di test (coordinamento tra la sicurezza delle informazioni e IT Operations).

### Integrazione con la risposta agli incidenti

Gli eventi del filtro web DEVONO essere integrati con il processo di gestione degli incidenti dell'organizzazione (A.5.24-28). Le seguenti soglie DEVONO attivare la creazione di un incidente:

| Attivatore | Gravità | Azione |
|------------|---------|--------|
| L'utente accede a un sito malware/C2 confermato (filtraggio aggirato o non riuscito) | Critica | Incidente immediato; isolare l'endpoint; indagine forense |
| Più utenti bloccati dallo stesso URL di phishing entro 1 ora | Alta | Investigare la potenziale campagna di phishing; valutare se alcuni utenti hanno acceduto all'URL prima del blocco |
| Singolo utente tenta ripetutamente di accedere a categorie bloccate (>20 tentativi/giorno) | Media | Investigare per violazione della policy o account compromesso |
| Rilevato bypass della piattaforma di filtraggio (evasione DoH/proxy riuscita) | Alta | Bloccare il vettore di evasione; investigare l'ambito; valutare le lacune nell'applicazione delle policy |
| Picco improvviso nelle richieste bloccate (>200% della baseline) | Media | Valutare per campagna malware, infrastruttura compromessa o configurazione errata |

---

## Processo di eccezione e override

### Richiesta di accesso a siti bloccati

Quando un utente incontra un sito web bloccato necessario per scopi aziendali legittimi:

1. **Pagina di blocco**: L'utente vede una pagina di blocco che mostra il motivo del blocco e un collegamento per richiedere l'accesso.
2. **Richiesta**: L'utente invia una richiesta di eccezione tramite [sistema di ticketing / portale self-service] con:
   - URL o dominio richiesto.
   - Giustificazione aziendale.
   - Durata necessaria (temporanea o permanente).
   - Contesto di reparto e progetto.
3. **Revisione**: La richiesta viene esaminata da:
   - **Responsabile diretto**: Conferma la giustificazione aziendale (entro 1 giorno lavorativo).
   - **Sicurezza IT**: Valuta il rischio di sicurezza (entro 1 giorno lavorativo).
4. **Decisione**:
   - **Approvare**: URL/dominio aggiunto alla lista di consentiti (a tempo limitato preferito; predefinito: 90 giorni).
   - **Rifiutare**: Utente informato con motivazione; alternativa suggerita dove possibile.
   - **Escalare**: Gli override di categorie ad alto rischio (elusione del proxy, strumenti di hacking) richiedono l'approvazione del RSSI.
5. **Implementazione**: IT Operations aggiunge l'eccezione approvata alla soluzione di filtraggio entro 4 ore dall'approvazione.
6. **Documentazione**: Eccezione registrata nel registro delle eccezioni con richiedente, giustificazione, approvatore, data di scadenza e data di revisione.

### Registro delle eccezioni

| Campo | Descrizione |
|-------|-------------|
| ID eccezione | Identificatore univoco |
| URL/Dominio | Cosa è consentito |
| Richiedente | Nome, reparto |
| Giustificazione aziendale | Perché è richiesto l'accesso |
| Valutazione del rischio | Risultato della valutazione del rischio di sicurezza |
| Approvatore | Nome e data |
| Data di scadenza | Predefinito: 90 giorni (temporanea) o revisione annuale (permanente) |
| Data di revisione | Quando l'eccezione viene prossimamente esaminata |
| Controlli compensativi | Eventuali controlli aggiuntivi applicati (ad es. monitoraggio, registrazione) |

### Governance delle eccezioni

- Tutte le eccezioni DEVONO essere revisionate **trimestralmente** dalla sicurezza IT.
- Le eccezioni scadute DEVONO essere automaticamente revocate.
- Le eccezioni non utilizzate (nessun accesso registrato negli ultimi 90 giorni) DEVONO essere rimosse.
- Il numero totale di eccezioni attive DEVE essere riportato trimestralmente al RSSI.
- Le eccezioni DEVONO avere l'ambito minimo necessario: URL specifico preferito rispetto al dominio completo; dominio preferito rispetto all'intera categoria.

---

## Considerazioni per i lavoratori remoti e BYOD

### Lavoratori remoti (dispositivi gestiti)

- Un agente SWG cloud o di filtraggio DNS DEVE essere installato su tutti gli endpoint gestiti.
- Le policy di filtro web DEVONO essere applicate in modo coerente che l'utente si trovi sulla rete aziendale, su Wi-Fi domestica, su hotspot mobile o su rete pubblica.
- Il tunneling diviso (VPN) NON deve bypassare il filtro web; il traffico web DEVE essere instradato attraverso la soluzione di filtraggio indipendentemente dalla configurazione VPN.

### BYOD (dispositivi personali)

- Il filtraggio DNS è la baseline minima per i dispositivi BYOD che accedono alle risorse aziendali.
- L'ispezione TLS **non** DEVE essere eseguita su dispositivi personali (vincoli di privacy e legali).
- Per l'accesso BYOD alle applicazioni web aziendali dovrebbe essere considerato un browser gestito o un contenitore workspace sicuro (ad es. Microsoft Edge for Business, VMware Workspace ONE).
- Per i dispositivi BYOD DEVONO essere applicate policy di filtraggio separate e meno invasive rispetto ai dispositivi gestiti dall'azienda.

---

## Privacy dei dipendenti e filtro web

### Requisiti legali

Il filtro web che tratta i dati di navigazione dei dipendenti DEVE essere conforme al diritto del lavoro svizzero:

- **OLL3 Art. 26**: I sistemi di filtro web NON devono essere utilizzati principalmente per monitorare il comportamento dei dipendenti. Il loro scopo è la sicurezza (prevenzione del malware, prevenzione della perdita di dati, applicazione delle policy).
- **CO svizzero Art. 328b**: Il trattamento dei dati di navigazione web dei dipendenti DEVE essere proporzionale e limitato agli scopi di sicurezza.
- **nLPD**: Liceità, proporzionalità, limitazione delle finalità e trasparenza si applicano a tutti i trattamenti dei dati di navigazione web.

### Misure di salvaguardia della privacy

- **Trasparenza**: I dipendenti DEVONO essere informati che il filtro web è in atto, quali categorie vengono filtrate e che l'accesso ai siti bloccati viene registrato. Queste informazioni DEVONO essere incluse nella politica di uso accettabile e nella documentazione di impiego.
- **Monitoraggio non personalizzato per default**: I log del filtro web DEVONO essere esaminati in forma aggregata per il monitoraggio della sicurezza (ad es. totale delle richieste bloccate per categoria, principali domini bloccati). L'attività di navigazione dei singoli utenti NON deve essere esaminata a meno che:
  - (a) Un avviso di sicurezza indichi un potenziale incidente o violazione della policy, e
  - (b) L'indagine sia documentata con giustificazione.
- **Limitazione delle finalità**: I dati del filtro web NON devono essere utilizzati per la valutazione delle prestazioni HR, azioni disciplinari per questioni non legate alla sicurezza o profilazione comportamentale generale.
- **Minimizzazione dei dati**: I log del filtro web DEVONO essere conservati solo per il tempo necessario agli scopi di sicurezza (secondo la pianificazione di conservazione dei log nella Politica di registrazione degli eventi, A.8.15).
- **VIPD**: Se il filtro web include l'ispezione TLS o la registrazione dettagliata a livello utente su larga scala, potrebbe essere richiesta una Valutazione d'impatto sulla protezione dei dati ai sensi della nLPD Art. 22.

---

## Formazione e sensibilizzazione

- Tutti i dipendenti DEVONO essere formati su:
  - La politica di filtro web dell'organizzazione e l'uso accettabile del web.
  - Come riconoscere gli avvisi di sicurezza del browser (errori di certificato, indicatori di phishing).
  - Come segnalare siti web sospetti malevoli alla sicurezza delle informazioni.
  - Il processo di richiesta di eccezione per accedere ai siti bloccati.
- La formazione DEVE essere inclusa nel programma annuale di sensibilizzazione alla sicurezza delle informazioni.
- Gli amministratori di sistema responsabili della manutenzione del filtro web DEVONO ricevere una formazione specifica sulla piattaforma.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approvazione delle decisioni di filtraggio per categoria; approvazione delle eccezioni ad alto rischio; supervisione dell'efficacia del filtro web |
| **IT Operations / Team di rete** | Distribuzione, configurazione e manutenzione della piattaforma di filtro web; implementazione delle eccezioni; gestione della capacità; gestione dei certificati di ispezione TLS |
| **Sicurezza delle informazioni** | Integrazione dell'intelligence sulle minacce; aggiornamenti delle liste di blocco; valutazione del rischio delle eccezioni; revisione trimestrale delle eccezioni; analisi dei log del filtro web |
| **Responsabili diretti** | Revisione della giustificazione aziendale per le richieste di eccezione |
| **Tutti i dipendenti** | Conformarsi alla politica di filtro web; segnalare siti web sospetti malevoli; utilizzare il processo di richiesta di eccezione per esigenze aziendali legittime |
| **Consulente per la protezione dei dati** | Valutazione VIPD per l'ispezione TLS; orientamento sulle misure di salvaguardia della privacy dei dipendenti |

### Revisione dell'accesso amministrativo (SOC 2: CC6.1)

L'accesso amministrativo alla piattaforma di filtro web DEVE essere:

- Limitato al personale IT Operations e della sicurezza delle informazioni con una necessità documentata.
- Revisionato trimestralmente per garantire che solo il personale autorizzato mantenga l'accesso.
- Protetto con AMF e controlli di gestione degli accessi privilegiati.
- Registrato — tutte le azioni amministrative (modifiche alle regole, modifiche alla configurazione, aggiunte alle eccezioni) DEVONO essere verificabili.
- Revocato entro 24 ore quando il personale cambia ruolo o lascia l'organizzazione.

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

| N. | Prova | Responsabile | Frequenza |
|----|-------|--------------|-----------|
| 1 | **Configurazione della piattaforma di filtro web** (categorie bloccate/consentite, impostazioni di ispezione TLS, configurazione del filtraggio DNS) | IT Operations | *Documentata; revisionata semestralmente e in seguito a modifiche delle policy* |
| 2 | **Registrazioni degli aggiornamenti delle liste di blocco** (fonti dell'intelligence sulle minacce, frequenza di aggiornamento, aggiunte manuali dalle indagini sugli incidenti) | Sicurezza delle informazioni | *Aggiornamenti automatici continui; aggiunte manuali registrate con data e fonte* |
| 3 | **Registro delle eccezioni** (eccezioni attive con giustificazione, approvatore, scadenza e data di revisione) | Sicurezza delle informazioni | *Mantenuto continuamente; revisionato trimestralmente; totale riportato trimestralmente al RSSI* |
| 4 | **Riepilogo dei log del filtro web** (statistiche aggregate: totale richieste, richieste bloccate per categoria, principali domini bloccati) | Sicurezza delle informazioni | *Riepilogo mensile; conservato 12 mesi* |
| 5 | **Lista delle esclusioni dalla privacy dell'ispezione TLS** (categorie che bypassano l'ispezione) | IT Operations | *Documentata; revisionata annualmente* |
| 6 | **Registrazioni della notifica ai dipendenti** (presa di conoscenza della politica di uso accettabile inclusa la comunicazione del filtro web) | HR / Sicurezza delle informazioni | *Aggiornato per ogni modifica della politica; presa di conoscenza monitorata annualmente* |
| 7 | **Copertura del filtraggio dei lavoratori remoti** (percentuale di endpoint remoti gestiti con agente di filtraggio attivo) | IT Operations | *Trimestrale; obiettivo: 100% dei dispositivi remoti gestiti* |
| 8 | **Registrazioni VIPD** (se è implementata l'ispezione TLS o la registrazione dettagliata a livello utente) | Consulente per la protezione dei dati | *Completata prima della distribuzione; revisionata annualmente* |
| 9 | **Rapporti SLO della piattaforma di filtraggio** — metriche di disponibilità, latenza e risoluzione degli incidenti (SOC 2: A1.1) | IT Operations | *Mensile; conservato 12 mesi* |
| 10 | **Registrazioni delle modifiche alle regole di filtraggio** — richieste di modifica, valutazioni del rischio, approvazioni, date di implementazione (SOC 2: CC8.1) | IT Operations / Sicurezza delle informazioni | *Per modifica; conservato 12 mesi* |
| 11 | **Registrazioni della valutazione dei rischi dei fornitori** — valutazioni dei provider SWG/DNS di terze parti, conformità agli SLA, rapporti SOC 2/ISO 27001 (SOC 2: CC9.2) | Sicurezza delle informazioni / Acquisti | *Annualmente; conservato contratto attivo + 2 anni* |
| 12 | **Registrazioni della revisione dell'accesso amministrativo** — lista degli admin della piattaforma di filtraggio, risultati della revisione, modifiche all'accesso (SOC 2: CC6.1) | IT Operations / Sicurezza delle informazioni | *Trimestrale; conservato 12 mesi* |
| 13 | **Risultati dei test dell'efficacia del filtraggio** — URL di test, risultati dei tentativi di bypass, misurazioni del tasso di rilevamento (SOC 2: CC4.1) | Sicurezza delle informazioni | *Semestrale; conservato 12 mesi* |
| 14 | **Reporting alla direzione** — riepilogo mensile delle metriche, analisi delle tendenze trimestrale, revisione annuale dell'efficacia (SOC 2: CC4.2) | RSSI / Sicurezza delle informazioni | *Mensile/trimestrale/annuale come specificato* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso revisioni della configurazione del filtro web, audit del registro delle eccezioni, analisi del tasso di blocco, controlli della copertura dei dispositivi remoti, audit interni ed esterni e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione a questa politica DEVE essere approvata e registrata secondo il Processo di eccezione e override definito sopra. Le eccezioni alla politica complessiva di filtro web (ad es. sistemi che non possono essere filtrati) DEVONO essere approvate dal RSSI con accettazione del rischio documentata e controlli compensativi.

## Non conformità

Un dipendente che risulti aver violato questa politica — incluso il tentativo di aggirare i controlli del filtro web (ad es. usando VPN personali, strumenti di elusione del proxy o resolver DNS non autorizzati) — può essere soggetto ad azioni disciplinari, fino al licenziamento.

## Test e convalida (SOC 2: CC4.1)

L'efficacia dei controlli del filtro web DEVE essere testata regolarmente:

| Test | Frequenza | Metodo | Responsabile |
|------|-----------|--------|--------------|
| **Verifica del blocco** | Mensile | Tentare l'accesso a URL noti come bloccati da account di test; verificare che la pagina di blocco venga visualizzata correttamente | Sicurezza delle informazioni |
| **Test di bypass** | Semestrale | Tentare di aggirare il filtraggio utilizzando tecniche di evasione comuni (DoH verso resolver non approvati, VPN, proxy) | Sicurezza delle informazioni |
| **Tasso di rilevamento malware** | Trimestrale | Inviare URL malevoli noti (da feed di test) attraverso la soluzione di filtraggio; misurare il tasso di rilevamento | Sicurezza delle informazioni |
| **Verifica dell'ispezione TLS** | Trimestrale | Verificare che l'ispezione TLS sia attiva sul traffico previsto; confermare che le esclusioni per la privacy funzionino correttamente | IT Operations |
| **Copertura dei lavoratori remoti** | Trimestrale | Verificare che l'agente di filtraggio sia attivo su un campione di endpoint remoti gestiti | IT Operations |

I risultati dei test DEVONO essere documentati e le azioni di rimedio monitorate per qualsiasi debolezza identificata.

## Metriche e reporting alla direzione (SOC 2: CC4.2)

Le seguenti metriche DEVONO essere riportate:

| Metrica | Obiettivo | Reporting |
|---------|-----------|-----------|
| Disponibilità della piattaforma di filtraggio | ≥99,9% di uptime | Mensile a IT Operations |
| Tasso di blocco malware/phishing | ≥99% delle minacce note bloccate | Trimestrale al RSSI |
| Tempi di elaborazione delle richieste di eccezione | ≤2 giorni lavorativi dalla richiesta alla decisione | Mensile al RSSI |
| Numero di eccezioni attive | In calo o stabile | Trimestrale al RSSI |
| Copertura del filtraggio dei lavoratori remoti | 100% degli endpoint remoti gestiti | Trimestrale al RSSI |
| URL di phishing segnalati dai dipendenti elaborati | Entro SLA di 4 ore | Mensile alla sicurezza delle informazioni |

## Miglioramento continuo

Questa politica viene rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti nel panorama delle minacce web, le capacità tecnologiche del filtraggio, i requisiti normativi, il feedback dei dipendenti sull'accesso legittimo bloccato e i tassi di falsi positivi/negativi.

---

# Aree dello standard ISO 27001 trattate

Politica di filtro web — Mapping dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| | 5.37 Procedure operative documentate |
| | 6.3 Sensibilizzazione, educazione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | **8.23 Filtro web** |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|-----------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative; Art. 6 — Proporzionalità |
| CO svizzero | Art. 328b — Limitazioni al trattamento dei dati dei dipendenti |
| OLL3 svizzera | Art. 26 — Divieto della sorveglianza comportamentale |
| GDPR UE (se applicabile) | Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Annex A Controllo 8.23 |
| ISO/IEC 27002:2022 | Sezione 8.23 — Indicazioni di implementazione |
| NIST SP 800-53 Rev 5 | AC-4 (Information Flow Enforcement), SC-7 (Boundary Protection), SC-7(8) (Route Traffic to Proxy), SI-3 (Malicious Code Protection) |
| NIST CSF 2.0 | PR.DS (Data Security), PR.IR (Infrastructure Resilience), DE.CM (Continuous Monitoring) |
| CIS Controls v8 | Controllo 9.2 (DNS Filtering Services), Controllo 9.3 (Network URL Filters) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
