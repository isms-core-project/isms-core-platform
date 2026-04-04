<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.20-22-IT:operational:OP-POL:a.8.20-22 -->
**ISMS-OP-POL-A.8.20-22 — Sicurezza della rete**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza della rete |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.20-22 |
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

- ISO/IEC 27001:2022 Controlli A.8.20, A.8.21, A.8.22 — Sicurezza della rete, sicurezza dei servizi di rete, segregazione delle reti

**Controlli correlati dell'Annex A**:

| Controllo | Relazione con la sicurezza della rete |
|-----------|---------------------------------------|
| A.5.14 Trasferimento di informazioni | Requisiti di crittografia e canali sicuri per i dati in transito |
| A.5.15 Controllo degli accessi | Controllo degli accessi di rete allineato con la politica di identità e accesso |
| A.5.23 Sicurezza delle informazioni per i servizi cloud | Connettività di rete cloud e segmentazione |
| A.8.1 Dispositivi endpoint degli utenti | Conformità degli endpoint prima dell'ammissione alla rete |
| A.8.5 Autenticazione sicura | Autenticazione per l'accesso alla rete (802.1X, VPN) |
| A.8.9 Gestione della configurazione | Baseline di configurazione e hardening dei dispositivi di rete |
| A.8.15 Registrazione degli eventi | Registrazione degli eventi e del traffico di rete |
| A.8.16 Attività di monitoraggio | Monitoraggio della rete, IDS/IPS, rilevamento delle anomalie |
| A.8.23 Filtro web | Filtraggio URL/DNS come controllo a livello di rete |
| A.8.24 Uso della crittografia | TLS/IPsec per il trasporto di rete crittografato |

**Politiche interne correlate**:

- Politica di controllo degli accessi
- Politica di uso della crittografia
- Politica di trasferimento delle informazioni
- Politica di sicurezza fisica e ambientale
- Politica di gestione degli asset
- Politica di registrazione degli eventi
- Politica delle attività di monitoraggio (A.8.16)

---

# Politica di gestione della sicurezza della rete

## Scopo

Lo scopo di questa politica è garantire la protezione delle informazioni nelle reti e nei relativi sistemi di elaborazione delle informazioni di supporto.

Questa politica supporta la nLPD svizzera (revDSG) e l'Ordinanza sulla protezione dei dati (OPDo) implementando misure tecniche e organizzative adeguate al rischio per proteggere i dati personali (inclusi i dati personali degni di particolare protezione) tramite controlli di sicurezza della rete. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Tutte le reti, i servizi di rete, le soluzioni di amministrazione e gestione della rete e i dispositivi di rete dell'organizzazione rientranti nell'ambito definito dalla dichiarazione di ambito ISO 27001.

## Principio

La rete è gestita secondo il principio del privilegio minimo con sicurezza by design e by default. L'accesso alla rete è negato per default e concesso solo con approvazione documentata. Tutte le decisioni architetturali di rete DEVONO essere basate sul rischio, tenendo conto della classificazione delle informazioni e della criticità dei sistemi.

---

## Controlli di rete

- Le responsabilità e le procedure per la gestione delle apparecchiature di rete DEVONO essere stabilite e documentate.
- La responsabilità operativa per le reti DEVE essere separata dalle operazioni informatiche dove appropriato.
- DEVONO essere stabiliti controlli speciali per salvaguardare la riservatezza e l'integrità dei dati che transitano su reti pubbliche o wireless, e per proteggere i sistemi e le applicazioni connessi.
- DEVONO essere applicate registrazioni e monitoraggio appropriati per consentire la registrazione e il rilevamento di azioni che possono influire sulla sicurezza delle informazioni o che sono rilevanti per essa.
- Le attività di gestione DEVONO essere strettamente coordinate sia per ottimizzare il servizio all'organizzazione sia per garantire che i controlli siano applicati in modo coerente nell'infrastruttura di elaborazione delle informazioni.
- I sistemi sulla rete DEVONO essere autenticati prima di ricevere l'accesso.
- Le connessioni di sistema alla rete DEVONO essere limitate ai dispositivi autorizzati e conformi.
- Le password e gli account predefiniti dei dispositivi di rete DEVONO essere modificati o disabilitati prima della distribuzione.
- L'accesso amministrativo ai dispositivi di rete DEVE utilizzare protocolli di gestione crittografati (SSH, HTTPS). Telnet e SNMP non crittografato (v1/v2c) NON devono essere utilizzati.
- Il firmware e il software dei dispositivi di rete DEVONO essere mantenuti alle versioni correnti supportate dal fornitore. Le patch di sicurezza DEVONO essere applicate secondo le seguenti tempistiche:

