<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.8-9-IT:operational:OP-POL:a.7.8-9 -->
**ISMS-OP-POL-A.7.8-9 — Ubicazione e protezione delle attrezzature**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Ubicazione e protezione delle attrezzature |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.7.8-9 |
| **Creatore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione esecutiva |
| **Data di creazione** | [Data] |
| **Versione** | 0.1 |
| **Data di versione** | [Data] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 0.1 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controlli A.7.8, A.7.9 — Ubicazione e protezione delle attrezzature, sicurezza delle risorse fuori sede
- ISO/IEC 27002:2022 Sezioni 7.8, 7.9 — Guida all'implementazione
- ISMS-OP-POL-A.7.1-2-3 (Controllo degli accessi fisici)
- ISMS-OP-POL-A.7.4-5-11 (Sicurezza delle infrastrutture fisiche)
- ISMS-OP-POL-A.6.7-8 (Lavoro da remoto e segnalazione degli eventi di sicurezza)
- ISMS-OP-POL-A.5.9 (Gestione delle risorse)
- ISMS-OP-POL-A.8.1-7-18-19 (Sicurezza degli endpoint)

**Controlli Allegato A correlati**:

| Controllo | Relazione con l'ubicazione e protezione delle attrezzature |
|-----------|-------------------------------------------------------------|
| A.7.1 Perimetri di sicurezza fisica | I confini perimetrali definiscono le zone in cui le attrezzature possono essere posizionate |
| A.7.2 Accesso fisico | I controlli di accesso proteggono le aree contenenti attrezzature |
| A.7.3 Protezione di uffici, locali e strutture | Le aree sicure ospitano le attrezzature critiche |
| A.7.4 Monitoraggio della sicurezza fisica | Il monitoraggio rileva gli accessi non autorizzati alle ubicazioni delle attrezzature |
| A.7.5 Protezione contro minacce fisiche e ambientali | I controlli ambientali proteggono le attrezzature dai rischi |
| A.7.11 Servizi di supporto | Alimentazione, raffreddamento e telecomunicazioni sostengono il funzionamento delle attrezzature |
| A.7.12 Sicurezza dei cablaggi | I cavi di alimentazione e di rete supportano la connettività delle attrezzature |
| A.7.13 Manutenzione delle attrezzature | La manutenzione preserva la disponibilità e l'integrità delle attrezzature |
| A.7.14 Smaltimento sicuro o riutilizzo delle attrezzature | La gestione a fine vita segue i requisiti di smaltimento sicuro |
| A.5.9 Inventario delle informazioni e delle altre risorse associate | L'inventario delle risorse registra l'ubicazione e il custode delle attrezzature |
| A.6.7 Lavoro da remoto | Le procedure di lavoro da remoto disciplinano l'utilizzo delle attrezzature fuori sede |
| A.8.1 Dispositivi endpoint degli utenti | Le politiche di sicurezza degli endpoint riguardano la protezione delle attrezzature portatili |

**Politiche interne correlate**:

- Politica di controllo degli accessi fisici
- Politica di sicurezza delle infrastrutture fisiche
- Politica di lavoro da remoto e segnalazione degli eventi di sicurezza
- Politica di gestione delle risorse
- Politica di sicurezza degli endpoint
- Politica di gestione degli incidenti

---

# Politica di ubicazione e protezione delle attrezzature

## Scopo

Lo scopo della presente politica è ridurre i rischi di perdita, danneggiamento, furto o compromissione delle attrezzature informatiche mediante un posizionamento sicuro, una protezione ambientale adeguata e misure di sicurezza appropriate per le risorse utilizzate sia in sede che fuori sede. Essa stabilisce i requisiti per l'ubicazione delle attrezzature, la protezione dell'alimentazione e dei cablaggi, nonché la sicurezza delle risorse quando vengono portate fuori dalle strutture dell'organizzazione.

La presente politica affronta due controlli ISO 27001:2022 correlati nell'ambito di un quadro unificato, poiché rappresentano aspetti complementari della protezione delle attrezzature lungo l'intero ciclo di vita operativo: il controllo A.7.8 disciplina il posizionamento sicuro e la protezione ambientale delle attrezzature presso le strutture dell'organizzazione, mentre il controllo A.7.9 estende tale protezione alle attrezzature utilizzate fuori sede — in transito, presso l'abitazione dei dipendenti, in spazi pubblici o installate in modo permanente in luoghi remoti.

La presente politica supporta la nLPD (revDSG) Art. 8 implementando misure tecniche e organizzative proporzionate al rischio, al fine di proteggere la disponibilità, l'integrità e la riservatezza dei dati personali attraverso controlli di protezione fisica delle attrezzature. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano altresì i requisiti del GDPR Art. 32 relativi alla sicurezza del trattamento, incluse le misure fisiche.

## Ambito di applicazione

Tutti i dipendenti, i collaboratori e gli utenti di terze parti che gestiscono, operano, trasportano o hanno la custodia di attrezzature dell'organizzazione.

Tutte le attrezzature informatiche di proprietà, in leasing o gestite dall'organizzazione, incluse:

- Server, sistemi di storage e infrastrutture di rete
- Workstation, laptop e dispositivi mobili
- Attrezzature di telecomunicazione e cablaggio
- Stampanti, scanner e dispositivi multifunzione
- Supporti di memorizzazione rimovibili (chiavette USB, dischi esterni)
- Appliance perimetrali, sensori e attrezzature permanentemente fuori sede

Tutte le ubicazioni in cui vengono utilizzate le attrezzature dell'organizzazione:

- Strutture in sede (data center, sale server, uffici)
- Strutture di colocation e data center di terze parti
- Uffici domestici dei dipendenti
- Luoghi di viaggio, hotel, sedi di clienti
- Spazi pubblici (aeroporti, caffè, spazi di co-working)
- Installazioni permanentemente fuori sede (sensori remoti, dispositivi edge)

**Fuori ambito**:

- Controllo degli accessi fisici alle aree attrezzature (disciplinato da A.7.1-2-3)
- Sistemi di monitoraggio e protezione ambientale (disciplinati da A.7.4-5-11)
- Servizi di supporto — alimentazione, raffreddamento, telecomunicazioni (disciplinati da A.7.4-5-11)
- Smaltimento delle attrezzature e riutilizzo sicuro (disciplinato da A.7.14)
- Sicurezza delle infrastrutture di cablaggio (disciplinata da A.7.12)
- Sicurezza del personale e verifiche dei precedenti (disciplinate da A.6.1-6.4)

