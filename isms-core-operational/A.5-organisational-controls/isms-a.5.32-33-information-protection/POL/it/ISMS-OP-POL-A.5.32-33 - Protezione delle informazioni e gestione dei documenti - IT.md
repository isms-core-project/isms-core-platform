<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.32-33-IT:operational:OP-POL:a.5.32-33 -->
**ISMS-OP-POL-A.5.32-33 — Protezione delle informazioni e gestione dei documenti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Protezione delle informazioni e gestione dei documenti |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.5.32-33 |
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
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.5.32 — Diritti di proprietà intellettuale
- ISO/IEC 27001:2022 Controllo A.5.33 — Protezione delle registrazioni
- ISO/IEC 27001:2022 Clausola 7.5 — Informazioni documentate

**Controlli Allegato A correlati**:

| Controllo | Relazione con la protezione delle informazioni e la gestione dei documenti |
|-----------|---------------------------------------------------------------------------|
| A.5.9 Inventario delle informazioni e degli asset | Gli asset di PI e le registrazioni sono inclusi nell'inventario degli asset |
| A.5.10 Uso accettabile delle informazioni | Le regole di uso accettabile disciplinano la gestione di PI e registrazioni |
| A.5.12–13 Classificazione ed etichettatura delle informazioni | Lo schema di classificazione applicato a PI e registrazioni |
| A.5.34 Privacy e protezione dei dati personali | Le registrazioni contenenti dati personali soggette ai requisiti di privacy |
| A.6.5 Responsabilità dopo la fine o il cambio del rapporto di lavoro | Le procedure di uscita garantiscono la restituzione/cancellazione della PI |
| A.6.6 Accordi di riservatezza o di non divulgazione | NDA richiesti per l'accesso di terzi alla PI |
| A.8.10 Cancellazione delle informazioni | Procedure di cancellazione sicura per la dismissione delle registrazioni |
| A.8.12 Prevenzione della perdita di dati | I controlli DLP proteggono la PI dall'esfiltrazione |
| A.8.13 Backup delle informazioni | Il backup protegge la disponibilità delle registrazioni |

**Policy interne correlate**:

- Policy sulla gestione degli asset
- Policy sulla classificazione e gestione delle informazioni
- Policy sulla privacy e protezione dei dati personali
- Policy sull'uso accettabile
- Policy sulla cancellazione delle informazioni

---

# Policy sulla protezione delle informazioni e gestione dei documenti

## Scopo

Lo scopo di questa policy è garantire che i diritti di proprietà intellettuale siano adeguatamente protetti e che le registrazioni siano protette da perdita, distruzione, falsificazione, accesso non autorizzato e divulgazione non autorizzata in conformità ai requisiti legislativi, normativi, contrattuali e aziendali.

Questa policy supporta la nLPD svizzera (revLPD) e l'Ordinanza sulla protezione dei dati (OPDo) implementando misure tecniche e organizzative adeguate al rischio, garantendo che le registrazioni contenenti dati personali siano conservate, protette e dismesse in conformità ai principi di protezione dei dati. L'Art. 958f del Codice delle obbligazioni svizzero (CO) richiede la conservazione delle registrazioni contabili e della documentazione di supporto per 10 anni. Laddove l'organizzazione tratti dati di persone nell'UE/SEE, si applicano anche i requisiti del GDPR sulla limitazione della conservazione (Art. 5(1)(e)) e sulla cancellazione (Art. 17), salvo obblighi legali di conservazione prevalenti.

**Approccio combinato ai controlli**: I Controlli A.5.32 (Diritti di proprietà intellettuale) e A.5.33 (Protezione delle registrazioni) vengono implementati congiuntamente in quanto condividono strutture di governance comuni, meccanismi di protezione e requisiti di gestione del ciclo di vita.

## Ambito

Tutti i dipendenti e gli utenti terzi.

