<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.32-33-IT:framework:POL:a.5.32-33 -->
**ISMS-POL-A.5.32-33 — Protezione della proprietà intellettuale e dei documenti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Protezione della proprietà intellettuale e dei documenti |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.32-33 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Consulente legale
- Integrazione: Responsabile della Protezione dei Dati (RPD)
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.5.12-13 (Classificazione ed etichettatura delle informazioni)
- ISMS-POL-A.5.34 (Riservatezza e protezione dei DCP)
- ISMS-POL-A.8.10 (Cancellazione delle informazioni)
- ISMS-POL-A.8.12 (Prevenzione della perdita di dati)
- ISMS-IMP-A.5.32-33.S1-UG/TG (Inventario dei diritti di PI e valutazione della conformità)
- ISMS-IMP-A.5.32-33.S2-UG/TG (Valutazione della protezione dei documenti)
- ISMS-IMP-A.5.32-33.S3-UG/TG (Valutazione del calendario di conservazione e smaltimento)
- ISO/IEC 27001:2022 Controlli A.5.32, A.5.33

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la protezione della proprietà intellettuale, delle informazioni proprietarie e per garantire l'adeguata protezione dei documenti durante il loro ciclo di vita.

**Perimetro**: Questa politica si applica a tutta la proprietà intellettuale, le informazioni proprietarie, i segreti commerciali e i documenti creati, elaborati, archiviati o trasmessi da [Organizzazione], in formato sia fisico che elettronico.

**Allineamento normativo**: CO svizzero (Art. 958f); nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; FINMA, normative sanitarie (applicabilità condizionale per ISMS-POL-00).

---

# Allineamento sui controlli e perimetro

**ISO/IEC 27001:2022 Allegato A.5.32 — Diritti di proprietà intellettuale**

> *L'organizzazione deve implementare procedure appropriate per proteggere i diritti di proprietà intellettuale.*

**ISO/IEC 27001:2022 Allegato A.5.33 — Protezione dei documenti**

> *I documenti devono essere protetti da perdita, distruzione, falsificazione, accesso non autorizzato e divulgazione non autorizzata in conformità con i requisiti legislativi, normativi, contrattuali e aziendali.*

**Obiettivi dei controlli**: Garantire che la proprietà intellettuale sia identificata, protetta e legalmente conforme; garantire che i documenti siano conservati, protetti e disponibili per i periodi richiesti; prevenire la perdita, la falsificazione o l'accesso non autorizzato.

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria**:

| Normativa | Applicabilità | Requisiti chiave |
|-----------|---------------|-----------------|
| **CO svizzero Art. 958f** | Tutte le entità svizzere | Conservazione della contabilità (10 anni) |
| **nLPD svizzera** | Tutto il trattamento di dati personali | Misure di protezione appropriate |
| **ISO/IEC 27001:2022** | Ambito di certificazione | Controlli A.5.32, A.5.33 |

**Livello 2 — Applicabilità condizionale**: RGPD dell'UE; Legge sui brevetti svizzera; Legge sul diritto d'autore svizzera; FINMA; Autorità fiscali; Normative sanitarie.

---

# Enunciati di politica

## Protezione della proprietà intellettuale (A.5.32)

### Identificazione e classificazione della PI

[Organizzazione] DEVE identificare e classificare tutta la proprietà intellettuale:

**Categorie di PI**:

| Categoria | Esempi | Livello di protezione |
|-----------|--------|-----------------------|
| **Segreti commerciali** | Algoritmi, formule, processi, liste clienti | Limitato (massima protezione) |
| **Software proprietario** | Codice sorgente, strumenti di sviluppo, script | Minimo Riservato |
| **Metodi aziendali** | Processi unici, metodologie | Riservato |
| **Documentazione tecnica** | Architettura, design, specifiche | Riservato |
| **Marchi/Branding** | Loghi, materiali del brand | Interno (utilizzo controllato) |

**Registro della PI (ISMS-REG-PI)**: Proprietario: Consulente legale; Custode: RSSI; Revisione: annuale. Campi minimi: nome dell'asset PI, categoria, proprietario aziendale, custode, classificazione, ubicazione/sistema, gruppo di accesso, condivisione con terze parti consentita (S/N), stato di protezione legale, data di revisione.

### Controlli di protezione della PI

[Organizzazione] DEVE implementare controlli di protezione in base al tipo di PI:

**Protezione tecnica**:

| Tipo di PI | Controlli richiesti |
|-----------|---------------------|
| **Codice sorgente** | Controllo degli accessi, controllo delle versioni, revisione del codice, restrizioni all'esportazione |
| **Segreti commerciali** | Accesso need-to-know, cifratura, monitoraggio DLP |
| **Design/Specifiche** | Registrazione degli accessi, watermarking, restrizioni alla condivisione |
| **Dati di ricerca** | Cifratura, controllo degli accessi, protezione del backup |

