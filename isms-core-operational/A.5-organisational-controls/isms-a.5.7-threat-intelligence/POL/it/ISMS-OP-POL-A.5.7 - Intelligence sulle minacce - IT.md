<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.7-IT:operational:OP-POL:a.5.7 -->
**ISMS-OP-POL-A.5.7 — Intelligence sulle minacce**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Intelligence sulle minacce |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.5.7 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
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
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Data prossima revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.5.7 — Intelligence sulle minacce
- ISO/IEC 27002:2022 Sezione 5.7 — Guida all'implementazione
- NIST SP 800-150 — Guida alla condivisione delle informazioni sulle minacce informatiche
- NIST SP 800-53 Rev 5 PM-16 — Programma di consapevolezza delle minacce
- NIST SP 800-53 Rev 5 RA-3 — Valutazione del rischio
- NIST SP 800-53 Rev 5 SI-5 — Avvisi, advisory e direttive di sicurezza
- FIRST TLP v2.0 — Traffic Light Protocol per la condivisione delle informazioni
- OASIS STIX v2.1 / TAXII v2.1 — Standard per lo scambio di intelligence sulle minacce

**Controlli Annex A correlati**:

| Controllo | Relazione con l'intelligence sulle minacce |
|-----------|---------------------------------------------|
| A.5.1 Politiche per la sicurezza delle informazioni | Quadro normativo generale che disciplina i requisiti di intelligence sulle minacce |
| A.5.24-28 Gestione degli incidenti | L'intelligence sulle minacce migliora il rilevamento, l'indagine e la risposta |
| A.5.30 Prontezza ICT per la continuità operativa | L'intelligence sulle minacce informa la pianificazione della continuità e la preparazione alle minacce |
| A.8.7 Protezione contro il malware | L'intelligence sulle minacce fornisce IoC per il rilevamento del malware |
| A.8.8 Gestione delle vulnerabilità tecniche | L'intelligence sullo sfruttamento prioritizza la remediation delle vulnerabilità |
| A.8.15 Registrazione | I log forniscono telemetria interna per l'analisi dell'intelligence sulle minacce |
| A.8.16 Attività di monitoraggio | L'intelligence sulle minacce fornisce contesto di rilevamento e regole di correlazione |
| A.8.23 Filtraggio web | L'intelligence sulle minacce fornisce feed di domini e URL dannosi |

**Politiche interne correlate**:

- Politica di gestione degli incidenti
- Politica di gestione del rischio
- Politica di gestione delle vulnerabilità
- Politica di registrazione
- Politica delle attività di monitoraggio (A.8.16)
- Politica di protezione contro il malware
- Politica di classificazione e gestione delle informazioni

---

# Politica sull'intelligence sulle minacce

## Scopo

Lo scopo della presente politica è stabilire i requisiti per la raccolta, l'analisi e l'utilizzo di informazioni sulle minacce attuali ed emergenti alla sicurezza delle informazioni, al fine di abilitare una difesa proattiva, informare le decisioni di gestione del rischio e migliorare la capacità dell'organizzazione di rilevare, prevenire e rispondere agli incidenti di sicurezza.

L'intelligence sulle minacce trasforma i dati grezzi sulle minacce in conoscenza actionable. Senza un'intelligence strutturata sulle minacce, l'organizzazione opera in modo reattivo — rispondendo agli incidenti dopo che si è verificato il danno anziché anticiparli e prevenirli. La presente politica garantisce che l'organizzazione mantenga un'adeguata consapevolezza situazionale del panorama delle minacce rilevante per le proprie operazioni, i propri asset e il proprio settore.

La presente politica supporta la nLPD svizzera attuando misure tecniche e organizzative proporzionate al rischio per proteggere l'integrità del trattamento dei dati personali. L'intelligence sulle minacce contribuisce alle misure di sicurezza dei dati richieste dall'Art. 8 nLPD, consentendo l'identificazione proattiva delle minacce ai sistemi che trattano dati personali. Laddove l'organizzazione tratti dati di soggetti nell'UE/SEE, si applicano altresì i requisiti del GDPR Art. 32 per le misure di sicurezza, incluso il monitoraggio delle minacce.

## Ambito di applicazione

Tutte le attività relative alla raccolta, all'analisi, alla produzione, alla diffusione e al consumo di intelligence sulle minacce in tutta l'organizzazione.

Ciò include:

- Raccolta di informazioni sulle minacce da fonti esterne e interne.
- Analisi e produzione di intelligence a livello strategico, tattico e operativo.
- Diffusione dell'intelligence agli stakeholder appropriati.
- Integrazione dell'intelligence sulle minacce con i processi di valutazione del rischio.
- Integrazione dell'intelligence sulle minacce con la gestione degli incidenti e il monitoraggio della sicurezza.
- Condivisione esterna di intelligence sulle minacce con partner e comunità fidate.

**Escluso dall'ambito**: Operazioni informatiche offensive o azioni di ritorsione (vietate); indagini delle forze dell'ordine (supportata la cooperazione, non la conduzione); operazioni di scansione delle vulnerabilità e penetration testing (disciplinate dall'A.8.8); procedure di threat hunting (disciplinate dall'A.8.16); operazioni di intelligence non correlate alla sicurezza delle informazioni.

## Principio

Le informazioni relative alle minacce alla sicurezza delle informazioni dovrebbero essere raccolte e analizzate per produrre intelligence sulle minacce. L'intelligence sulle minacce DEVE essere pertinente al panorama specifico delle minacce dell'organizzazione, tecnicamente accurata, contestualizzata agli asset e al profilo di rischio organizzativo, e actionable — fornendo indicazioni chiare che consentano all'organizzazione di rilevare, prevenire o rispondere alle minacce identificate.

L'organizzazione DEVE mantenere capacità di intelligence sulle minacce proporzionate alle proprie dimensioni, all'esposizione al rischio e al settore. Non ogni organizzazione necessita di un Security Operations Centre (SOC) dedicato o di analisti di intelligence sulle minacce a tempo pieno. Ciò che ogni organizzazione richiede è un processo strutturato e documentato per mantenersi informata sulle minacce rilevanti per le proprie operazioni e per agire su tali informazioni.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Intelligence sulle minacce** | Informazioni sulle minacce attuali o emergenti che sono state raccolte, elaborate e analizzate per abilitare decisioni di sicurezza informate e una difesa proattiva |
| **Intelligence strategica** | Intelligence di alto livello che affronta le tendenze generali delle minacce, le motivazioni degli attori delle minacce e i rischi specifici del settore, a supporto delle decisioni dirigenziali e della strategia di sicurezza a lungo termine |
| **Intelligence tattica** | Intelligence che descrive le tattiche, le tecniche e le procedure (TTP) degli avversari, a supporto della pianificazione delle operazioni di sicurezza e della configurazione delle difese |
| **Intelligence operativa** | Intelligence tecnica actionable che include indicatori di compromissione (IoC) e firme di rilevamento, a supporto delle operazioni immediate di rilevamento e risposta |
| **Indicatore di compromissione (IoC)** | Un artefatto osservabile — come un indirizzo IP, un nome di dominio, un hash di file o un indirizzo e-mail — che indica che si è verificata o è in corso una violazione della sicurezza |
| **Tattiche, Tecniche e Procedure (TTP)** | Schemi di comportamento e metodi utilizzati dagli attori delle minacce per condurre attacchi, documentati in framework come MITRE ATT&CK |
| **Traffic Light Protocol (TLP)** | Un sistema di classificazione per la condivisione delle informazioni che utilizza codici colore (TLP:RED, TLP:AMBER+STRICT, TLP:AMBER, TLP:GREEN, TLP:CLEAR) per indicare i limiti di condivisione consentiti |
| **STIX (Structured Threat Information eXpression)** | Un linguaggio standard OASIS e un formato di serializzazione per lo scambio di intelligence sulle minacce informatiche in modo strutturato e leggibile dalle macchine |
| **TAXII (Trusted Automated eXchange of Intelligence Information)** | Un protocollo applicativo standard OASIS per lo scambio automatizzato di intelligence sulle minacce informatiche tramite HTTPS |
| **MITRE ATT&CK** | Una base di conoscenza globalmente accessibile di tattiche e tecniche degli avversari basata su osservazioni del mondo reale, mantenuta dalla MITRE Corporation |
| **Attore della minaccia** | Un individuo, un gruppo o un'organizzazione che conduce attività informatiche malevole con intento e capacità identificabili |
| **OSINT (Open-Source Intelligence)** | Intelligence sulle minacce derivata da fonti pubblicamente disponibili inclusi blog di sicurezza, database di vulnerabilità, social media e advisory pubblici |

