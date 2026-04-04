<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.12-13-IT:operational:OP-POL:a.5.12-13 -->
**ISMS-OP-POL-A.5.12-13 — Classificazione e gestione delle informazioni**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Classificazione e gestione delle informazioni |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.5.12-13 |
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

- Controlli ISO/IEC 27001:2022 A.5.12, A.5.13 — Classificazione delle informazioni, etichettatura delle informazioni

**Controlli Annex A correlati**:

| Controllo | Relazione con la classificazione delle informazioni |
|-----------|-----------------------------------------------------|
| A.5.9 Inventario delle informazioni e altri asset associati | La classificazione è assegnata agli asset informativi inventariati |
| A.5.10 Uso accettabile delle informazioni | Le regole di uso accettabile applicano i requisiti di gestione per classificazione |
| A.5.14 Trasferimento delle informazioni | Il metodo di trasferimento è determinato dal livello di classificazione |
| A.5.15–18 Controllo degli accessi e gestione delle identità | I diritti di accesso sono concessi in base alla classificazione e al principio del bisogno di sapere |
| A.5.33 Protezione dei documenti | Conservazione e protezione dei documenti in linea con la classificazione |
| A.5.34 Privacy e protezione dei dati personali | Requisiti di classificazione e gestione dei dati personali |
| A.7.10 Supporti di archiviazione | Gestione e dismissione dei supporti per classificazione |
| A.7.14 Smaltimento o riutilizzo sicuro delle attrezzature | Standard di dismissione determinati dalla classificazione |
| A.8.10 Cancellazione delle informazioni | Standard di cancellazione sicura per livello di classificazione |
| A.8.11 Mascheramento dei dati | Mascheramento dei dati classificati in ambienti non di produzione |
| A.8.12 Prevenzione della perdita dei dati | I controlli DLP applicano le regole di gestione della classificazione |
| A.8.24 Uso della crittografia | I requisiti di cifratura sono determinati dalla classificazione |

**Policy interne correlate**:

- Policy di gestione degli asset
- Policy di controllo degli accessi
- Policy di trasferimento delle informazioni
- Policy sull'uso della crittografia
- Policy sulla privacy e protezione dei dati personali
- Policy sull'uso accettabile

---

# Policy di classificazione e gestione delle informazioni

## Scopo

Lo scopo di questa policy è garantire la corretta classificazione e gestione delle informazioni in base alla loro sensibilità, valore e requisiti legali, affinché le informazioni ricevano un livello di protezione adeguato per tutto il loro ciclo di vita.

Questa policy supporta la nLPD svizzera (revDSG) e l'Ordinanza sulla protezione dei dati (OPDo) implementando misure tecniche e organizzative proporzionate al rischio per proteggere i dati personali (inclusi i dati personali degni di particolare protezione) attraverso controlli basati sulla classificazione. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Tutte le informazioni in qualsiasi formato (digitale, fisico, verbale) che fanno parte dei sistemi e delle applicazioni inclusi nell'ambito della dichiarazione di scopo ISO 27001.

## Principio

Le informazioni DEVONO essere classificate in base ai requisiti legali, al valore, alla criticità e alla sensibilità rispetto a divulgazione o modifica non autorizzate. La classificazione determina i controlli di gestione applicati per tutto il ciclo di vita delle informazioni — dalla creazione all'archiviazione, trasmissione e distruzione.

---

## Schema di classificazione

Le informazioni DEVONO essere classificate in uno dei tre livelli seguenti:

| Livello | Descrizione | Impatto della divulgazione non autorizzata |
|---------|-------------|---------------------------------------------|
| **RISERVATO** | Informazioni la cui divulgazione causerebbe danni significativi all'organizzazione, ai suoi clienti o agli interessati. Include i dati protetti dalla legge. | Gravi perdite finanziarie, sanzioni normative, azioni legali, danni reputazionali significativi, rischio elevato per gli interessati |
| **INTERNO** | Informazioni destinate all'uso interno all'organizzazione. Non destinate alla divulgazione pubblica. | Lieve disagio operativo, lieve imbarazzo, impatto reputazionale limitato |
| **PUBBLICO** | Informazioni approvate per la diffusione pubblica. La divulgazione non causa alcun danno. | Nessun impatto negativo |