### Organizzazioni esclusivamente cloud

Le organizzazioni che operano al 100% in ambienti cloud, prive di strutture informatiche in sede, possono contrassegnare il Controllo A.7.8 come "Non applicabile" nella Dichiarazione di applicabilità. Tuttavia, A.7.9 rimane applicabile ovunque i dipendenti utilizzino laptop, dispositivi mobili o altre attrezzature portatili fuori sede.

La determinazione di "Non applicabile" per A.7.8 deve essere documentata con:

- Riferimento all'inventario delle risorse che confermi l'assenza di strutture informatiche in sede.
- Verifica della sicurezza fisica del fornitore cloud tramite report SOC 2 Tipo II o revisione della certificazione ISO 27001.
- Conferma della revisione annuale che lo stato esclusivamente cloud rimanga invariato.

## Principio

L'ubicazione e la protezione delle attrezzature si fondano sul principio che le attrezzature informatiche richiedono misure di sicurezza fisiche proporzionate alla sensibilità dei dati trattati e alla criticità dei servizi supportati — indipendentemente dal fatto che tali attrezzature si trovino all'interno o all'esterno delle strutture dell'organizzazione. I controlli devono essere selezionati sulla base di una valutazione documentata del rischio.

---

## Classificazione delle attrezzature ai fini della protezione

Le attrezzature devono essere classificate in categorie di protezione per determinare i requisiti di ubicazione appropriati e i livelli di protezione fuori sede:

| Categoria | Esempi | Requisito di ubicazione | Fuori sede |
|-----------|--------|------------------------|------------|
| **Categoria A — Infrastruttura critica** | Server, switch di rete core, storage SAN/NAS, firewall, domain controller | Sala dedicata con controllo degli accessi; monitoraggio ambientale; alimentazione ridondante | La rimozione richiede l'approvazione del RSSI; limitata a: (1) migrazione o trasferimento del data center, (2) riparazione/sostituzione hardware ove il servizio in sede non sia possibile, (3) trasferimento per disaster recovery in sito alternativo pre-approvato |
| **Categoria B — Attrezzature aziendali** | Workstation, stampanti, telefoni VoIP, display per sale riunioni | Ambiente ufficio controllato; condizioni ambientali standard | Autorizzazione del responsabile diretto; tracciabilità delle risorse richiesta |
| **Categoria C — Attrezzature portatili** | Laptop, tablet, telefoni cellulari, proiettori portatili | Protette se incustodite; lucchetti a cavo in spazi condivisi | Autorizzazione del responsabile diretto; crittografia completa del disco (FDE); cancellazione remota; GPS dove tecnicamente supportato |
| **Categoria D — Supporti rimovibili** | Chiavette USB, dischi esterni, nastri di backup | Conservazione in luogo chiuso a chiave quando non in uso; supporti classificati in cassaforte | Solo supporti crittografati; autorizzazione richiesta; catena di custodia |
| **Categoria E — Permanentemente fuori sede** | Appliance perimetrali, sensori remoti, ATM, terminali kiosk, segnaletica digitale | Contenitore antimanomissione; alloggiamento con grado IP; monitoraggio remoto | N/D (sempre fuori sede); calendario di ispezione fisica; rilevamento manomissioni |

L'assegnazione di categoria deve essere registrata nel [Sistema di gestione delle risorse] o nel [CMDB] come parte della registrazione delle risorse.

---

## Requisiti di ubicazione delle attrezzature (A.7.8)

> *Le attrezzature dovrebbero essere posizionate in modo sicuro e protette.*

Le attrezzature che trattano o memorizzano informazioni devono essere posizionate in modo da ridurre i rischi derivanti da minacce fisiche e ambientali, accessi non autorizzati e danni.

### Selezione dell'ubicazione

- Le attrezzature devono essere collocate in aree con controllo fisico degli accessi, proporzionato alla classificazione delle informazioni trattate.
- Le attrezzature critiche (server, infrastrutture di rete, sistemi di storage) devono essere ubicate in sale dedicate con controllo degli accessi — non in aree ufficio generali, zone di reception o spazi accessibili al pubblico.
- Le attrezzature devono essere posizionate in modo da minimizzare il rischio di shoulder surfing. Gli schermi che visualizzano informazioni sensibili o riservate devono essere orientati lontano da finestre, corridoi e aree ad alto traffico.
- Le strutture informatiche che trattano dati classificati dovrebbero essere posizionate con attenzione affinché persone non autorizzate non possano visualizzare le informazioni mostrate sugli schermi durante l'uso. Laddove il riposizionamento non sia fattibile, devono essere utilizzati schermi privacy.
- Le attrezzature gestite dall'organizzazione devono essere chiaramente segregate da attrezzature non sotto controllo organizzativo (es. dispositivi personali, attrezzature di visitatori, infrastrutture in co-locazione condivisa).
- Le strutture di storage (rack server, armadi di storage, sale sicure) devono essere protette per impedire accessi non autorizzati.

### Considerazioni ambientali

- Le attrezzature devono essere protette da temperature estreme, umidità, polvere, vibrazioni e atmosfere corrosive. Le condizioni ambientali accettabili per il funzionamento delle attrezzature devono essere definite in base alle specifiche del produttore.
- Devono essere garantiti ventilazione e raffreddamento adeguati per le sale attrezzature. Le sale server e i data center devono mantenere una temperatura compresa tra 18 e 27 gradi Celsius e un'umidità relativa compresa tra 20 e 80%, in conformità con le linee guida termiche ASHRAE.
- Le attrezzature devono essere sollevate o protette laddove esiste un rischio di alluvione (es. pavimenti sopraelevati, barriere a livello del suolo, evitando ubicazioni in seminterrati in zone a rischio alluvione).
- Fumare, mangiare e bere devono essere vietati nelle sale server, nei data center e negli armadi di distribuzione. Le istruzioni per l'alimentazione e il consumo di bevande vicino alle postazioni di lavoro devono essere comunicate a tutto il personale.
- Le condizioni ambientali che possono interrompere le operazioni (temperatura, umidità, particolato aereo) devono essere monitorate in modo continuo nelle sale che ospitano attrezzature di Categoria A (infrastruttura critica), con avvisi automatici entro 15 minuti dal superamento delle soglie. Per le sale che ospitano attrezzature di Categoria B, il monitoraggio continuo dovrebbe essere implementato ove tecnicamente fattibile.