---

## Tipologie e livelli di intelligence

L'organizzazione DEVE produrre o consumare intelligence sulle minacce a tre livelli, ciascuno al servizio di un pubblico e di uno scopo distinto. Non tutte le organizzazioni produrranno intelligence a ogni livello internamente; il consumo da fonti esterne è accettabile laddove la capacità di produzione interna sia limitata.

### Intelligence strategica

**Pubblico**: Direzione generale, RSSI, Gestione del rischio.
**Scopo**: Informare le decisioni aziendali, gli investimenti in sicurezza e la strategia a lungo termine.

L'intelligence strategica DEVE affrontare:

- Il panorama complessivo delle minacce rilevante per il settore e la geografia dell'organizzazione.
- Le motivazioni e le capacità degli attori delle minacce che prendono di mira il settore dell'organizzazione.
- Le tendenze emergenti delle minacce e il loro potenziale impatto sul business.
- Gli sviluppi normativi e geopolitici che influenzano l'ambiente delle minacce.
- Gli incidenti di organizzazioni simili e le campagne di attacco a livello di settore.

**Frequenza di produzione**: Trimestrale come minimo, o attivata da cambiamenti significativi nel panorama delle minacce. Laddove l'organizzazione non produca intelligence strategica internamente, DEVE abbonarsi o accedere ad almeno una fonte di reportistica strategica sulle minacce pertinente al settore (es. rapporti semestrali dell'NCSC svizzero, advisory CERT o servizi commerciali di intelligence strategica).

### Intelligence tattica

**Pubblico**: Personale delle operazioni di sicurezza, amministratori IT, operatori della risposta agli incidenti.
**Scopo**: Informare le configurazioni difensive, le regole di rilevamento e l'architettura di sicurezza.

L'intelligence tattica DEVE affrontare:

- Profili degli attori delle minacce e TTP rilevanti per il parco tecnologico dell'organizzazione.
- Pattern di attacco e analisi delle campagne che prendono di mira il settore dell'organizzazione.
- Famiglie di malware e le loro caratteristiche comportamentali.
- Tecniche di ingegneria sociale e pattern delle campagne di phishing.
- Misure difensive raccomandate e strategie di rilevamento.

**Frequenza di produzione**: Mensile come minimo, o attivata da minacce emergenti. Laddove la capacità di analisi interna sia limitata, l'organizzazione DEVE consumare intelligence tattica da almeno una fonte strutturata (es. MITRE ATT&CK, advisory dell'NCSC svizzero, feed CERT o report commerciali sulle minacce).

### Intelligence operativa

**Pubblico**: Personale tecnico di sicurezza, amministratori di sistema, analisti SOC.
**Scopo**: Abilitare il rilevamento e il blocco immediato delle minacce note.

L'intelligence operativa DEVE includere:

- Indicatori di compromissione (IoC): indirizzi IP dannosi, domini, URL, hash di file, indirizzi e-mail.
- Firme malware e indicatori comportamentali.
- Regole di rilevamento e regole YARA.
- Blocklist per firewall, gateway e-mail e filtri web.

**Frequenza di produzione**: Continuamente tramite feed automatizzati, con revisione periodica degli analisti (giornaliera dove è operativo un SOC; settimanale come minimo per le organizzazioni senza un SOC dedicato).

---

## Categorie di fonti

L'organizzazione DEVE mantenere fonti di intelligence sulle minacce in più categorie per evitare la dipendenza da una singola fonte e garantire una copertura completa. Il numero e la profondità delle fonti DEVONO essere proporzionati alle dimensioni organizzative e all'esposizione al rischio.

### Categorie di fonti obbligatorie

| Categoria | Descrizione | Esempi | Requisito minimo |
|-----------|-------------|--------|-----------------|
| **Governo / CERT** | Advisory e avvisi dei CERT nazionali e specifici del settore | NCSC svizzero (ncsc.admin.ch), GovCERT.ch, CERT-EU, US-CERT/CISA | Almeno un abbonamento a un CERT nazionale |
| **Open-Source Intelligence (OSINT)** | Dati sulle minacce pubblicamente disponibili, database di vulnerabilità, ricerca sulla sicurezza | CVE/NVD, AlienVault OTX, Abuse.ch, VirusTotal, blog di ricercatori di sicurezza | Almeno due feed OSINT |
| **Telemetria interna** | Eventi di sicurezza e risultati dei sistemi propri dell'organizzazione | Alert [SIEM], log del firewall, report del gateway e-mail, alert di rilevamento endpoint, post-mortem degli incidenti | Tutti gli output disponibili degli strumenti di sicurezza interni |

### Categorie di fonti raccomandate

| Categoria | Descrizione | Esempi | Quando implementare |
|-----------|-------------|--------|---------------------|
| **Piattaforme commerciali** | Intelligence sulle minacce curata e validata con qualità garantita da SLA | [Piattaforma di intelligence sulle minacce], Recorded Future, Mandiant, CrowdStrike | Quando il budget lo consente e l'esposizione alle minacce giustifica l'investimento |
| **Condivisione di settore (ISAC/ISAO)** | Intelligence sulle minacce specifica del settore condivisa tra peer | Financial ISAC (FS-ISAC), Health ISAC, gruppi di condivisione specifici del settore | Quando esiste un ISAC/ISAO rilevante per il settore dell'organizzazione |
| **Advisory di sicurezza dei fornitori** | Informazioni su minacce e vulnerabilità dai fornitori di tecnologia | Microsoft Security Response Centre, AWS Security Bulletins, feed specifici dei fornitori | Per tutti i fornitori di tecnologia critici in uso |

### Valutazione delle fonti

Tutte le fonti di intelligence sulle minacce DEVONO essere valutate prima dell'operativizzazione e periodicamente in seguito. La valutazione DEVE considerare:

- **Affidabilità**: La storia della fonte nel fornire informazioni accurate.
- **Tempestività**: Con quale rapidità le informazioni sono disponibili dopo l'emergere di una minaccia.
- **Pertinenza**: Se la fonte copre minacce applicabili al settore, alla geografia e al parco tecnologico dell'organizzazione.
- **Actionabilità**: Se le informazioni abilitano azioni difensive concrete.
- **Tasso di falsi positivi**: La proporzione di indicatori che si rivelano benigni dopo l'indagine.

Le fonti che forniscono costantemente informazioni imprecise, irrilevanti o eccessivamente rumorose DEVONO essere sostituite o de-prioritizzate. Le prestazioni delle fonti DEVONO essere riviste almeno annualmente.

---

## Gestione dell'intelligence fornita dai fornitori

Laddove l'organizzazione sottoscriva servizi o piattaforme commerciali di intelligence sulle minacce, si applicano i requisiti di gestione dei fornitori.

### Criteri di selezione dei fornitori

I fornitori commerciali di intelligence sulle minacce DEVONO essere valutati sulla base di:

| Criterio | Metodo di valutazione | Soglia di accettazione |
|----------|-----------------------|------------------------|
| **Qualità dell'intelligence** | Revisione di un campione di 30 giorni durante il periodo di prova; analisi del tasso di falsi positivi | <10% di tasso di falsi positivi; >90% di pertinenza al settore dell'organizzazione |
| **Tempestività** | Tempo dall'emergere della minaccia alla disponibilità del feed | <24 ore per gli IoC critici; <72 ore per l'intelligence tattica |
| **Trasparenza delle fonti** | Il fornitore divulga i metodi di raccolta dell'intelligence e le fonti | Metodologia documentata; fonti primarie identificate |
| **Conformità alla protezione dei dati** | Il trattamento dei dati personali negli IoC da parte del fornitore è conforme alla nLPD/GDPR | Accordo di trattamento dei dati in vigore; base giuridica documentata |
| **Integrazione con la piattaforma** | Compatibilità con gli strumenti di sicurezza dell'organizzazione (SIEM, EDR, firewall) | Protocolli di integrazione standard supportati (STIX/TAXII, API, syslog) |
| **Stabilità del fornitore** | Solidità finanziaria, base clienti, reputazione nel settore | Fornitore consolidato con >2 anni di attività; riferimenti disponibili |

