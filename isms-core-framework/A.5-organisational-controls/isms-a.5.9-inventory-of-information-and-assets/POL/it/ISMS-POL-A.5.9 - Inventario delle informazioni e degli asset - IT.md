<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.9-IT:framework:POL:a.5.9 -->
**ISMS-POL-A.5.9 — Inventario delle informazioni e degli asset**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Inventario delle informazioni e degli asset |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.9 |
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
| 1.0 | [Data] | RSSI | Politica iniziale monitorata nei Cruscotti di sintesi per la prima certificazione ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Direttore dei Sistemi Informativi (DSI)
- Conformità: Responsabile Legale/Conformità
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.5.10–A.5.18 (Controlli di gestione degli asset)
- ISMS-POL-A.8.x (Controlli tecnici)
- ISMS-IMP-A.5.9.1-UG/TG (Identificazione e scoperta degli asset)
- ISMS-IMP-A.5.9.2-UG/TG (Struttura e manutenzione dell'inventario)
- ISMS-IMP-A.5.9.3-UG/TG (Specifiche di valutazione)
- ISMS-IMP-A.5.9.4-UG/TG (Valutazione della responsabilità del proprietario)
- ISO/IEC 27001:2022 Controllo A.5.9

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per il mantenimento di un inventario delle informazioni e degli asset associati, conformemente al Controllo A.5.9 della norma ISO/IEC 27001:2022.

**Il principio fondamentale**: Non si può proteggere ciò di cui non si conosce l'esistenza. L'inventario degli asset è la fondazione su cui si basano tutti gli altri controlli di sicurezza — valutazione del rischio, controllo degli accessi, classificazione, gestione delle vulnerabilità, risposta agli incidenti e pianificazione della continuità operativa.

**Perimetro**: Questa politica si applica a tutti gli asset informativi (dati, contenuti, proprietà intellettuale) e agli asset associati (infrastruttura IT, applicazioni, strutture fisiche, competenze del personale) nell'ambito della gestione della sicurezza delle informazioni di [Organizzazione].

**Scopo**: Definire i requisiti organizzativi per la creazione, manutenzione e governance dell'inventario degli asset. Questa politica stabilisce COSA deve essere inventariato, CHI è responsabile e COME viene verificata la conformità. Le procedure di attuazione (COME) sono documentate separatamente nella suite ISMS-IMP-A.5.9.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2, HIPAA (applicabilità condizionale per ISMS-POL-00).

---

# Allineamento sui controlli e perimetro

## Controllo ISO/IEC 27001:2022 A.5.9

**ISO/IEC 27001:2022 Allegato A.5.9 — Inventario delle informazioni e degli altri asset associati**

> *Deve essere creato e mantenuto un inventario delle informazioni e degli altri asset associati, compresi i rispettivi proprietari.*

**Obiettivo del controllo (ISO/IEC 27002:2022)**: Identificare le informazioni e gli altri asset associati dell'organizzazione al fine di mantenerne la sicurezza e assegnare le responsabilità appropriate.

**Tipo di controllo**: Organizzativo
**Proprietà della sicurezza delle informazioni**: Riservatezza, Integrità, Disponibilità
**Concetti di cybersicurezza**: Identificare
**Capacità operative**: Gestione degli asset
**Domini di sicurezza**: Governance ed Ecosistema

## Cosa fa questa politica

Questa politica: **definisce** cosa costituisce un asset informativo e un asset associato che richiede l'inventario; **stabilisce** gli attributi obbligatori per i record dell'inventario; **specifica** i requisiti di assegnazione della proprietà e la responsabilità del proprietario; **fissa** gli standard di accuratezza, completezza e aggiornamento per la manutenzione dell'inventario; **identifica** i ruoli e le responsabilità organizzativi; **fa riferimento** ai requisiti normativi applicabili per ISMS-POL-00.

## Cosa NON fa questa politica

Questa politica NON: specifica dettagli tecnici di implementazione; definisce la selezione degli strumenti di inventario; fornisce procedure dettagliate di scoperta; descrive flussi di lavoro di manutenzione; sostituisce la valutazione del rischio.

## Perimetro

**Categorie di asset nel perimetro**:

1. **Asset informativi**: Qualsiasi dato, contenuto o conoscenza con valore per [Organizzazione]

   - Dati strutturati (database, data warehouse)
   - Documenti non strutturati (file, email, report)
   - Documenti e archivi (conservazione normativa)
   - Proprietà intellettuale (segreti commerciali, brevetti, design)
   - Configurazione e parametri (configurazioni di sistema)
   - Materiali di autenticazione e crittografici (chiavi, certificati, credenziali)

2. **Asset associati — Infrastruttura IT**: Sistemi che elaborano, archiviano o trasmettono informazioni

   - Server fisici e macchine virtuali
   - Sistemi di storage e infrastruttura di backup
   - Infrastruttura di rete (router, switch, firewall, load balancer)
   - Endpoint (postazioni di lavoro, laptop, dispositivi mobili)
   - Infrastruttura e servizi cloud

3. **Asset associati — Applicazioni**: Software che elabora le informazioni

   - Applicazioni aziendali (ERP, CRM, sistemi finanziari)
   - SaaS e servizi cloud
   - Applicazioni sviluppate internamente
   - Strumenti di sviluppo e pipeline CI/CD
   - API e piattaforme di integrazione

4. **Asset associati — Fisici**: Risorse tangibili che supportano le operazioni

   - Strutture e data center
   - Supporti rimovibili (chiavette USB, nastri di backup, unità portatili)
   - Apparecchiature di sicurezza fisica (controllo degli accessi, sorveglianza)
   - Documenti cartacei e materiali stampati

5. **Asset associati — Personale**: Risorse umane e competenze

   - Ruoli chiave del personale (critici per le operazioni)
   - Competenze specializzate (competenze uniche, certificazioni)
   - NON i record individuali delle persone (conformità alla privacy)

**Fuori dal perimetro**: Asset di proprietà di terzi (salvo che trattino informazioni di [Organizzazione]); dispositivi personali non utilizzati per il lavoro di [Organizzazione]; informazioni pubbliche senza requisiti di riservatezza, integrità o disponibilità; materiale di consumo di ufficio senza impatto sulla sicurezza.

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria** (si applica a tutte le operazioni di [Organizzazione]):

- **nLPD svizzera (Art. 8)**: La sicurezza dei dati personali richiede di sapere quali dati esistono e dove
- **RGPD dell'UE (Artt. 5, 32)**: La protezione dei dati fin dalla progettazione richiede un inventario documentato dei dati
- **ISO/IEC 27001:2022 (Controllo A.5.9)**: Requisito di controllo esplicito per la certificazione

**Livello 2 — Applicabilità condizionale** (attivata da attività aziendali specifiche):

- **PCI DSS v4.0.1 (Requisiti 2.4, 12.5)**: Inventario dei componenti di sistema nell'ambiente dei dati dei titolari di carta
- **HIPAA (164.310(d)(1))**: Inventario e controlli degli asset per i sistemi informativi sanitari
- **FINMA**: Requisiti di inventario degli asset basati sul rischio per le istituzioni finanziarie svizzere
- **DORA/NIS2**: Inventario degli asset TIC per le infrastrutture critiche e le entità finanziarie
- **SOX**: I controlli IT generali richiedono un inventario documentato dei sistemi per la reportistica finanziaria

**Livello 3 — Riferimento informativo**: ISO/IEC 19770-1; ISO 55001; NIST SP 800-53 (CM-8, PM-5); CIS Controls (1, 2); COBIT 2019 (BAI09).

---

# Quadro dei requisiti

## Creazione dell'inventario degli asset

**Requisito A.5.9-R1**: [Organizzazione] DEVE mantenere un inventario delle informazioni e degli asset associati.

**Copertura obbligatoria**: Tutti gli asset informativi nell'ambito del SGSI; tutta l'infrastruttura IT che elabora informazioni; tutte le applicazioni e i servizi; tutti gli asset fisici che supportano la sicurezza; tutti gli asset del personale critici per le operazioni.

**Approccio di implementazione**: [Organizzazione] determina la struttura appropriata dell'inventario in base alla valutazione del rischio. L'inventario può essere composto da più inventari specializzati (CMDB per l'IT, HRIS per il personale, repository di documenti) a condizione che soddisfino collettivamente i requisiti di controllo.

## Categorizzazione degli asset

**Requisito A.5.9-R2**: [Organizzazione] DEVE categorizzare gli asset per consentire l'applicazione appropriata dei controlli di sicurezza.

**Dimensioni di categorizzazione**:

1. **Per tipo di asset** (categorizzazione primaria): Asset informativi; Infrastruttura IT; Applicazioni; Asset fisici; Asset del personale.

2. **Per criticità** (per il trattamento basato sul rischio):
   - Critico: La perdita causerebbe un grave impatto aziendale (interruzione operativa, violazione normativa)
   - Alto: La perdita causerebbe un impatto aziendale significativo (perdita finanziaria, danno reputazionale)
   - Medio: La perdita causerebbe un impatto aziendale moderato (riduzione dell'efficienza)
   - Basso: La perdita causerebbe un impatto aziendale minimo (inconveniente minore, facilmente sostituibile)

3. **Per stato del ciclo di vita** (per la pianificazione della manutenzione): Attivo; Sviluppo; Manutenzione; Ritirato; Archiviato.

## Attributi obbligatori dell'inventario

**Requisito A.5.9-R3**: [Organizzazione] DEVE documentare gli attributi obbligatori per ciascun asset inventariato.

**Attributi di base** (richiesti per tutti gli asset):

| Attributo | Descrizione | Scopo | Verifica |
|-----------|-------------|-------|----------|
| **ID asset** | Identificativo univoco | Tracciabilità tra i sistemi | Automatica (generato dal sistema) |
| **Nome asset** | Nome leggibile dall'uomo | Comunicazione e reportistica | Verifica del proprietario |
| **Tipo di asset** | Categoria per R2 | Applicabilità del controllo | Validazione della categoria |
| **Proprietario** | Individuo responsabile (per gli asset informativi, questo è il «Titolare dei dati» nella terminologia RGPD) | Assegnazione della responsabilità | Riconoscimento del proprietario |
| **Custode** | Gestore quotidiano (può differire dal proprietario) — parte tecnica che gestisce l'infrastruttura/i sistemi | Responsabilità operativa | Riconoscimento del custode |
| **Descrizione** | Scopo e funzione | Comprensione e contesto | Verifica del proprietario |
| **Ubicazione** | Posizione fisica o logica | Tracciamento degli asset, residenza dei dati | Verifica fisica |
| **Stato** | Stato del ciclo di vita per R2 | Pianificazione della manutenzione | Flusso di lavoro degli stati |
| **Criticità** | Impatto aziendale per R2 | Prioritizzazione del rischio | Allineamento alla valutazione del rischio |
| **Data di creazione** | Data di acquisizione/creazione | Tracciamento dell'età dell'asset | Verifica della documentazione |
| **Ultimo aggiornamento** | Record ultima modifica | Tracciamento dell'aggiornamento | Timestamp automatico |
| **Ultima revisione** | Ultima revisione da parte del proprietario | Garanzia dell'accuratezza | Attestazione del proprietario |
| **Prossima data di revisione** | Revisione pianificata | Manutenzione proattiva | Calendario di revisione |

**Attributi specifici degli asset informativi**:

| Attributo | Descrizione | Scopo |
|-----------|-------------|-------|
| **Classificazione dei dati** | Livello di riservatezza/integrità/disponibilità per A.5.12 | Selezione del controllo di sicurezza |
| **Formato dei dati** | Formato di file, schema, struttura | Compatibilità tecnica |
| **Ubicazione/i di archiviazione** | Dove risiedono fisicamente i dati | Conformità alla residenza dei dati |
| **Periodo di conservazione** | Requisito di conservazione legale/aziendale | Conformità, pianificazione dello storage |
| **Requisiti legali/normativi** | Normative applicabili | Monitoraggio della conformità |
| **Sistemi correlati** | Sistemi che accedono a queste informazioni | Analisi delle dipendenze |
| **Stato della cifratura** | A riposo, in transito, o entrambi | Verifica della protezione crittografica |

**Attributi specifici dell'infrastruttura IT**:

| Attributo | Descrizione | Scopo |
|-----------|-------------|-------|
| **Produttore/Fornitore** | Produttore dell'asset | Contratti di supporto, compatibilità |
| **Modello/Versione** | Versione specifica del prodotto | Gestione delle patch, tracciamento EOL |
| **Numero seriale/Tag asset** | Identificativo fisico | Verifica dell'asset fisico |
| **Indirizzo IP/Nome host** | Identificativo di rete | Gestione della rete |
| **Riferimento di configurazione** | Riferimento alla configurazione standard | Gestione della configurazione (A.8.9) |
| **Dipendenze** | Asset richiesti per il funzionamento | Valutazione dell'impatto |
| **Informazioni supportate** | Asset informativi che elabora | Ereditarietà della classificazione |

## Proprietà degli asset

**Requisito A.5.9-R4**: [Organizzazione] DEVE assegnare un proprietario a ogni asset inventariato.

**Principi di proprietà**:

- **Assegnazione universale**: Ogni asset DEVE avere un proprietario assegnato (nessuna eccezione)
- **Responsabilità**: Il proprietario è responsabile dell'asset per tutto il suo ciclo di vita
- **Delega consentita**: Il proprietario può delegare le responsabilità del custode ma mantiene la responsabilità
- **Riconoscimento richiesto**: I proprietari devono riconoscere formalmente la proprietà e le responsabilità
- **Gestione dei cambiamenti**: I cambiamenti di proprietà attivano l'aggiornamento dell'inventario

**Responsabilità del proprietario**:

- Classificare l'asset in base al valore aziendale e al rischio
- Garantire che vengano applicati i controlli di sicurezza appropriati
- Rivedere l'accuratezza del record dell'inventario almeno annualmente
- Approvare le richieste di accesso agli asset di proprietà
- Segnalare gli incidenti di sicurezza che interessano gli asset di proprietà
- Partecipare alle decisioni sul ciclo di vita degli asset (dismissione, archiviazione)
- Mantenere la consapevolezza dei requisiti normativi che interessano gli asset di proprietà

**Quando la proprietà non è chiara**:

1. Escalation al livello di gestione appropriato entro 5 giorni lavorativi dalla scoperta dell'asset
2. Documentare l'assegnazione temporanea del custode
3. Fissare una scadenza per la determinazione del proprietario permanente:
   - **Scadenza iniziale**: 30 giorni di calendario
   - **Proroga consentita**: Fino a 90 giorni di calendario con approvazione del RSSI se la proprietà richiede una risoluzione interfunzionale (documentare la giustificazione e i controlli compensativi)
4. Gli asset senza proprietario oltre 90 giorni richiedono l'approvazione della Direzione generale come eccezione formale

Gli asset senza proprietario vengono monitorati nel registro delle eccezioni. Obiettivo: ≥95% degli asset con proprietari permanenti assegnati entro 30 giorni, 100% entro 90 giorni.

## Standard di qualità dell'inventario

**Requisito A.5.9-R5**: [Organizzazione] DEVE mantenere la qualità dell'inventario attraverso standard di accuratezza, completezza e aggiornamento.

### Completezza

**Standard**: L'inventario deve includere tutti gli asset nel perimetro.

**Obiettivo di certificazione iniziale**: 85% di completezza per gli asset critici, 80% per gli asset standard, valutati entro 90 giorni dall'approvazione della politica.

**Obiettivo di stato maturo** (entro 12 mesi post-certificazione): 95% di completezza per gli asset critici, 90% per gli asset standard.

### Accuratezza

**Standard**: I dati dell'inventario devono riflettere correttamente lo stato effettivo dell'asset.

**Obiettivi di accuratezza per la certificazione iniziale** (riferimento + 90 giorni):

- Asset informativi: 85% di accuratezza
- Infrastruttura IT: 90% di accuratezza
- Asset fisici: 80% di accuratezza
- Asset del personale: 95% di accuratezza

**Obiettivi di accuratezza per lo stato maturo** (entro 12 mesi post-certificazione):

- Asset informativi: 95% di accuratezza
- Infrastruttura IT: 98% di accuratezza
- Asset fisici: 90% di accuratezza
- Asset del personale: 100% di accuratezza

### Aggiornamento

**Standard**: L'inventario deve riflettere lo stato corrente, non lo stato storico.

**Trigger di aggiornamento**: Creazione dell'asset; modifica dell'asset; dismissione dell'asset; cambiamento di proprietà; cambiamento di classificazione; revisione periodica programmata.

**Massima obsolescenza** (trigger di aggiornamento — con quale rapidità viene aggiornato l'inventario dopo un evento di cambiamento):

- Asset critici: Aggiornamenti in tempo reale o giornalieri
- Asset ad alto rischio: Aggiornamenti entro 3 giorni lavorativi
- Asset standard: Aggiornamenti entro 1 settimana
- Asset a basso rischio: Aggiornamenti entro 1 mese
- Tutti gli asset: Revisione minima annuale

**Calendario di verifica**:

| Categoria asset | Frequenza di revisione | Ruolo responsabile | Metodo di verifica |
|----------------|----------------------|--------------------|-------------------|
| Informazioni critiche | Trimestrale | Proprietario delle informazioni | Attestazione del proprietario + campionamento |
| Infrastruttura IT ad alto rischio | Trimestrale | Proprietario del sistema | Scansione automatica + verifica manuale |
| Asset standard | Semestrale | Proprietario dell'asset | Revisione del proprietario + verifiche a campione |
| Asset a basso rischio | Annuale | Proprietario dell'asset | Attestazione del proprietario |
| Tutti gli asset del personale | Trimestrale | HR + Responsabili di dipartimento | Riconciliazione del sistema HR |

## Requisiti di integrazione

**Requisito A.5.9-R6**: [Organizzazione] DEVE integrare l'inventario degli asset con altri processi SGSI e sistemi organizzativi.

**Punti di integrazione obbligatori**:

| Controllo/Processo SGSI | Requisito di integrazione | Scopo |
|------------------------|--------------------------|-------|
| **A.5.12 (Classificazione delle informazioni)** | Classificazione assegnata agli asset informativi | Selezione del controllo di sicurezza |
| **A.5.13 (Etichettatura)** | Le etichette fanno riferimento alla classificazione dell'inventario | Marcatura di sicurezza visibile |
| **A.5.15 (Controllo degli accessi)** | Regole di accesso basate sulla proprietà e la classificazione degli asset | Decisioni di autorizzazione |
| **A.5.18 (Diritti di accesso)** | Diritti di accesso approvati dai proprietari degli asset | Applicazione della responsabilità |
| **A.8.x (Controlli tecnici)** | I controlli tecnici proteggono gli asset inventariati | Mappatura controllo-asset |
| **Gestione del rischio (Clausola 6)** | L'inventario fornisce input alla valutazione del rischio | Identificazione minaccia-asset-vulnerabilità |
| **Gestione dei cambiamenti** | I cambiamenti attivano gli aggiornamenti dell'inventario | Manutenzione dell'aggiornamento |
| **Gestione degli incidenti** | Gli incidenti fanno riferimento agli asset interessati | Valutazione dell'impatto |
| **Continuità operativa** | Identificazione degli asset critici per BCP/DRP | Prioritizzazione |

**Integrazione con i sistemi organizzativi**:

| Sistema | Scopo dell'integrazione | Sincronizzazione |
|---------|------------------------|----------------|
| **CMDB** | Fonte dell'inventario degli asset IT | Bidirezionale (dove tecnicamente fattibile) |
| **Acquisti/Finanza** | Tracciamento dell'acquisizione degli asset | In entrata (acquisti → inventario) |
| **Sistema HR** | Validazione degli asset del personale | In entrata (HR → inventario per ruoli/competenze) |
| **Sistema di gestione degli asset** | Tracciamento degli asset fisici | Bidirezionale |
| **Gestione dei documenti** | Repository degli asset informativi | In entrata (DMS → metadati dell'inventario) |

**Approccio a fasi per la maturità dell'integrazione**:

**Fase 1 — Certificazione iniziale** (integrazione minima vitale): Riconciliazione manuale trimestrale con CMDB/HR/Acquisti; nuovo record dell'asset aggiunto entro 30 giorni dall'approvazione dell'acquisto.

**Fase 2 — Stato maturo** (entro 18 mesi post-certificazione): Sincronizzazione automatica bidirezionale dove tecnicamente fattibile; scansioni di scoperta automatiche (settimanali) con avvisi di riconciliazione.

---

# Governance e conformità

## Ruoli e responsabilità

**Direzione generale**: Approvare la politica; allocare le risorse; ricevere i report annuali di conformità; garantire che la cultura organizzativa supporti la responsabilità degli asset.

**RSSI**: Essere proprietario della politica e del quadro dell'inventario degli asset; definire i requisiti e gli standard di qualità; monitorare la conformità; riferire alla Direzione generale.

**Responsabile della Sicurezza delle Informazioni**: Implementare il quadro dell'inventario; condurre valutazioni periodiche; fornire guida ai proprietari e ai custodi degli asset; monitorare e riferire le metriche.

**Operazioni IT / Team infrastrutturali**: Mantenere l'inventario dell'infrastruttura IT; integrare con il CMDB; condurre scansioni di scoperta automatiche; aggiornare l'inventario per gli eventi del ciclo di vita degli asset IT.

**Proprietari delle applicazioni / Proprietari dei sistemi**: Mantenere l'inventario delle applicazioni e dei sistemi; documentare le dipendenze e i flussi di informazioni; classificare le applicazioni per criticità; aggiornare l'inventario per i cambiamenti delle applicazioni.

**Proprietari delle informazioni / Titolari dei dati**: Essere proprietari degli asset informativi assegnati durante il loro ciclo di vita; classificare le informazioni per A.5.12; rivedere i record dell'inventario almeno annualmente; approvare l'accesso alle informazioni di proprietà; partecipare alle decisioni di conservazione e dismissione per A.8.10.

**Custodi degli asset**: Eseguire le attività operative delegate dal proprietario dell'asset; mantenere la disponibilità e l'integrità dell'asset; aggiornare i record dell'inventario per i cambiamenti di routine. *Distinzione*: I custodi hanno la responsabilità operativa ma la responsabilità rimane con il proprietario.

**Tutto il personale**: Segnalare immediatamente gli asset smarriti, rubati o danneggiati; rispettare le politiche di utilizzo accettabile; notificare le Operazioni IT dei cambiamenti degli asset; restituire gli asset alla partenza o al cambio di ruolo; partecipare alla verifica periodica degli asset quando richiesto.

**Audit interno / Conformità**: Condurre audit indipendenti dell'inventario; verificare la conformità ai requisiti della politica; testare l'efficacia dei controlli; riferire i risultati alla Direzione generale e al RSSI.

## Matrice RACI

| Attività | Dir. Gen. | RSSI | Resp. Sic. | Op. IT | Prop. App. | Prop. Info. | Custodi | Utenti | Audit |
|----------|-----------|------|------------|--------|------------|-------------|---------|--------|-------|
| Approvazione politica | A | R | C | I | I | I | I | I | C |
| Progettazione quadro | I | A | R | C | C | C | I | I | C |
| Identificazione asset | I | I | C | R | R | R | C | I | I |
| Assegnazione proprietario | I | A | C | C | C | R | I | I | I |
| Creazione record | I | I | C | R | R | C | C | I | I |
| Manutenzione record | I | I | C | R | R | R | R | I | I |
| Revisione accuratezza | I | I | C | C | R | R | C | I | I |
| Valutazione conformità | I | A | R | C | C | C | I | I | C |
| Rimedio lacune | C | A | R | R | R | R | C | I | I |
| Reportistica | I | A | R | C | C | I | I | I | C |
| Audit indipendente | I | I | C | I | I | I | I | I | A/R |
| Approvazione eccezioni | A | R | C | I | C | C | I | I | C |

**Legenda**: R = Responsabile, A = Accountable, C = Consultato, I = Informato

## Valutazione e verifica

**Requisito A.5.9-R7**: [Organizzazione] DEVE condurre valutazioni periodiche per verificare la conformità dell'inventario.

**Quadro di valutazione** (5 domini):

| Dominio di valutazione | ID documento | Focus della valutazione | Frequenza |
|-----------------------|-------------|------------------------|-----------|
| **Identificazione e scoperta degli asset** | ISMS-IMP-A.5.9-1 | Procedure di scoperta, completezza | Trimestrale |
| **Manutenzione dell'inventario** | ISMS-IMP-A.5.9-2 | Struttura, procedure di aggiornamento, integrazione | Trimestrale |
| **Qualità e conformità** | ISMS-IMP-A.5.9-3 | Accuratezza, completezza, verifica dell'aggiornamento | Trimestrale |
| **Responsabilità del proprietario** | ISMS-IMP-A.5.9-4 | Assegnazione del proprietario, riconoscimento, formazione | Trimestrale |

**Metriche di conformità**:

| Metrica | Obiettivo | Metodo di misurazione | Frequenza di reportistica |
|---------|-----------|----------------------|--------------------------|
| **Completezza** | ≥95% critici, ≥90% standard | Riconciliazione scoperta | Trimestrale |
| **Accuratezza** | ≥95% informazioni, ≥98% infrastruttura IT | Campionamento statistico | Trimestrale |
| **Aggiornamento** | ≥98% entro le soglie di obsolescenza | Analisi delle date di revisione | Mensile |
| **Assegnazione del proprietario** | 100% | Verifica campo proprietario nullo | Mensile |
| **Riconoscimento del proprietario** | ≥95% entro 30 giorni | Monitoraggio dei riconoscimenti | Mensile |
| **Conformità al calendario di revisione** | ≥90% revisioni nei tempi | Aderenza al calendario | Trimestrale |

## Gestione delle eccezioni

**Requisito A.5.9-R8**: [Organizzazione] DEVE stabilire un processo formale di eccezione per le deviazioni dai requisiti dell'inventario.

**Categorie di eccezioni**: Eccezione di granularità; Eccezione di frequenza di revisione; Eccezione di proprietà; Eccezione tecnica.

**Processo di richiesta di eccezione**:
1. Il richiedente presenta la richiesta di eccezione con giustificazione aziendale
2. Il Responsabile della Sicurezza delle Informazioni effettua la valutazione del rischio
3. Il RSSI approva/rifiuta l'eccezione
4. Le eccezioni approvate sono documentate con: giustificazione e valutazione del rischio; controlli compensativi; data di scadenza dell'eccezione (massimo 12 mesi); criteri di rivalutazione
5. Le eccezioni vengono riviste durante le valutazioni periodiche
6. Il registro delle eccezioni è mantenuto come prova

**Autorità di eccezione**:

- **Responsabile della Sicurezza delle Informazioni**: Approvare le eccezioni temporanee ≤30 giorni
- **RSSI**: Approvare le eccezioni ≤12 mesi
- **Direzione generale**: Approvare le eccezioni >12 mesi (rare, documentate)

**Durata massima dell'eccezione**: 12 mesi (deve essere rinnovata o rimediata)

## Risposta agli incidenti

**Requisito A.5.9-R9**: [Organizzazione] DEVE utilizzare l'inventario degli asset per supportare i processi di risposta agli incidenti.

**L'inventario nella risposta agli incidenti**: Identificazione rapida degli asset interessati e delle dipendenze; notifica ai proprietari degli asset per la valutazione dell'impatto aziendale; determinazione della criticità e dell'impatto aziendale; isolamento dei sistemi interessati; prioritizzazione del ripristino basata sulla classificazione della criticità degli asset; analisi delle cause profonde.

**Azioni di inventario attivate dall'incidente**: Verificare che i record degli asset interessati siano aggiornati; aggiornare lo stato dell'asset se danneggiato o compromesso; documentare l'incidente nella cronologia dell'asset; rivedere e aggiornare la classificazione del rischio se necessario; condurre la validazione post-incidente dell'inventario.

## Governance della politica

**Frequenza di revisione**: Annuale minima, o attivata da: cambiamenti organizzativi significativi; principali cambiamenti normativi; risultati di audit; identificazione di lacune nella politica; cambiamenti tecnologici.

**Autorità di approvazione**: Direzione generale (AD o autorità designata)

**Controllo delle versioni**: Tutte le versioni della politica conservate per la pista di audit (conservazione minima 7 anni)

---

# Implementazione e riferimenti

## Integrazione con il SGSI

**Valutazione del rischio** (Clausola 6.1 ISO 27001): L'inventario degli asset fornisce la base per l'identificazione dei rischi; la criticità degli asset influenza la valutazione e la prioritizzazione del trattamento del rischio; l'analisi minaccia-asset-vulnerabilità richiede un inventario completo degli asset.

**Dichiarazione di Applicabilità** (Clausola 6.1.3): L'applicabilità del Controllo A.5.9 è giustificata nella DdA di [Organizzazione].

**Controlli correlati**:

| Controllo | Relazione | Punto di integrazione |
|-----------|----------|-----------------------|
| **A.5.10 (Utilizzo accettabile)** | Definisce l'utilizzo accettabile degli asset inventariati | I record dell'asset fanno riferimento alla politica di utilizzo accettabile |
| **A.5.11 (Restituzione degli asset)** | Restituzione degli asset monitorata nell'inventario | Stato aggiornato alla restituzione/dismissione |
| **A.5.12 (Classificazione)** | Classificazione applicata agli asset informativi | Campo classificazione nell'inventario |
| **A.5.13 (Etichettatura)** | Etichette applicate per la classificazione dell'inventario | La generazione delle etichette utilizza i dati dell'inventario |
| **A.5.14 (Trasferimento delle informazioni)** | Controlli di trasferimento basati sulla classificazione degli asset | I log di trasferimento fanno riferimento all'inventario degli asset |
| **A.5.15 (Controllo degli accessi)** | Le regole di accesso proteggono gli asset inventariati | Politiche di controllo degli accessi basate sugli asset |
| **A.5.18 (Diritti di accesso)** | I proprietari degli asset approvano i diritti di accesso | La proprietà nell'inventario abilita il flusso di lavoro di approvazione |
| **A.8.9 (Gestione della configurazione)** | Riferimenti di configurazione per l'infrastruttura IT | Riferimento di base nell'inventario |
| **A.8.10 (Cancellazione delle informazioni)** | La dismissione aggiorna lo stato dell'inventario | La dismissione attiva l'aggiornamento dell'inventario |

## Risorse di implementazione

| ID documento | Titolo | Scopo | Pubblico destinatario |
|-------------|--------|-------|----------------------|
| **ISMS-IMP-A.5.9-1-UG/TG** | Identificazione e scoperta degli asset | Procedure per l'identificazione degli asset, metodi di scoperta, verifica della completezza | Team di sicurezza, Operazioni IT |
| **ISMS-IMP-A.5.9-2-UG/TG** | Manutenzione dell'inventario | Progettazione della struttura dell'inventario, procedure di aggiornamento, metodi di integrazione | Team di sicurezza, Operazioni IT, Proprietari dei sistemi |
| **ISMS-IMP-A.5.9-3-UG/TG** | Valutazione di qualità e conformità | Campionamento dell'accuratezza, verifica dell'aggiornamento, analisi delle lacune | Team di sicurezza, Audit, Conformità |
| **ISMS-IMP-A.5.9-4-UG/TG** | Valutazione della responsabilità del proprietario | Assegnazione del proprietario, monitoraggio dei riconoscimenti, verifica delle responsabilità | Team di sicurezza, Direzione, Proprietari degli asset |

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Asset** | Qualsiasi cosa abbia valore per [Organizzazione] e richieda protezione. Comprende informazioni, infrastruttura IT, applicazioni, risorse fisiche e competenze del personale |
| **Asset informativo** | Dati, contenuti o conoscenze in qualsiasi forma con requisiti di riservatezza, integrità o disponibilità |
| **Asset associato** | Infrastruttura, applicazioni, strutture o personale che elabora, archivia, trasmette o protegge gli asset informativi |
| **Proprietario dell'asset** | Individuo responsabile di un asset durante tutto il suo ciclo di vita. Il proprietario è responsabile della classificazione, dell'approvazione dell'accesso, delle decisioni di protezione e della conformità ai requisiti di sicurezza |
| **Custode dell'asset** | Individuo o team con responsabilità operativa quotidiana per un asset. Il custode implementa i controlli di sicurezza come indicato dal proprietario, ma la responsabilità rimane con il proprietario |
| **Inventario degli asset** | Registro strutturato delle informazioni e degli asset associati, che documenta gli attributi obbligatori inclusi il proprietario, la classificazione, l'ubicazione e lo stato del ciclo di vita |
| **Completezza dell'inventario** | Grado in cui l'inventario include tutti gli asset nel perimetro. Misurato come percentuale degli asset individuabili presenti nell'inventario |
| **Accuratezza dell'inventario** | Grado in cui i dati dell'inventario riflettono correttamente lo stato effettivo dell'asset. Misurato attraverso campionamento e validazione |
| **Aggiornamento dell'inventario** | Grado in cui l'inventario riflette lo stato corrente piuttosto che lo stato storico. Misurato tramite le date di revisione e la tempestività degli aggiornamenti |
| **Criticità** | Valutazione dell'impatto aziendale qualora un asset diventasse non disponibile, compromesso o distrutto |
| **Stato del ciclo di vita** | Fase corrente nel ciclo di vita dell'asset (attivo, sviluppo, manutenzione, ritirato, archiviato) |
| **Scoperta** | Processo automatizzato o manuale per identificare gli asset nell'ambiente organizzativo |
| **CMDB** | Configuration Management Database — sistema organizzativo che documenta le configurazioni dell'infrastruttura IT |
| **Asset del personale** | Ruoli organizzativi chiave e competenze specializzate (non record individuali delle persone). Documentati in modo generico per proteggere la privacy |
| **Granularità** | Livello di dettaglio a cui vengono inventariati gli asset. Gli asset ad alto rischio richiedono record individuali; gli asset a basso rischio possono essere raggruppati |

---

# Prove per questa politica

**Prove per la Fase 1**: Documento di politica con firme di approvazione; requisiti di creazione dell'inventario definiti; quadro di categorizzazione degli asset documentato; attributi obbligatori dell'inventario specificati; requisiti di proprietà degli asset definiti; standard di qualità dell'inventario stabiliti (completezza, accuratezza, aggiornamento); requisiti di integrazione con altri controlli SGSI documentati; ruoli e responsabilità assegnati; procedure di governance e revisione definiti.

**Prove per la Fase 2**: Valutazioni di identificazione e scoperta degli asset per ISMS-IMP-A.5.9-1; valutazioni di manutenzione dell'inventario per ISMS-IMP-A.5.9-2; valutazioni di qualità e conformità per ISMS-IMP-A.5.9-3; valutazioni della responsabilità del proprietario per ISMS-IMP-A.5.9-4; record dell'inventario degli asset (tutti i tipi: informativi, infrastruttura IT, applicazioni, fisici, personale); determinazioni di categorizzazione degli asset; assegnazioni di proprietà degli asset con riconoscimenti dei proprietari (obiettivo: 100%); metriche di completezza dell'inventario; metriche di accuratezza dell'inventario; metriche di aggiornamento dell'inventario; prove di integrazione con altri controlli (controllo degli accessi, classificazione, gestione dei cambiamenti, gestione degli incidenti); documentazione del ciclo di vita degli asset.

---

# Allegato A: Matrice di decisione per la categorizzazione degli asset

## Categorizzazione primaria: Asset informativo vs. Asset associato

**Domanda di decisione**: Si tratta di INFORMAZIONI o di QUALCOSA CHE ELABORA/ARCHIVIA INFORMAZIONI?

**Asset informativi** (dati, contenuti, conoscenze): Dati strutturati; Documenti non strutturati; Documenti e archivi; Proprietà intellettuale; Configurazione e parametri; Autenticazione e crittografici; Registrazioni delle comunicazioni; Business intelligence.

**Asset associati** (sistema, dispositivo, struttura, persona): Infrastruttura IT; Applicazioni; Asset fisici; Asset del personale.

## Quadro di valutazione della criticità

**Domande sull'impatto aziendale** (determina la criticità):

| Area di impatto | Critico | Alto | Medio | Basso |
|----------------|---------|------|-------|-------|
| **Operativo** | Completa interruzione del business | Grave fallimento del processo | Degradazione del processo | Inconveniente minore |
| **Finanziario** | >5% del fatturato annuo | 1-5% del fatturato annuo | <1% del fatturato annuo | Trascurabile |
| **Normativo** | Segnalazione obbligatoria, sanzioni | Violazione della conformità | Violazione minore | Nessun impatto |
| **Reputazionale** | Media nazionale, esodo clienti | Stampa di settore, perdita clienti | Stampa locale, reclami | Nessuna visibilità |
| **Tempo di ripristino** | Non può essere sostituito | >1 mese per sostituire | 1 settimana-1 mese | <1 settimana |

**Assegnazione della criticità**: Utilizzare l'area di impatto più alta per la classificazione complessiva della criticità.

## Quadro di decisione sulla granularità

**Alta granularità** (record individuali) quando: l'asset è critico per le operazioni; l'asset elabora informazioni sensibili (classificazione Alta/Molto Alta per A.5.12); i requisiti normativi richiedono il tracciamento individuale; l'asset è unico o specializzato.

**Bassa granularità** (record raggruppati) quando: gli asset sono commodity/standardizzati; gli asset sono a basso rischio e facilmente sostituibili; il tracciamento individuale crea un onere di manutenzione eccessivo; gli asset sono omogenei.

**Esempi**:

| Tipo di asset | Granularità | Motivazione |
|--------------|-------------|-------------|
| Server di database in produzione | Individuale | Critico, unico, elabora dati sensibili |
| Laptop standard per dipendenti (modello identico) | Raggruppato (quantità: 100) | Commodity, standardizzato, basso rischio individuale |
| Database DCP dei clienti | Individuale | Requisito normativo, alta sensibilità |
| Repository del codice sorgente | Individuale | Proprietà intellettuale, controllo delle versioni necessario |
| Account amministratore di dominio | Individuale | Alto privilegio, deve essere tracciato con precisione |
| Nastri di backup | Raggruppato per set di rotazione | Tracciato per set, non singolo nastro |

---

# Allegato B: Guida di riferimento rapido per i proprietari degli asset

## Il vostro ruolo come proprietario dell'asset

**Siete responsabili** delle informazioni o degli asset associati assegnati alla vostra proprietà. Questa guida di riferimento rapido riassume le vostre responsabilità.

## Errori comuni da evitare

1. **Confondere «Proprietario» con «Custode»**: Siete responsabili anche se l'IT gestisce il sistema. Proprietario = responsabilità aziendale, Custode = gestione operativa.
2. **Classificare tutti gli asset come «Critici»**: Utilizzare il quadro dell'impatto aziendale (Allegato A). Non tutto è critico — questo ne diluisce il significato.
3. **Elencare persone individuali come asset del personale**: Documentare ruoli/competenze, non nomi. «Competenza di Amministratore di Database (3 personale qualificato)» NON «Mario Rossi — DBA».
4. **Dimenticare di aggiornare l'inventario quando gli asset cambiano**: Impostare promemoria sul calendario per gli asset di proprietà.
5. **Presumere che qualcun altro aggiornerà**: Come Proprietario, siete responsabili dell'accuratezza del record anche se il Custode esegue gli aggiornamenti.

## Responsabilità principali

**1. Classificare i propri asset** (per ISMS-POL-A.5.12 se implementata): Determinare i requisiti di riservatezza, integrità, disponibilità; considerare l'impatto aziendale se l'asset viene compromesso; documentare la classificazione nell'inventario.

**2. Rivedere i record dell'inventario**: Frequenza: almeno annualmente, o dopo cambiamenti significativi; Verificare: descrizione, ubicazione, classificazione, dipendenze accurate; Aggiornare: inviare aggiornamenti se le informazioni cambiano; Attestare: confermare l'accuratezza firmando il record di revisione.

**3. Approvare le richieste di accesso**: Rivedere le richieste di accesso per gli asset di proprietà; verificare la necessità aziendale e i privilegi appropriati; approvare/rifiutare in base al principio del minimo privilegio; documentare la motivazione dell'approvazione.

**4. Segnalare gli incidenti di sicurezza**: Segnalare immediatamente gli incidenti che interessano gli asset di proprietà; partecipare all'indagine sugli incidenti; approvare le procedure di ripristino e recupero.

**5. Gestire il ciclo di vita dell'asset**: Partecipare alle decisioni di conservazione, archiviazione, dismissione; garantire la corretta dismissione per ISMS-POL-A.8.10; aggiornare l'inventario quando gli asset vengono ritirati o archiviati; trasferire la proprietà quando si cambia ruolo.

## Lista di controllo per la revisione annuale

- [ ] Verificare che la descrizione dell'asset sia accurata
- [ ] Confermare che l'ubicazione fisica/logica sia corretta
- [ ] Convalidare che la classificazione della criticità sia ancora appropriata
- [ ] Verificare che le dipendenze siano documentate
- [ ] Assicurarsi che l'assegnazione del custode sia aggiornata
- [ ] Confermare che la classificazione sia appropriata (per A.5.12)
- [ ] Firmare il modulo di attestazione
- [ ] Inviare al Responsabile della Sicurezza delle Informazioni

## Transizione del proprietario (cambio di ruolo)

- [ ] Generare l'elenco degli asset di proprietà
- [ ] Identificare i nuovi proprietari (con approvazione del responsabile)
- [ ] Documentare la transizione nella gestione dei cambiamenti
- [ ] Condurre la riunione di handover con il nuovo proprietario
- [ ] Aggiornare l'inventario con il nuovo proprietario
- [ ] Confermare il riconoscimento del nuovo proprietario

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data] |
| **Direttore dei Sistemi Informativi (DSI)** | [Nome] | [Data] |
| **Responsabile Legale/Conformità** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per l'inventario delle informazioni e degli asset associati. Le procedure di attuazione sono documentate in ISMS-IMP-A.5.9-1–4 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