| Gravità | Tempistica |
|---------|------------|
| Vulnerabilità critiche (CVSS 9.0+, sfruttamento attivo) | Entro 14 giorni |
| Vulnerabilità alte (CVSS 7.0–8.9) | Entro 30 giorni |
| Vulnerabilità medie (CVSS 4.0–6.9) | Entro 90 giorni |
| Vulnerabilità basse (CVSS 0.1–3.9) | Alla prossima finestra di manutenzione programmata |

Le patch d'emergenza per vulnerabilità attivamente sfruttate possono essere distribuite senza test in ambienti non di produzione con l'approvazione del RSSI e l'accettazione documentata del rischio.

## Sicurezza dei servizi di rete

I meccanismi di sicurezza, i livelli di servizio e i requisiti di gestione di tutti i servizi di rete DEVONO essere identificati e inclusi negli accordi sui servizi di rete, indipendentemente dal fatto che tali servizi siano forniti internamente o in outsourcing.

La capacità del fornitore di servizi di rete di gestire i servizi concordati in modo sicuro DEVE essere determinata e monitorata regolarmente, e il diritto di audit DEVE essere concordato.

Le misure di sicurezza necessarie per particolari servizi, come le caratteristiche di sicurezza, i livelli di servizio e i requisiti di gestione, DEVONO essere identificate. L'organizzazione DEVE garantire che i fornitori di servizi di rete implementino queste misure.

I servizi di rete includono, a titolo non esaustivo:

- Servizi DNS, DHCP e NTP.
- Servizi di posta elettronica, condivisione file e applicazioni web.
- Servizi di firewall, rilevamento/prevenzione delle intrusioni e sicurezza del gateway.
- Servizi di accesso remoto e VPN.

## Segregazione delle reti

Le reti di grandi dimensioni DEVONO essere suddivise in domini di rete separati. I domini DEVONO essere scelti in base ai livelli di fiducia, alla classificazione dei dati e alla funzione aziendale.

La segregazione può essere ottenuta utilizzando reti fisicamente diverse o reti logiche diverse (ad es. VLAN, software-defined networking).

Il perimetro di ogni dominio DEVE essere ben definito. L'accesso tra i domini di rete DEVE essere controllato al perimetro utilizzando un gateway (ad es. firewall, router di filtraggio) con una postura di negazione per default.

I criteri per la segregazione delle reti in domini e l'accesso consentito attraverso i gateway DEVONO essere basati su una valutazione dei requisiti di sicurezza di ogni dominio. La valutazione DEVE essere conforme alla politica di controllo degli accessi, ai requisiti di accesso, al valore e alla classificazione delle informazioni trattate, e DEVE tener conto del costo relativo e dell'impatto sulle prestazioni dell'incorporazione di tecnologie gateway appropriate.

**Governance delle regole del firewall:**

- Tutte le modifiche alle regole del firewall DEVONO seguire un processo documentato di gestione delle modifiche con giustificazione aziendale e approvazione.
- I set di regole del firewall DEVONO essere revisionati almeno **annualmente** per rimuovere le regole obsolete e verificare la giustificazione aziendale continuata.
- Le revisioni DEVONO essere documentate con la firma dell'amministratore di rete e del RSSI.
- La policy di negazione per default DEVE essere verificata durante ogni revisione (tutto il traffico bloccato a meno che non sia esplicitamente consentito).

I segmenti di rete minimi DEVONO includere:

| Segmento | Scopo |
|----------|-------|
| Rete aziendale / utenti | Workstation e dispositivi standard dei dipendenti |
| Rete server / applicazioni | Applicazioni aziendali e database |
| Rete di gestione | Amministrazione dei dispositivi di rete (out-of-band ove fattibile) |
| Rete ospiti | Accesso per visitatori e dispositivi non aziendali (isolata dalla rete aziendale) |
| Rete IoT / OT | Dispositivi Internet of Things e di tecnologia operativa (isolata) |

Segmenti aggiuntivi (ad es. DMZ per i servizi rivolti al pubblico, ambienti di sviluppo/test) DEVONO essere creati in base alla valutazione del rischio.

### Requisiti della rete ospiti

Le reti ospiti DEVONO essere configurate con i seguenti controlli di sicurezza:

- **Isolamento**: Nessun accesso ai segmenti di rete aziendale (le regole del firewall DEVONO applicare la separazione).
- **Accesso solo a Internet**: Gli ospiti DEVONO accedere solo a Internet, non alle risorse interne.
- **Crittografia**: WPA2-Personal come minimo con una passphrase robusta, o WPA2-Enterprise con credenziali ospite.
- **Accesso a tempo limitato**: Le credenziali ospite DEVONO scadere dopo un periodo definito (ad es. 24 ore) e essere riemesse secondo necessità.
- **Monitoraggio**: Il traffico della rete ospiti DEVE essere registrato per le indagini di sicurezza se necessario.

La passphrase della rete ospiti DEVE essere cambiata almeno **trimestralmente** o immediatamente in caso di sospetta compromissione.

### Sicurezza dei dispositivi IoT e OT

I dispositivi IoT (Internet of Things) e OT (Operational Technology) DEVONO essere collocati su un segmento di rete isolato con i seguenti controlli:

- I dispositivi IoT/OT NON devono avere accesso diretto e non controllato a Internet. La comunicazione Internet DEVE essere instradata tramite un proxy o gateway con destinazioni in lista di consentiti.
- I dispositivi IoT/OT NON devono essere accessibili da Internet senza VPN e autorizzazione esplicita.
- L'accesso dalla rete aziendale al segmento IoT/OT DEVE essere limitato al personale autorizzato tramite regole del firewall.
- L'accesso remoto dei fornitori terzi ai dispositivi IoT/OT DEVE richiedere approvazione, VPN e credenziali a tempo limitato.
- Tutte le password predefinite dei dispositivi IoT/OT DEVONO essere cambiate prima della distribuzione.
- Tutti i dispositivi IoT/OT DEVONO essere registrati nel registro degli asset con proprietario, scopo e posizione di rete.

### Segregazione delle reti wireless

Le reti wireless richiedono un trattamento speciale a causa del perimetro di rete scarsamente definito. Per gli ambienti sensibili, tutti gli accessi wireless DEVONO essere trattati come connessioni esterne e segregati dalle reti interne fino a quando l'accesso non ha attraversato un gateway prima di concedere l'accesso ai sistemi interni.

L'accesso alla rete wireless per il personale e gli ospiti DEVE essere segregato su SSID separati con controlli di sicurezza distinti.

### Standard di sicurezza wireless

Si applicano i seguenti standard di sicurezza wireless:

- WPA3 è preferito per tutte le reti wireless.
- La modalità WPA2 Enterprise con autenticazione 802.1X e crittografia AES è lo standard minimo accettabile per le reti aziendali.
- La modalità WPA2 Personal può essere utilizzata per le reti non di produzione (ad es. accesso ospiti) con una passphrase casuale di almeno 16 caratteri e crittografia AES.
- WEP NON deve essere utilizzato in nessuna circostanza.
- WPA (originale) e la crittografia TKIP NON devono essere utilizzati.

## Accesso alle reti e ai servizi di rete

Agli utenti DEVE essere fornito accesso solo alla rete e ai servizi di rete per i quali sono stati specificamente autorizzati.

L'accesso alle reti e ai servizi di rete DEVE essere conforme alla Politica di controllo degli accessi.

Prima di connettersi alla rete, i dispositivi DEVONO:

- Essere stati registrati nel registro degli asset.
- Essere stati aggiornati con le ultime patch di sicurezza.
- Avere installata e aggiornata una protezione adeguata contro il malware.
- Avere password e account predefiniti modificati o disabilitati.
- Essere stati inclusi dove possibile nel sistema di gestione e monitoraggio della rete.
- Avere le porte, i servizi, le applicazioni e gli account ospite non necessari rimossi o disabilitati.

L'organizzazione DEVE implementare controlli tecnici per verificare la conformità dei dispositivi prima di concedere l'accesso alla rete. I meccanismi di applicazione includono soluzioni NAC (Network Access Control), autenticazione 802.1X basata su certificati o credenziali, valutazione della postura al gateway VPN, o registrazione e approvazione manuale da parte dell'IT. I dispositivi non conformi DEVONO essere collocati in un segmento di quarantena o limitato fino al raggiungimento della conformità.

## Accesso remoto

L'accesso remoto alla rete dell'organizzazione DEVE essere protetto utilizzando tunnel crittografati (VPN o equivalente) con autenticazione a più fattori (AMF).

Le connessioni VPN DEVONO utilizzare protocolli correnti e sicuri:

- WireGuard o IKEv2/IPsec sono preferiti.
- OpenVPN è accettabile dove WireGuard o IKEv2 non sono supportati.
- PPTP e L2TP senza IPsec NON devono essere utilizzati.