Tutta la proprietà intellettuale (brevetti, diritti d'autore, marchi, segreti commerciali, software proprietario, codice sorgente), tutte le registrazioni (aziendali, finanziarie, del personale, tecniche, operative, di sicurezza) e tutti i formati (documenti fisici, file elettronici, database, e-mail).

Tutti gli ambienti in cui la PI o le registrazioni vengono create, elaborate, archiviate o trasmesse.

## Principio

La proprietà intellettuale DEVE essere identificata, classificata e protetta in base al suo valore e ai requisiti legali applicabili. Le registrazioni DEVONO essere conservate per i periodi richiesti, protette da perdita e falsificazione, e dismesse in modo sicuro quando non più necessarie. La conformità alle licenze software e ai diritti di PI di terzi DEVE essere mantenuta in ogni momento.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Proprietà intellettuale (PI)** | Creazioni della mente: invenzioni, opere letterarie e artistiche, simboli, nomi, design e informazioni aziendali proprietarie |
| **Segreto commerciale** | Informazioni aziendali riservate che forniscono un vantaggio competitivo e sono soggette a ragionevoli sforzi per mantenerne la segretezza |
| **Registrazione** | Informazioni create, ricevute e conservate come prova di attività aziendali o per adempiere a obblighi legali |
| **Periodo di conservazione** | La durata richiesta per mantenere una registrazione prima della dismissione autorizzata |
| **Blocco legale** | Un requisito di conservazione dovuto a contenzioso, indagine o azione normativa che prevale sui normali calendari di dismissione |
| **Gestione degli asset software (SAM)** | Processi e strumenti per gestire, controllare e proteggere gli asset software durante il loro ciclo di vita |

---

## Sistemi di gestione di PI e registrazioni

L'organizzazione DEVE utilizzare i seguenti sistemi per gestire la proprietà intellettuale e le registrazioni:

| Funzione | Sistema/Strumento | Responsabile | Controllo degli accessi |
|----------|-------------------|--------------|------------------------|
| **Registro PI** | [es. Sistema di gestione dei casi legali, SharePoint, registro Excel] | Consulente legale | Limitato a Legale, RSSI, Direzione generale |
| **Gestione degli asset software (SAM)** | [es. Snow License Manager, ServiceNow SAM, Flexera, foglio di calcolo manuale] | IT Operations | Responsabili IT, Acquisti, RSSI |
| **Calendario di conservazione** | [es. Documentato nell'appendice della policy, piattaforma GRC, database legale] | Consulente legale | Tutto il personale (sola lettura); Consulente legale (modifica) |
| **Registro dismissioni** | [es. Foglio di calcolo, piattaforma GRC, sistema di ticketing] | Responsabile delle registrazioni | Responsabile delle registrazioni, Consulente legale, Revisione interna |
| **Registro dei blocchi legali** | [es. Sistema di gestione dei casi legali, foglio di calcolo] | Consulente legale | Solo Consulente legale |
| **Repository del codice sorgente** | [es. GitHub Enterprise, GitLab, Bitbucket] | Development Manager | Sviluppatori (basato sul ruolo); RSSI (accesso di audit) |
| **Controllo versioni (documenti)** | [es. SharePoint, Confluence, Git] | IT Operations | Proprietari dei documenti e utenti autorizzati |

**Integrazione**: Ove fattibile, i registri di PI e registrazioni dovrebbero integrarsi con il sistema di gestione degli asset (per la Policy sulla gestione degli asset) per garantire che tutti gli asset di PI e le registrazioni critiche siano monitorati come asset organizzativi.

---

## Protezione della proprietà intellettuale (A.5.32)

### Identificazione e classificazione della PI

L'organizzazione DEVE identificare e classificare tutti gli asset di proprietà intellettuale:

| Categoria | Esempi | Livello di protezione |
|-----------|--------|-----------------------|
| **Segreti commerciali** | Algoritmi, formule, processi, liste clienti | Riservato (protezione massima) |
| **Software proprietario** | Codice sorgente, strumenti di sviluppo, script interni | Minimo Confidenziale |
| **Metodi aziendali** | Processi unici, metodologie, modelli di business | Confidenziale |
| **Documentazione tecnica** | Diagrammi di architettura, design, specifiche | Confidenziale |
| **Marchi e brand** | Loghi, materiali del brand, nomi di dominio | Interno (uso controllato) |

### Registro PI

DEVE essere mantenuto un Registro PI che registri tutti gli asset di proprietà intellettuale significativi. Il registro DEVE includere, come minimo:

- Nome e descrizione dell'asset PI.
- Categoria (come da tabella sopra).
- Proprietario aziendale e custode.
- Classificazione (per la Policy sulla classificazione e gestione delle informazioni).
- Posizione o sistema in cui è archiviato.
- Condivisione con terzi consentita (Sì/No).
- Stato di protezione legale (brevetto, diritto d'autore, marchio, segreto commerciale).
- Data dell'ultima revisione e data della prossima revisione.

Il Registro PI DEVE essere rivisto **annualmente** dal Consulente legale (o ruolo equivalente) e dall'RSSI.

### Controlli di protezione della PI

I controlli di protezione DEVONO essere implementati in base al tipo di PI e alla classificazione:

**Protezione tecnica**:

| Tipo di PI | Controlli richiesti |
|------------|---------------------|
| **Codice sorgente** | Controllo degli accessi, controllo versioni (es. Git), revisione del codice, restrizioni all'esportazione |
| **Segreti commerciali** | Accesso basato sulla necessità di sapere, cifratura a riposo e in transito, monitoraggio DLP |
| **Design e specifiche** | Registrazione degli accessi, restrizioni alla condivisione, filigrana ove appropriato |
| **Dati di ricerca** | Cifratura, controllo degli accessi, protezione dei backup |

**Protezione amministrativa**:

- Clausole di riservatezza in tutti i contratti di lavoro.
- Accordi di non divulgazione (NDA) per l'accesso di terzi alla PI.
- Clausole di proprietà della PI negli accordi con fornitori e collaboratori.
- Procedure di uscita che garantiscano la restituzione o la cancellazione verificata dei materiali di PI alla partenza.

**Protezione legale**:

- Deposito di domande di brevetto ove commercialmente appropriato.
- Applicazione di avvisi di diritto d'autore ai materiali protetti.
- Mantenimento delle registrazioni dei marchi.
- Documentazione dei segreti commerciali mantenuta a supporto della difesa legale.

### Accesso di terzi alla proprietà intellettuale

Tutti i terzi (fornitori, consulenti, collaboratori, partner) che accedono alla PI o alle registrazioni riservate dell'organizzazione DEVONO firmare un Accordo di non divulgazione (NDA) **prima** che venga concesso l'accesso.

**Processo di approvazione dell'NDA**:

1. **Richiesta**: Il proprietario aziendale richiede l'accesso di terzi tramite [sistema di ticketing/richiesta contrattuale].
2. **Selezione dell'NDA**: Il Consulente legale fornisce il modello di NDA appropriato (unilaterale, reciproco o personalizzato).
3. **Negoziazione**: Il Consulente legale negozia i termini se la terza parte propone modifiche.
4. **Approvazione**: Il Consulente legale approva l'NDA definitivo.
5. **Esecuzione**: Entrambe le parti firmano (la firma elettronica è accettabile).
6. **Registrazione**: Il Consulente legale registra l'NDA eseguito nel registro degli accordi legali con: nome della terza parte, tipo di NDA, data di entrata in vigore, data di scadenza, ambito di accesso, asset PI coperti.
7. **Concessione dell'accesso**: Solo dopo che l'NDA eseguito è registrato, IT Operations o il proprietario aziendale possono concedere l'accesso al sistema.
8. **Rinnovo**: Per le relazioni continuative, gli NDA DEVONO essere rivisti e rinnovati prima della scadenza.

**Restituzione/Cancellazione della PI alla fine del rapporto**:

- L'NDA DEVE richiedere alla terza parte di restituire o certificare la cancellazione di tutta la PI dell'organizzazione alla risoluzione del contratto.
- Il proprietario aziendale DEVE verificare la restituzione/cancellazione e documentare la verifica nel registro degli accordi.
- Se la terza parte non restituisce/cancella la PI entro **30 giorni**, escalare al Consulente legale.

**Revisione del Registro NDA**: Il Consulente legale DEVE revisionare il Registro NDA **trimestralmente** per identificare gli NDA in scadenza che richiedono il rinnovo e le relazioni terminate che richiedono la verifica della restituzione della PI. Obiettivo: 100% dei terzi attivi con NDA validi.

### Licenze software e conformità

Tutto il software utilizzato dall'organizzazione DEVE essere adeguatamente concesso in licenza e conforme:

- Il software DEVE essere acquisito solo attraverso canali ufficiali. DEVONO essere conservate prove delle licenze valide.
- Il software DEVE essere utilizzato in conformità con i termini della licenza.
- DEVE essere mantenuto un **registro SAM (Software Asset Management)** che registri: nome e versione del software, tipo di licenza (commerciale, open source, freeware), persona responsabile, numero di licenze acquistate rispetto a quelle in uso, ubicazione della licenza (chiave, certificato, portale), sedi di distribuzione e date di revisione.
- **Solo il software supportato dal produttore** DEVE essere utilizzato in produzione. Il software giunto a fine vita DEVE essere identificato e migrato per la policy di gestione delle vulnerabilità.
- Il software DEVE essere installato solo da personale autorizzato.

### Processo di gestione degli asset software (SAM)

**Manutenzione del Registro SAM**: Responsabile: IT Operations Manager. Frequenza di aggiornamento: in tempo reale per i nuovi deployment software; riconciliazione completa trimestrale. Strumento: [Specificare il nome dello strumento SAM].

**Processo di riconciliazione trimestrale**:

1. **Rilevamento** (Settimana 1): Eseguire scansioni automatizzate dell'inventario software su tutti gli endpoint e server tramite lo strumento SAM o l'agente di gestione degli endpoint.
2. **Riconciliazione degli acquisti** (Settimana 2): Confrontare il software rilevato con i registri di acquisto e i diritti di licenza.
3. **Analisi delle lacune** (Settimana 2): Identificare il software privo di licenza (distribuito ma senza licenza), il software distribuito in eccesso (più installazioni rispetto alle licenze) e le licenze inutilizzate (licenze a pagamento non distribuite).
4. **Rimedio** (Settimane 3–4):
   - **Critico**: Software business-critical privo di licenza — acquistare la licenza entro **5 giorni lavorativi** o disinstallare.
   - **Standard**: Distribuzione in eccesso — raccogliere/riallocare le licenze entro **30 giorni** o acquistare licenze aggiuntive.
   - **Basso**: Problemi di conformità freeware/open source — rivedere la licenza e documentare la conformità entro **90 giorni**.
5. **Revisione della Direzione** (Fine trimestre): IT Operations Manager presenta il report SAM all'RSSI includendo: totale degli asset software, tasso di conformità delle licenze, opportunità di ottimizzazione dei costi e stato delle eccezioni.
6. **Approvazione**: RSSI e Direttore finanziario (CFO) approvano il report SAM trimestrale.

**Risposta al software privo di licenza**:

- Sospensione immediata dell'accesso se la violazione della licenza crea un rischio legale.
- Notifica all'utente e raccomandazione di un software approvato alternativo.
- Escalation al responsabile dell'utente e all'RSSI entro 24 ore.

**Metriche SAM**:

| Metrica | Obiettivo |
|---------|-----------|
| Tasso di conformità delle licenze | 100% |
| Tempo di rimedio del software privo di licenza (critico) | <5 giorni lavorativi |
| Identificazione delle licenze inutilizzate | >80% delle licenze a pagamento utilizzate attivamente |

L'uso di software privo di licenza è vietato.

### Conformità alla PI di terzi

L'organizzazione DEVE rispettare i diritti di proprietà intellettuale di terzi:

- **Verifica del diritto d'autore** prima di utilizzare contenuti di terzi.
- **Corretta attribuzione** in conformità con i termini della licenza.
- **Conformità alle licenze open source**: vedere Conformità alle licenze software open source di seguito.
- Le restrizioni delle licenze **Creative Commons** e di altre licenze di contenuto DEVONO essere rispettate.

### Conformità alle licenze software open source

Prima di distribuire qualsiasi software open source (OSS) o di incorporare componenti OSS nelle applicazioni dell'organizzazione:

1. **Identificazione**: Lo sviluppatore identifica il componente OSS e la sua licenza (dai metadati del package manager, dal file LICENSE o dal repository).
2. **Generazione SBOM**: Generare una Distinta base del software (SBOM) che elenchi tutte le dipendenze OSS e le relative licenze utilizzando [nome dello strumento, es. Syft, Trivy, Snyk].
3. **Revisione della licenza**: L'IT Security Analyst o il Development Manager rivede la SBOM per:
   - **Licenze approvate**: MIT, Apache 2.0, BSD (2-clausole, 3-clausole), ISC.
   - **Licenze con restrizioni** (richiedono l'approvazione dell'RSSI): GPL v2/v3 (obblighi copyleft), LGPL, AGPL, MPL.
   - **Licenze vietate**: Licenze personalizzate con termini poco chiari, licenze incompatibili con l'uso commerciale.
4. **Approvazione**:
   - **Licenze approvate**: Il Development Manager autorizza il deployment.
   - **Licenze con restrizioni**: L'RSSI rivede e approva/nega in base al rischio copyleft, all'ambito del progetto e alla consultazione legale se necessario.
   - **Licenze vietate**: Negato; è richiesto un componente alternativo.
5. **Documentazione**: Registrare i componenti OSS approvati nel Registro OSS: nome/versione del componente, tipo di licenza, data di approvazione, approvatore, progetto/sistema che utilizza il componente, data dell'ultima revisione SBOM.
6. **Monitoraggio continuo**: Rigenerazione trimestrale della SBOM per rilevare nuove dipendenze o modifiche alle licenze.

**Obblighi copyleft**: Se il codice con licenza GPL attiva obblighi copyleft (es. distribuzione di binari modificati), il Development Manager DEVE fornire il codice sorgente ai destinatari per i termini GPL, documentare la conformità nel Registro OSS e notificare il Consulente legale.

**Risposta alle violazioni delle licenze**: Se viene scoperta una violazione della licenza (OSS utilizzato al di fuori dei termini della licenza), rimedio immediato (rimuovere il componente, interrompere la distribuzione o ottenere la licenza appropriata), creazione di un incidente per la Policy sulla gestione degli incidenti e consultazione del Consulente legale entro 24 ore per le violazioni ad alto rischio.

**Revisione del Registro OSS**: Il Development Manager DEVE revisionare il Registro OSS **trimestralmente** per verificare che tutti i componenti siano adeguatamente concessi in licenza e documentati. Obiettivo: 100% dei componenti OSS con approvazione della licenza valida.

---

## Protezione delle registrazioni (A.5.33)

### Classificazione e conservazione delle registrazioni

L'organizzazione DEVE classificare le registrazioni in base ai requisiti di conservazione e alle esigenze di protezione:

| Categoria | Periodo di conservazione | Requisito di protezione | Esempi |
|-----------|--------------------------|------------------------|--------|
| **Legale e contrattuale** | Durata + 10 anni | Confidenziale, protetto dall'integrità | Contratti, accordi legali, NDA |
| **Finanziaria** | 10 anni (CO svizzero Art. 958f) | Confidenziale, a prova di manomissione | Fatture, libri contabili, documenti fiscali, rapporti di revisione |
| **Del personale** | Rapporto di lavoro + 10 anni | Confidenziale, protetto dalla privacy | Fascicoli HR, registri paga, valutazioni delle prestazioni |
| **Normativa e conformità** | Per normativa applicabile | Per classificazione | Prove SGSI, rapporti di audit, certificazioni |
| **Tecnica** | Ciclo di vita del sistema + 3 anni | Minimo Interno | Configurazioni, registrazioni delle modifiche, documenti di architettura |
| **Operativa** | 3–7 anni | Interno | Verbali di riunione, file di progetto, corrispondenza |
| **Sicurezza e audit** | 2–7 anni | Confidenziale, protetto dall'integrità | Registri di accesso, registrazioni degli incidenti, file di indagine |

### Calendario di conservazione

DEVE essere mantenuto un calendario di conservazione documentato:

- **Responsabile**: Consulente legale (o ruolo equivalente).
- **Contenuto**: Categoria della registrazione, periodo di conservazione, base di conservazione (legge, contratto, esigenza aziendale), metodo di dismissione e proprietario della registrazione.
- **Revisione**: Annuale, con verifica dell'allineamento normativo.
- **Risoluzione dei conflitti**: Laddove si applichino più normative, prevale il requisito di conservazione più restrittivo. Laddove una richiesta di cancellazione o eliminazione sia in conflitto con gli obblighi legali di conservazione, prevale la conservazione — le registrazioni DEVONO essere soggette a restrizioni di accesso, la decisione documentata con l'approvazione del Consulente legale e con il coinvolgimento del DPD per i dati personali.

**Formato di esempio del calendario di conservazione**:

| Categoria registrazione | Tipo di registrazione | Periodo di conservazione | Base legale | Metodo di dismissione | Proprietario |
|------------------------|----------------------|--------------------------|-------------|----------------------|--------------|
| Finanziaria | Fatture e ricevute | 10 anni | CO svizzero Art. 958f | Cancellazione sicura (NIST SP 800-88) | Finance Manager |
| Finanziaria | Libro mastro generale | 10 anni | CO svizzero Art. 958f | Cancellazione sicura | Finance Manager |
| Del personale | Contratti di lavoro | Rapporto di lavoro + 10 anni | CO svizzero Art. 958f | Distruzione sicura (P-4) | HR Manager |
| Del personale | Registri paga | Rapporto di lavoro + 10 anni | CO svizzero Art. 958f | Cancellazione sicura | HR Manager |
| Del personale | Valutazioni delle prestazioni | Rapporto di lavoro + 5 anni | Esigenza aziendale | Cancellazione sicura | HR Manager |
| Legale | Contratti e NDA | Fine contratto + 10 anni | CO svizzero Art. 958f | Cancellazione sicura | Consulente legale |
| SGSI | Prove di audit ISO 27001 | 3 cicli di audit (9 anni) | ISO 27001 Clausola 9.2 | Cancellazione sicura | RSSI |
| SGSI | Valutazioni del rischio | Superato + 3 anni | ISO 27001 Clausola 6.1 | Cancellazione sicura | RSSI |
| SGSI | Registri di sicurezza | 12 mesi | OPDo Art. 4 (ove applicabile) | Cancellazione sicura | IT Security |
| Tecnica | Registrazioni di configurazione del sistema | Ciclo di vita del sistema + 3 anni | Esigenza aziendale | Cancellazione standard | IT Operations |
| Operativa | Verbali di riunione | 3 anni | Esigenza aziendale | Cancellazione standard | Organizzatore della riunione |

**Periodo di tolleranza**: Le registrazioni possono essere conservate fino a 12 mesi oltre il periodo minimo di conservazione per consentire processi di dismissione ordinati. Le registrazioni NON DEVONO essere conservate indefinitamente senza una giustificazione documentata.

**Revisione annuale**: Il Consulente legale DEVE revisionare il calendario di conservazione annualmente e aggiornarlo per i cambiamenti normativi, i nuovi tipi di registrazioni o le esigenze aziendali.

### Controlli di conservazione

| Controllo | Requisito |
|-----------|-----------|
| **Conservazione minima** | Le registrazioni NON DEVONO essere cancellate prima della scadenza del periodo di conservazione |
| **Conservazione massima** | Le registrazioni dovrebbero essere cancellate dopo il periodo di conservazione più un periodo di tolleranza (massimo 12 mesi), a supporto della limitazione della conservazione del GDPR e della minimizzazione dei dati della nLPD |
| **Blocco legale** | I blocchi per contenzioso o indagini prevalgono sui normali calendari di cancellazione; i blocchi sono a tempo indeterminato fino al rilascio formale da parte del Consulente legale |
| **Protezione dell'integrità** | Le registrazioni critiche DEVONO avere una verifica dell'integrità (checksum, firme digitali o archiviazione a prova di manomissione) |

Le **registrazioni critiche** includono: prove normative e di audit, libri contabili e documentazione fiscale, registri di sicurezza e accesso, contratti firmati e accordi legali, registrazioni master HR e registrazioni delle indagini sugli incidenti.

### Controlli di protezione delle registrazioni

Le registrazioni DEVONO essere protette durante tutto il loro ciclo di vita:

**Integrità**:

- Registrazioni critiche archiviate con verifica dell'integrità (checksum, valori hash o firme digitali).
- Registri di audit a prova di manomissione (archiviazione in sola scrittura, solo aggiunta o concatenamento crittografico).
- Controllo versioni per le registrazioni che richiedono il monitoraggio delle modifiche.

**Processo di verifica dell'integrità**:

| Tipo di registrazione | Metodo di verifica | Strumento |
|----------------------|-------------------|-----------|
| Registrazioni elettroniche (file) | Confronto hash SHA-256 | [es. PowerShell Get-FileHash, Linux sha256sum, piattaforma GRC] |
| Database | Controlli di integrità del database | Strumenti nativi del database (es. SQL Server DBCC CHECKDB) |
| Registri di audit | Verifica dell'archiviazione a prova di manomissione | Verifica dell'integrità nativa SIEM o firma crittografica dei log |
| Documenti digitali | Verifica della firma digitale | Adobe Acrobat, verifica DocuSign o equivalente |

- **Frequenza**: Annualmente (o più frequentemente per le registrazioni ad alto rischio).
- **Responsabile**: IT Operations (elettroniche); Responsabile delle registrazioni (fisiche con firme digitali).
- **Processo**: Generare l'hash/checksum corrente, confrontare con l'hash baseline archiviato alla creazione della registrazione o all'ultima verifica.

**Risposta al fallimento della verifica**:

1. **Isolamento immediato**: Mettere in quarantena la registrazione interessata per prevenire ulteriori modifiche.
2. **Creazione incidente**: Creare un incidente di sicurezza per la Policy sulla gestione degli incidenti.
3. **Indagine**: Determinare la causa (corruzione, modifica non autorizzata, errore di sistema).
4. **Ripristino**: Ripristinare dal backup verificato se disponibile.
5. **Notifica**: Notificare il Consulente legale e l'RSSI entro 4 ore per le registrazioni critiche (finanziarie, legali, normative).
6. **Analisi della causa radice**: Documentare la causa e implementare l'azione correttiva.

**Disponibilità**:

- Backup in base alla criticità (per la policy di backup e ripristino).
- Ridondanza geografica per le registrazioni critiche ove fattibile.
- Aggiornamento dei supporti e migrazione del formato prima che il deterioramento renda le registrazioni illeggibili.

**Requisiti di backup per categoria di registrazione**:

| Categoria registrazione | Frequenza backup | Conservazione backup | RTO | RPO |
|------------------------|------------------|---------------------|-----|-----|
| Registrazioni finanziarie | Giornaliera | 10 anni (online: 90 giorni; archivio: 9+ anni) | 24 ore | 24 ore |
| Contratti legali | Giornaliera | Durata + 10 anni | 24 ore | 24 ore |
| Registrazioni del personale | Giornaliera | Rapporto di lavoro + 10 anni | 48 ore | 24 ore |
| Prove di audit SGSI | Settimanale | 9 anni | 72 ore | 1 settimana |
| Registri di sicurezza | Giornaliera (inoltro continuo al SIEM) | 12 mesi (online: 90 giorni; archivio: 9 mesi) | 4 ore | 1 ora |
| Asset PI (codice sorgente) | Continua (controllo versioni) + backup giornaliero | Indefinita (cronologia versioni conservata) | 4 ore | Tempo reale (tramite controllo versioni) |

- Il test di ripristino dei backup DEVE essere eseguito **trimestralmente** per le registrazioni critiche (selezionare 3 registrazioni campione da ogni categoria, eseguire il test di ripristino, verificare l'integrità e la completezza). Obiettivo: 100% di ripristini riusciti.
- Le registrazioni critiche DEVONO avere backup archiviati in una posizione geograficamente separata (minimo 100 km dal sito primario).
- I backup contenenti registrazioni riservate DEVONO essere cifrati (AES-256 o equivalente).
- L'eliminazione dei backup richiede doppia approvazione (IT Operations Manager + RSSI).

**Riservatezza**:

- Controllo degli accessi basato sulla necessità di sapere e sul ruolo.
- Cifratura per le registrazioni riservate a riposo e in transito.
- Protezione fisica per le registrazioni cartacee (archiviazione sotto chiave, accesso controllato).

### Dismissione delle registrazioni

Le registrazioni DEVONO essere dismesse in modo sicuro alla scadenza del periodo di conservazione (e in assenza di blocchi legali):

| Tipo di registrazione | Metodo di dismissione |
|----------------------|-----------------------|
| **Carta (Riservato o superiore)** | Distruzione con taglia trasversale (DIN 66399 P-4 minimo) o incenerimento testimoniato |
| **Carta (Interno)** | Distruzione standard (P-3 minimo) |
| **Elettronico (Riservato o superiore)** | Cancellazione sicura per la policy sulla cancellazione delle informazioni (NIST SP 800-88: Clear, Purge o Destroy) |
| **Elettronico (Interno)** | Cancellazione standard con verifica |
| **Supporti (HDD, SSD, nastri)** | Degaussing, distruzione fisica o distruzione certificata da terzi |

**Documentazione della dismissione**:

- I registri di dismissione DEVONO essere mantenuti per la traccia di audit (minimo 3 anni).
- DEVONO essere ottenuti certificati di distruzione per le registrazioni riservate e superiori.
- La distruzione da parte di terzi DEVE essere verificata tramite certificazioni del fornitore e documentazione della catena di custodia.

### Processo di dismissione delle registrazioni

**Dismissione automatizzata** (per registrazioni elettroniche con conservazione gestita dal sistema):

1. **Identificazione della scadenza**: Il sistema di gestione della conservazione (o script) identifica le registrazioni il cui periodo di conservazione è scaduto.
2. **Verifica del blocco pre-dismissione**: Il sistema verifica che non siano in vigore blocchi legali attivi per la registrazione.
3. **Notifica al proprietario** (30 giorni prima della dismissione): Il proprietario della registrazione riceve una notifica con la data di dismissione programmata; il proprietario può presentare una richiesta di proroga con motivazione aziendale.
4. **Richiesta di proroga** (se necessario): Il proprietario presenta la richiesta al Consulente legale con motivazione; il Consulente legale approva/nega entro 5 giorni lavorativi.
5. **Esecuzione della dismissione**: Il sistema esegue la cancellazione sicura per il metodo definito nel calendario di conservazione.
6. **Registrazione della dismissione**: Il sistema registra l'evento di dismissione (ID registrazione, data di dismissione, metodo, utente/sistema che ha avviato la dismissione).

**Dismissione manuale** (per registrazioni fisiche o registrazioni elettroniche che richiedono revisione manuale):

1. **Richiesta di dismissione**: Il Responsabile delle registrazioni genera l'elenco trimestrale delle dismissioni dal calendario di conservazione.
2. **Revisione del proprietario**: I proprietari delle registrazioni esaminano l'elenco e confermano l'autorizzazione alla dismissione entro 10 giorni lavorativi.
3. **Verifica del blocco legale**: Il Consulente legale conferma che non sono in vigore blocchi attivi.
4. **Autorizzazione alla dismissione**: Il Responsabile delle registrazioni autorizza la dismissione.
5. **Dismissione fisica**: La carta riservata viene triturata con taglia trasversale (DIN 66399 P-4) in loco o da un fornitore certificato; i supporti (HDD, SSD) vengono fisicamente distrutti o degaussati da un fornitore certificato.
6. **Certificato di distruzione**: Ottenere il certificato dal fornitore di distruzione entro 5 giorni lavorativi.
7. **Documentazione della dismissione**: Il Responsabile delle registrazioni registra la dismissione nel registro delle dismissioni (data di dismissione, descrizione della registrazione, metodo, riferimento del certificato, persona autorizzante).

**Verifica della dismissione**: La Revisione interna DEVE verificare annualmente i registri di dismissione per verificare che la dismissione sia avvenuta nei tempi previsti, che siano stati ottenuti certificati di distruzione per le registrazioni riservate e che i blocchi legali siano stati verificati. Obiettivo: 100% di conformità alle procedure di dismissione.

### Processo di blocco legale

**Trigger del blocco legale**: Contenzioso effettivo o potenziale, indagine governativa o citazione, indagine interna (frode, irregolarità, violazione dei dati) o azione di enforcement normativo.

**Emissione del blocco legale**:

1. **Notifica del blocco**: Il Consulente legale emette un avviso formale di blocco legale documentando: nome e numero della causa/questione, ambito (sistemi specifici, intervalli di date, custodi, parole chiave), data di entrata in vigore, obblighi di conservazione e contatto per le domande.
2. **Notifica ai custodi** (entro 24 ore): Il Consulente legale invia l'avviso di blocco a tutti i custodi identificati tramite e-mail. I custodi DEVONO confermare la ricezione e la comprensione entro **2 giorni lavorativi**. L'avviso DEVE indicare: *"Con la presente si dispone di conservare e non eliminare, modificare o distruggere alcuna registrazione relativa a [questione]. Ciò include e-mail, documenti, file e qualsiasi altra informazione in Vostro possesso o controllo. Le normali attività di cancellazione devono essere sospese. Questo blocco rimane in vigore fino al rilascio formale da parte del Consulente legale."*
3. **Sospensione del sistema IT**: IT Operations sospende la cancellazione automatizzata per i sistemi interessati (conservazione e-mail, rotazione dei log, sovrascrittura dei backup). I sistemi/dati interessati vengono contrassegnati con lo stato di blocco. IT conferma la sospensione entro **48 ore** e fornisce conferma scritta al Consulente legale.
4. **Monitoraggio del blocco**: Il Consulente legale mantiene il Registro dei blocchi legali che registra: ID del blocco, nome della questione, data di emissione, ambito, sistemi interessati, custodi, stato di conferma, data di revisione mensile, data di rilascio (quando revocato).
5. **Revisione mensile**: Il Consulente legale esamina tutti i blocchi attivi mensilmente per verificare che il blocco sia ancora necessario, aggiornare l'ambito se la causa evolve e confermare che la sospensione IT rimane attiva.
6. **Rilascio del blocco**: Alla conclusione della questione, il Consulente legale emette un avviso formale di rilascio del blocco. Custodi e IT Operations notificati entro **24 ore**. IT Operations riabilita i normali calendari di cancellazione. Il Responsabile delle registrazioni può quindi dismettere le registrazioni per il normale calendario di conservazione.

**Verifica della conformità**: La Revisione interna DEVE verificare annualmente la conformità al blocco legale (verificare le conferme dei custodi, verificare che la sospensione IT sia stata implementata).

---

## Protezioni della privacy per le registrazioni contenenti dati personali

Laddove le registrazioni contengano dati personali (come definito dalla nLPD svizzera o dal GDPR):

**Controllo degli accessi**:

- Registrazioni del personale (fascicoli HR, buste paga, valutazioni delle prestazioni): accesso limitato al team HR e al responsabile diretto del dipendente su base di necessità di sapere.
- Registri di sicurezza contenenti attività degli utenti: accesso limitato al team IT Security e alla Revisione interna; i registri NON DEVONO essere consultati dai responsabili di linea per il monitoraggio dei dipendenti.
- Registrazioni finanziarie con identificatori personali: accesso limitato al team Finance e ai revisori autorizzati.

**Pseudonimizzazione**: Ove fattibile, i registri e le registrazioni utilizzati per l'analisi della sicurezza dovrebbero pseudonimizzare gli identificatori personali (sostituire nomi/e-mail con ID anonimizzati) mantenendo la capacità di re-identificazione se necessario per le indagini.

**Diritti degli interessati**: I dipendenti e i clienti possono esercitare i diritti ai sensi della nLPD/GDPR (accesso, rettifica, cancellazione, restrizione):

1. L'interessato presenta la richiesta al DPD o alle Risorse umane (HR) (per le registrazioni dei dipendenti).
2. Il DPD/HR verifica l'identità.
3. Il Responsabile delle registrazioni identifica tutte le registrazioni contenenti i dati personali dell'interessato.
4. In caso di **richiesta di accesso**: fornire copia entro 30 giorni (nLPD Art. 25), gratuitamente per la prima richiesta.
5. In caso di **richiesta di cancellazione**: se si applica un obbligo di conservazione (es. CO svizzero Art. 958f), negare la cancellazione ma limitare l'accesso e documentare la decisione con l'approvazione del Consulente legale; se non si applica alcun obbligo di conservazione, eseguire la cancellazione sicura per le procedure di dismissione.
6. Documentare tutte le richieste degli interessati e le risposte nel registro delle richieste degli interessati.

**Minimizzazione della conservazione**: I dati personali nelle registrazioni NON DEVONO essere conservati più a lungo del necessario. Revisione annuale: il Responsabile delle registrazioni e il DPD DEVONO revisionare il calendario di conservazione per verificare che i periodi di conservazione dei dati personali rimangano giustificati e conformi all'Art. 6 nLPD (proporzionalità).

**Notifica delle violazioni**: Se la verifica dell'integrità fallisce o viene rilevato un accesso non autorizzato alle registrazioni contenenti dati personali, seguire le procedure di notifica della violazione dei dati per la Policy sulla privacy e protezione dei dati personali. L'Art. 24 nLPD svizzera richiede la notifica all'IFPDT "il prima possibile" per le violazioni ad alto rischio.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della policy; controlli di protezione della PI; requisiti di sicurezza delle registrazioni; autorizzazione delle eccezioni per l'accesso alla PI |
| **Consulente legale** | Registrazione e protezione legale della PI; proprietà del calendario di conservazione; gestione dei blocchi legali; approvazione della dismissione per i casi incerti |
| **Responsabile delle registrazioni** | Manutenzione del calendario di conservazione; supervisione della dismissione; gestione dei registri; monitoraggio della conformità |
| **IT Operations** | Implementazione dei controlli tecnici; verifica dei backup e dell'integrità; esecuzione della dismissione sicura |
| **Proprietari delle informazioni** | Decisioni di classificazione e conservazione per le registrazioni e la PI di propria competenza; revisione e approvazione della dismissione |
| **Tutto il personale** | Gestire PI e registrazioni per la policy; segnalare violazioni o preoccupazioni; non utilizzare software privo di licenza |

---

## Prove

Le seguenti prove dimostrano la conformità a questa policy:

| # | Prova | Responsabile | Frequenza |
|---|-------|--------------|-----------|
| 1 | **Registro PI** con proprietà, classificazione e stato di protezione | Consulente legale / RSSI | *Mantenuto continuamente; rivisto annualmente; obiettivo: 100% degli asset PI registrati con proprietario designato* |
| 2 | **Report SAM (Software Asset Management)** che mostra la riconciliazione delle licenze e la conformità | IT Operations | *Riconciliazione trimestrale; obiettivo: 100% di conformità delle licenze* |
| 3 | **Calendario di conservazione** con allineamento normativo e registrazioni di approvazione | Consulente legale | *Rivisto annualmente; con controllo versioni; approvato dalla Direzione generale* |
| 4 | **Registri di dismissione** e certificati di distruzione | Responsabile delle registrazioni | *Per evento; conservati 3 anni; obiettivo: 100% delle registrazioni scadute dismesse per calendario* |
| 5 | **Risultati della verifica dell'integrità** per le registrazioni critiche (checksum, test di backup) | IT Operations | *Annualmente; obiettivo: 100% di superamento per le registrazioni critiche* |
| 6 | **Registro dei blocchi legali** con blocchi attivi, ambito e registrazioni delle revisioni | Consulente legale | *Blocchi attivi rivisti mensilmente; il rilascio richiede approvazione* |
| 7 | **Registrazioni di NDA e accordi PI** per l'accesso di terzi | Consulente legale / HR | *Per accordo; conservati per la durata dell'accordo + 10 anni* |
| 8 | **Registrazioni di conformità alle licenze open source** (SBOM, revisione della licenza, approvazione) | IT Operations / Sviluppo | *Per adozione; rivisto trimestralmente dove viene utilizzato l'open source* |
| 9 | **Registrazioni di formazione** per la consapevolezza sulla gestione di PI e registrazioni | Sicurezza delle informazioni / HR | *Per evento; obiettivo: 100% del personale con accesso a PI/registrazioni formato* |

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa policy attraverso vari metodi, tra cui: revisioni del Registro PI, audit delle licenze software, controlli di conformità al calendario di conservazione, campionamento dei registri di dismissione, audit interni ed esterni e feedback al proprietario della policy.

## Eccezioni

Qualsiasi eccezione a questa policy DEVE essere approvata e registrata anticipatamente dal Responsabile della sicurezza delle informazioni, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita. Le eccezioni alla conservazione richiedono l'approvazione del Consulente legale. Le eccezioni DEVONO essere riportate al team di revisione della Direzione.

## Non conformità

Un dipendente che violi questa policy può essere soggetto a provvedimenti disciplinari, fino al licenziamento. L'uso di software privo di licenza può esporre ulteriormente l'organizzazione a responsabilità legale.

## Miglioramento continuo

Questa policy viene rivista e aggiornata come parte del processo di miglioramento continuo. Le revisioni DEVONO tenere conto dei cambiamenti alla legislazione sulla proprietà intellettuale, ai regolamenti sulla gestione dei documenti (inclusi gli sviluppi della nLPD e del GDPR), ai modelli di licenza software, ai cambiamenti tecnologici che influiscono sui formati delle registrazioni, ai risultati degli audit e alle lezioni apprese dagli incidenti relativi alla PI o dai fallimenti nella dismissione.

---

# Aree dello standard ISO 27001 trattate

Policy sulla protezione delle informazioni e gestione dei documenti — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi per la sicurezza delle informazioni | 5.9 Inventario delle informazioni e degli altri asset associati |
| Clausola 7.3 Consapevolezza | 5.36 Conformità a policy, regole e standard |
| Clausola 7.5.1 Informazioni documentate — Generalità | **5.32 Diritti di proprietà intellettuale** |
| Clausola 7.5.3 Controllo delle informazioni documentate | **5.33 Protezione delle registrazioni** |
| | 6.3 Consapevolezza, formazione e istruzione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 8.10 Cancellazione delle informazioni |
| | 8.19 Installazione di software nei sistemi operativi |

**Framework normativo e legale**:

| Framework | Rilevanza |
|-----------|-----------|
| CO svizzero (Codice delle obbligazioni) | Art. 958f — Conservazione delle registrazioni contabili (10 anni); Art. 962 — Obblighi di rendicontazione finanziaria |
| nLPD svizzera (revLPD) | Art. 6 — Minimizzazione dei dati e limitazione della conservazione; Art. 8 — Misure tecniche e organizzative (protezione delle registrazioni come misura organizzativa) |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati (protezione delle registrazioni contenenti dati personali) |
| GDPR UE (ove applicabile) | Art. 5(1)(e) — Limitazione della conservazione; Art. 17 — Diritto alla cancellazione (soggetto alla conservazione legale); Art. 32 — Sicurezza del trattamento |
| Legge federale sui brevetti / Legge sul diritto d'autore svizzera | Protezione della documentazione dei brevetti e del codice sorgente (ove applicabile) |
| ISO/IEC 27001:2022 | Controlli A.5.32, A.5.33 dell'Allegato A |
| ISO/IEC 27002:2022 | Sezioni 5.32, 5.33 — Guida all'implementazione |
| NIST SP 800-53 Rev 5 | MP-6 (Sanitizzazione dei supporti), SI-12 (Gestione e conservazione delle informazioni), PM-22 (Gestione della qualità delle informazioni di identificazione personale) |
| NIST SP 800-88 Rev 1 | Linee guida per la sanitizzazione dei supporti (Clear, Purge, Destroy) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