### Monitoraggio continuativo delle prestazioni del fornitore

| Metrica | Obiettivo | Frequenza di revisione | Proprietario |
|---------|-----------|------------------------|--------------|
| **Uptime del feed** | >99% | Mensile | Operazioni IT |
| **Tasso di falsi positivi** | <10% | Trimestrale | RSSI |
| **Contributo di veri positivi** | >5 rilevamenti validati per trimestre | Trimestrale | RSSI |
| **Tempestività vs. fonti OSINT** | Il feed commerciale fornisce intelligence ≥24 ore prima delle fonti gratuite | Trimestrale | RSSI |
| **Reattività del supporto** | Richieste di supporto risolte entro lo SLA del fornitore | Per incidente | Operazioni IT |
| **Conformità alla protezione dei dati** | Nessun incidente di trattamento non autorizzato di dati personali | Continuativa | Consulente per la protezione dei dati |

### Requisiti del contratto con il fornitore

I contratti con i fornitori commerciali di intelligence sulle minacce DEVONO includere:

- **Accordo sul livello di servizio (SLA)** che specifica uptime, aggiornamento del feed e tempi di risposta del supporto
- **Accordo di trattamento dei dati (DPA)** che affronta i dati personali negli IoC (obblighi del responsabile ai sensi della nLPD Art. 9 o del GDPR Art. 28)
- **Termini di proprietà intellettuale** che chiariscono l'uso consentito dell'intelligence (solo sicurezza interna; nessuna ridistribuzione senza approvazione)
- **Risoluzione e portabilità dei dati** — possibilità di esportare i dati di intelligence in formato standard alla risoluzione del contratto
- **Notifica degli incidenti** — obbligo del fornitore di notificare l'organizzazione di qualsiasi incidente di sicurezza che interessa il servizio di intelligence entro 24 ore

### Revisione annuale del fornitore