**Classificazione predefinita**: Le informazioni che non sono state classificate esplicitamente DEVONO essere trattate come **INTERNO** fino a quando non vengono classificate dal relativo proprietario.

### Classificazione per tipo di informazione

| Tipo di informazione | Classificazione minima |
|----------------------|------------------------|
| **Dati personali degni di particolare protezione** (nLPD Art. 5: salute, origine razziale/etnica, convinzioni religiose/politiche, casellari giudiziari, dati genetici, dati biometrici) | **RISERVATO** |
| **Dati personali** (nomi, indirizzi email, numeri di telefono, dati dei dipendenti) | **INTERNO** (minimo); **RISERVATO** se volume >1.000 record o combinati con categorie sensibili |
| **Documenti finanziari** (conti, transazioni, informazioni sugli stipendi, coordinate bancarie) | **RISERVATO** |
| **Segreti aziendali e proprietà intellettuale** (metodi proprietari, codice sorgente, progetti, formule) | **RISERVATO** |
| **Password, chiavi crittografiche, credenziali** | **RISERVATO** |
| **Contratti e accordi legali** | **RISERVATO** |
| **Policy, procedure e verbali di riunioni interne** | **INTERNO** |
| **Organigrammi, comunicazioni interne** | **INTERNO** |
| **Materiale di marketing, comunicati stampa, contenuti pubblicati** | **PUBBLICO** |
| **Informazioni già nel dominio pubblico** | **PUBBLICO** |

### Responsabilità di classificazione

- I **proprietari delle informazioni** (come definiti nella Policy di gestione degli asset) sono responsabili della classificazione dei propri asset informativi.
- La classificazione DEVE essere assegnata al momento della creazione o ricezione delle informazioni.
- La classificazione DEVE essere rivista quando le informazioni vengono significativamente modificate, condivise con nuovi destinatari o quando le circostanze aziendali cambiano.
- La classificazione eccessiva deve essere evitata — classificare tutto come RISERVATO ne diluisce il significato e spreca risorse.
- **Rischio di aggregazione**: Le informazioni classificate individualmente come INTERNO possono richiedere la riclassificazione a RISERVATO se combinate con altri dataset, qualora l'aggregazione generi un rischio di danno materialmente più elevato (ad es. combinazione di nomi con condizioni di salute, o di retribuzioni individuali in un rapporto di compensazione per dipartimento). I proprietari delle informazioni DEVONO considerare il rischio di aggregazione nella classificazione dei dataset.

---

## Etichettatura delle informazioni

### Requisiti di etichettatura

Tutte le informazioni DEVONO essere etichettate in base al loro livello di classificazione:

| Formato | Metodo di etichettatura |
|---------|-------------------------|
| **Documenti digitali** (Word, PDF, Excel) | Classificazione nell'intestazione o nel piè di pagina di ogni pagina (ad es. "RISERVATO") |
| **Email** | Prefisso di classificazione nell'oggetto (ad es. "[RISERVATO] Oggetto") |
| **Documenti fisici** | Classificazione sulla pagina di copertina; intestazione o piè di pagina nelle pagine successive |
| **Supporti fisici** (chiavette USB, nastri di backup) | Etichetta fisica applicata al dispositivo o al contenitore |
| **Metadati dei file** | Classificazione registrata nelle proprietà del file o nei metadati del sistema di gestione documentale |
| **Record di database** | Colonna di classificazione o tag di metadati per dataset |

Le informazioni **PUBBLICO** non richiedono un'etichetta di classificazione, salvo che vengano pubblicate su piattaforme interne dove il loro stato pubblico potrebbe non essere chiaro.

Le **informazioni non etichettate** DEVONO essere trattate come **INTERNO** per impostazione predefinita.