### Protezione dell'alimentazione e dei cablaggi

**Alimentazione elettrica**:

- Le attrezzature devono essere protette da interruzioni di corrente mediante sistemi UPS (gruppo di continuità) appropriati alla criticità delle attrezzature.
- I cavi di alimentazione devono essere protetti da intercettazioni o danni tramite conduit, canalizzazioni o passerelle cavi chiuse.
- Gli interruttori di emergenza (EPO — Emergency Power-Off) devono essere ubicati in prossimità delle uscite delle sale server e dei data center per l'uso in caso di emergenza. Gli EPO devono essere chiaramente etichettati, protetti da attivazioni accidentali (es. coperchio incernierato, alloggiamento rompibile) e testati annualmente nell'ambito del programma di sicurezza elettrica.
- Le alimentazioni devono essere ridondanti per le attrezzature critiche (configurazione N+1 raccomandata).
- La protezione contro i fulmini deve essere applicata agli edifici che ospitano strutture informatiche. Filtri di protezione dalle sovratensioni devono essere installati su tutte le linee di alimentazione e telecomunicazione in ingresso.

**Cablaggio di rete**:

- I cavi di rete che trasportano dati o supportano servizi informativi devono essere protetti da intercettazioni, interferenze o danni.
- I cavi di alimentazione devono essere segregati dai cavi di comunicazione per prevenire interferenze elettromagnetiche.
- I percorsi dei cavi devono essere documentati nel registro delle risorse e rivisti almeno annualmente e a fronte di modifiche rilevanti.
- I cavi in fibra ottica dovrebbero essere utilizzati per le trasmissioni dati ad alta sicurezza laddove il rischio di intercettazione lo giustifichi.
- Gli armadi di distribuzione e i patch panel devono disporre di controlli di accesso fisico appropriati.
- Le prese di rete in aree pubbliche non devono fornire accesso alla rete interna salvo esplicita autorizzazione e monitoraggio.

### Colocation e data center di terze parti

Laddove le attrezzature siano ospitate in strutture di colocation o data center di terze parti:

- L'organizzazione deve garantire che l'ubicazione, il controllo degli accessi fisici, la protezione ambientale e la resilienza dell'alimentazione soddisfino i requisiti della presente politica, verificati attraverso obblighi contrattuali e assicurazione periodica.
- L'assicurazione della struttura di terze parti deve essere ottenuta tramite uno o più dei seguenti metodi: report di audit SOC 2 Tipo II (con revisione specifica dei controlli PE), certificazione ISO 27001 (che confermi i controlli fisici dell'Allegato A nell'ambito), o ispezione documentata in loco mediante la checklist di sicurezza fisica dell'organizzazione. Laddove ci si avvalga di report SOC 2 o ISO 27001, l'organizzazione deve verificare:
  - Che il report riguardi la struttura specifica in cui sono ospitate le attrezzature dell'organizzazione (non solo la sede centrale del fornitore).
  - Che il periodo del report sia attuale (emesso negli ultimi 12 mesi).
  - Che eventuali qualifiche, eccezioni o controlli utente entità complementari (CUEC) siano esaminati e affrontati.
- Una matrice formale delle responsabilità deve essere mantenuta nel contratto di colocation, documentando quale parte è responsabile di ciascun controllo di sicurezza fisica e ambientale.
- La documentazione della conformità di terze parti deve essere conservata e rivista annualmente. Le modifiche rilevanti alla sicurezza delle strutture di terze parti devono essere comunicate all'organizzazione ai sensi delle clausole di notifica contrattuale.
- **Gestione del rischio fornitore (SOC 2: CC9.2)**: I fornitori di colocation e data center devono essere inclusi nel programma di gestione del rischio fornitori dell'organizzazione. I rischi correlati alle attrezzature (sicurezza fisica, resilienza ambientale, personale, stabilità finanziaria) devono essere valutati all'onboarding e rivisti annualmente. La conformità agli SLA per uptime, risposta agli incidenti e notifica degli accessi fisici deve essere monitorata rispetto alle soglie contrattuali.

### Attrezzature dei visitatori in sede (SOC 2: CC6.4)

Laddove i visitatori (clienti, fornitori, collaboratori, revisori) portino attrezzature personali o del proprio datore di lavoro in sede:

- I dispositivi dei visitatori non devono connettersi alla rete interna dell'organizzazione. Deve essere fornita una rete WiFi guest segregata ove sia richiesto l'accesso a Internet per i visitatori.
- I visitatori che portano attrezzature in aree con controllo degli accessi (sale server, aree sicure) devono dichiarare le attrezzature alla reception e confermarne la rimozione alla partenza.
- Laddove le attrezzature dei visitatori debbano interfacciarsi con i sistemi dell'organizzazione (es. strumenti diagnostici di fornitori, attrezzature di revisori), il Reparto IT deve ispezionare il dispositivo, verificare la protezione endpoint aggiornata e fornire una connessione di rete temporanea con ambito limitato.
- L'utilizzo di attrezzature da parte dei visitatori deve essere documentato nel registro dei visitatori, registrando: tipo di dispositivo, scopo, aree accedute e durata della presenza in sede.

### Ambienti industriali e ostili

Laddove le attrezzature si trovino in ambienti industriali, manifatturieri o comunque impegnativi:

- Devono essere implementate misure di protezione aggiuntive, inclusi coperchi antipolvere, contenitori sigillati e alloggiamenti protettivi classificati secondo gli standard IP (grado di protezione) appropriati.
- Le classificazioni IP delle attrezzature devono essere uguali o superiori alle condizioni ambientali. IP65 o superiore dovrebbe essere utilizzato per ambienti con significativa esposizione a polvere o acqua.
- Devono essere considerate misure di protezione speciali, come membrane per tastiera in ambienti industriali per prevenire la contaminazione.
- La frequenza di manutenzione deve essere aumentata per le attrezzature in ambienti ostili, con intervalli di ispezione definiti nel calendario di manutenzione.
- Le attrezzature che trattano informazioni classificate in ubicazioni esposte devono essere protette contro le perdite di informazioni dovute a emanazioni elettromagnetiche, laddove la valutazione del rischio lo giustifichi.