I fornitori commerciali di intelligence DEVONO essere revisionati annualmente coprendo:
- Prestazioni rispetto agli SLA e alle metriche di qualità
- Analisi costi-benefici (valore erogato vs. costo dell'abbonamento)
- Confronto con fornitori alternativi o fonti OSINT
- Raccomandazione di rinnovo del contratto con giustificazione documentata

**Documentazione della revisione conservata 3 anni; decisioni di rinnovo documentate nel registro dei rischi dei fornitori.**

---

## Raccolta e analisi

### Processo di raccolta

L'organizzazione DEVE implementare un processo documentato per la raccolta di intelligence sulle minacce che include:

1. **Raccolta automatizzata**: I feed sulle minacce DEVONO essere acquisiti automaticamente ove fattibile, utilizzando protocolli standard (STIX/TAXII ove supportato) o API specifiche del fornitore. I feed automatizzati DEVONO essere indirizzati al [SIEM] o alla [Piattaforma di intelligence sulle minacce] per l'elaborazione centralizzata.

2. **Raccolta manuale**: Il personale di sicurezza DEVE revisionare fonti di advisory, notizie di sicurezza e forum della comunità secondo un calendario definito. I risultati della raccolta manuale DEVONO essere documentati e inseriti nel registro dell'intelligence sulle minacce.

3. **Raccolta interna**: Gli eventi di sicurezza, i risultati delle indagini sugli incidenti e i risultati dell'analisi forense DEVONO essere acquisiti come intelligence sulle minacce interna. Le revisioni post-incidente DEVONO identificare e registrare esplicitamente gli IoC e le TTP riscontrate.

4. **Protezione dei dati**: Tutta l'intelligence raccolta DEVE essere conforme ai requisiti applicabili di protezione dei dati. I dati personali inclusi nell'intelligence sulle minacce (es. indirizzi e-mail negli indicatori di phishing) DEVONO essere trattati solo per il legittimo interesse della sicurezza delle informazioni e conservati solo finché l'indicatore rimane operativamente rilevante.

### Processo di analisi

I dati grezzi sulle minacce DEVONO essere analizzati prima della diffusione per garantire qualità e pertinenza. L'analisi DEVE:

- **Validare** le informazioni attraverso più fonti ove possibile.
- **Contestualizzare** le minacce rispetto agli asset specifici, al parco tecnologico e al profilo di rischio dell'organizzazione.
- **Valutare** la probabilità e il potenziale impatto delle minacce identificate sull'organizzazione.
- **Prioritizzare** le minacce in base alla pertinenza, alla gravità e all'esposizione dell'organizzazione.
- **Produrre** raccomandazioni actionable o indicazioni di rilevamento.

Laddove l'organizzazione non disponga di analisti di intelligence sulle minacce dedicati, le responsabilità di analisi DEVONO essere assegnate al RSSI o al personale di sicurezza designato. L'analisi non deve necessariamente essere un'attività a tempo pieno per le organizzazioni più piccole, ma DEVE essere un'attività documentata e ricorrente con una chiara titolarità.

### Requisiti di qualità

Tutta l'intelligence sulle minacce — prodotta internamente o consumata da fonti esterne — DEVE soddisfare i seguenti criteri di qualità prima di essere presa in considerazione:

- **Pertinente**: Applicabile al panorama delle minacce, al settore e all'ambiente tecnologico dell'organizzazione.
- **Accurata**: Validata attraverso corroborazione o valutazione dell'affidabilità della fonte.
- **Tempestiva**: Attuale e consegnata entro un lasso di tempo che consenta un'azione efficace.
- **Actionable**: Accompagnata da indicazioni chiare sulle azioni di rilevamento, prevenzione o risposta.

L'intelligence che non soddisfa questi criteri DEVE essere segnalata, indagata o scartata. I verbali di valutazione delle fonti DEVONO documentare i problemi di qualità.

---

## Gestione del ciclo di vita dei dati di intelligence

### Requisiti di conservazione

I dati di intelligence sulle minacce DEVONO essere conservati in conformità ai requisiti operativi e normativi:

| Tipo di intelligence | Periodo di conservazione | Motivazione |
|---------------------|--------------------------|-------------|
| **IoC operativi** (in rilevamento attivo) | Finché la minaccia rimane rilevante; minimo 90 giorni | Il rilevamento attivo richiede indicatori aggiornati |
| **IoC storici** (non più attivi) | 12 mesi dopo la disattivazione | Contesto storico per le indagini sugli incidenti; analisi delle tendenze |
| **Report di intelligence strategica e tattica** | 3 anni | Audit trail della valutazione del rischio; valutazione della maturità del programma; contesto storico |
| **Intelligence interna dagli incidenti** | Secondo il calendario di conservazione degli incidenti (tipicamente 5 anni) | Conformità normativa; eventuali procedimenti legali |
| **Verbali di valutazione delle fonti** | 3 anni | Audit trail per le decisioni di selezione delle fonti |
| **Accordi di condivisione dell'intelligence** | 7 anni dopo la risoluzione | Requisiti di conservazione dei verbali legali |

### Gestione del ciclo di vita degli IoC

Gli indicatori di compromissione distribuiti ai sistemi di rilevamento DEVONO essere gestiti attraverso un processo di ciclo di vita:

1. **Acquisizione** — IoC ricevuto dalla fonte, validato e classificato (TLP, tipo di minaccia, gravità)
2. **Distribuzione** — IoC distribuito ai sistemi di rilevamento pertinenti (SIEM, EDR, firewall, filtro web)
3. **Monitoraggio attivo** — L'IoC genera alert quando corrisposto; alert sottoposti a triage e indagine
4. **Revisione** — Gli IoC vengono revisionati trimestralmente per la pertinenza continuativa:
   - L'indicatore è stato osservato negli alert? (Attivo vs. dormiente)
   - La minaccia è ancora attuale? (Fonte di intelligence aggiornata o deprecata?)
   - Il tasso di falsi positivi è accettabile? (Se >20% di falsi positivi, considerare la rimozione)
5. **Disattivazione** — IoC rimosso dai sistemi di rilevamento quando non più pertinente
6. **Archiviazione** — IoC spostato nel database storico per l'analisi delle tendenze e il riferimento nelle indagini sugli incidenti
7. **Eliminazione** — IoC eliminato definitivamente dopo la scadenza del periodo di conservazione

**Automazione**: Dove tecnicamente fattibile, la gestione del ciclo di vita degli IoC dovrebbe essere automatizzata attraverso la piattaforma di intelligence sulle minacce (TIP) o la funzionalità SIEM. La gestione manuale degli IoC è accettabile per le organizzazioni senza capacità TIP.

### Considerazioni sulla protezione dei dati

Laddove l'intelligence sulle minacce contenga dati personali (es. indirizzi e-mail negli indicatori di phishing, indirizzi IP di sistemi compromessi):

- **Base giuridica**: Trattamento giustificato dal legittimo interesse per la sicurezza delle informazioni (nLPD Art. 6 par. 2; GDPR Art. 6(1)(f) ove applicabile)
- **Limitazione delle finalità**: I dati personali negli IoC sono trattati solo per il rilevamento delle minacce e la risposta agli incidenti; non utilizzati per altri scopi
- **Minimizzazione della conservazione**: I dati personali sono conservati solo per il tempo operativamente necessario; gli IoC contenenti dati personali vengono prioritizzati per la revisione del ciclo di vita
- **Limitazione degli accessi**: I database di intelligence contenenti dati personali sono limitati al solo personale di sicurezza autorizzato

**DPIA**: Se il trattamento dell'intelligence sulle minacce comporta un monitoraggio sistematico su larga scala o categorie particolari di dati personali, potrebbe essere richiesta una Valutazione d'impatto sulla protezione dei dati (DPIA) ai sensi della nLPD Art. 22.

---

## Diffusione e condivisione

### Diffusione interna

L'intelligence sulle minacce DEVE essere distribuita al pubblico appropriato in base al tipo di intelligence:

| Tipo di intelligence | Destinatari | Formato | Frequenza |
|---------------------|-------------|---------|-----------|
| **Strategica** | Direzione generale, RSSI, Gestione del rischio | Documenti di briefing, report trimestrali | Trimestrale o in caso di cambiamento significativo |
| **Tattica** | Operazioni IT, team di sicurezza, amministratori di sistema | Advisory, sintesi TTP, raccomandazioni difensive | Mensile o in caso di minaccia emergente |
| **Operativa** | [SIEM] / strumenti di sicurezza, analisti SOC, amministratori IT | Feed IoC, regole di rilevamento, blocklist | Continuamente (automatizzato) o settimanalmente (manuale) |

### Escalation per minacce critiche

Quando l'intelligence sulle minacce identifica una minaccia imminente o attiva che prende di mira l'organizzazione o il suo settore:

1. **Notifica immediata** al RSSI (entro 1 ora dall'identificazione).
2. **Valutazione rapida** dell'esposizione organizzativa (entro 4 ore).
3. **Briefing di emergenza** agli stakeholder interessati con le azioni raccomandate.
4. **Attivazione della risposta agli incidenti** se la valutazione della minaccia lo giustifica (ai sensi della Politica di gestione degli incidenti).

### Condivisione esterna

L'organizzazione può condividere intelligence sulle minacce con parti esterne fidate soggette ai seguenti controlli:

- **Classificazione TLP**: Tutta l'intelligence condivisa DEVE essere classificata utilizzando il Traffic Light Protocol v2.0 (TLP:RED, TLP:AMBER+STRICT, TLP:AMBER, TLP:GREEN, TLP:CLEAR). La condivisione NON DEVE superare la designazione TLP assegnata dall'autore originale.
- **Accordi di condivisione**: DEVONO essere in vigore accordi formali (NDA, accordo di condivisione delle informazioni o termini di adesione) prima della condivisione con parti esterne.
- **Protezione dei dati**: L'intelligence condivisa NON DEVE includere dati personali al di là di quanto necessario per il rilevamento delle minacce (es. IoC). Laddove vengano condivisi dati personali, DEVE essere stabilita una base giuridica ai sensi della nLPD.
- **Segnalazione normativa**: Laddove si applichino gli obblighi di segnalazione obbligatoria dell'NCSC svizzero (operatori di infrastrutture critiche — LSIn Art. 74b), l'organizzazione DEVE segnalare gli incidenti informatici rilevanti all'NCSC entro 24 ore in conformità ai requisiti applicabili.

### Ricezione di intelligence esterna

Quando si riceve intelligence sulle minacce da fonti esterne:

- **Rispettare i contrassegni TLP**: L'intelligence ricevuta con designazioni TLP NON DEVE essere condivisa al di là dei limiti consentiti.
- **Validare prima di agire**: Gli IoC ricevuti esternamente DEVONO essere validati rispetto all'ambiente dell'organizzazione prima della distribuzione ai sistemi di blocco o rilevamento per minimizzare i falsi positivi.
- **Accusare ricevuta**: Laddove la condivisione sia bidirezionale, l'organizzazione DEVE accusare ricevuta e fornire feedback sull'utilità dell'intelligence quando richiesto.

---

## Integrazione con la valutazione del rischio

L'intelligence sulle minacce DEVE informare il processo di valutazione del rischio dell'organizzazione ai sensi della Clausola 6.1 di ISO 27001:2022. Questa integrazione è obbligatoria — l'intelligence sulle minacce che non influenza le decisioni di rischio fornisce un valore limitato.

### Punti di integrazione obbligatori

- **Valutazione della probabilità**: L'intelligence sulle minacce relativa a campagne attive, attività di sfruttamento e targeting degli attori delle minacce DEVE informare le stime di probabilità assegnate ai rischi identificati.
- **Valutazione dell'impatto**: L'intelligence sulle tecniche di attacco e le conseguenze osservate nelle organizzazioni peer DEVE informare le valutazioni dell'impatto.
- **Aggiornamenti del registro dei rischi**: Quando l'intelligence sulle minacce identifica nuove minacce o cambiamenti alle minacce esistenti, il registro dei rischi DEVE essere aggiornato di conseguenza. Ogni aggiornamento DEVE fare riferimento alla fonte di intelligence sulle minacce di supporto.
- **Efficacia dei controlli**: L'intelligence sulle minacce relativa a controlli aggirati o inefficaci osservati in natura DEVE attivare una rivalutazione dell'efficacia dei controlli dell'organizzazione.

### Processo

1. Il RSSI o il personale di sicurezza designato DEVE revisionare almeno trimestralmente gli output dell'intelligence sulle minacce strategica e tattica rispetto al registro dei rischi attuale.
2. Le nuove minacce identificate attraverso l'analisi dell'intelligence DEVONO essere sottoposte alla Gestione del rischio per la valutazione formale del rischio.
3. Le modifiche alla probabilità o all'impatto delle minacce basate sull'intelligence DEVONO essere documentate con riferimenti tracciabili ai report di intelligence di supporto.
4. Le decisioni di trattamento del rischio influenzate dall'intelligence sulle minacce DEVONO essere registrate nel registro dei rischi.

### Valutazione delle minacce alla privacy e alla riservatezza

Laddove l'organizzazione tratti dati personali soggetti alla nLPD o al GDPR, l'intelligence sulle minacce DEVE affrontare specificamente le minacce alla riservatezza dei dati e alla privacy:

| Categoria di minaccia | Impatto sulla privacy | Requisiti di intelligence |
|----------------------|----------------------|--------------------------|
| **Esfiltrazione di dati** | Divulgazione non autorizzata di dati personali | IoC per malware di furto di dati, tecniche di esfiltrazione (DNS tunnelling, steganografia), infrastruttura degli attaccanti utilizzata per la gestione dei dati |
| **Furto di credenziali** | Accesso non autorizzato ai sistemi che trattano dati personali | Indicatori di campagne di phishing, firme di malware che rubano credenziali, database di credenziali compromesse |
| **Minacce interne** | Uso improprio intenzionale o accidentale dei dati | Indicatori comportamentali, pattern di abuso degli accessi privilegiati, rilevamento delle anomalie negli accessi ai dati |
| **Violazioni di terze parti** | Compromissione dei dati personali tramite responsabili del trattamento/fornitori | Intelligence sui fornitori di servizi violati, piattaforme SaaS compromesse, fuga di dati dalla supply chain |

**Impatto sul registro dei rischi:**
- I rischi relativi al trattamento dei dati personali (es. "R-DATA-01: Accesso non autorizzato ai dati personali dei clienti") DEVONO essere rivisti trimestralmente rispetto ai risultati dell'intelligence sulle minacce
- L'intelligence sulle minacce che indica un aumento del targeting dei titolari del trattamento nel settore dell'organizzazione DEVE attivare una rivalutazione dell'adeguatezza dei controlli di protezione dei dati
- Le regole di rilevamento per i tentativi di esfiltrazione dei dati DEVONO essere aggiornate in base alle tecniche osservate degli attaccanti

---

## Integrazione con la gestione degli incidenti

L'intelligence sulle minacce DEVE migliorare il rilevamento, l'indagine e la risposta agli incidenti ai sensi dei Controlli A.5.24-28.

### Miglioramento del rilevamento

- Gli IoC dalle fonti di intelligence sulle minacce DEVONO essere distribuiti ai sistemi di rilevamento ([SIEM], [EDR], gateway e-mail, filtro web) per abilitare gli alert automatici.
- Le TTP degli attori delle minacce dall'intelligence tattica DEVONO essere tradotte in regole di rilevamento o casi d'uso di monitoraggio ove fattibile.
- L'efficacia delle regole di rilevamento DEVE essere revisionata periodicamente e le regole aggiornate in base all'evoluzione dell'intelligence.

### Supporto alle indagini

- Quando si verifica un incidente di sicurezza, l'intelligence sulle minacce disponibile DEVE essere interrogata per gli indicatori correlati, i profili noti degli attori delle minacce e il contesto dei pattern di attacco.
- Il contesto dell'intelligence sulle minacce DEVE essere incluso nei verbali delle indagini sugli incidenti a supporto dell'analisi della causa principale e della valutazione dell'attribuzione.

### Feedback post-incidente

- I risultati degli incidenti — inclusi gli IoC di nuova scoperta, le TTP osservate e l'infrastruttura degli attaccanti — DEVONO essere acquisiti come intelligence sulle minacce interna.
- Le revisioni post-incidente DEVONO valutare se le fonti di intelligence sulle minacce esistenti abbiano fornito un adeguato preavviso e se le regole di rilevamento abbiano funzionato come previsto.
- Le lezioni apprese DEVONO essere restituite alla valutazione delle fonti, alla messa a punto delle regole di rilevamento e agli aggiornamenti della valutazione del rischio.

---

## Integrazione con il monitoraggio della sicurezza

L'intelligence sulle minacce DEVE essere integrata con le capacità di monitoraggio della sicurezza per migliorare l'efficacia del rilevamento.

### Requisiti di integrazione

- **Integrazione [SIEM]**: Gli IoC operativi DEVONO essere acquisiti nel [SIEM] per la correlazione con gli eventi di sicurezza interni. Laddove l'acquisizione automatizzata non sia fattibile, l'inserimento manuale degli IoC DEVE essere effettuato secondo un calendario definito.
- **Rilevamento endpoint**: Laddove [EDR] o le piattaforme di protezione endpoint supportino l'integrazione dei feed di intelligence sulle minacce, gli IoC pertinenti DEVONO essere distribuiti ai sistemi di rilevamento endpoint.
- **Sicurezza e-mail**: I domini di phishing noti, gli indirizzi mittente dannosi e gli hash degli allegati DEVONO essere distribuiti alle regole di filtraggio del gateway e-mail.
- **Filtraggio web**: I domini e gli URL dannosi dall'intelligence sulle minacce DEVONO essere distribuiti ai sistemi di filtraggio web o di sicurezza DNS.
- **Regole firewall**: Gli indirizzi IP dannosi noti e gli indicatori di rete DEVONO essere distribuiti alle blocklist del perimetro e dei firewall interni, previa validazione dei falsi positivi.

### Efficacia del monitoraggio

L'organizzazione DEVE tracciare quanto segue per valutare l'efficacia dell'integrazione:

- Numero di alert generati da indicatori derivati dall'intelligence sulle minacce.
- Tasso di veri positivi confermati per gli alert derivati dall'intelligence sulle minacce.
- Tempo dalla ricezione dell'intelligence alla distribuzione della regola di rilevamento.
- Lacune di copertura tra l'intelligence sulle minacce e le capacità di monitoraggio.

---

## Integrazione con la disponibilità e la continuità operativa

L'intelligence sulle minacce DEVE informare la pianificazione della continuità operativa e la protezione della disponibilità del servizio ai sensi dei Controlli A.5.29-30.

### Monitoraggio delle minacce alla disponibilità

Le seguenti categorie di minacce DEVONO essere prioritizzate per il rilevamento e la risposta a causa del loro potenziale impatto sulla disponibilità del servizio:

| Tipo di minaccia | Impatto sulla disponibilità | Priorità di rilevamento | Azione di risposta |
|-----------------|----------------------------|-------------------------|--------------------|
| **Attacco DDoS (Distributed Denial of Service)** | Interruzione diretta del servizio | Alta | Attivare il servizio di mitigazione DDoS; filtraggio del traffico; coordinamento con l'ISP upstream |
| **Ransomware** | Indisponibilità di dati e sistemi | Critica | Contenimento immediato; ripristino dal backup; nessun pagamento del riscatto |
| **Malware wiper** | Distruzione permanente dei dati | Critica | Isolamento immediato; conservazione forense; attivazione del disaster recovery |
| **Attacchi alla supply chain** | Interruzione delle dipendenze da terze parti | Alta | Valutazione di fornitori alternativi; procedure di degrado del servizio |
| **Attacchi di esaurimento delle risorse** | Degradazione della capacità | Media | Scalabilità della capacità; limitazione della frequenza; blocco degli attori malintenzionati |

### Input per la pianificazione della continuità

L'intelligence sulle minacce DEVE fornire i seguenti input alla pianificazione della continuità operativa e del disaster recovery:

1. **Scenari di minaccia** — La revisione annuale degli scenari di minaccia plausibili (ransomware, DDoS, distruzione di dati) basata sugli incidenti osservati nel settore DEVE informare l'analisi dell'impatto sul business (BIA) e le strategie di ripristino.

2. **Validazione degli obiettivi di tempo di ripristino (RTO)** — Le velocità di attacco osservate in natura (es. tempo di cifratura del ransomware, durata degli attacchi DDoS) DEVONO essere confrontate con le assunzioni RTO per validare la fattibilità del ripristino.

3. **Rischi delle dipendenze da terze parti** — L'intelligence sugli attacchi alla supply chain o sugli incidenti dei fornitori di servizi cloud DEVE attivare revisioni dei piani di contingenza dei fornitori e della preparazione dei fornitori alternativi.

4. **Scenari per le esercitazioni tabletop** — Le esercitazioni annuali di continuità operativa DEVONO incorporare scenari di minaccia realistici derivati dall'intelligence sulle minacce attuale.

**Processo di integrazione:**
- Revisione trimestrale delle minacce che impattano sulla disponibilità da parte del RSSI e del Responsabile della continuità operativa
- Aggiornamento annuale delle assunzioni BIA sulle minacce basate sui risultati dell'intelligence
- Aggiornamenti del piano di continuità operativa documentati con riferimento all'intelligence sulle minacce di supporto

---

## Misurazione dell'efficacia

L'organizzazione DEVE misurare l'efficacia del programma di intelligence sulle minacce per giustificare l'investimento, identificare opportunità di miglioramento e dimostrare valore agli stakeholder.

### Metriche

Le seguenti metriche DEVONO essere tracciate e riferite al RSSI trimestralmente:

| Metrica | Obiettivo | Soglia critica |
|---------|-----------|----------------|
| Fonti di intelligence sulle minacce attive | Secondo i requisiti minimi sopra indicati | Al di sotto del minimo in qualsiasi categoria obbligatoria |
| Revisioni di valutazione delle fonti completate | 100% annualmente | <80% delle fonti riviste |
| Aggiornamenti del registro dei rischi informati dall'intelligence sulle minacce | Almeno 1 per trimestre | 0 aggiornamenti in qualsiasi trimestre |
| Distribuzione degli IoC ai sistemi di rilevamento | Entro 24 ore dalla ricezione validata | >72 ore di tempo medio di distribuzione |
| Alert derivati dall'intelligence sulle minacce (tasso di veri positivi) | >70% | <50% |
| Briefing di intelligence strategica erogati alla Direzione generale | Trimestrale come minimo | Mancato >1 trimestre |
| Feedback di intelligence sulle minacce post-incidente completato | 100% degli incidenti P1/P2 | <80% degli incidenti P1/P2 |

### Revisione annuale del programma

Il RSSI DEVE condurre una revisione annuale del programma di intelligence sulle minacce coprendo:

- Adeguatezza e prestazioni del portafoglio di fonti.
- Qualità e tempestività della produzione di intelligence.
- Efficacia dell'integrazione con la valutazione del rischio, la gestione degli incidenti e il monitoraggio.
- Adeguatezza delle risorse (personale, strumenti, budget).
- Valutazione della maturità rispetto al livello di maturità target dell'organizzazione.
- Raccomandazioni per il miglioramento del programma.

---

## Test e validazione

L'organizzazione DEVE testare l'efficacia dell'intelligence sulle minacce per validare che le fonti di intelligence e le integrazioni di rilevamento funzionino come previsto.

### Test di rilevamento dell'intelligence

| Tipo di test | Frequenza | Metodo | Criteri di successo | Proprietario |
|-------------|-----------|--------|---------------------|--------------|
| **Validazione del rilevamento IoC** | Trimestrale | Distribuire IoC di test (simulazione non dannosa) agli strumenti di sicurezza; verificare che gli alert vengano generati | >90% degli IoC distribuiti attiva gli alert attesi | Sicurezza IT |
| **Integrità del feed di intelligence sulle minacce** | Mensile | Verificare che i feed automatizzati vengano acquisiti correttamente; verificare la presenza di dati obsoleti | Tutti i feed aggiornati entro 24 ore; nessun errore di acquisizione >48 ore | Operazioni IT |
| **Copertura di rilevamento TTP** | Semestrale | Mappare le regole di rilevamento dell'organizzazione su MITRE ATT&CK; identificare le lacune di copertura | >70% delle tecniche MITRE ATT&CK rilevanti per il profilo di minaccia dell'organizzazione coperte da regole di rilevamento | RSSI |
| **Analisi dei falsi positivi** | Trimestrale | Campionare 20 alert derivati dall'intelligence sulle minacce; indagare il tasso di veri positivi | >70% di tasso di veri positivi | Sicurezza IT |
| **Test del percorso di escalation** | Annuale | Simulare uno scenario di minaccia critica; testare l'escalation al RSSI e alla Direzione generale | Escalation completata entro 1 ora; tutti gli stakeholder coinvolti | RSSI |
| **Valutazione dell'utilità delle fonti** | Annuale | Per ogni fonte di intelligence, identificare l'intelligence actionable prodotta negli ultimi 12 mesi | Ogni fonte ha prodotto ≥1 elemento di intelligence actionable o motivazione documentata per la conservazione | RSSI |

### Esercitazioni purple team

Ove le risorse lo consentano, l'organizzazione dovrebbe condurre esercitazioni annuali di purple team:
- **Red team** simula un attacco basato sull'intelligence sulle minacce attuale (TTP realistiche degli avversari)
- **Blue team** (rilevamento e risposta) tenta di rilevare e rispondere utilizzando rilevamenti informati dall'intelligence sulle minacce
- **Debriefing** identifica le lacune nella copertura dell'intelligence, nelle regole di rilevamento o nelle procedure di risposta
- **Azioni di miglioramento** documentate e tracciate attraverso il processo di azione correttiva

**Per le organizzazioni senza capacità purple team:** Le esercitazioni tabletop che simulano scenari di incidenti guidati dall'intelligence sulle minacce costituiscono un'alternativa accettabile.

### Documentazione dei test

Tutte le attività di test DEVONO essere documentate con:
- Data del test, ambito e partecipanti
- Risultati del test (superato/fallito, metriche raggiunte, lacune identificate)
- Azioni correttive assegnate (dove vengono identificate lacune)
- Validazione di follow-up delle azioni correttive

Documentazione dei test conservata 3 anni; riferita nella revisione annuale del programma.

---

## Condivisione dell'intelligence sulle minacce con i clienti (se applicabile)

*Nota: Questa sezione si applica solo se l'organizzazione fornisce servizi di sicurezza gestiti o ha impegni contrattuali per condividere l'intelligence sulle minacce con i clienti.*

### Deliverable di intelligence per i clienti

Laddove l'organizzazione si sia contrattualmente impegnata a fornire intelligence sulle minacce ai clienti:

| Deliverable | Frequenza | Contenuto | Pubblico |
|-------------|-----------|-----------|---------|
| **Briefing sulle minacce** | Trimestrale | Sintesi strategica dell'intelligence rilevante per il settore del cliente; minacce emergenti; azioni raccomandate | Leadership di sicurezza del cliente |
| **Feed IoC** | Continuo o giornaliero | IoC operativi rilevanti per l'ambiente del cliente | SOC del cliente o sicurezza IT |
| **Notifiche di incidenti** | Immediata | Notifica di minacce che prendono attivamente di mira il settore o il parco tecnologico del cliente | Contatto di sicurezza del cliente |
| **Report annuale sulle minacce** | Annuale | Analisi completa del panorama delle minacce; dati sulle tendenze degli attacchi; profili degli attori delle minacce specifici del settore | Direzione generale del cliente |

### Intelligence specifica per il cliente

Per i clienti con accordi di servizio dedicati, l'organizzazione DEVE:
- Personalizzare l'intelligence per il parco tecnologico, la geografia e il profilo di minaccia specifici del cliente
- Fornire raccomandazioni actionable specifiche per l'ambiente del cliente
- Coordinare con il team di sicurezza del cliente sull'applicazione dell'intelligence
- Mantenere la riservatezza dell'intelligence specifica del cliente (non condivisa con altri clienti salvo che anonimizzata)

### Ciclo di feedback dell'intelligence per i clienti

- I clienti DEVONO essere invitati a fornire feedback sull'utilità e la pertinenza dell'intelligence
- Il feedback dei clienti viene incorporato nella revisione trimestrale del programma di intelligence
- Le modifiche ai deliverable vengono effettuate in base alle esigenze e al feedback dei clienti

**Evidenze**: I deliverable di intelligence per i clienti sono documentati con conferma della consegna; il feedback dei clienti è registrato; la conformità ai livelli di servizio è tracciata.

---

## Guida alla scalabilità per le PMI

Non tutte le organizzazioni dispongono di team di intelligence sulle minacce dedicati o di capacità SOC. Le seguenti linee guida aiutano le organizzazioni più piccole a implementare un'intelligence sulle minacce proporzionata alle loro risorse:

### Programma minimo vitale (organizzazioni senza personale di sicurezza dedicato)

- Abbonarsi agli alert dell'NCSC svizzero e ad almeno un feed CERT pertinente.
- Abbonarsi ad almeno due feed gratuiti di minacce OSINT (es. Abuse.ch, AlienVault OTX).
- Assegnare a un individuo (RSSI, IT Manager o contatto di sicurezza designato) la responsabilità di revisionare gli advisory settimanalmente.
- Revisionare i report strategici sul panorama delle minacce dell'NCSC svizzero semestralmente.
- Garantire che gli advisory di sicurezza dei fornitori critici siano monitorati e gestiti.
- Documentare i risultati dell'intelligence sulle minacce in un registro semplice (un foglio di calcolo è accettabile).
- Revisionare il registro trimestralmente rispetto al registro dei rischi.

### Percorso di crescita (organizzazioni con una funzione di sicurezza emergente)

- Aggiungere feed commerciali di intelligence sulle minacce pertinenti al settore e al parco tecnologico.
- Implementare l'acquisizione automatizzata degli IoC nel [SIEM] o nei sistemi firewall.
- Iniziare a produrre intelligence tattica interna dai post-mortem degli incidenti.
- Aderire alle comunità di condivisione delle informazioni pertinenti (ISAC/ISAO) ove disponibili.
- Stabilire un calendario formale di diffusione e briefing agli stakeholder.
- Mappare le minacce osservate al framework MITRE ATT&CK per un'analisi strutturata.

### Programma maturo (organizzazioni con operazioni di sicurezza dedicate)

- Distribuire una [Piattaforma di intelligence sulle minacce] dedicata per la raccolta, l'analisi e la diffusione.
- Impiegare o contrattare analisti di intelligence sulle minacce dedicati.
- Produrre intelligence a tutti e tre i livelli (strategico, tattico, operativo).
- Integrare l'intelligence sulle minacce con tutti gli strumenti di sicurezza tramite feed automatizzati.
- Partecipare attivamente alle comunità di condivisione esterna.
- Condurre esercizi di threat modelling informati dall'intelligence.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità relative all'intelligence sulle minacce |
|-------|--------------------------------------------------------|
| **Direzione generale** | Approvare la politica sull'intelligence sulle minacce; allocare le risorse; ricevere briefing di intelligence strategica; approvare gli accordi di condivisione |
| **RSSI** | Titolarità del programma; gestione del portafoglio di fonti; supervisione della qualità dell'intelligence; escalation per minacce critiche; revisione annuale del programma; approvazione delle eccezioni |
| **IT Manager / Responsabile della sicurezza** | Raccolta e revisione giornaliera dell'intelligence; distribuzione degli IoC agli strumenti di sicurezza; consumo di intelligence tattica e operativa; analisi della telemetria interna |
| **Gestione del rischio** | Integrare l'intelligence sulle minacce nelle valutazioni del rischio; aggiornare il registro dei rischi in base ai risultati dell'intelligence; valutare i cambiamenti del rischio guidati dalle minacce |
| **Risposta agli incidenti** | Applicare l'intelligence sulle minacce durante le indagini; estrarre gli IoC dagli incidenti; fornire feedback post-incidente alla funzione di intelligence |
| **Operazioni IT** | Distribuire gli IoC ai sistemi di rilevamento e blocco; mantenere le integrazioni dei feed; segnalare le anomalie tecniche identificate attraverso il monitoraggio |
| **Tutto il personale** | Segnalare attività sospette e potenziali eventi di sicurezza; completare la formazione sulla consapevolezza delle minacce; seguire gli advisory diffusi |

### Percorso di escalation

- **Intelligence di routine**: IT Manager / Responsabile della sicurezza esamina e agisce. Il RSSI viene informato agli intervalli di reportistica regolari.
- **Minaccia elevata**: IT Manager / Responsabile della sicurezza effettua l'escalation al RSSI entro 4 ore. Il RSSI valuta l'esposizione organizzativa e determina la risposta.
- **Minaccia critica / imminente**: Escalation immediata al RSSI. Il RSSI informa la Direzione generale e attiva la risposta agli incidenti se giustificato.
- **Segnalazione normativa**: Il RSSI coordina la segnalazione obbligatoria all'NCSC svizzero ove applicabile (operatori di infrastrutture critiche — entro 24 ore ai sensi della LSIn Art. 74b).

---

## Evidenze (migliorate per l'audit)

Le seguenti evidenze dimostrano la conformità alla presente politica. **Per gli audit SOC 2 Type II**, i revisori testeranno l'efficacia operativa campionando le evidenze del periodo di audit (tipicamente 12 mesi).

| # | Evidenza | Proprietario | Frequenza | Dettagli dell'audit trail |
|---|----------|--------------|-----------|---------------------------|
| 1 | **Inventario delle fonti di intelligence sulle minacce** | RSSI | *Revisione annuale; aggiornato al verificarsi di modifiche* | Documento di inventario con cronologia delle versioni; registro delle modifiche che mostra aggiunte/rimozioni delle fonti con date e approvazioni |
| 2 | **Verbali di valutazione delle fonti** | RSSI | *Annuale per fonte* | Modello di valutazione completato per ogni fonte; punteggio documentato; decisione di conservare/sostituire la fonte con giustificazione |
| 3 | **Report di intelligence strategica** | RSSI | *Trimestrale come minimo* | Documenti di report con lista di distribuzione e conferma della consegna; verbali delle riunioni della Direzione generale che mostrano la ricezione e la discussione |
| 4 | **Advisory di intelligence tattica** | IT Manager / Responsabile della sicurezza | *Mensile come minimo; ad hoc* | Documenti di advisory con timestamp di distribuzione; conferma di ricevuta da parte degli stakeholder chiave |
| 5 | **Verbali di distribuzione degli IoC** | Operazioni IT | *Per distribuzione* | Ticket di distribuzione o log TIP che mostrano: identificatore IoC, fonte, data/ora di distribuzione, sistemi target, metodo di distribuzione, risultati del test di validazione |
| 6 | **Aggiornamenti del registro dei rischi** | Gestione del rischio | *Per aggiornamento* | Voci del registro dei rischi con timestamp dell'ultimo aggiornamento; campo "fonte di intelligence" che documenta il report di intelligence sulle minacce che ha attivato l'aggiornamento |
| 7 | **Verbali delle indagini sugli incidenti** | Risposta agli incidenti | *Per incidente P1/P2* | Ticket degli incidenti con sezione "contesto dell'intelligence sulle minacce" popolata; risultati della correlazione degli IoC; valutazione dell'attribuzione degli attori delle minacce (ove fattibile) |
| 8 | **Feedback di intelligence post-incidente** | Risposta agli incidenti | *Per incidente P1/P2* | Sezione del post-mortem dell'incidente che documenta: nuovi IoC scoperti, TTP osservate, lacune di intelligence identificate, raccomandazioni per il miglioramento del rilevamento |
| 9 | **Accordi di condivisione esterna** | RSSI | *Per accordo; revisione annuale* | NDA firmati, accordi di adesione ISAC, MoU di condivisione delle informazioni; note della revisione annuale che confermano l'aggiornamento degli accordi |
| 10 | **Verbali di conformità TLP** | RSSI | *Per evento di condivisione* | Registro delle condivisioni che documenta: data, destinatario, classificazione TLP assegnata, approvazione (se TLP:AMBER o superiore), conferma della presa d'atto TLP del destinatario |
| 11 | **Revisioni delle prestazioni dei fornitori** | RSSI | *Annuale per fornitore* | Modello di revisione del fornitore con dati di conformità agli SLA, tassi di falsi positivi, analisi costi-benefici, raccomandazione di rinnovo con firma di approvazione |
| 12 | **Risultati dei test di intelligence** | Sicurezza IT | *Per test (trimestrale/semestrale)* | Report di test che documentano: data del test, ambito, risultati (metriche superato/fallito), lacune identificate, azioni correttive assegnate con scadenze |
| 13 | **Dashboard delle metriche** | RSSI | *Trimestrale* | Screenshot o report del dashboard che mostra tutti i KPI; grafici delle tendenze per il confronto anno su anno; superamenti delle soglie critiche evidenziati con lo stato delle azioni correttive |
| 14 | **Revisione annuale del programma** | RSSI | *Annuale* | Documento di revisione completo che copre le prestazioni delle fonti, l'efficacia dell'integrazione, la valutazione della maturità, l'adeguatezza delle risorse, slide della presentazione alla Direzione generale con firme di approvazione |

### Requisiti dell'audit trail

Per i test di efficacia operativa degli audit SOC 2 Type II, garantire:

- **Completezza**: Tutte le evidenze richieste esistono per l'intero periodo di audit (tipicamente 12 mesi)
- **Accuratezza**: Le evidenze riflettono le attività effettive (non segnaposto del modello)
- **Timestamp**: Tutte le evidenze chiaramente datate; le evidenze elettroniche includono metadati che mostrano le date di creazione/modifica
- **Approvazioni**: Laddove la politica richieda l'approvazione (es. eccezioni, selezioni dei fornitori, accordi di condivisione), l'approvazione è documentata con il nome e la data dell'approvatore
- **Popolazione vs. Campione**: I revisori testeranno tipicamente:
  - **Tutti** i report strategici (dovrebbero essere almeno 4 all'anno)
  - **Campione** di distribuzioni IoC (20-25 campioni)
  - **Tutti** gli incidenti con rating P1/P2 (dovrebbero avere il contesto dell'intelligence sulle minacce)
  - **Tutte** le fonti (dovrebbero avere una valutazione annuale)
  - **Tutti** i contratti con i fornitori (dovrebbero avere una revisione annuale delle prestazioni)

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità alla presente politica attraverso vari metodi, inclusi ma non limitati a: audit delle fonti di intelligence sulle minacce, revisioni dell'efficacia dell'integrazione, tracciamento della diffusione, riferimento incrociato al registro dei rischi, audit interni ed esterni, e feedback al proprietario della politica.

Le seguenti metriche DEVONO essere tracciate e riferite al RSSI trimestralmente:

| Metrica | Obiettivo | Soglia critica |
|---------|-----------|----------------|
| Fonti di intelligence sulle minacce attive nelle categorie obbligatorie | 100% delle categorie obbligatorie coperte | Qualsiasi categoria obbligatoria con 0 fonti attive |
| Revisioni di valutazione delle fonti completate nei tempi previsti | 100% annualmente | <80% delle fonti riviste |
| Briefing di intelligence strategica erogati | Trimestrale come minimo | Mancato >1 trimestre consecutivo |
| Tempestività della distribuzione degli IoC | Entro 24 ore dalla ricezione validata | >72 ore in media |
| Aggiornamenti del registro dei rischi informati dall'intelligence sulle minacce | Almeno 1 per trimestre | 0 aggiornamenti in qualsiasi trimestre |
| Completamento del feedback di intelligence post-incidente (P1/P2) | 100% | <80% |

**Requisiti di reportistica**:
- **Dashboard mensile RSSI**: Fonti attive, highlights recenti dell'intelligence, stato della distribuzione degli IoC, azioni aperte.
- **Report trimestrale alla Direzione generale**: Sintesi del panorama strategico delle minacce, stato delle metriche, raccomandazioni di miglioramento del programma.
- **Riesame annuale della direzione**: Valutazione completa dell'efficacia del programma, inclusa la valutazione della maturità, l'adeguatezza delle risorse e le raccomandazioni strategiche.

Le metriche che superano le soglie critiche DEVONO essere segnalate al RSSI per attenzione immediata e riferite al successivo Riesame della direzione.

## Eccezioni

Qualsiasi eccezione alla presente politica DEVE essere approvata e registrata dal RSSI in anticipo, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita. Le eccezioni comuni includono i vincoli di budget che limitano l'accesso alle fonti commerciali, le limitazioni tecniche che impediscono l'integrazione automatizzata dei feed e i programmi appena implementati che non hanno ancora raggiunto le metriche target. Le eccezioni che richiedono un'allocazione di risorse al di là dell'autorità del RSSI DEVONO richiedere l'approvazione congiunta del RSSI e della Direzione generale. Le eccezioni DEVONO essere limitate nel tempo (massimo 12 mesi), riviste trimestralmente e riferite al team di Riesame della direzione.

## Non conformità

Un dipendente che abbia violato la presente politica può essere soggetto a provvedimenti disciplinari, fino e inclusa la risoluzione del rapporto di lavoro. Le preoccupazioni specifiche di non conformità includono: condivisione di intelligence in violazione delle designazioni TLP; mancato intervento sugli advisory critici sulle minacce entro i lasso di tempo richiesti; mancata segnalazione di minacce note attraverso i canali stabiliti; e divulgazione non autorizzata di fonti o metodi di intelligence.

## Miglioramento continuo

La presente politica è revisionata e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO considerare i cambiamenti nel panorama delle minacce, le nuove fonti e capacità di intelligence, i risultati degli audit, i cambiamenti normativi (inclusi i requisiti di segnalazione dell'NCSC svizzero), l'efficacia dell'integrazione con la valutazione del rischio e la gestione degli incidenti, la progressione della maturità del programma e le lezioni apprese dagli incidenti correlati all'intelligence sulle minacce. Le non conformità relative alla presente politica DEVONO essere registrate e gestite attraverso il processo di azione correttiva del SGSI (Clausola 10.2) con analisi della causa principale e remediation tracciata.

---

# Aree dello standard ISO 27001 trattate

Politica sull'intelligence sulle minacce — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.3 Ruoli, responsabilità e autorità organizzative | **5.7 Intelligence sulle minacce** |
| Clausola 6.1 Azioni per affrontare rischi e opportunità | 5.24 Pianificazione e preparazione della gestione degli incidenti di sicurezza delle informazioni |
| Clausola 7.3 Consapevolezza | 5.25 Valutazione e decisione sugli eventi di sicurezza delle informazioni |
| Clausola 8.1 Pianificazione e controllo operativi | 8.7 Protezione contro il malware |
| Clausola 9.1 Monitoraggio, misurazione, analisi e valutazione | 8.8 Gestione delle vulnerabilità tecniche |
| Clausola 10.2 Non conformità e azioni correttive | 8.15 Registrazione |
| | 8.16 Attività di monitoraggio |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|------------------|-----------|
| nLPD svizzera | Art. 8 — Misure tecniche e organizzative (l'intelligence sulle minacce come misura di sicurezza proattiva a protezione dell'integrità del trattamento dei dati) |
| OPDo svizzera | Art. 1-3 — Requisiti minimi per la sicurezza dei dati |
| LSIn svizzera Art. 74b | Segnalazione obbligatoria degli attacchi informatici per gli operatori di infrastrutture critiche (segnalazione entro 24 ore all'NCSC, in vigore dall'aprile 2025) |
| GDPR dell'UE (ove applicabile) | Art. 32 — Sicurezza del trattamento (misure tecniche e organizzative appropriate, incluso il rilevamento delle minacce) |
| ISO/IEC 27001:2022 | Controllo Annex A 5.7 — Intelligence sulle minacce |
| ISO/IEC 27002:2022 | Sezione 5.7 — Guida all'implementazione per l'intelligence sulle minacce |
| NIST SP 800-53 Rev 5 | PM-16 (Programma di consapevolezza delle minacce), RA-3 (Valutazione del rischio), SI-5 (Avvisi, advisory e direttive di sicurezza) |
| NIST SP 800-150 | Guida alla condivisione delle informazioni sulle minacce informatiche |
| NIST CSF 2.0 | ID.RA (Valutazione del rischio), DE.AE (Eventi avversi), DE.CM (Monitoraggio continuo) |
| CIS Controls v8 | Controllo 13 (Monitoraggio e difesa della rete) — L'intelligence sulle minacce supporta la consapevolezza situazionale e il rilevamento |
| MITRE ATT&CK | Base di conoscenza sulle tattiche e tecniche degli avversari — Tassonomia strutturata per l'analisi dell'intelligence sulle minacce |
| FIRST TLP v2.0 | Traffic Light Protocol — Standard per la classificazione e il controllo della condivisione dell'intelligence sulle minacce |
| OASIS STIX v2.1 / TAXII v2.1 | Standard per lo scambio strutturato di informazioni sulle minacce e il protocollo di condivisione automatizzata |

---

## Appendice A: Modello di dashboard delle metriche dell'intelligence sulle minacce

**Periodo di report:** Q[X] [ANNO]
**Data del report:** [Data]
**Preparato da:** [RSSI/Responsabile della sicurezza]

### Riepilogo esecutivo
[Paragrafo di riepilogo del panorama delle minacce, minacce chiave identificate, azioni intraprese]

### Stato del portafoglio delle fonti

| Categoria delle fonti | Obbligatorio | Attivo | Stato | Azione richiesta |
|-----------------------|--------------|--------|-------|-----------------|
| Governo/CERT | ≥1 | [X] | Verde | Nessuna |
| OSINT | ≥2 | [X] | Verde | Nessuna |

---

<!-- QA_VERIFIED: 2026-04-03 -->
