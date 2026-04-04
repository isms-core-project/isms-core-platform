<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.5-7-IT:privacy:POL:a.3.5-7 -->
**PRIV-POL-A.3.5-7 — Classificazione delle informazioni e trasferimento**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Classificazione delle informazioni e trasferimento |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | PRIV-POL-A.3.5-7 |
| **Autore del documento** | Responsabile della Protezione dei Dati (RPD) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto Privacy** | 1.0 |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data da definire] | RPD | Politica iniziale per la prima certificazione ISO/IEC 27701:2025 |

**Ciclo di revisione** : Annuale | **Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** : Principale: RPD; Secondaria: RSSI; Legale: Responsabile Legale/Conformità; Autorità finale: Direzione generale.

**Documenti correlati** :
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.3.5-7-UG / TG
- ISMS-POL-A.5.12-13 (Classificazione ed etichettatura — parallelo SGSI)
- ISMS-POL-A.5.14 (Trasferimento di informazioni — parallelo SGSI)
- ISO/IEC 27701:2025 Controlli A.3.5, A.3.6, A.3.7
- RGPD Articolo 32 (sicurezza); Articoli 44–49 (trasferimenti internazionali)
- LPD svizzera Articolo 7 (sicurezza dei dati); Articoli 16–17 (comunicazione transfrontaliera)

**Applicabilità del ruolo** : Questa politica si applica all'organizzazione che agisce sia come **Titolare del trattamento che come Responsabile del trattamento dei DCP**. I controlli A.3.5, A.3.6 e A.3.7 sono controlli condivisi (Tabella A.3).

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la classificazione, l'etichettatura e il trasferimento delle informazioni in relazione al trattamento dei DCP — conformemente ai controlli A.3.5, A.3.6 e A.3.7 di ISO/IEC 27701:2025.

**Perimetro** : Tutte le informazioni contenenti o relative ai DCP; tutte le procedure di classificazione ed etichettatura applicate ai DCP; qualsiasi trasferimento di DCP all'interno di [Organizzazione] e tra [Organizzazione] e altre parti.

**Motivazione dei controlli combinati** : A.3.5 (classificazione), A.3.6 (etichettatura) e A.3.7 (trasferimento) formano una triade coesiva di protezione dei flussi di dati DCP. La classificazione informa l'etichettatura applicata; l'etichettatura determina il metodo di trasferimento richiesto. Vengono implementati insieme come livello integrato di protezione dei DCP.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27701:2025

**Controllo A.3.5 — Classificazione delle informazioni**
Il controllo A.3.5 richiede che [Organizzazione] classifichi le informazioni in base alle loro esigenze di sicurezza, tenendo conto del contenuto in DCP oltre a riservatezza, integrità, disponibilità e requisiti delle parti interessate.

**Controllo A.3.6 — Etichettatura delle informazioni**
Il controllo A.3.6 richiede che [Organizzazione] sviluppi e implementi procedure di etichettatura che riconoscano i DCP, coerenti con lo schema di classificazione.

**Controllo A.3.7 — Trasferimento delle informazioni**
Il controllo A.3.7 richiede che [Organizzazione] disponga di regole, procedure e accordi che disciplinino il trasferimento dei DCP attraverso tutti i tipi di mezzi, sia all'interno che all'esterno dell'organizzazione.

## Quadro normativo

**Obbligatorio (Livello 1)** (per PRIV-POL-00):
- **RGPD UE** : Articolo 32 (sicurezza appropriata del trattamento, incluso durante il trasferimento); Articoli 44–49 (garanzie per i trasferimenti internazionali); Articolo 5(1)(f) (principio di integrità e riservatezza)
- **LPD svizzera** : Articolo 7 (misure tecniche e organizzative proporzionate alla sensibilità); Articoli 16–17 (comunicazione transfrontaliera — equivalenza, clausole standard)
- **ISO/IEC 27701:2025** : Controlli A.3.5, A.3.6, A.3.7 (normativi)

---

# Classificazione delle informazioni relative ai DCP (A.3.5)

## Estensione dello schema di classificazione per i DCP

Lo schema di classificazione delle informazioni di [Organizzazione] (definito in ISMS-POL-A.5.12-13) DEVE essere applicato a tutte le informazioni. Per le informazioni contenenti o relative ai DCP, questa politica stabilisce criteri specifici ai DCP che estendono e integrano lo schema di classificazione SGSI.

### Livelli minimi di classificazione per i DCP

I seguenti livelli minimi di classificazione DEVONO applicarsi alle informazioni contenenti DCP, indipendentemente dagli altri criteri di classificazione:

| Categoria di DCP | Classificazione minima |
|-----------------|----------------------|
| **Dati a carattere personale ordinari** (nome, indirizzo, dati di contatto, fascicolo di impiego) | RISERVATO |
| **Dati a carattere personale finanziari** (conti bancari, registrazioni di pagamento, stipendio, credito) | RISERVATO |
| **DCP di categoria speciale** (salute/medico, biometrico, genetico, origine razziale/etnica, convinzione religiosa, opinione politica, vita/orientamento sessuale, appartenenza sindacale) | LIMITATO |
| **Dati a carattere personale sensibili** (dati di minori, casellari giudiziari, numeri di identificazione nazionale) | LIMITATO |
| **Credenziali di autenticazione** (password, token, chiavi crittografiche associate a identità individuali) | LIMITATO — incluse per comodità operativa poiché coesistono frequentemente con DCP nei registri di identità; classificate LIMITATO per motivi di sicurezza per ISMS-POL-A.5.12-13 |
| **DCP di persone ad alto rischio** (persone vulnerabili, informatori, interessati sotto misure di protezione) | LIMITATO |

### Regola di aggregazione dei DCP

Laddove le informazioni classificate individualmente al di sotto di RISERVATO vengano combinate in modo tale che i DCP possano essere derivati, identificati o dedotti, il dataset aggregato DEVE essere classificato come minimo RISERVATO. Laddove il dataset aggregato contenga o consenta la derivazione di DCP di categoria speciale, DEVE essere classificato LIMITATO.

Il Proprietario dei dati (o il RPD laddove non sia assegnato alcun Proprietario dei dati) DEVE effettuare la determinazione della classificazione per aggregazione e documentarla nel Registro di classificazione. Il RPD è proprietario del Registro di classificazione.

### Autorità di classificazione per i DCP

| Livello di classificazione | Chi può classificare i DCP | Chi può declassificare |
|---------------------------|--------------------------|----------------------|
| RISERVATO (DCP ordinari) | Proprietario dei dati, RPD | Proprietario dei dati con notifica al RPD |
| LIMITATO (DCP categoria speciale) | Proprietario dei dati con approvazione RPD | Proprietario dei dati con approvazione RPD e Direzione generale |
| LIMITATO (DCP ad alto rischio) | RPD con approvazione Direzione generale | RPD con approvazione Direzione generale |

### Revisione della classificazione dei DCP

In aggiunta ai trigger di revisione definiti in ISMS-POL-A.5.12-13, la classificazione dei DCP DEVE essere rivista: quando la finalità del trattamento cambia, coinvolgendo diverse categorie di DCP; quando la base giuridica del trattamento cambia, incidendo sul livello di sensibilità; a seguito di una DPIA che identifica un requisito di riclassificazione; alla notifica di un'APD o autorità di controllo; quando nuovi orientamenti o giurisprudenza modificano materialmente l'interpretazione di una categoria di DCP.

---

# Etichettatura delle informazioni relative ai DCP (A.3.6)

## Requisiti di etichettatura dei DCP

[Organizzazione] DEVE sviluppare e implementare procedure di etichettatura che identifichino le informazioni contenenti DCP come tali. Le procedure di etichettatura dei DCP DEVONO essere coerenti con e integrare lo schema di etichettatura SGSI (ISMS-POL-A.5.12-13).

### Etichettatura obbligatoria dei DCP

Tutte le informazioni classificate RISERVATO o LIMITATO in base al loro contenuto in DCP DEVONO riportare:

1. L'etichetta di classificazione applicabile (RISERVATO o LIMITATO) per gli standard di etichettatura SGSI
2. Un indicatore DCP che designa che l'informazione contiene dati a carattere personale

**Formati dell'indicatore DCP** (definiti in dettaglio in PRIV-IMP-A.3.5-7-TG):

| Formato | Indicatore DCP |
|---------|---------------|
| Documenti elettronici | Notazione «Contiene dati a carattere personale» nell'intestazione/piè di pagina o nelle proprietà del documento |
| Documenti fisici | Timbro «DATI PERSONALI» o indicatore stampato sulla copertina e sulla prima pagina |
| Database e archivi dati | Campo di metadati di classificazione: `pii_present = true`; campo categoria DCP compilato |
| E-mail | Aggiunta di prefisso all'oggetto dove il contenuto contiene DCP: `[DP]` o `[DPS]` per categoria speciale |
| Nomi di file/cartelle | Suffisso `_DCP` o `_DCS` dove pratico e coerente con le capacità del sistema |

### Etichettatura dei DCP di categoria speciale

Le informazioni contenenti DCP di categoria speciale DEVONO riportare in aggiunta un indicatore di categoria speciale per consentire una gestione rafforzata. Il formato specifico di questo indicatore è definito in PRIV-IMP-A.3.5-7-TG.

### Etichettatura di sistemi e repository