**Protezione amministrativa**: Clausole di riservatezza nei contratti di lavoro (per ISMS-POL-A.6.1-2); accordi di non divulgazione per l'accesso di terze parti (per A.6.6); clausole di proprietà della PI nei contratti dei fornitori (per A.5.20); procedure di uscita che garantiscano la restituzione/cancellazione della PI (per A.6.5).

**Protezione legale**: Domande di brevetto depositate dove appropriato; avvisi di copyright sui materiali protetti; registrazioni dei marchi mantenute; documentazione dei segreti commerciali per la difesa legale.

### Conformità alla PI di terze parti

**Licenze software**: Tutto il software DEVE essere correttamente concesso in licenza; inventario SAM (Software Asset Management) mantenuto; verifica della conformità alle licenze trimestrale; il software senza licenza è VIETATO.

**Contenuto di terze parti**: Verifica del copyright prima dell'uso; attribuzione e licenza appropriate; conformità alle licenze open source (GPL, Apache, MIT, ecc.); rispetto delle restrizioni Creative Commons.

## Protezione dei documenti (A.5.33)

### Classificazione dei documenti

[Organizzazione] DEVE classificare i documenti in base ai requisiti di conservazione e alle esigenze di protezione:

**Categorie di documenti**:

| Categoria | Periodo di conservazione | Requisito di protezione | Esempi |
|-----------|--------------------------|------------------------|--------|
| **Legale/Contratti** | Durata + 10 anni | Riservato, integrità protetta | Contratti, accordi legali |
| **Finanziario** | 10 anni (CO svizzero) | Riservato, resistente alla manomissione | Fatture, registri, documenti fiscali |
| **Personale** | Rapporto + 10 anni | Riservato, protezione della privacy | File HR, buste paga, valutazioni |
| **Normativo** | Per normativa | Per classificazione | Report di audit, prove di conformità |
| **Tecnico** | Ciclo di vita sistema + 3 anni | Interno come minimo | Configurazioni, record di modifica |
| **Operativo** | 3-7 anni | Interno | Verbali riunioni, file di progetto |
| **Sicurezza/Audit** | 2-7 anni | Riservato, integrità protetta | Log degli accessi, record degli incidenti |

### Requisiti di conservazione

[Organizzazione] DEVE implementare controlli di conservazione dei documenti:

**Calendario di conservazione (ISMS-REG-CON)**: Proprietario: Consulente legale; Approvato da: Direzione generale; Revisione: annuale. Campi minimi: categoria del documento, descrizione, sistemi nel perimetro, periodo di conservazione, base di conservazione (legge/contratto/business), applicabilità del blocco legale, metodo di smaltimento, proprietario del documento.

**Controlli di conservazione**:

| Controllo | Requisito |
|-----------|-----------|
| **Conservazione minima** | I documenti NON DEVONO essere eliminati prima della scadenza del periodo di conservazione |
| **Conservazione massima** | I documenti DOVREBBERO essere eliminati dopo conservazione + periodo di tolleranza (limitazione della conservazione RGPD) |
| **Blocco legale** | Il blocco per contenzioso sostituisce la normale eliminazione (indefinito fino al rilascio) |
| **Protezione dell'integrità** | I documenti critici DEVONO avere verifica dell'integrità (checksum, firme digitali) |

**Risoluzione del conflitto conservazione vs. cancellazione**: Quando una richiesta di cancellazione o anonimizzazione è in conflitto con gli obblighi legali di conservazione, la conservazione ha la precedenza. I documenti in conservazione hanno accesso limitato, la base della decisione è documentata (approvazione del Consulente legale richiesta) e il coinvolgimento del RPD è obbligatorio per i dati personali.

**Registro dei blocchi legali (ISMS-REG-BLOCCO)**: Proprietario: Consulente legale. Campi minimi: ID blocco, descrizione della questione, perimetro del blocco (sistemi/documenti/custodi), data di inizio, data di rilascio, autorizzazione del Consulente legale, prove dell'applicazione del sistema, verifica del rilascio. I blocchi attivi vengono rivisti mensilmente; il rilascio richiede la firma del Consulente legale.

**Definizione di documenti critici**: I «documenti critici» per i requisiti di protezione dell'integrità includono: prove normative e di audit, registri finanziari e documentazione fiscale, log di sicurezza e degli accessi, contratti firmati e accordi legali, documenti HR master, documenti di indagine sugli incidenti e qualsiasi documento soggetto a blocco legale.

