<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.12-13-IT:framework:POL:a.5.12-13 -->
**ISMS-POL-A.5.12-13 — Classificazione ed etichettatura delle informazioni**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Classificazione ed etichettatura delle informazioni |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.12-13 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data da definire] | RSSI | Politica iniziale per la certificazione ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Responsabile della Protezione dei Dati (RPD)
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.5.9 (Inventario delle informazioni e degli asset)
- ISMS-POL-A.5.14 (Trasferimento delle informazioni)
- ISMS-POL-A.5.34 (Riservatezza e protezione dei DCP)
- ISMS-POL-A.8.10 (Cancellazione delle informazioni)
- ISMS-POL-A.8.12 (Prevenzione della perdita di dati)
- ISMS-IMP-A.5.12-13.S1-UG/TG (Definizione del sistema di classificazione)
- ISMS-IMP-A.5.12-13.S2-UG/TG (Procedure ed standard di etichettatura)
- ISMS-IMP-A.5.12-13.S3-UG/TG (Inventario della classificazione degli asset)
- ISO/IEC 27001:2022 Controlli A.5.12, A.5.13

---

## Riepilogo esecutivo

Questa politica stabilisce il sistema di classificazione delle informazioni e i requisiti di etichettatura di [Organizzazione] per garantire che le informazioni ricevano un livello appropriato di protezione in base alla loro sensibilità, al loro valore e ai requisiti legali.

**Perimetro**: Questa politica si applica a tutte le informazioni create, ricevute, elaborate, archiviate o trasmesse da [Organizzazione], indipendentemente dal formato (elettronico, fisico, verbale).

**Scopo**: Definire i requisiti organizzativi per la classificazione e l'etichettatura delle informazioni. Questa politica stabilisce QUALI livelli di classificazione si applicano e CHI è responsabile. Le procedure di attuazione (COME) sono documentate separatamente in ISMS-IMP-A.5.12-13 (varianti UG/TG).

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; FINMA, segreto bancario svizzero (applicabilità condizionale per ISMS-POL-00).

---

# Allineamento sui controlli e perimetro

## Controlli ISO/IEC 27001:2022 A.5.12 e A.5.13

**ISO/IEC 27001:2022 Allegato A.5.12 — Classificazione delle informazioni**

> *Le informazioni devono essere classificate in base alle esigenze di sicurezza delle informazioni dell'organizzazione, basandosi sulla riservatezza, l'integrità, la disponibilità e i requisiti delle parti interessate rilevanti.*

**ISO/IEC 27001:2022 Allegato A.5.13 — Etichettatura delle informazioni**

> *Un insieme appropriato di procedure per l'etichettatura delle informazioni deve essere sviluppato e attuato conformemente al sistema di classificazione delle informazioni adottato dall'organizzazione.*

**Obiettivi dei controlli**:

- Stabilire una classificazione coerente per tutti i tipi di informazioni
- Consentire una gestione appropriata basata sulla sensibilità
- Soddisfare i requisiti normativi per la protezione dei dati
- Supportare le decisioni sul controllo degli accessi e sulla protezione dei dati

**Tipo di controllo**: Preventivo
**Categoria del controllo**: Organizzativo

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria**:

| Normativa | Applicabilità | Requisiti chiave |
|-----------|---------------|-----------------|
| **nLPD svizzera** | Tutto il trattamento dei dati personali | Misure tecniche e organizzative appropriate |
| **ISO/IEC 27001:2022** | Ambito di certificazione | Controlli A.5.12, A.5.13 — Classificazione ed etichettatura |

**Livello 2 — Applicabilità condizionale**:

| Normativa | Condizione scatenante | Requisiti di classificazione |
|-----------|----------------------|------------------------------|
| **RGPD dell'UE Art. 32** | Elaborazione di dati personali UE | Sicurezza appropriata alla sensibilità dei dati personali |
| **FINMA** | Istituto finanziario svizzero regolamentato | Requisiti di classificazione dei dati dei clienti |
| **Segreto bancario svizzero** | Dati dei clienti bancari | Classificazione di riservatezza rigorosa |
| **Contratti governativi** | Lavoro nel settore pubblico | Possono richiedere livelli di classificazione aggiuntivi |