I repository, i database, i sistemi e gli ambienti di trattamento che conservano o trattano DCP DEVONO essere etichettati a livello di sistema con: la presenza di DCP (sì/no); le categorie di DCP trattati (ordinari, finanziari, categoria speciale, o elenco delle categorie applicabili); il perimetro giurisdizionale applicabile (es. interessati UE/SEE, interessati svizzeri).

L'etichettatura a livello di sistema è mantenuta nel Registro degli asset dati (vedere PRIV-IMP-A.3.5-7-TG per la struttura del registro).

### Obbligo di coerenza dell'etichettatura

Laddove l'etichetta di classificazione SGSI e il requisito di etichettatura DCP siano in conflitto (es. un asset è classificato INTERNO per criteri SGSI ma contiene DCP ordinari che richiedono la classificazione RISERVATO), la classificazione più alta DEVE prevalere e il livello minimo DCP DEVE applicarsi.

---

# Regole e accordi di trasferimento dei DCP (A.3.7)

## Requisiti di trasferimento dei DCP

[Organizzazione] DEVE stabilire e mantenere regole, procedure e accordi che coprono qualsiasi trasferimento di DCP attraverso tutti i tipi di mezzi, sia interni che esterni, elettronici o fisici.

### Trasferimento interno dei DCP

**All'interno di [Organizzazione]** : I DCP DEVONO essere trasferiti solo ai ruoli e al personale organizzativo con una finalità di trattamento legittima e un'autorizzazione di accesso appropriata; il trasferimento interno di DCP LIMITATI (categoria speciale) DEVE essere registrato nei log e tracciabile; i trasferimenti di DCP da sistema a sistema DEVONO utilizzare canali cifrati; il trasferimento interno di DCP verso ambienti di trattamento in giurisdizioni diverse DEVE essere trattato come trasferimento transfrontaliero.

### Trasferimento esterno dei DCP

**Verso i Responsabili del trattamento dei DCP** : I trasferimenti esterni di DCP verso responsabili del trattamento RICHIEDONO un accordo di trattamento attuale e valido (Articolo 28 RGPD; Articolo 9 LPD svizzera) in vigore prima dell'inizio del trasferimento. Nessun trasferimento di DCP verso un responsabile del trattamento esterno DEVE avvenire senza un accordo di trattamento firmato. Il RPD mantiene il Registro degli accordi di trattamento.

**Verso i Contitolari** : I trasferimenti esterni di DCP verso contitolari RICHIEDONO un accordo di contitolarità (Articolo 26 RGPD) che documenta le rispettive responsabilità. Il RPD DEVE approvare gli accordi di contitolarità prima del trasferimento dei DCP.

**Verso Destinatari e Terze Parti** : I trasferimenti esterni di DCP verso destinatari diversi da responsabili del trattamento o contitolari richiedono: una base giuridica documentata per la divulgazione per RGPD Articolo 6; la revisione del RPD laddove la divulgazione non sia routinaria; un registro del trasferimento nel RAT.

### Trasferimento internazionale e transfrontaliero dei DCP

I trasferimenti di DCP verso paesi o organizzazioni internazionali al di fuori del SEE (per il RGPD) o al di fuori della Svizzera (per la LPD svizzera) sono soggetti ai seguenti requisiti:

**Base giuridica del trasferimento** :