---

## Sicurezza delle risorse fuori sede (A.7.9)

> *Le risorse fuori sede dovrebbero essere protette.*

Le risorse fuori sede devono essere protette per prevenire perdita, danneggiamento, furto o compromissione dei dispositivi e per evitare interruzioni alle attività informatiche dell'organizzazione.

### Autorizzazione e tracciabilità

**Autorizzazione alla rimozione**:

- La rimozione di attrezzature dalle strutture dell'organizzazione deve essere autorizzata dal responsabile diretto appropriato prima della rimozione.
- I registri di autorizzazione devono documentare: dati dell'attrezzatura (etichetta di inventario, numero seriale, tipo), scopo della rimozione, persona responsabile, data di rientro prevista e requisiti particolari di gestione.
- Le attrezzature di alto valore (valore superiore a [soglia in CHF]) o le attrezzature contenenti dati classificati devono richiedere ulteriore approvazione dal [Responsabile IT Operations] o equivalente.
- I trasferimenti massicci di attrezzature (es. trasloco di ufficio, distribuzione di progetto) devono essere autorizzati tramite una richiesta formale di spostamento attrezzature.

**Tracciabilità delle risorse**:

- Le attrezzature rimosse dalle strutture devono essere registrate nel [Sistema di gestione delle risorse] o nel [CMDB] con ubicazione attuale, custode e data di rientro prevista.
- La catena di custodia deve essere mantenuta quando le attrezzature vengono trasferite tra individui. I registri di trasferimento devono includere sia la parte cedente che quella ricevente, la data e le condizioni dell'attrezzatura.
- Il rientro delle attrezzature deve essere verificato e registrato. Le attrezzature devono essere ispezionate al rientro per rilevare danni, manomissioni o componenti mancanti.
- Le attrezzature non rientrate entro la data prevista devono attivare un sollecito da parte del proprietario della risorsa. Le attrezzature in ritardo di oltre 30 giorni devono essere segnalate al responsabile diretto e al Reparto IT Operations.

### Sicurezza fisica fuori sede

**Requisiti generali**:

- Le attrezzature non devono essere lasciate incustodite in luoghi pubblici (aeroporti, caffè, sedi congressuali, mezzi pubblici, veicoli).
- Le attrezzature devono essere trasportate in borse anonime e non identificabili — non in borse o custodie con marchio del produttore che pubblicizzino il contenuto di valore.
- Quando non in uso attivo, le attrezzature devono essere conservate in cassaforte dell'hotel (tenendo conto dei limiti di dimensione — i laptop potrebbero non entrare nelle casseforti standard degli hotel), in contenitori chiusi a chiave o in altre aree sicure. Laddove la capacità della cassaforte dell'hotel non sia sufficiente, le attrezzature devono essere conservate in bagagli chiusi a chiave o il dipendente deve portarle con sé. Le attrezzature non devono essere lasciate visibili nelle camere d'hotel.
- Il deposito in veicoli deve essere utilizzato solo quando assolutamente necessario, e le attrezzature devono essere riposte nel bagagliaio fuori dalla vista — mai sui sedili o visibili dai finestrini.

**Protezione ambientale durante il trasporto**:

- Le attrezzature devono essere protette da temperature estreme durante il trasporto e lo stoccaggio. Devono essere rispettate le linee guida del produttore per i range di temperatura di funzionamento e conservazione sicuri.
- Le attrezzature non devono essere esposte alla luce solare diretta per periodi prolungati.
- La protezione dall'umidità deve essere mantenuta durante il trasporto (borse imbottite, custodie impermeabili per il trasporto all'esterno).
- Le attrezzature devono essere trasportate in custodie imbottite per proteggerle da urti fisici e vibrazioni.

**Misure di prevenzione del furto**:

- Le attrezzature devono essere fisicamente assicurate ove possibile mediante lucchetti a cavo, piastre di ancoraggio o equivalenti sistemi di fissaggio fisico in ambienti condivisi o semi-pubblici.
- Il tracciamento GPS o i servizi di localizzazione devono essere abilitati sui dispositivi supportati ove tecnicamente fattibile e legalmente consentito. La configurazione del tracciamento GPS deve:
  - Minimizzare il monitoraggio della posizione del dipendente (solo posizione del dispositivo, non tracciamento personale continuo).
  - Essere documentata nella politica sulla privacy interna dell'organizzazione con un'informativa di trasparenza adeguata agli utenti.
  - Rispettare i requisiti di proporzionalità della nLPD e le eventuali restrizioni cantonali sul monitoraggio dei dipendenti.
  - Tener conto dei vincoli tecnici: i servizi GPS/localizzazione richiedono supporto a livello di sistema operativo (iOS Find My, Android Device Manager o funzionalità MDM equivalente); i dispositivi privi di connettività di rete potrebbero non segnalare la posizione finché non riconnessi; le modalità di risparmio energetico possono limitare la precisione della localizzazione.
  - Laddove il tracciamento GPS non sia tecnicamente fattibile o legalmente consentito, devono essere documentati controlli compensativi (es. maggiore sensibilizzazione sulla sicurezza fisica, protezione con FDE, riduzione della residenza dei dati sul dispositivo).
- La capacità di cancellazione remota deve essere configurata su tutti i dispositivi mobili supportati tramite [MDM] e deve essere:
  - Testata almeno annualmente e dopo modifiche significative alla piattaforma MDM.
  - Eseguibile entro 4 ore dalla segnalazione confermata di perdita o furto durante l'orario lavorativo; entro 12 ore per le segnalazioni fuori orario.
  - Per gli incidenti fuori orario: deve essere documentata e comunicata a tutto il personale una procedura di contatto d'emergenza, che consenta l'avvio della cancellazione remota fuori orario tramite [contatto IT Operations di turno / portale self-service MDM].
  - Con prove dei risultati dei test conservate per scopi di audit.
- I numeri seriali, le etichette di inventario e le descrizioni delle attrezzature devono essere registrati nel [Sistema di gestione delle risorse] per supportare le denunce alle autorità di polizia e le richieste assicurative in caso di furto.
- Le etichette delle attrezzature dell'organizzazione (nome dell'azienda, etichette di inventario) dovrebbero essere discrete — sufficienti per l'identificazione interna ma senza pubblicizzare il valore:
  - **Buona pratica**: Piccola etichetta di inventario con codice a barre/QR; numero seriale inciso sul lato inferiore; tag RFID interno.
  - **Da evitare**: Adesivi con logo aziendale di grandi dimensioni sul coperchio del laptop; etichette "Proprietà di [Nome Azienda]" visibili durante il trasporto; borse o custodie per laptop con marchio aziendale.

