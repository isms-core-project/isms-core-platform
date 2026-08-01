<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.5.39-IT:sec:POL:a.5.39 -->
**CLD-SEC-POL-A.5.39 — Accordo sui ruoli e le responsabilità del partner di servizio cloud**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Accordo sui ruoli e le responsabilità del partner di servizio cloud |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-SEC-POL-A.5.39 |
| **Autore del documento** | RSSI / Responsabile Sicurezza Cloud |
| **Proprietario del documento** | RSSI |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Data da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto Cloud** | 1.0 |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data da definire] | RSSI | Politica iniziale per l'implementazione di ISO/IEC 27017:2026 Ed. 2 |

**Ciclo di revisione** : Annuale (o in caso di onboarding/cambio di un partner di servizio cloud, o a seguito di qualsiasi escalation per conflitto di perimetro)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :

- Principale: RSSI
- Secondaria: Responsabile Sicurezza Cloud
- Conformità: Responsabile Legale/Conformità
- Autorità finale: Direzione generale

**Documenti correlati** :

- CLD-SEC-POL-A.5.38 (Ruoli e responsabilità condivisi in un ambiente di cloud computing — l'allocazione CSC/CSP con cui questa politica deve rimanere coerente)
- ISMS-POL-A.5.19-23-S1 (Fondamenti delle relazioni con i fornitori)
- ISMS-POL-A.5.19-23-S2 (Requisiti degli accordi con i fornitori)
- ISMS-POL-A.5.19-23-S5 (Sicurezza dei servizi cloud)
- CLD-SEC-IMP-A.5.39-TG (Accordo sui ruoli e le responsabilità del partner di servizio cloud — Guida tecnica, contiene lo schema completo del registro dei ruoli CSN e del controllo di coerenza)
- CLD-SEC-REF-A.5-A.8 (Addendum di guidance sulla sicurezza cloud)
- ISO/IEC 27017:2026, Clausola 5.39 (CLD — Accordo sui ruoli e le responsabilità del partner di servizio cloud)
- ISO/IEC 22123-3 (Cloud computing — Architettura di riferimento)

---

## Riepilogo esecutivo

Questa politica stabilisce come [Organizzazione] classifica, definisce e concorda i ruoli e le responsabilità in materia di sicurezza delle informazioni di qualsiasi **partner di servizio cloud (CSN)** che ingaggia o da cui è ingaggiata, in conformità con ISO/IEC 27017:2026, Clausola 5.39.

**Perimetro** : Tutti i partner di servizio cloud — terze parti le cui attività supportano o sono ausiliarie al ruolo di cliente di servizio cloud (CSC) di [Organizzazione], al ruolo di fornitore di servizio cloud (CSP) di [Organizzazione], o a entrambi. Secondo ISO/IEC 22123-3, le attività di un CSN rientrano tipicamente in uno o più dei tre sotto-ruoli: sviluppatore di servizi cloud, auditor cloud e broker di servizi cloud.

**Nota sui controlli estesi** : ISO/IEC 27017:2026, Clausola 5.39 è uno dei quattro controlli estesi specifici per il cloud «CLD» introdotti dalla seconda edizione dello standard (insieme a 5.38, 8.35 e 8.36). È interamente nuovo — non ha equivalenti nella prima edizione del 2015 di ISO/IEC 27017 né un equivalente diretto in ISO/IEC 27002:2022. [Organizzazione] lo implementa come estensione informativa del proprio SGSI basato su ISO/IEC 27001:2022.

**Relazione con CLD-SEC-POL-A.5.38** : Il CSC e il CSP dispongono già di ruoli e responsabilità condivisi tra loro ai sensi di CLD-SEC-POL-A.5.38. Qualsiasi accordo che [Organizzazione] stipuli con un partner di servizio cloud DEVE essere coerente con tale allocazione condivisa preesistente — un accordo CSN non può riassegnare una responsabilità dal CSC o dal CSP senza il consenso di entrambi. Un ingaggio CSN che determinerebbe tale riassegnazione è trattato come un rischio per la sicurezza delle informazioni che richiede escalation prima della firma, non come una questione da risolvere a posteriori.

---

# Perimetro e applicabilità

## ISO/IEC 27017:2026 — Clausola 5.39

**Dichiarazione del controllo (ISO/IEC 27017:2026, 5.39):**
> «I ruoli e le responsabilità in materia di sicurezza delle informazioni del CSN dovrebbero essere definiti e concordati con il CSC o il CSP che utilizza il servizio del CSN.»

**Finalità (ISO/IEC 27017:2026, 5.39):**
> «Delineare i ruoli e le responsabilità del CSC e del CSP quando si utilizza un CSN.»

*(Traduzione di lavoro predisposta a partire dal testo originale inglese della norma, a fini di leggibilità; in caso di discrepanza, fa fede il testo inglese ufficiale di ISO/IEC 27017:2026.)*

## Sotto-ruoli del partner di servizio cloud (secondo ISO/IEC 22123-3)

| Sotto-ruolo | Descrizione | Esempi tipici per [Organizzazione] |
|-------------|-------------|----------------------------------------|
| **Sviluppatore di servizi cloud** | Progetta, sviluppa, testa o mantiene componenti utilizzati per erogare un servizio cloud | Società di ingegneria a contratto che sviluppa un modulo utilizzato in un servizio erogato; fornitore di pipeline CI/CD gestita |
| **Auditor cloud** | Esegue una valutazione indipendente del funzionamento, dei controlli o della conformità di un servizio cloud | Auditor esterno ISO/IEC 27001 o SOC 2; società indipendente di penetration test |
| **Broker di servizi cloud** | Gestisce l'uso, le prestazioni o l'erogazione di servizi cloud e negozia le relazioni tra CSC e CSP | Rivenditore cloud; fornitore di servizi gestiti che aggrega più CSP per conto di [Organizzazione] |

Un CSN può detenere un unico sotto-ruolo, più sotto-ruoli o — in alcuni ingaggi — agire come CSN autonomo in una relazione e come CSP in un'altra. [Organizzazione] DEVE determinare e documentare quale/i sotto-ruolo/i si applichi/applichino a ciascun partner di servizio cloud che ingaggia, utilizzando la procedura di classificazione descritta in CLD-SEC-IMP-A.5.39-UG, Parte 1.

## Applicabilità

Questa politica si applica a:

- Tutte le terze parti che [Organizzazione] ingaggia, in qualità di CSC o di CSP, le cui attività soddisfano la definizione ISO/IEC 22123-3 di partner di servizio cloud (sotto-ruolo sviluppatore, auditor o broker)
- Tutti i team interni responsabili della selezione, contrattazione o supervisione di tali partner

---

# Disposizioni della politica: Accordo sui ruoli del partner di servizio cloud (5.39)

## Classificazione e accordo sui ruoli del CSN

[Organizzazione] DEVE, prima che un partner di servizio cloud avvii qualsiasi attività che riguardi un servizio cloud utilizzato da [Organizzazione] (in qualità di CSC) o erogato da [Organizzazione] (in qualità di CSP):

- Classificare la terza parte rispetto ai tre sotto-ruoli ISO/IEC 22123-3, e confermare se l'ingaggio rende la terza parte anche indipendentemente un CSP a pieno titolo (nel qual caso CLD-SEC-POL-A.5.38 si applica altresì a tale porzione della relazione)
- Definire chiaramente i ruoli e le responsabilità che il CSN è tenuto ad assumere, in relazione al/ai sotto-ruolo/i classificato/i, prima della conclusione della negoziazione contrattuale
- Recuperare e verificare le responsabilità proposte dal CSN rispetto alla matrice di responsabilità condivisa (CLD-SEC-IMP-A.5.38-TG, Sezione 1) per la relazione di servizio cloud che il CSN supporterà
- Raggiungere un accordo scritto con il CSN su tali ruoli e responsabilità prima che il CSN inizi a operare — un'intesa informale o verbale non soddisfa questo requisito
- Laddove il controllo di coerenza individui un conflitto con l'allocazione CSC/CSP esistente, ottenere il consenso scritto della controparte (CSC o CSP) prima di procedere, oppure rifiutare l'ingaggio

## Requisiti contrattuali

Ogni ingaggio di partner di servizio cloud rientrante nel perimetro di questa politica DEVE essere disciplinato da un accordo scritto, negoziato ai sensi di ISMS-POL-A.5.19-23-S2 (Requisiti degli accordi con i fornitori), che come minimo:

- Identifichi il/i sotto-ruolo/i del CSN (sviluppatore, auditor, broker o combinazione)
- Indichi le specifiche responsabilità in materia di sicurezza delle informazioni assegnate al CSN, come testo contrattuale — non come intesa informale collaterale
- Confermi che gli obblighi del CSN non sono in conflitto con gli impegni di responsabilità condivisa CSC/CSP esistenti di [Organizzazione], facendo riferimento al controllo di coerenza effettuato

## Comunicazione dei ruoli concordati

[Organizzazione] DEVE comunicare i ruoli e le responsabilità concordati del CSN ai team interni che collaborano con il CSN (erogazione del servizio cloud, ingegneria, personale di progetto interessato) tramite il registro dei ruoli CSN e il programma di sensibilizzazione alla sicurezza delle informazioni dell'organizzazione (vedere ISMS-POL-A.6.3), nonché al personale operativo proprio del CSN tramite l'accordo firmato, integrato da una discussione congiunta sulle responsabilità per gli ingaggi con perimetro rilevante ai fini della sicurezza delle informazioni.

## Registro dei ruoli CSN — Contenuto minimo

Il registro dei ruoli CSN (schema completo in CLD-SEC-IMP-A.5.39-TG, Sezione 1) DEVE registrare, per ciascun partner di servizio cloud, come minimo: il nome del CSN; il/i suo/i sotto-ruolo/i classificato/i e se agisca anche indipendentemente come CSP; le responsabilità ad esso assegnate; la relativa relazione di servizio cloud e il riferimento alla matrice di responsabilità condivisa; il riferimento e la data dell'accordo; l'esito del controllo di coerenza; e la data dell'ultima revisione. Il registro DEVE essere mantenuto dal Responsabile Sicurezza Cloud e rivisto almeno una volta all'anno.

## Supervisione continua e cambiamenti di perimetro

[Organizzazione] DEVE:

- Rivedere il registro dei ruoli CSN almeno una volta all'anno, confermando che la classificazione, le responsabilità concordate e la continua coerenza con la matrice di responsabilità condivisa pertinente di ciascun CSN rimangano accurate
- Rivalutare la classificazione e la coerenza, e modificare l'accordo di conseguenza, ogniqualvolta l'attività effettiva di un CSN cambi sostanzialmente rispetto al perimetro originariamente concordato
- Sottoporre all'escalation del Responsabile Sicurezza Cloud, e ove non risolto del RSSI, qualsiasi caso in cui l'attività di un CSN risulti eccedere il perimetro concordato, trattandolo come un rischio per la sicurezza delle informazioni che richiede una valutazione, non come una mera formalità contrattuale

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|-----------------|
| **RSSI** | È proprietario di CLD-SEC-POL-A.5.39; approva gli ingaggi CSN con perimetro rilevante ai fini della sicurezza delle informazioni; risolve i conflitti tra accordi CSN e allocazioni CSC/CSP esistenti; esamina le escalation di rischio relative ai CSN |
| **Responsabile Sicurezza Cloud** | Classifica ciascun CSN potenziale per sotto-ruolo; esegue e registra il controllo di coerenza rispetto alla matrice di responsabilità condivisa applicabile prima della firma dell'accordo CSN; mantiene il registro dei ruoli CSN; riferisce al RSSI gli indicatori di copertura CSN |
| **Responsabile Legale/Conformità** | Negozia e conclude gli accordi CSN ai sensi di ISMS-POL-A.5.19-23-S2; garantisce che i ruoli e le responsabilità concordati siano riportati nel testo contrattuale |
| **Erogazione del servizio cloud / Ingegneria** | Opera entro i confini dei ruoli concordati del CSN; sottopone all'escalation qualsiasi attività del CSN che ecceda il perimetro concordato |

---

# Requisiti in materia di prove

| Prova | Descrizione | Responsabile | Conservazione |
|-------|-------------|--------------|---------------|
| Registro dei ruoli CSN | Elenco di tutti i partner di servizio cloud attivi con sotto-ruolo/i assegnato/i, perimetro e riferimento dell'accordo | Responsabile Sicurezza Cloud | In corso + 3 anni dalla fine dell'ingaggio |
| Estratti degli accordi CSN | Estratto dell'accordo scritto di ciascun CSN che riporta i ruoli e le responsabilità concordati | Responsabile Legale/Conformità | Durata dell'accordo + 3 anni |
| Registrazioni del controllo di coerenza | Registrazioni che confermano che ciascun accordo CSN è stato verificato rispetto alla matrice di responsabilità condivisa applicabile prima della firma, incluso l'esito e qualsiasi consenso della controparte ottenuto | Responsabile Sicurezza Cloud | In corso + 3 anni |
| Registrazioni di modifica per cambiamento di perimetro | Registrazioni della riclassificazione del perimetro CSN e della modifica dell'accordo in caso di cambiamento sostanziale dell'attività di un CSN | Responsabile Sicurezza Cloud | In corso + 3 anni |
| Registrazioni di escalation di rischio legate ai CSN | Registrazioni di qualsiasi conflitto legato a un CSN o eccedenza di perimetro sottoposta a escalation nel processo di valutazione e trattamento del rischio, con relativa risoluzione | RSSI | In corso + 3 anni |

---

# Monitoraggio e indicatori

Il Responsabile Sicurezza Cloud riferisce al RSSI, con cadenza almeno trimestrale:

- La proporzione dei partner di servizio cloud attivi con una voce del registro dei ruoli CSN aggiornata e classificata e un controllo di coerenza completato
- Il numero di ingaggi CSN per cui è stato individuato un conflitto con l'allocazione CSC/CSP esistente, e come è stato risolto
- Il numero di escalation per eccedenza di perimetro e il relativo stato di risoluzione

---

# Considerazioni di audit

Gli auditor che verificano la conformità a CLD-SEC-POL-A.5.39 devono aspettarsi di trovare:

- Un registro dei ruoli CSN che copra ogni terza parte rispondente alla definizione ISO/IEC 22123-3 di partner di servizio cloud
- Accordi scritti che indichino esplicitamente il/i sotto-ruolo/i assegnato/i e le responsabilità in materia di sicurezza delle informazioni del CSN
- Prove documentate che ciascun accordo CSN sia stato verificato rispetto alla matrice di responsabilità condivisa pertinente ai sensi di CLD-SEC-POL-A.5.38 prima della sottoscrizione, incluso il modo in cui eventuali conflitti sono stati risolti
- Prove che i cambiamenti di perimetro abbiano innescato una riclassificazione e una modifica dell'accordo, e non una deriva silenziosa
- Indicatori di monitoraggio trimestrali che dimostrino una supervisione attiva, non un esercizio una tantum in fase di onboarding

---

<!-- QA_VERIFIED: 2026-08-01 -->