**Livello 3 — Riferimento informativo**: ISO 27002:2022; NIST SP 800-53 (Categorizzazione della sicurezza); CIS Controls v8.1 (Classificazione e protezione dei dati); sistemi di classificazione governativi (per riferimento nel lavoro nel settore pubblico).

---

# Enunciati di politica

## Sistema di classificazione

### Livelli di classificazione

[Organizzazione] adotta un sistema di classificazione a quattro livelli:

| Livello | Etichetta | Descrizione | Esempi |
|---------|-----------|-------------|--------|
| **Pubblico** | PUBBLICO | Informazioni approvate per la divulgazione non limitata | Materiali di marketing, comunicati stampa, contenuti del sito web pubblico |
| **Interno** | INTERNO | Informazioni per uso interno solo, non per distribuzione esterna | Procedure interne, organigrammi, comunicazioni aziendali generali |
| **Riservato** | RISERVATO | Informazioni sensibili che richiedono protezione, distribuzione limitata | Dati dei clienti, contratti, report finanziari, documenti HR |
| **Limitato** | LIMITATO | Informazioni altamente sensibili, controllo degli accessi rigoroso | Segreti commerciali, dati M&A, configurazioni di sicurezza, chiavi crittografiche |

### Criteri di classificazione

Le informazioni DEVONO essere classificate in base a:

**Impatto sulla riservatezza** (se divulgate):

| Livello di impatto | Criteri | Classificazione minima |
|-------------------|---------|------------------------|
| Nessuno | Nessun impatto negativo | Pubblico |
| Basso | Inconveniente minore | Interno |
| Moderato | Danno significativo alle operazioni o alla reputazione | Riservato |
| Alto | Danno grave, sanzioni normative, minaccia esistenziale | Limitato |

**Requisiti normativi**:

| Tipo di dati | Classificazione minima |
|--------------|------------------------|
| Dati personali (non sensibili) | Riservato |
| Categorie speciali di dati personali | Limitato |
| Documenti finanziari (clienti) | Riservato |
| Informazioni sanitarie | Limitato |
| Materiali crittografici | Limitato |

**Requisiti di integrità e disponibilità**:

- Informazioni che richiedono alta integrità (finanziarie, legali) → minimo Riservato
- Informazioni che richiedono alta disponibilità (operazioni critiche) → considerare misure di protezione della disponibilità

### Classificazione predefinita

- **Informazioni non classificate**: Trattate come INTERNO fino alla classificazione formale
- **Informazioni esterne**: Classificate alla ricezione in base al contenuto e alla classificazione del mittente
- **Informazioni aggregate**: Classificate al livello più alto dei dati componenti

Dove il sistema di classificazione di una parte esterna differisce dal sistema a quattro livelli di [Organizzazione], il Proprietario delle informazioni DEVE mapparlo al livello di classificazione [Organizzazione] più vicino superiore e documentare la mappatura.

## Responsabilità di classificazione

### Proprietari delle informazioni

I Proprietari delle informazioni DEVONO:

- Classificare le informazioni alla creazione o alla ricezione
- Rivedere la classificazione quando il contenuto delle informazioni cambia
- Autorizzare l'accesso appropriato al livello di classificazione
- Garantire che i subordinati comprendano le responsabilità di classificazione
- Rivedere e aggiornare la classificazione annualmente o in seguito a un evento scatenante

### Autorità di classificazione

| Livello di classificazione | Chi può classificare | Chi può declassificare |
|---------------------------|---------------------|------------------------|
| Pubblico | Proprietario delle informazioni | Proprietario delle informazioni |
| Interno | Proprietario delle informazioni | Proprietario delle informazioni |
| Riservato | Proprietario delle informazioni, Responsabile di dipartimento | Proprietario delle informazioni, Responsabile di dipartimento |
| Limitato | Responsabile di dipartimento, Direzione generale | Solo Direzione generale |

### Riclassificazione

Le informazioni DEVONO essere riclassificate quando:

- Il valore o la sensibilità aziendale cambia
- I requisiti legali/normativi cambiano
- Si applica una declassificazione basata sul tempo (es. dopo un annuncio pubblico)
- Il Proprietario delle informazioni determina una classificazione diversa appropriata

**Processo di declassificazione**:

- Documentare il motivo della declassificazione
- Ottenere l'approvazione richiesta per autorità di classificazione
- Aggiornare le etichette su tutte le istanze
- Notificare i destinatari delle informazioni riclassificate

Le decisioni di classificazione e declassificazione per le informazioni LIMITATE DEVONO essere registrate (proprietario, approvatore, data, motivazione, ubicazioni interessate) nel Registro delle prove o nel sistema di flusso di lavoro designato.

## Requisiti di etichettatura

### Etichettatura obbligatoria

Tutte le informazioni classificate RISERVATO o LIMITATO DEVONO essere chiaramente etichettate.

**Documenti elettronici**:

- Intestazione e/o piè di pagina su ogni pagina: «RISERVATO» o «LIMITATO»
- Proprietà/metadati del documento inclusa la classificazione
- Prefisso dell'oggetto dell'email per le email sensibili: [RISERVATO] o [LIMITATO]
- Convenzione di denominazione dei file per includere la classificazione dove pratico

**Documenti fisici**:

- Etichetta di classificazione sulla pagina di copertina
- Marcatura della classificazione su ogni pagina (intestazione o piè di pagina)
- Contenitori sigillati etichettati con la classificazione più alta del contenuto
- Scatole di archivio contrassegnate con il livello di classificazione

**Altri formati**:

| Formato | Metodo di etichettatura |
|---------|------------------------|
| Supporti rimovibili | Etichetta fisica + cifratura con metadati di classificazione |
| Database | Campo di classificazione per record o designazione a livello di tabella |
| Comunicazioni verbali | Dichiarazione verbale della classificazione prima della discussione |
| Presentazioni | Classificazione sulla diapositiva del titolo e su ogni diapositiva successiva |

### Eccezioni all'etichettatura

Informazioni PUBBLICHE e INTERNE:

- Etichettatura raccomandata ma non obbligatoria
- Le informazioni non etichettate vengono trattate come INTERNO solo all'interno dei sistemi interni approvati con controlli degli accessi
- Qualsiasi informazione condivisa esternamente o archiviata in repository di collaborazione condivisi DEVE avere una classificazione esplicita applicata quando RISERVATO o LIMITATO
- I contenuti sensibili non etichettati rilevati dal monitoraggio DLP o da scansioni periodiche DEVONO essere trattati come una non conformità o registrati come eccezione con controlli compensativi

### Etichettatura automatizzata

Dove tecnicamente fattibile, [Organizzazione] DEVE implementare:

- Auto-classificazione basata su modelli di contenuto (regole DLP)
- Ereditarietà della classificazione dalle cartelle/sistemi parent
- Prompt di classificazione obbligatori prima del salvataggio/invio
- Integrazione con Microsoft Information Protection o equivalente

## Requisiti di gestione

### Matrice di gestione per classificazione

| Requisito | PUBBLICO | INTERNO | RISERVATO | LIMITATO |
|-----------|---------|---------|-----------|---------|
| **Archiviazione** | Qualsiasi | Sistemi aziendali | Storage cifrato | Cifrato, accessi registrati |
| **Trasmissione** | Qualsiasi | Email aziendale | Cifrata | Cifrata, canale sicuro |
| **Stampa** | Illimitata | Standard | Coda di stampa sicura | Solo stampante autorizzata |
| **Smaltimento** | Standard | Tritatura (P-3) | Tritatura incrociata (P-4) | Incrociata (P-5) + testimone |
| **Accesso** | Chiunque | Dipendenti | Need-to-know | Individui nominati |
| **Copia** | Illimitata | Consentita | Approvazione del proprietario | Non consentita (eccezioni richiedono DG) |
| **Condivisione esterna** | Consentita | Non senza approvazione | NDA richiesto | Vietata (eccezioni richiedono DG) |

### Sicurezza fisica

| Classificazione | Controllo fisico |
|----------------|-----------------|
| Pubblico | Nessun requisito speciale |
| Interno | Locali protetti |
| Riservato | Archiviazione chiusa quando incustodito |
| Limitato | Contenitore sicuro (cassaforte), log degli accessi |