Le connessioni remote DEVONO essere impostate per disconnettersi dopo un periodo di inattività definito.

DEVE essere mantenuto e revisionato trimestralmente un elenco degli utenti con accesso remoto.

Il tunneling diviso (split tunnelling, che consente ad alcuni traffici di bypassare la VPN) può essere consentito solo quando:

- Una valutazione del rischio documentata dimostra un rischio residuo accettabile.
- Tutte le risorse dell'organizzazione (condivisioni file, database, applicazioni, e-mail) sono accessibili solo tramite il tunnel crittografato.
- Il traffico con tunneling diviso è limitato a destinazioni non sensibili e solo su Internet.
- L'endpoint dell'utente soddisfa tutti i requisiti di baseline di sicurezza (patch aggiornate, antivirus/EDR, crittografia).
- Il tunneling diviso è disabilitato per gli account privilegiati e amministrativi.

## Posizioni di rete

Le infrastrutture di rete e i siti di elaborazione dei dati DEVONO essere selezionati in base alla valutazione del rischio, alla classificazione dei dati e ai requisiti applicabili di protezione dei dati.

Si applica la seguente gerarchia di preferenza per la posizione di infrastrutture di rete, data center e servizi cloud che trattano dati personali o riservati:

1. In Svizzera.
2. In paesi riconosciuti dal Consiglio federale svizzero come fornitori di protezione dei dati adeguata per **l'Allegato 1 dell'Ordinanza sulla protezione dei dati (OPDo)**. L'attuale elenco di adeguatezza è pubblicato dall'Incaricato federale della protezione dei dati e della trasparenza (IFPDT) e DEVE essere verificato prima di distribuire infrastrutture o servizi in una nuova giurisdizione.
3. In paesi in cui sono in vigore Clausole contrattuali standard (SCC) o altre garanzie adeguate ai sensi della nLPD Art. 16-17.

I trasferimenti di dati transfrontalieri DEVONO essere conformi alla Politica di trasferimento delle informazioni e ai requisiti della nLPD. Il consulente legale DEVE verificare lo stato di adeguatezza di qualsiasi paese prima della distribuzione.

## Dispositivi di rete fisici

I dispositivi di rete fisici DEVONO essere gestiti in conformità con la Politica di sicurezza fisica e ambientale, in particolare le sezioni sulla sicurezza dei cablaggi, l'ubicazione e la protezione delle attrezzature e il controllo degli accessi.

I dispositivi di rete fisici DEVONO essere distrutti in conformità con la Politica di classificazione e gestione delle informazioni, in particolare la sezione sulla distruzione di supporti e dispositivi elettronici.

I dispositivi di rete fisici DEVONO essere gestiti in conformità con la Politica di gestione degli asset e soggetti al processo di gestione degli asset.

## Filtro web

L'accesso ai siti web contenenti informazioni illegali o noti per contenere contenuti malevoli DEVE essere limitato.

L'accesso ai seguenti tipi di siti web DEVE essere bloccato ove praticabile:

- Siti web con una funzione di caricamento delle informazioni, a meno che non sia consentito per validi motivi aziendali.
- Siti web malevoli noti o sospetti (phishing, distribuzione di malware).
- Server di comando e controllo.
- Siti web malevoli identificati nei feed di intelligence sulle minacce.
- Siti web che condividono contenuti illegali.
- Servizi proxy e anonimizzatori (a meno che non siano necessari per scopi aziendali approvati).

Il filtro web DEVE essere implementato utilizzando filtraggio basato su DNS, proxy web o tecnologia equivalente. Le categorie di filtro e le eccezioni DEVONO essere revisionate trimestralmente.

### Sicurezza DNS

- I resolver DNS dovrebbero convalidare le firme DNSSEC dove disponibili per proteggersi dallo spoofing DNS.
- Le zone DNS interne NON devono essere esposte a Internet. Il DNS split-horizon è raccomandato per le organizzazioni con risoluzione dei nomi interna ed esterna.
- Le query DNS dovrebbero essere registrate per le indagini di sicurezza e il rilevamento delle minacce.

## Intrusione host, intrusione di rete, malware e antivirus

I servizi e i dispositivi di rete DEVONO essere gestiti in conformità con la Politica su malware e antivirus.

Il rilevamento delle intrusioni host e il rilevamento/prevenzione delle intrusioni di rete DEVONO essere distribuiti in base al rischio, alla necessità aziendale e ove praticamente fattibile.

**Posizioni minime di distribuzione IDS/IPS:**