### Requisiti per l'ufficio domestico

Laddove i dipendenti lavorino da casa con attrezzature dell'organizzazione:

- Le attrezzature devono essere conservate in modo sicuro quando non in uso — in una stanza, armadietto o cassetto chiuso a chiave ove fattibile.
- Le connessioni di rete devono essere protette con WiFi crittografato (WPA3 preferito, WPA2 minimo). La VPN deve essere utilizzata per tutti gli accessi ai sistemi dell'organizzazione, salvo nei casi in cui l'organizzazione abbia implementato un'architettura di rete Zero Trust o in cui l'accesso sia esclusivamente a applicazioni SaaS tramite HTTPS con SSO obbligatorio e validazione del certificato del dispositivo.
- I familiari, i visitatori e gli altri conviventi non devono avere accesso alle attrezzature dell'organizzazione. Il blocco schermo deve essere attivato quando il dipendente si allontana.
- L'ambiente dell'ufficio domestico dovrebbe garantire condizioni ambientali adeguate (temperatura, umidità, ventilazione) per prevenire danni alle attrezzature.
- I dipendenti devono riconoscere i requisiti di sicurezza dell'ufficio domestico come condizione per l'autorizzazione al lavoro da remoto.

### Spazi pubblici

Quando si lavora con attrezzature dell'organizzazione in spazi pubblici o condivisi:

- Gli schermi privacy devono essere utilizzati quando si lavora con informazioni sensibili o riservate in ambienti in cui il shoulder surfing è possibile (mezzi pubblici, caffè, sale lounge aeroportuali, spazi di co-working).
- Il WiFi pubblico deve essere utilizzato solo con protezione VPN, salvo nei casi in cui l'organizzazione abbia implementato un'architettura di rete Zero Trust o in cui l'accesso sia limitato a applicazioni SaaS tramite HTTPS con SSO obbligatorio e validazione del certificato del dispositivo. La connessione diretta a WiFi pubblico senza VPN o protezione equivalente per l'accesso ai sistemi o ai dati dell'organizzazione è vietata.
- Bluetooth, AirDrop e altri protocolli di condivisione wireless devono essere disabilitati quando non attivamente necessari.
- Le attrezzature non devono mai essere lasciate incustodite in spazi pubblici, neppure brevemente.
- Le notifiche pop-up e gli avvisi sullo schermo (avvisi di messaggistica, anteprime e-mail, voci di calendario) dovrebbero essere disabilitati durante presentazioni, condivisione dello schermo o quando si lavora in aree pubbliche per prevenire divulgazioni accidentali.

### Attrezzature permanentemente fuori sede

Laddove l'organizzazione distribuisca attrezzature installate in modo permanente al di fuori delle strutture organizzative, rientrano nell'ambito i seguenti scenari:

- **Appliance ospitati dal cliente**: Dispositivi di rete, sensori di monitoraggio o attrezzature di elaborazione installati presso le strutture del cliente nell'ambito di contratti di servizi gestiti.
- **Infrastrutture remote**: Attrezzature di telecomunicazione presso torri cellulari, sottostazioni elettriche o uffici remoti senza personale permanente.
- **Terminali pubblici**: ATM, kiosk self-service, terminali di pagamento o segnaletica digitale in luoghi di vendita al dettaglio o pubblici.
- **Sensori ambientali**: Dispositivi IoT per la gestione degli edifici, il monitoraggio ambientale o il controllo di processi industriali.
- **Nodi di edge computing**: Server edge o gateway distribuiti presso filiali, magazzini o strutture produttive.

Requisiti per le attrezzature permanentemente fuori sede:

- Deve essere implementato il rilevamento fisico delle manomissioni (sigilli antimanomissione, rilevamento intrusione nello chassis, allarmi antimanomissione) appropriato alla criticità della risorsa.
- Il monitoraggio ambientale deve essere continuo ove tecnicamente fattibile, con allarmi remoti per le deviazioni dalle soglie.
- Devono essere stabiliti calendari regolari di ispezione fisica, con frequenza basata sulla valutazione del rischio e sulla criticità delle attrezzature.
- Devono essere abilitate capacità di monitoraggio e gestione da remoto per mantenere la visibilità sullo stato delle attrezzature, sulla postura di sicurezza e sull'integrità della configurazione.
- Le restrizioni di accesso logico (comunicazioni crittografate, autenticazione forte, accesso basato su certificati) devono compensare la ridotta sicurezza fisica.
- Le procedure di risposta agli incidenti devono tenere conto delle ubicazioni remote, incluse le aspettative sui tempi di risposta e le disposizioni di contatto locali.
- **Failover per guasti ambientali (SOC 2: A1.2)**: Per le attrezzature permanentemente fuori sede a supporto di servizi critici, devono essere documentate procedure di failover per scenari di guasto ambientale (interruzione di corrente, guasto al raffreddamento, interruzione di rete). Il failover può includere: commutazione automatica ad attrezzature ridondanti in ubicazione alternativa, degradazione controllata con servizio ridotto, o trasferimento manuale a un sito di recovery pre-approvato. Le procedure di failover devono essere testate annualmente nell'ambito dei test di continuità operativa.
- Le istruzioni di protezione del produttore (campi elettromagnetici, umidità, temperatura, polvere) devono essere rispettate per le attrezzature installate in modo permanente.

### Sicurezza durante i viaggi

Quando si trasportano attrezzature dell'organizzazione durante viaggi di lavoro:

- Le attrezzature devono essere tenute nel bagaglio a mano durante i viaggi aerei — mai affidate come bagaglio da stiva.
- Le attrezzature non devono essere lasciate nei veicoli durante la notte o per periodi prolungati, nemmeno in veicoli chiusi a chiave.
- In destinazioni di viaggio ad alto rischio, devono essere adottate precauzioni aggiuntive: utilizzo di dispositivi specifici per i viaggi con dati minimi, contenitori crittografati per i dati sensibili e maggiore attenzione fisica. Le destinazioni ad alto rischio sono determinate dalla valutazione del rischio di viaggio dell'organizzazione in base a:
  - Livello di avvertimento di viaggio del governo (DFAE svizzero, advisory nazionale equivalente) in stato elevato o limitato.
  - Note attività di cyber-spionaggio statale mirate al settore industriale dell'organizzazione.
  - Pratiche delle autorità doganali/di frontiera che richiedono abitualmente l'ispezione dei dispositivi o la divulgazione delle password.
  - Precedenti di furto o sequestro di attrezzature che hanno interessato i viaggiatori d'affari in quella giurisdizione.
- I viaggi internazionali con dispositivi crittografati devono rispettare le normative del Paese di destinazione sull'importazione/esportazione di attrezzature crittografiche.
- Le attrezzature smarrite o rubate durante i viaggi devono essere segnalate immediatamente al Reparto IT Operations (per l'avvio della cancellazione remota) e alle autorità di polizia locali. Il dipendente deve documentare le circostanze e segnalarle tramite il processo di gestione degli incidenti al rientro.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Ubicazione delle attrezzature** | Il posizionamento sicuro e strategico delle attrezzature informatiche per minimizzare i rischi fisici, ambientali e di accesso |
| **Risorse fuori sede** | Attrezzature dell'organizzazione utilizzate al di fuori delle strutture organizzative, incluso presso l'abitazione dei dipendenti, le sedi dei clienti e durante i viaggi |
| **Catena di custodia** | Trasferimento documentato della responsabilità delle attrezzature tra individui, con registrazione della parte cedente, della parte ricevente, della data e delle condizioni dell'attrezzatura |
| **Cancellazione remota** | La capacità di cancellare da remoto i dati da un dispositivo tramite [MDM] o piattaforma di gestione equivalente |
| **Rilevamento manomissioni** | Meccanismi fisici o elettronici per rilevare l'accesso non autorizzato o la modifica delle attrezzature (sigilli antimanomissione, sensori di intrusione nello chassis) |
| **Grado IP (Ingress Protection)** | Sistema di classificazione IEC 60529 che indica la resistenza delle attrezzature alla penetrazione di polvere e acqua (es. IP65 = a prova di polvere, protetto contro i getti d'acqua) |
| **UPS (gruppo di continuità)** | Sistema di alimentazione con backup a batteria che fornisce alimentazione a breve termine durante un'interruzione della rete, consentendo uno spegnimento ordinato o il trasferimento al generatore |
| **EPO (Emergency Power-Off)** | Meccanismo di spegnimento d'emergenza per la rapida de-energizzazione delle attrezzature nelle sale server o nei data center |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **Responsabile della sicurezza delle informazioni (RSSI)** | Responsabilità complessiva per la politica di ubicazione e protezione delle attrezzature; accettazione del rischio per le eccezioni; revisione e approvazione degli standard di ubicazione; reportistica esecutiva sulla postura di sicurezza delle attrezzature |
| **Responsabile della struttura** | Decisioni sull'ubicazione delle attrezzature in sede; gestione delle condizioni ambientali; coordinamento con proprietari e fornitori di colocation; infrastrutture fisiche a supporto delle attrezzature |
| **IT Operations** | Distribuzione e configurazione delle attrezzature; tracciabilità delle risorse nel [Sistema di gestione delle risorse]; gestione MDM; capacità di cancellazione remota; monitoraggio delle attrezzature fuori sede |
| **Responsabili diretti** | Autorizzano la rimozione di attrezzature dalla sede; garantiscono la conformità del team ai requisiti di sicurezza fuori sede; seguono i rientri in ritardo delle attrezzature |
| **Proprietari di sistema** | Definiscono i requisiti di ubicazione per i sistemi di loro competenza; partecipano alla valutazione del rischio per il posizionamento delle attrezzature; segnalano i problemi di sicurezza delle attrezzature |
| **Responsabile della protezione dei dati (DPD) (ove nominato)** | Fornisce consulenza sulle implicazioni privacy del tracciamento GPS e della cancellazione remota; esamina le informative di trasparenza sul monitoraggio dei dipendenti |
| **Tutto il personale** | Proteggere le attrezzature in loro custodia; rispettare i requisiti di sicurezza fuori sede; segnalare immediatamente perdita, furto, danni o incidenti di sicurezza delle attrezzature; seguire le linee guida di trasporto e stoccaggio |

### Percorso di escalation

- Problemi di ubicazione attrezzature: Dipendente → Responsabile della struttura → RSSI
- Problemi di sicurezza attrezzature (fuori sede): Dipendente → Responsabile diretto → IT Operations → RSSI
- Perdita o furto di attrezzature: Dipendente → IT Operations (immediato, per cancellazione remota) → RSSI → Direzione esecutiva
- Danni alle attrezzature (ambientali): Dipendente → Responsabile della struttura → IT Operations → RSSI

---

## Classificazione degli incidenti

Gli eventi di sicurezza relativi alle attrezzature devono essere classificati e gestiti in base alla gravità:

| Gravità | Esempi | Risposta richiesta |
|---------|--------|-------------------|
| **Critica** | Furto di attrezzature (Categoria A o B); perdita di un dispositivo contenente dati classificati; violazione fisica della sala server; comprovata esposizione di dati da attrezzature rubate | Risposta immediata; avviare la cancellazione remota; attivare il processo di gestione degli incidenti; notificare RSSI e direzione esecutiva entro 1 ora; presentare denuncia alle autorità di polizia |
| **Alta** | Perdita di un dispositivo portatile (Categoria C); attrezzature trovate incustodite in area pubblica; evidenza di manomissione su attrezzature fuori sede; rilevata rimozione non autorizzata di attrezzature | Indagine e risposta nella stessa giornata; avviare la cancellazione remota se la perdita è confermata; notificare il RSSI entro 4 ore |
| **Media** | Rilevata non conformità nell'ubicazione delle attrezzature; rientro in ritardo di attrezzature (> 30 giorni); deviazione ambientale nella sala attrezzature; rilievo di audit del fornitore di colocation | Documentato e analizzato entro 5 giorni lavorativi; piano di rimedio richiesto |
| **Bassa** | Necessità di piccole modifiche all'ubicazione; singolo rientro in ritardo di attrezzature (< 30 giorni); etichetta attrezzatura mancante; discrepanza nel percorso dei cavi | Registrato per l'analisi dei trend; corretto alla successiva revisione programmata |

Gli incidenti di sicurezza relativi alle attrezzature devono essere segnalati e gestiti tramite il processo di gestione degli incidenti dell'organizzazione (A.5.24-28).

---

## Checklist di implementazione

La seguente checklist riassume le principali azioni di implementazione per ruolo responsabile:

**IT Operations:**

- [ ] Configurare la capacità di cancellazione remota su tutti i dispositivi mobili supportati tramite [MDM]
- [ ] Abilitare il tracciamento GPS sui dispositivi supportati (con informativa sulla privacy esaminata dal DPD)
- [ ] Registrare tutte le attrezzature nel [Sistema di gestione delle risorse] / [CMDB] con ubicazione e custode
- [ ] Stabilire il calendario annuale di test della cancellazione remota e conservare i relativi registri
- [ ] Configurare gli avvisi di monitoraggio ambientale per le sale attrezzature (soglia di 15 minuti per la Categoria A)
- [ ] Verificare che i report di assicurazione di colocation/terze parti siano aggiornati (entro 12 mesi)
- [ ] Stabilire calendari di ispezione per le attrezzature permanentemente fuori sede

**Responsabile della struttura:**

- [ ] Completare la valutazione dell'ubicazione delle attrezzature per tutte le attrezzature informatiche in sede
- [ ] Verificare che le condizioni ambientali (temperatura, umidità) nelle sale attrezzature rispettino le linee guida ASHRAE
- [ ] Confermare che gli interruttori EPO siano funzionanti e le ubicazioni chiaramente contrassegnate
- [ ] Mantenere la documentazione dei percorsi cavi e rivederla annualmente
- [ ] Stabilire procedure di ispezione e isolamento per le attrezzature dei visitatori
- [ ] Coordinare le revisioni di sicurezza fisica dei fornitori di colocation

**Responsabili diretti:**

- [ ] Comunicare ai membri del team i requisiti di sicurezza per le attrezzature fuori sede
- [ ] Stabilire il processo di autorizzazione alla rimozione delle attrezzature per il team
- [ ] Monitorare i rientri in ritardo delle attrezzature ed escalare ove necessario
- [ ] Garantire che le dichiarazioni di sicurezza per l'ufficio domestico siano aggiornate per tutti i lavoratori da remoto
- [ ] Informare il team sui requisiti di sicurezza durante i viaggi, incluse le procedure per le destinazioni ad alto rischio

---

## Prove a supporto della presente politica

| # | Prova | Responsabile | Frequenza | Conservazione |
|---|-------|-------------|-----------|---------------|
| 1 | **Registro di ubicazione delle attrezzature** (ubicazione, valutazione dell'ubicazione, conformità ambientale) | Responsabile della struttura | *Valutazione annuale; aggiornamento a fronte di modifiche rilevanti* | 3 anni |
| 2 | **Registri di autorizzazione alla rimozione delle attrezzature** (approvazione, dati dell'attrezzatura, scopo, rientro previsto) | IT Operations | *Per evento* | 3 anni |
| 3 | **Registri di tracciabilità delle risorse** (registro delle attrezzature fuori sede dal [Sistema di gestione delle risorse] / [CMDB]) | IT Operations | *Continuo; revisione trimestrale* | 3 anni |
| 4 | **Registri della catena di custodia** (documentazione di trasferimento delle attrezzature tra individui) | IT Operations | *Per evento di trasferimento* | 3 anni |
| 5 | **Registri di verifica del rientro delle attrezzature** (ispezione al rientro, condizioni, completezza) | IT Operations | *Per evento di rientro* | 3 anni |
| 6 | **Registri di test della capacità di cancellazione remota** (risultati annuali del test MDM, log di esecuzione cancellazione) | IT Operations | *Annuale; dopo modifiche MDM* | 3 anni |
| 7 | **Rapporti di incidente per perdita/furto di attrezzature** (dettagli dell'incidente, azioni di risposta, denunce alle autorità ove applicabile) | RSSI / IT Operations | *Per incidente* | 5 anni |
| 8 | **Documentazione di assicurazione colocation/terze parti** (report SOC 2, certificati ISO 27001, rapporti di ispezione) | IT Operations / Responsabile della struttura | *Annuale* | Contratto attivo + 2 anni |
| 9 | **Informativa sulla privacy del tracciamento GPS** (notifica ai dipendenti, documentazione della politica, registrazioni di consenso/trasparenza) | DPD / RSSI | *Revisione annuale; aggiornamento a fronte di modifiche* | Attivo + 2 anni |
| 10 | **Dichiarazioni di sicurezza per l'ufficio domestico** (firma del dipendente sui requisiti di sicurezza per il lavoro da remoto) | Responsabili diretti / HR | *All'autorizzazione al lavoro da remoto; rinnovo annuale* | Rapporto di lavoro + 2 anni |
| 11 | **Registri di monitoraggio ambientale per le sale attrezzature** (log di temperatura e umidità, registrazioni degli avvisi) | Responsabile della struttura | *Registrazione continua; conservazione minima 12 mesi* | 12 mesi |
| 12 | **Registro delle eccezioni all'ubicazione delle attrezzature** (deroghe approvate con accettazione del rischio e controlli compensativi) | RSSI | *Per eccezione; revisione trimestrale* | Attivo + 2 anni |
| 13 | **Registri di ispezione delle attrezzature permanentemente fuori sede** (risultati delle ispezioni fisiche, verifica dei sigilli antimanomissione) | IT Operations | *Per calendario di ispezione* | 3 anni |
| 14 | **Documentazione dei percorsi cavi** (tracciati, registrazioni delle revisioni annuali) | Responsabile della struttura / IT Operations | *Revisione annuale* | Attuale + 1 anno |
| 15 | **Registri degli accessi delle attrezzature dei visitatori** (dispositivi dei visitatori portati in sede, ispezione, conferma dell'isolamento di rete) | Responsabile della struttura / IT Operations | *Per visita* | 3 anni |
| 16 | **Registri di valutazione del rischio fornitori** (valutazioni del rischio dei fornitori correlate alle attrezzature, conformità SLA, verifica della sicurezza fisica) | RSSI / Procurement | *Annuale; all'onboarding del fornitore* | Contratto attivo + 2 anni |
| 17 | **Registri di failover per guasti ambientali** (log di attivazione del failover, documentazione di trasferimento delle attrezzature, risultati dei test di recovery) | IT Operations / Responsabile della struttura | *Per evento; test di recovery annuale* | 3 anni |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità alla presente politica tramite vari metodi, inclusi tra gli altri: ispezioni dell'ubicazione delle attrezzature, report del sistema di tracciabilità delle risorse, report di conformità MDM, audit delle attrezzature fuori sede, registrazioni degli incidenti, audit interni ed esterni, e feedback al proprietario della politica.

La conformità sarà valutata utilizzando le seguenti metriche:

| Metrica | Obiettivo | Fonte di misurazione |
|---------|-----------|---------------------|
| Attrezzature con ubicazione conforme (valutata rispetto alla presente politica) | 100% | Registro di ubicazione delle attrezzature |
| Attrezzature fuori sede con tracciabilità aggiornata nel [Sistema di gestione delle risorse] | 100% | [Sistema di gestione delle risorse] / [CMDB] |
| Dispositivi mobili con capacità di cancellazione remota abilitata | 100% | Report di conformità [MDM] |
| Perdite/furti di attrezzature per anno | 0 | Registrazioni degli incidenti |
| Rientri in ritardo di attrezzature (> 30 giorni dalla data prevista) | < 5 in qualsiasi momento | [Sistema di gestione delle risorse] |
| Test della cancellazione remota superato nei tempi previsti | 100% | Registrazioni dei test |
| Report di assicurazione colocation/terze parti aggiornati (entro 12 mesi) | 100% | Registrazioni di assicurazione fornitori |
| Dichiarazioni di sicurezza per l'ufficio domestico aggiornate | 100% per i lavoratori da remoto | Registrazioni HR / responsabili diretti |

| Punteggio | Valutazione | Azione |
|-----------|------------|--------|
| > 90% | Eccellente | Mantenere i controlli attuali |
| 75-89% | Buono | Colmare le lacune nel prossimo ciclo di revisione |
| 60-74% | Accettabile | Sviluppare un piano di rimedio entro 30 giorni |
| < 60% | Non conforme | Rimedio immediato richiesto; escalation al RSSI |

## Eccezioni

Qualsiasi eccezione alla presente politica deve essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con valutazione documentata del rischio, controlli compensativi e una data di revisione definita (massimo 6 mesi, rinnovabile). Gli scenari di eccezione validi includono:

- Posizionamento delle attrezzature in ubicazioni non standard per requisiti operativi (con monitoraggio potenziato).
- Periodi prolungati fuori sede oltre l'autorizzazione standard (con giustificazione documentata).
- Misure di protezione alternative per attrezzature legacy che non supportano la cancellazione remota o il tracciamento (con controlli compensativi quali FDE e maggiore sicurezza fisica).
- Rinuncia al tracciamento GPS laddove vincoli di privacy o legali ne impediscano l'abilitazione (con misure alternative di prevenzione delle perdite).

Le eccezioni devono essere segnalate al Team di revisione della direzione. Le eccezioni permanenti ai requisiti di prevenzione del furto o di tracciabilità delle risorse non sono consentite.

## Non conformità

Un dipendente che risulti aver violato la presente politica può essere soggetto a provvedimenti disciplinari, fino al licenziamento. La perdita o il furto di attrezzature derivante dal mancato rispetto negligente della presente politica può comportare responsabilità finanziaria ove consentito dalla normativa lavoristica applicabile.

## Miglioramento continuo

La presente politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono tener conto di: modifiche alle operazioni delle strutture, evoluzione tecnologica delle attrezzature, cambiamenti nei modelli di lavoro da remoto, requisiti normativi, insegnamenti tratti dagli incidenti relativi alle attrezzature (perdita, furto, danni ambientali) e risultati degli audit.

---

# Aree della norma ISO 27001 trattate

Politica di ubicazione e protezione delle attrezzature — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | **7.8 Ubicazione e protezione delle attrezzature** |
| | **7.9 Sicurezza delle risorse fuori sede** |
| | 7.1 Perimetri di sicurezza fisica |
| | 7.4 Monitoraggio della sicurezza fisica |
| | 7.5 Protezione contro minacce fisiche e ambientali |
| | 7.11 Servizi di supporto |
| | 7.12 Sicurezza dei cablaggi |

# Quadro normativo

| Quadro | Rilevanza |
|--------|-----------|
| **nLPD svizzera (revDSG)** | Art. 8 — Misure tecniche e organizzative per la sicurezza fisica delle attrezzature informatiche |
| **OPDo svizzera (ordinanza sulla protezione dei dati)** | Art. 1-3 — Requisiti minimi per la sicurezza dei dati, incluse le misure di protezione fisica |
| **GDPR UE (ove applicabile)** | Art. 32 — Sicurezza del trattamento, incluse misure fisiche per la protezione delle attrezzature |
| **ISO/IEC 27001:2022** | Controlli Allegato A 7.8 (Ubicazione e protezione delle attrezzature), 7.9 (Sicurezza delle risorse fuori sede) |
| **ISO/IEC 27002:2022** | Sezioni 7.8, 7.9 — Guida all'implementazione |
| **NIST SP 800-53 Rev 5** | PE-14 (Controlli ambientali), PE-18 (Ubicazione dei componenti di sistema), PE-17 (Sito di lavoro alternativo) |
| **CIS Controls v8** | Controllo 1 (Inventario e controllo delle risorse aziendali), Controllo 12 (Gestione dell'infrastruttura di rete) |
| **ASHRAE** | Linee guida termiche per gli ambienti di elaborazione dei dati (range di temperatura e umidità) |
| **IEC 60529** | Standard di classificazione IP (grado di protezione) per la protezione degli alloggiamenti delle attrezzature |
| **Condizionale: Circolare FINMA 2023/1** | Istituto finanziario svizzero regolamentato — maggiore sicurezza fisica delle infrastrutture ICT |
| **Condizionale: DORA (UE) 2022/2554** | Entità di servizi finanziari UE — protezione delle risorse ICT, incluse quelle fuori sede |
| **Condizionale: Direttiva NIS 2 (UE) 2022/2555** | Entità essenziale/importante nell'UE — misure di sicurezza fisica per le infrastrutture critiche |

---

<!-- QA_VERIFIED: 2026-04-03 -->