### Controlli di protezione dei documenti

**Protezione dell'integrità**: I documenti critici sono archiviati con verifica dell'integrità; i log di audit sono protetti dalla manomissione (write-once o crittografici); controllo delle versioni per i documenti che richiedono il tracciamento delle modifiche; firme digitali per i documenti che richiedono l'autenticità.

**Protezione della disponibilità**: Backup secondo la criticità (per ISMS-POL-A.8.13); ridondanza geografica per i documenti critici; aggiornamento dei supporti prima del degrado (piano di migrazione); manutenzione del formato leggibile (migrazione del formato quando necessario).

**Protezione della riservatezza**: Controllo degli accessi basato sul need-to-know; cifratura per i documenti riservati; protezione fisica per i documenti cartacei; smaltimento sicuro per il calendario di conservazione.

### Smaltimento dei documenti

[Organizzazione] DEVE smaltire i documenti in modo sicuro alla scadenza del periodo di conservazione:

| Tipo di documento | Metodo di smaltimento |
|------------------|----------------------|
| **Cartaceo (Riservato+)** | Tritatura incrociata (minimo P-4) o incenerimento testimoniato |
| **Cartaceo (Interno)** | Tritatura standard (minimo P-3) |
| **Elettronico (Riservato+)** | Cancellazione sicura per ISMS-POL-A.8.10 |
| **Elettronico (Interno)** | Cancellazione standard con verifica |
| **Supporti (HDD, nastri)** | Smagnetizzazione, distruzione fisica o distruzione certificata |

**Documentazione dello smaltimento**: Record di smaltimento mantenuti per la pista di audit; certificati di distruzione per i documenti Riservati+; distruzione da parte di terze parti verificata (certificazioni del fornitore).

---

# Ruoli e responsabilità

| Ruolo | Responsabilità per PI e Documenti |
|-------|----------------------------------|
| **Direzione generale** | Approvazione della strategia PI, approvazione della politica di conservazione dei documenti |
| **RSSI** | Controlli di protezione della PI, requisiti di sicurezza dei documenti |
| **Consulente legale** | Registrazione della PI, calendario di conservazione, conformità legale |
| **RPD** | Dati personali nei documenti, limitazione della conservazione RGPD |
| **Responsabile dei documenti** | Manutenzione del calendario di conservazione, supervisione dello smaltimento |
| **Proprietari delle informazioni** | Classificazione, decisioni di conservazione per i documenti di proprietà |
| **Operazioni IT** | Controlli tecnici, backup, esecuzione dello smaltimento |
| **Tutto il personale** | Gestire PI e documenti per politica, segnalare le violazioni |

---

# Governance e conformità

## Quadro di valutazione

| Valutazione | Frequenza | Responsabile | Prove |
|------------|-----------|-------------|-------|
| Revisione del Registro PI | Annuale | Consulente legale | Registro aggiornato, conferma di proprietà |
| Audit delle licenze software | Trimestrale | Operazioni IT | Report SAM, riconciliazione licenze |
| Revisione del calendario di conservazione | Annuale | Consulente legale | Calendario aggiornato, allineamento normativo |
| Audit dello smaltimento dei documenti | Annuale | Audit interno | Record di smaltimento, campionamento certificati |
| Controllo dell'integrità dei documenti | Annuale | Operazioni IT | Verifica del backup, risultati del test di integrità |

**Metriche di governance**:

- Asset PI con proprietari designati (obiettivo: 100%)
- Tasso di conformità alle licenze software (obiettivo: 100%)
- Documenti con periodi di conservazione assegnati (obiettivo: 100%)
- Documenti smaltiti per calendario (obiettivo: >95%)
- Tasso di superamento del controllo dell'integrità dei documenti (obiettivo: 100%)

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Proprietà intellettuale (PI)** | Creazioni della mente: invenzioni, opere letterarie/artistiche, simboli, design |
| **Segreto commerciale** | Informazioni aziendali riservate che forniscono un vantaggio competitivo |
| **Documento** | Informazioni create, ricevute e mantenute come prova dell'attività aziendale |
| **Periodo di conservazione** | Durata richiesta per mantenere un documento prima dello smaltimento |
| **Blocco legale** | Requisito di conservazione a causa di un contenzioso o di un'indagine |
| **SAM (Software Asset Management)** | Processi per la gestione delle licenze e dell'utilizzo del software |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Consulente legale** | [Nome] | [Data da definire] |
| **Responsabile della Protezione dei Dati (RPD)** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la protezione della proprietà intellettuale e dei documenti. Le procedure di attuazione sono documentate in ISMS-IMP-A.5.32-33 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