| Meccanismo | Applicabilità |
|-----------|--------------|
| Decisione di adeguatezza (Commissione UE / IFPDT svizzero) | Trasferimenti verso paesi con protezione adeguata riconosciuta — nessuna misura aggiuntiva richiesta |
| Clausole Contrattuali Standard (CCS) | Trasferimenti verso paesi senza adeguatezza — CCS UE (2021) o CCS svizzere secondo i casi |
| Norme vincolanti d'impresa (BCR) | Trasferimenti intra-gruppo con BCR approvate dall'APD competente — applicabile solo ai gruppi che hanno ottenuto l'approvazione APD; questo meccanismo è incluso per completezza; la sua disponibilità dipende dalla struttura aziendale |
| Deroghe Articolo 49 | Circostanze eccezionali solo (consenso dell'interessato, interessi vitali, importante interesse pubblico, rivendicazioni legali) — non per trasferimenti sistematici |

**Valutazione d'Impatto del Trasferimento (VIT)** : Laddove vengano utilizzate CCS o altri meccanismi contrattuali, [Organizzazione] DEVE condurre una VIT valutando se il quadro giuridico del paese di destinazione fornisce una protezione essenzialmente equivalente. La VIT, la decisione sulle misure supplementari e l'approvazione del RPD DEVONO essere documentate nel Registro dei trasferimenti internazionali.

### Metodi di trasferimento per i DCP

| Tipo di trasferimento | DCP RISERVATO | DCP LIMITATO / Categoria speciale |
|----------------------|---------------|-----------------------------------|
| **Elettronico — interno** | Canale cifrato (TLS minimo) | Canale cifrato + voce nel log di accesso |
| **Elettronico — esterno** | Email cifrata o piattaforma di trasferimento sicuro | Piattaforma con cifratura end-to-end; verifica dell'identità del destinatario richiesta |
| **Fisico — documenti** | Busta sigillata, consegna tracciata, firma del destinatario | Doppia sigillatura, corriere autorizzato, documentazione della catena di custodia |
| **Fisico — supporti** | Supporto cifrato, consegna tracciata | Supporto cifrato, corriere sicuro, conferma di consegna |
| **Cloud — trattamento** | Cifrato a riposo e in transito; residenza dei dati verificata | Cifrato a riposo e in transito; residenza confermata; responsabile del trattamento approvato dall'APD |

### Accordi di trasferimento

Tutti i trasferimenti esterni di DCP nell'ambito di relazioni continuative DEVONO essere disciplinati da un accordo scritto che copra come minimo: le finalità per cui il destinatario può utilizzare i DCP; i limiti di conservazione e gli obblighi di cancellazione/restituzione; le misure di sicurezza che il destinatario deve mantenere; le restrizioni sull'ingaggio di sub-responsabili del trattamento; gli obblighi e i termini di notifica delle violazioni; i diritti di audit (ove applicabile); la legge applicabile e la giurisdizione. Il RPD mantiene il Registro degli accordi di trasferimento. Nessun trasferimento esterno continuativo di DCP DEVE essere stabilito senza un accordo attuale nel registro.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità per A.3.5–A.3.7 |
|-------|-------------------------------|
| **RPD** | Autorità principale per i livelli minimi di classificazione DCP e le regole di trasferimento; approva i meccanismi di trasferimento transfrontaliero; mantiene il Registro dei trasferimenti internazionali e il Registro degli accordi di trasferimento |
| **Proprietario dei dati** | Classifica i dataset DCP nel proprio dominio; applica le etichette DCP; autorizza i trasferimenti interni; escalate i trasferimenti transfrontalieri al RPD |
| **RSSI** | Garantisce l'estensione coerente dello schema di classificazione SGSI ai DCP per questa politica; garantisce l'implementazione dei controlli di trasferimento (cifratura, registrazione nei log) |
| **Team Sicurezza IT / Proprietari di sistemi** | Implementano l'etichettatura DCP a livello di sistema; configurano i canali di trasferimento cifrati; mantengono i metadati di classificazione dei sistemi |
| **Referenti per la privacy** | Supporto di prima linea per le domande di classificazione DCP; escalation dei trigger di riclassificazione |
| **Legale/Conformità** | Consulenza sui meccanismi di trasferimento transfrontaliero; revisione delle CCS e delle decisioni di adeguatezza delle APD |
| **Tutto il personale** | Applica la classificazione e l'etichettatura ai DCP gestiti nel proprio ruolo; utilizza solo metodi di trasferimento approvati; segnala qualsiasi sospetta classificazione errata |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Registro di classificazione | Registrazioni delle classificazioni dei dataset DCP, incluse le determinazioni per aggregazione | 3 anni dalla sostituzione della classificazione o smaltimento del dataset |
| Registro degli asset dati | Registrazioni di etichettatura DCP a livello di sistema | In corso + 3 anni |
| Registro dei trasferimenti internazionali | Registrazioni VIT, CCS, riferimenti alle decisioni di adeguatezza, approvazioni RPD | Durata dell'attività di trasferimento + 3 anni |
| Registro degli accordi di trasferimento | Accordi di trattamento firmati, accordi di contitolarità, accordi con destinatari | Durata dell'accordo + 3 anni |
| Log di trasferimento interno | Log dei trasferimenti interni di DCP LIMITATI, inclusi finalità e autorizzazione | 3 anni dalla data del trasferimento |
| Registrazioni di revisione della classificazione | Prove di revisione periodica e innescata | 3 anni dalla data della revisione |

---

# Considerazioni di audit

**Per A.3.5 (Classificazione)** : Documentazione dello schema di classificazione che mostra i livelli minimi DCP; prove che i dataset DCP siano classificati al livello minimo richiesto; determinazioni di classificazione per aggregazione; registrazioni di revisione della classificazione.

**Per A.3.6 (Etichettatura)** : Procedure di etichettatura che coprono le informazioni contenenti DCP in tutti i formati; esempi di documenti etichettati e metadati di sistema che mostrano i campi indicatore DCP; Registro degli asset dati con campi DCP compilati.

**Per A.3.7 (Trasferimento)** : Regole e procedure di trasferimento che coprono i trasferimenti interni ed esterni; accordi di trattamento firmati per tutte le relazioni attive; Registro dei trasferimenti internazionali con documentazione VIT; log di trasferimento per i DCP LIMITATI.

---

<!-- QA_VERIFIED: 2026-04-03 -->