### Sicurezza digitale

| Classificazione | Controllo tecnico |
|----------------|------------------|
| Pubblico | Backup standard |
| Interno | Controllo degli accessi, backup |
| Riservato | Cifratura a riposo, controllo degli accessi, registrazione degli audit |
| Limitato | Cifratura avanzata, accesso con AMF, audit completo, DLP |

I requisiti di cifratura e registrazione DEVONO soddisfare gli standard minimi definiti in ISMS-POL-A.8.24 (crittografia) e ISMS-POL-A.8.15/A.8.16 (registrazione/monitoraggio). Per le informazioni RISERVATE e LIMITATE, la cifratura a riposo DEVE essere verificabile tramite report sullo stato della cifratura della piattaforma o riferimenti di configurazione. I log degli accessi DEVONO essere inoltrati alla piattaforma di registrazione centralizzata con conservazione per ISMS-POL-A.8.15 e prove di revisione trimestrale.

---

# Ruoli e responsabilità

## Matrice delle responsabilità

| Ruolo | Responsabilità di classificazione |
|-------|----------------------------------|
| **Direzione generale** | Approvare il sistema di classificazione; autorizzare la declassificazione delle informazioni Limitate |
| **RSSI** | Definire i requisiti di classificazione; monitorare la conformità; gestire gli strumenti di etichettatura |
| **RPD** | Garantire che la classificazione dei dati personali soddisfi i requisiti normativi |
| **Proprietari delle informazioni** | Classificare ed etichettare le informazioni; autorizzare l'accesso; rivedere le classificazioni |
| **Responsabili di dipartimento** | Garantire la conformità del dipartimento; autorità di classificazione Riservato/Limitato |
| **Tutto il personale** | Gestire le informazioni per classificazione; segnalare le informazioni classificate in modo errato |

## Percorso di escalation

- Controversie sulla classificazione: Proprietario delle informazioni → Responsabile di dipartimento → RSSI
- Classificazione incerta: Classificare al livello superiore, richiedere chiarimenti al RSSI
- Presunta classificazione errata: Segnalare al Proprietario delle informazioni e al RSSI

---

# Governance e conformità

## Quadro di valutazione

| Valutazione | Frequenza | Responsabile | Prove |
|------------|-----------|-------------|-------|
| Audit di conformità alla classificazione | Annuale | Audit interno | Report di audit |
| Revisione dell'efficacia degli strumenti di etichettatura | Trimestrale | RSSI | Report degli strumenti |
| Revisione del sistema di classificazione | Annuale | RSSI | Documentazione del sistema |
| Completamento della formazione dei Proprietari delle informazioni | Annuale | HR | Documenti di formazione |

**Metriche di governance**:

- Asset informativi con classificazione assegnata (obiettivo: ≥95% classificati con eccezioni documentate; 100% per i sistemi nell'ambito di certificazione)
- Conformità all'etichettatura per Riservato/Limitato (obiettivo: ≥95%, le eccezioni devono essere a tempo limitato con controlli compensativi)
- Risultati di audit sulla classificazione (obiettivo: tendenza decrescente trimestre su trimestre)
- Tasso di completamento della formazione (obiettivo: 100%)

## Revisione della politica

- **Frequenza**: Annuale come minimo
- **Trigger**: Cambiamenti normativi, cambiamenti del modello di business, risultati di audit
- **Revisori**: RSSI, RPD, Consulente legale, Responsabili di dipartimento
- **Approvazione**: Direzione generale

## Gestione delle eccezioni

**Eccezioni all'etichettatura**: Sistemi legacy dove l'etichettatura non è tecnicamente fattibile: documentare nel registro delle eccezioni, implementare controlli compensativi; dati automatizzati ad alto volume: regole di classificazione applicate a livello di sistema/dataset.

**Eccezioni alla gestione**: Le situazioni di emergenza possono consentire una deviazione con documentazione immediata e revisione post-evento; richiede l'approvazione del RSSI e controlli compensativi.

Tutte le eccezioni DEVONO essere registrate nel Registro delle eccezioni (ISMS-REG-EXCEPTIONS).

## Collegamento all'azione correttiva

Le non conformità relative a questa politica (es. etichette mancanti, informazioni classificate in modo errato, violazioni della gestione) DEVONO essere registrate e gestite attraverso il processo di azione correttiva SGSI (Clausola 10.2) con analisi delle cause profonde e rimedio monitorato.

---

# Implementazione e riferimenti

## Integrazione con il SGSI

**Valutazione del rischio** (Clausola 6.1): I livelli di classificazione allineati con la valutazione del rischio e l'analisi dell'impatto di [Organizzazione]; i requisiti di gestione determinati dagli impatti sulla riservatezza, l'integrità e la disponibilità.

**Dichiarazione di Applicabilità** (Clausola 6.1.3): L'applicabilità dei Controlli A.5.12 e A.5.13 è giustificata nella DdA di [Organizzazione].

**Controlli correlati**:

| Controllo | Punto di integrazione |
|-----------|----------------------|
| **A.5.9** | Inventario delle informazioni e degli asset — Gli asset sono classificati secondo questo sistema |
| **A.5.14** | Trasferimento delle informazioni — I metodi di trasferimento determinati dalla classificazione |
| **A.5.34** | Privacy e DCP — Requisiti di classificazione dei dati personali |
| **A.8.10** | Cancellazione delle informazioni — Metodi di cancellazione per livello di classificazione |
| **A.8.12** | Prevenzione della perdita di dati — Le regole DLP applicano i confini della classificazione |
| **A.8.24** | Utilizzo della crittografia — Requisiti di cifratura per classificazione |

**Flussi di dati bidirezionali**: Le decisioni di classificazione informano il controllo degli accessi (A.5.15), le etichette DLP (A.8.12) e i metodi di trasferimento (A.5.14). L'inventario degli asset (A.5.9), gli insegnamenti tratti dagli incidenti e i cambiamenti normativi alimentano le revisioni della classificazione.

## Risorse di implementazione

| ID documento | Titolo | Scopo |
|-------------|--------|-------|
| **ISMS-IMP-A.5.12-13-UG/TG** | Guida all'implementazione della classificazione e dell'etichettatura | Procedure dettagliate, modelli e strumenti |

---

# Prove per questa politica

**Prove per la Fase 1**: Documento di politica con firme di approvazione; sistema di classificazione con definizioni dei livelli documentato; requisiti di etichettatura specificati; requisiti di gestione per livello di classificazione definiti; responsabilità del Proprietario delle informazioni documentate; ruoli e responsabilità assegnati.

**Prove per la Fase 2**: Documenti classificati campione con etichette appropriate; report degli strumenti di classificazione (es. Microsoft Information Protection); inventario degli asset informativi con assegnazioni di classificazione; documenti di formazione per le responsabilità di classificazione; report di audit sulla conformità alla classificazione; documenti di riclassificazione/declassificazione; registro delle eccezioni per eccezioni all'etichettatura/gestione; report sugli incidenti che coinvolgono informazioni classificate in modo errato (se presenti).

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Classificazione** | Il processo di categorizzazione delle informazioni in base alla loro sensibilità e al potenziale impatto della divulgazione, modifica o indisponibilità non autorizzata |
| **Etichettatura** | L'applicazione di marcatori visibili o di metadati alle informazioni che indicano il loro livello di classificazione |
| **Proprietario delle informazioni** | L'individuo o il ruolo responsabile della classificazione, della gestione e della protezione di specifici asset informativi |
| **Need-to-know** | Un principio che limita l'accesso alle informazioni a coloro che ne hanno bisogno per svolgere le proprie funzioni lavorative |
| **Declassificazione** | La riduzione di un livello di classificazione quando le informazioni non richiedono più il livello superiore di protezione |
| **Aggregazione** | La combinazione di più informazioni che, insieme, possono richiedere una classificazione più alta rispetto ai singoli componenti |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Responsabile della Protezione dei Dati (RPD)** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la classificazione e l'etichettatura delle informazioni. Le procedure di attuazione sono documentate in ISMS-IMP-A.5.12-13 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