| Posizione | Tipo | Scopo |
|-----------|------|-------|
| Perimetro Internet (firewall/gateway) | IDS/IPS di rete | Rilevare/prevenire attacchi esterni e traffico malevolo in entrata |
| Tra i segmenti di rete (inter-VLAN) | IDS/IPS di rete | Rilevare il movimento laterale tra le zone di fiducia |
| Rete server/applicazioni | IDS di rete o host-based IDS | Rilevare accessi anomali ai sistemi critici |
| Endpoint (workstation, server) | IDS host-based (EDR/XDR) | Rilevare minacce a livello di endpoint, malware fileless, processi sospetti |
| Carichi di lavoro cloud (IaaS/PaaS) | IDS cloud-nativo o CASB | Rilevare minacce che prendono di mira l'infrastruttura cloud |

Le posizioni di distribuzione aggiuntive DEVONO essere determinate dalla valutazione del rischio. Laddove gli appliance IDS/IPS dedicati non siano fattibili, sono accettabili capacità di rilevamento equivalenti (ad es. EDR con visibilità di rete, strumenti di sicurezza cloud-nativi).

Il traffico di rete DEVE essere monitorato per rilevare comportamenti anomali. Gli avvisi di sicurezza DEVONO essere sottoposti a triage ed escalation secondo il processo di gestione degli incidenti.

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

- **Diagramma dell'architettura di rete** (attuale, con segmenti, zone di fiducia, gateway) — *aggiornato in seguito a modifiche; revisionato annualmente*
- **Set di regole del firewall e del gateway** con cronologia documentata delle modifiche e firma di revisione annuale — *modifiche delle regole conservate per 3 anni; revisione annuale documentata con firma del RSSI*
- **Inventario e baseline di configurazione dei dispositivi di rete** — *aggiornato entro 5 giorni lavorativi dalla modifica; verificato annualmente*
- **Registrazioni della configurazione della sicurezza wireless** (WPA3/WPA2-Enterprise) — *revisionate semestralmente*
- **Elenco degli accessi VPN e registrazioni delle revisioni trimestrali** — *revisionate trimestralmente; account inattivi disabilitati*
- **Configurazione del filtro web e log delle eccezioni** — *eccezioni revisionate trimestralmente; categorie di filtro aggiornate mensilmente*
- **Rapporti di monitoraggio della rete e avvisi IDS/IPS** — *conservati per un minimo di 12 mesi; avvisi critici revisionati quotidianamente*
- **Revisione degli accessi alla rete e registrazioni della conformità dei dispositivi** — *revisionate trimestralmente per gli accessi privilegiati; annualmente per gli accessi standard*
- **Rapporti di conformità alla gestione delle patch** (dispositivi di rete secondo la tabella CVSS) — *revisionati mensilmente*
- **Registrazioni della rotazione della passphrase della rete ospiti** — *rotazione trimestrale documentata*

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, audit della configurazione di rete, test di penetrazione, scansione delle vulnerabilità, audit interni ed esterni e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita. Le eccezioni devono essere riportate al team di revisione della direzione.

## Non conformità

Un dipendente che risulti aver violato questa politica può essere soggetto ad azioni disciplinari, fino al licenziamento.

## Miglioramento continuo

Questa politica viene rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti agli standard di sicurezza della rete, le minacce emergenti, i cambiamenti normativi e le lessons learned dagli incidenti.

---

# Aree dello standard ISO 27001 trattate

Politica di sicurezza della rete — Mapping dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 6.3 Sensibilizzazione, educazione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | **8.20 Sicurezza della rete** |
| | **8.21 Sicurezza dei servizi di rete** |
| | **8.22 Segregazione delle reti** |
| | 8.23 Filtro web |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|-----------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la protezione dei dati |
| OPDo svizzero | Art. 1-3 — Requisiti minimi per la sicurezza dei dati; Allegato 1 — Elenco di adeguatezza |
| GDPR UE (se applicabile) | Art. 32 — Sicurezza del trattamento (controlli di rete come misura appropriata) |
| ISO/IEC 27001:2022 | Annex A Controlli 8.20, 8.21, 8.22 |
| ISO/IEC 27002:2022 | Sezioni 8.20, 8.21, 8.22 — Indicazioni di implementazione |
| NIST SP 800-53 Rev 5 | SC-7 (Boundary Protection), SC-8 (Transmission Confidentiality) |
| CIS Controls v8 | Controllo 12 (Network Infrastructure Management), Controllo 13 (Network Monitoring and Defense) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