Laddove l'organizzazione utilizzi Microsoft 365 o piattaforme equivalenti, le etichette di sensibilità dovrebbero essere configurate per automatizzare l'applicazione della classificazione, inclusa la cifratura, le restrizioni di accesso e le marcature visive.

---

## Gestione delle informazioni

### Matrice di gestione

| Aspetto di gestione | PUBBLICO | INTERNO | RISERVATO |
|--------------------|----------|---------|-----------|
| **Archiviazione digitale** | Nessuna restrizione | Solo sistemi gestiti dall'organizzazione; non su dispositivi personali senza MDM | Cifratura a riposo (AES-256); cartelle con controllo degli accessi; nessun supporto rimovibile senza cifratura |
| **Archiviazione fisica** | Nessuna restrizione | Locali aziendali; archivio standard | Armadi con serratura o locali ad accesso limitato; scrivania pulita applicata |
| **Trasmissione email** | Nessuna restrizione | Email interna o email esterna cifrata | Email cifrata obbligatoria; password/chiave di decifratura tramite canale separato |
| **Trasferimento file** | Nessuna restrizione | Solo piattaforme di condivisione file approvate | Solo trasferimento cifrato (SFTP, HTTPS); nessun servizio cloud non approvato |
| **Trasferimento fisico** | Nessuna restrizione | Busta sigillata; posta interna | Imballaggio antimanomissione; corriere approvato con tracciamento; conferma del destinatario |
| **Condivisione — interna** | Senza restrizioni | All'interno dell'organizzazione | Su base del bisogno di sapere con approvazione documentata dal proprietario delle informazioni |
| **Condivisione — esterna** | Senza restrizioni | NDA richiesto; canali approvati | NDA + autorizzazione specifica dal proprietario delle informazioni; accordo di trasferimento ove richiesto |
| **Stampa** | Nessuna restrizione | Ritirare rapidamente; nessun documento abbandonato | Stampa sicura con sblocco (badge/PIN); ritirare immediatamente |
| **Archiviazione cloud** | Servizi approvati | Servizi approvati; dati in Svizzera o paese adeguato | Servizi approvati; dati preferibilmente in Svizzera; cifratura con chiavi gestite dall'organizzazione |
| **Dispositivi mobili** | Nessuna restrizione | Solo dispositivi con MDM aziendale | MDM iscritto; cifratura del dispositivo; capacità di cancellazione remota |
| **Backup** | Backup standard | Backup cifrato | Backup cifrato; accesso al ripristino limitato |

### Archiviazione delle informazioni

Le informazioni dell'organizzazione NON devono essere archiviate su attrezzature personali, account email personali o servizi cloud personali, salvo approvazione del RSSI e registrazione in un registro approvato.

Le informazioni dell'organizzazione DEVONO essere protette da controlli degli accessi come definito nella Policy di controllo degli accessi.

Le informazioni riservate DEVONO essere cifrate a riposo e in transito quando archiviate o trasmesse attraverso qualsiasi sistema, in conformità con la Policy sull'uso della crittografia.

Le informazioni riservate e interne NON devono essere archiviate o trattate in ambienti di sviluppo o test, a meno che i dati non siano stati mascherati, anonimizzati o pseudonimizzati. Laddove sia necessario utilizzare dati di produzione in ambienti non di produzione, è richiesta l'approvazione del proprietario delle informazioni e del RSSI, e i dati DEVONO essere gestiti allo stesso livello di classificazione della produzione.

Laddove l'organizzazione implementi strumenti di Data Leakage Prevention (DLP), le policy DLP DEVONO essere allineate allo schema di classificazione per rilevare e prevenire il trasferimento o la divulgazione non autorizzata di informazioni RISERVATE (ad es. blocco di email esterne contenenti file etichettati RISERVATO, impedimento dell'upload su servizi cloud non approvati).

### Gestione delle informazioni verbali

Le informazioni riservate discusse verbalmente (in riunioni, telefonate o conversazioni) DEVONO essere trattate con la dovuta cura:

- Le discussioni di informazioni riservate DEVONO avvenire in ambienti privati (uffici chiusi, sale riunioni con porte chiuse) — non in spazi open space, luoghi pubblici o mezzi di trasporto pubblici.
- Le riunioni virtuali in cui si discutono informazioni riservate DEVONO utilizzare piattaforme cifrate con accesso limitato ai partecipanti autorizzati.
- I partecipanti DEVONO essere informati della natura riservata della discussione all'inizio della riunione.
- Appunti o verbali di discussioni riservate DEVONO essere classificati e gestiti di conseguenza.

### Controllo dei dispositivi e dei supporti

Tutti i supporti elettronici e cartacei contenenti informazioni riservate DEVONO essere fisicamente protetti da accessi non autorizzati, mediante conservazione in cassetti, armadi con serratura o locali ad accesso limitato.

I supporti rimovibili (chiavette USB, hard disk esterni, nastri di backup) contenenti dati riservati DEVONO essere cifrati e registrati nell'inventario degli asset, in conformità con la Policy di gestione degli asset.

### Backup delle informazioni

Le informazioni dell'organizzazione DEVONO essere sottoposte a backup, conservate e testate in conformità con il calendario di backup. I backup DEVONO essere cifrati con cifratura robusta. Tutti i backup DEVONO essere archiviati in luoghi sicuri con accesso limitato al personale autorizzato.

---

## Distruzione delle informazioni

Quando le informazioni non sono più necessarie e il loro periodo di conservazione è scaduto, DEVONO essere distrutte in modo sicuro in base al loro livello di classificazione.

### Distruzione di documenti cartacei

| Classificazione | Standard di distruzione |
|-----------------|-------------------------|
| **RISERVATO** | Distruzione a taglio incrociato secondo DIN 66399 Livello di sicurezza P-4 o superiore, oppure deposito in contenitori per documenti riservati gestiti da un fornitore certificato di distruzione |
| **INTERNO** | Distruzione a taglio incrociato secondo DIN 66399 Livello di sicurezza P-3 o superiore, oppure contenitori per documenti riservati approvati |
| **PUBBLICO** | Raccolta differenziata o rifiuti generici |

### Distruzione di informazioni elettroniche

| Classificazione | Standard di distruzione |
|-----------------|-------------------------|
| **RISERVATO** | Cancellazione crittografica (distruzione della chiave di cifratura) o sovrascrittura conforme a NIST SP 800-88; documentazione della verifica della cancellazione |
| **INTERNO** | Cancellazione sicura (sovrascrittura); sanificazione standard dei supporti |
| **PUBBLICO** | Cancellazione standard |

I log del processo di sanificazione DEVONO essere conservati laddove lo strumento di sanificazione lo consenta.

### Distruzione di supporti e dispositivi elettronici

I supporti e i dispositivi elettronici che hanno archiviato informazioni riservate o interne DEVONO essere distrutti con metodi approvati quando non più necessari:

- **SSD e storage flash**: Cancellazione crittografica (ATA Secure Erase) o distruzione fisica.
- **Hard disk magnetici**: Sovrascrittura conforme a NIST SP 800-88 o distruzione fisica (smagnetizzazione, triturazione).
- **Nastri di backup**: Smagnetizzazione o distruzione fisica.
- **Supporti ottici**: Triturazione fisica.

La distruzione di supporti riservati DEVE essere eseguita da fornitori terzi specializzati e approvati laddove la distruzione interna non sia fattibile. DEVONO essere ottenuti e conservati certificati di distruzione come evidenza.

Un inventario dei dispositivi, inclusi quelli distrutti, DEVE essere mantenuto in conformità con la Policy di gestione degli asset.

---

## Riclassificazione

La classificazione delle informazioni non è permanente. Le informazioni DEVONO essere riclassificate quando:

- La sensibilità o il valore delle informazioni cambia.
- I requisiti legali o normativi cambiano.
- Un obbligo contrattuale scade (ad es. il periodo di NDA termina).
- Le informazioni vengono approvate per la diffusione pubblica.
- Il proprietario delle informazioni determina che la classificazione attuale non è più appropriata.

La riclassificazione DEVE essere eseguita dal proprietario delle informazioni e l'etichettatura DEVE essere aggiornata di conseguenza.

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa policy:

- **Documentazione dello schema di classificazione delle informazioni** (questa policy) — *rivista annualmente*
- **Campioni di documenti classificati** che mostrano la corretta etichettatura (intestazioni, piè di pagina, prefissi email) — *campione di 5–10 documenti per livello di classificazione raccolto durante l'audit annuale*
- **Evidenze di implementazione della matrice di gestione** (controlli degli accessi, impostazioni di cifratura, restrizioni di condivisione) — *screenshot delle configurazioni di sistema o esportazioni di audit; revisione annuale*
- **Registri di distruzione dei supporti riservati** (certificati di distruzione, log di cancellazione) — *conservati per 5 anni; riconciliati annualmente con i registri di dismissione degli asset*
- **Registro degli asset informativi** con le assegnazioni di classificazione (ai sensi della Policy di gestione degli asset) — *obiettivo: 100% degli asset informativi classificati; misurato annualmente*
- **Registri di formazione** che attestano che i dipendenti sono stati formati sui requisiti di classificazione e gestione — *formazione annuale di sensibilizzazione; completamento tracciato*
- **Registri delle eccezioni** per qualsiasi deviazione dalle regole di gestione — *revisione trimestrale; presentazione alla revisione del management*
- **Configurazione delle policy DLP e rapporti sugli incidenti** (dove implementato il DLP) — *revisione trimestrale*

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa policy attraverso vari metodi, inclusi a titolo non esaustivo: campionamento di documenti per la verifica della corretta etichettatura, audit dei controlli degli accessi, registri di distruzione dei supporti, audit interni ed esterni, e feedback al proprietario della policy.

## Deroghe

Qualsiasi deroga a questa policy DEVE essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con documentazione dell'accettazione del rischio, dei controlli compensativi e di una data di revisione definita. Le deroghe DEVONO essere segnalate al Team di revisione del management.

## Non conformità

Un dipendente ritenuto responsabile di aver violato questa policy potrà essere soggetto a misure disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa policy è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO tener conto delle variazioni agli standard di classificazione, dei requisiti normativi (inclusi gli sviluppi della nLPD svizzera e del GDPR), dei rischi emergenti in materia di protezione dei dati e delle lezioni apprese dagli incidenti.

---

# Sezioni della norma ISO 27001 trattate

Policy di classificazione e gestione delle informazioni — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.4 Responsabilità del management |
| Clausola 6.2 Obiettivi per la sicurezza delle informazioni | 5.36 Conformità a policy, regole e standard |
| Clausola 7.3 Consapevolezza | **5.12 Classificazione delle informazioni** |
| Clausola 7.5.2 Creazione e aggiornamento della documentazione | **5.13 Etichettatura delle informazioni** |
| Clausola 7.5.3 Controllo delle informazioni documentate | 6.3 Sensibilizzazione, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 7.10 Supporti di archiviazione |
| | 7.14 Smaltimento o riutilizzo sicuro delle attrezzature |
| | 8.10 Cancellazione delle informazioni |
| | 8.11 Mascheramento dei dati |

**Quadro normativo e legale**:

| Quadro di riferimento | Rilevanza |
|-----------------------|-----------|
| nLPD svizzera (revDSG) | Art. 5 — Definizione di dati personali degni di particolare protezione (mappatura a RISERVATO); Art. 8 — Misure tecniche e organizzative |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 5 — Principi di protezione dei dati; Art. 9 — Categorie particolari di dati personali; Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Controlli Annex A 5.12, 5.13 |
| ISO/IEC 27002:2022 | Sezioni 5.12, 5.13 — Linee guida per l'implementazione |
| NIST SP 800-53 Rev 5 | RA-2 (Categorizzazione della sicurezza), AC-16 (Attributi di sicurezza e privacy), MP-3 (Marcatura dei supporti), MP-6 (Sanificazione dei supporti) |
| CIS Controls v8 | Controllo 3 (Protezione dei dati — inclusa classificazione, cifratura, dismissione) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
