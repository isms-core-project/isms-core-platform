<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.5.38-IT:sec:POL:a.5.38 -->
**CLD-SEC-POL-A.5.38 — Ruoli e responsabilità condivisi in un ambiente di cloud computing**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Ruoli e responsabilità condivisi in un ambiente di cloud computing |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-SEC-POL-A.5.38 |
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

**Ciclo di revisione** : Annuale (o in caso di cambiamenti significativi al modello di servizio cloud o alle relazioni con i fornitori, o a seguito di qualsiasi incidente o controversia relativi alla responsabilità condivisa)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :

- Principale: RSSI
- Secondaria: Responsabile Sicurezza Cloud
- Conformità: Responsabile Legale/Conformità
- Autorità finale: Direzione generale

**Documenti correlati** :

- ISMS-POL-A.5.1-2-6.1-2 (Impiego sicuro e ruoli — politica SGSI principale per ruoli e responsabilità A.5.2)
- ISMS-POL-A.5.19-23-S5 (Sicurezza dei servizi cloud — politica SGSI cloud principale)
- CLD-SEC-POL-A.5.39 (Accordo sui ruoli e le responsabilità del partner di servizio cloud — disciplina la cascata di tali responsabilità verso i partner di servizio cloud)
- CLD-SEC-POL-A.8.35 (Separazione negli ambienti di elaborazione virtuale)
- CLD-SEC-POL-A.8.36 (Rilevamento e prevenzione dell'uso non autorizzato dei servizi cloud)
- CLD-SEC-IMP-A.5.38-TG (Ruoli e responsabilità condivisi — Guida tecnica, contiene lo schema completo della matrice di responsabilità condivisa)
- CLD-SEC-REF-A.5-A.8 (Addendum di guidance sulla sicurezza cloud)
- ISO/IEC 27017:2026, Clausola 5.38 (CLD — Ruoli e responsabilità condivisi in un ambiente di cloud computing)
- ISO/IEC 27002:2022 (Controlli di sicurezza delle informazioni)
- ISO/IEC 22123-3 (Cloud computing — Architettura di riferimento)

---

## Riepilogo esecutivo

Questa politica stabilisce come [Organizzazione] alloca, documenta, comunica e implementa i ruoli e le responsabilità in materia di sicurezza delle informazioni in ogni relazione di cloud computing a cui partecipa, in conformità con ISO/IEC 27017:2026, Clausola 5.38.

**Perimetro** : Tutti i servizi cloud a cui [Organizzazione] partecipa — sia come cliente di servizio cloud (CSC) che utilizza un servizio cloud di terzi, sia come fornitore di servizio cloud (CSP) che eroga un servizio cloud ai propri clienti. Laddove [Organizzazione] ricopra entrambi i ruoli simultaneamente (ad esempio, basandosi sull'infrastruttura di un CSP per erogare il proprio servizio cloud), questa politica si applica a ciascun ruolo in modo indipendente. Copre le distribuzioni pubbliche, private, ibride e multi-cloud nei modelli IaaS, PaaS e SaaS, comprese le relazioni a più livelli in cui le responsabilità si propagano lungo una catena di fornitura.

**Nota sui controlli estesi** : ISO/IEC 27017:2026, Clausola 5.38 è uno dei quattro controlli estesi specifici per il cloud «CLD» introdotti dalla seconda edizione dello standard (insieme a 5.39, 8.35 e 8.36) che non hanno un equivalente diretto in ISO/IEC 27002:2022 o nell'Annex A di ISO/IEC 27001:2022. [Organizzazione] lo implementa come estensione informativa del proprio SGSI basato su ISO/IEC 27001:2022, coerentemente con il modo in cui ISO/IEC 27017:2026 stesso inquadra questi controlli.

**Principio fondamentale** : La sicurezza delle informazioni nel cloud computing non è mai unicamente responsabilità del CSP né unicamente del CSC — è condivisa, e l'allocazione condivisa deve essere identificata, documentata, comunicata e implementata da entrambe le parti prima di poter essere invocata. Un'ambiguità in tale allocazione è trattata come un rischio per la sicurezza delle informazioni, non come una formalità da risolvere successivamente.

---

# Perimetro e applicabilità

## ISO/IEC 27017:2026 — Clausola 5.38

**Dichiarazione del controllo (ISO/IEC 27017:2026, 5.38):**
> «Le responsabilità per i ruoli condivisi in materia di sicurezza delle informazioni nell'uso del servizio cloud dovrebbero essere allocate a parti identificate, documentate, comunicate e implementate sia dal CSC sia dal CSP.»

**Finalità (ISO/IEC 27017:2026, 5.38):**
> «Chiarire la relazione riguardante i ruoli e le responsabilità condivisi tra il CSC e il CSP per la gestione della sicurezza delle informazioni.»

*(Traduzione di lavoro predisposta a partire dal testo originale inglese della norma, a fini di leggibilità; in caso di discrepanza, fa fede il testo inglese ufficiale di ISO/IEC 27017:2026.)*

## Applicabilità

Questa politica si applica a:

- Tutti i servizi cloud che [Organizzazione] utilizza in qualità di cliente di servizio cloud (CSC), indipendentemente dal modello di distribuzione (pubblico, privato, ibrido, multi-cloud) e dal modello di servizio (IaaS, PaaS, SaaS)
- Tutti i servizi cloud che [Organizzazione] eroga in qualità di fornitore di servizio cloud (CSP) ai propri clienti
- Tutto il personale coinvolto nella selezione, configurazione, gestione operativa o erogazione di servizi cloud per conto di [Organizzazione]

## Quadro normativo e degli standard

ISO/IEC 27017:2026 è un'estensione informativa di ISO/IEC 27002:2022, che fornisce indicazioni specifiche per il cloud per controlli che l'organizzazione già implementa nell'ambito del proprio SGSI basato su ISO/IEC 27001:2022. La clausola 5.38 non corrisponde ad alcun controllo numerato di ISO/IEC 27002:2022; si tratta di un nuovo controllo introdotto nella seconda edizione 2026, tematicamente più vicino — e implementato in parallelo — agli obblighi di ruoli e responsabilità del controllo 5.2 dell'Annex A di ISO/IEC 27001:2022.

---

# Disposizioni della politica: Ruoli e responsabilità condivisi (5.38)

## Obblighi in qualità di cliente di servizio cloud (CSC)

Quando [Organizzazione] agisce in qualità di cliente di servizio cloud, [Organizzazione] DEVE:

- Ottenere l'allocazione proposta dal CSP dei ruoli e delle responsabilità in materia di sicurezza delle informazioni durante la selezione e l'onboarding del servizio, ed esaminarla rispetto alle proprie capacità e alla propensione al rischio di [Organizzazione] prima che il servizio entri in produzione
- Assicurarsi che i ruoli e le responsabilità in materia di sicurezza delle informazioni sia di [Organizzazione] sia del CSP siano indicati in un accordo scritto — e non lasciati alla sola documentazione pubblica del CSP, che può variare senza preavviso
- Identificare e mantenere un punto di contatto designato all'interno della funzione di assistenza clienti del CSP per l'escalation delle questioni di sicurezza delle informazioni
- Richiedere al CSP informazioni riguardanti le sue capacità in materia di sicurezza delle informazioni — inclusi autenticazione, crittografia, backup e registrazione (logging) — e utilizzare quadri di riferimento di terze parti o organismi indipendenti (ad es. l'ambito della certificazione ISO/IEC 27001, un report SOC 2, una voce CSA STAR) per integrare tali informazioni laddove le dichiarazioni del CSP siano insufficienti
- Valutare qualsiasi divario tra l'allocazione proposta dal CSP e la capacità di [Organizzazione] di adempiere alle proprie responsabilità allocate come un rischio per la sicurezza delle informazioni, integrandolo nel processo documentato di valutazione e trattamento del rischio di [Organizzazione] laddove non possa essere colmato prima dell'avvio in produzione
- Mantenere la consapevolezza del personale riguardo all'allocazione concordata per i servizi cloud utilizzati, attraverso il programma di sensibilizzazione alla sicurezza delle informazioni dell'organizzazione (vedere ISMS-POL-A.6.3) e l'inclusione nelle attività di revisione dell'architettura cloud

## Obblighi in qualità di fornitore di servizio cloud (CSP)

Quando [Organizzazione] agisce in qualità di fornitore di servizio cloud, [Organizzazione] DEVE:

- Definire e documentare l'allocazione dei ruoli e delle responsabilità in materia di sicurezza delle informazioni che i propri CSC, [Organizzazione] stessa e i propri fornitori o partner di servizio cloud sono ciascuno tenuti a implementare
- Comunicare l'allocazione ai CSC prospettici ed esistenti prima della firma del contratto e dopo ogni modifica sostanziale — tramite l'accordo di servizio, la documentazione di sicurezza rivolta ai clienti o i materiali di onboarding, a seconda di quanto appropriato per il servizio
- Stabilire e mantenere la relazione con ciascun CSC riguardo alle questioni di sicurezza delle informazioni, incluso un percorso di escalation definito e documentato nell'accordo
- Fornire ai CSC informazioni riguardanti le capacità di sicurezza delle informazioni del servizio cloud e le misure di sicurezza delle informazioni adottate da [Organizzazione], a un livello di chiarezza sufficiente affinché il CSC le comprenda adeguatamente — utilizzando quadri di riferimento riconosciuti di terze parti o organismi indipendenti laddove utile per trasmettere tali informazioni
- Laddove il servizio si basi su un CSP sottostante (relazione a più livelli o di catena di fornitura), valutare e documentare come le responsabilità si propagano, e assicurare la coerenza con gli accordi che [Organizzazione] detiene con i propri partner di servizio cloud ai sensi di CLD-SEC-POL-A.5.39
- Trattare una controversia o un'ambiguità persistente riguardo all'allocazione delle responsabilità, sollevata da un CSC o individuata internamente, come un evento di sicurezza delle informazioni che richiede escalation, non come una richiesta di assistenza di routine

## Principio di allocazione condivisa

I ruoli e le responsabilità nel cloud computing sono tipicamente ripartiti tra il CSC e il CSP. [Organizzazione] DEVE tenere conto, nell'allocare ruoli e responsabilità in entrambe le vesti, dei dati del CSC e delle applicazioni del CSC di cui [Organizzazione] (in qualità di CSP) è depositaria, o di cui [Organizzazione] (in qualità di CSC) rimane responsabile nonostante la custodia tecnica del CSP.

## Matrice di responsabilità condivisa — Contenuto minimo

Ogni relazione di servizio cloud rientrante nel perimetro di questa politica DEVE essere supportata da una matrice di responsabilità condivisa aggiornata. Come minimo, la matrice registra, per ciascuna area di responsabilità (ad es. autenticazione, crittografia, backup, registrazione, applicazione delle patch, segmentazione di rete): a quale parte è allocata (CSC, CSP o condivisa); quale azione ciascuna parte deve intraprendere per adempiere alla propria quota; se [Organizzazione] ha confermato di poter adempiere alla propria quota allocata; e la data dell'ultima revisione. Lo schema completo è mantenuto in CLD-SEC-IMP-A.5.38-TG, Sezione 1. La matrice DEVE essere rivista dal Responsabile Sicurezza Cloud prima che una nuova relazione di servizio cloud entri in produzione, e successivamente almeno una volta all'anno.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|-----------------|
| **RSSI** | È proprietario di CLD-SEC-POL-A.5.38; approva l'allocazione di responsabilità condivisa per le relazioni di servizio cloud strategiche o ad alto rischio; sottopone all'escalation della Direzione generale gli scostamenti di allocazione non risolti; esamina l'efficacia della politica in sede di riesame della direzione |
| **Responsabile Sicurezza Cloud** | Esamina la documentazione su ruoli/responsabilità fornita dal CSP per i servizi utilizzati (ruolo CSC); crea e mantiene la documentazione su ruoli/responsabilità pubblicata ai CSC per i servizi erogati (ruolo CSP); mantiene la matrice di responsabilità condivisa per ogni relazione attiva; riferisce al RSSI gli indicatori relativi agli scostamenti di allocazione e alla copertura della matrice |
| **Responsabile Legale/Conformità** | Garantisce che l'allocazione concordata dei ruoli e delle responsabilità sia riflessa nell'accordo scritto con ciascuna controparte CSC o CSP |
| **Erogazione del servizio cloud / Ingegneria** | Implementa i controlli tecnici corrispondenti alle responsabilità allocate a [Organizzazione]; sottopone all'escalation qualsiasi responsabilità che [Organizzazione] non è in grado di adempiere |
| **Tutto il personale** | Opera esclusivamente nell'ambito dei ruoli e delle responsabilità allocati alla propria funzione; segnala qualsiasi ambiguità nell'allocazione di responsabilità condivisa al Responsabile Sicurezza Cloud |

---

# Requisiti in materia di prove

| Prova | Descrizione | Responsabile | Conservazione |
|-------|-------------|--------------|---------------|
| Matrice di responsabilità condivisa | Per ciascuna relazione di servizio cloud, che documenta quali responsabilità di sicurezza spettano a [Organizzazione] e quali alla controparte (CSC o CSP), secondo il contenuto minimo sopra indicato | Responsabile Sicurezza Cloud | In corso + 3 anni dalla fine della relazione |
| Clausole dell'accordo | Estratto dell'accordo scritto che riporta i ruoli e le responsabilità concordati | Responsabile Legale/Conformità | Durata dell'accordo + 3 anni |
| Registrazioni di revisione e approvazione | Registrazioni che dimostrano che la matrice è stata attivamente esaminata e approvata prima dell'avvio in produzione, e non accettata passivamente | Responsabile Sicurezza Cloud | In corso + 3 anni |
| Dichiarazioni di capacità del CSP (ruolo CSC) | Registrazioni delle informazioni richieste e fornite dai CSP riguardo alle loro capacità di sicurezza | Responsabile Sicurezza Cloud | In corso + 3 anni |
| Documentazione delle capacità rivolta ai CSC (ruolo CSP) | Documentazione pubblicata ai CSC che descrive le capacità e le misure di sicurezza di [Organizzazione] | Responsabile Sicurezza Cloud | Versione attuale + versioni precedenti per 3 anni |
| Registrazioni di scostamenti di allocazione / rischi | Registrazioni di qualsiasi scostamento di allocazione sottoposto a escalation nel processo di valutazione e trattamento del rischio, con relativa risoluzione | RSSI | In corso + 3 anni |

> **Base di conservazione** : I periodi di 3 anni sono allineati all'approccio di conservazione utilizzato nell'intera gamma di prodotti cloud di ISMS Core per le prove relative a contratti e accordi.

---

# Monitoraggio e indicatori

Il Responsabile Sicurezza Cloud riferisce al RSSI, con cadenza almeno trimestrale:

- La proporzione delle relazioni di servizio cloud attive (ruoli CSC e CSP) dotate di una matrice di responsabilità condivisa aggiornata e rivista
- Il numero di scostamenti di allocazione individuati e sottoposti a escalation nel processo di valutazione e trattamento del rischio, con il relativo stato di risoluzione
- Il numero di controversie o ambiguità riguardanti l'allocazione delle responsabilità sollevate da CSC o da team interni

L'efficacia di questa politica è valutata nell'ambito del riesame della direzione, e a seguito di qualsiasi incidente di sicurezza legato al cloud in cui l'allocazione di responsabilità condivisa sia rilevante ai fini dell'analisi delle cause profonde.

---

# Considerazioni di audit

Gli auditor che verificano la conformità a CLD-SEC-POL-A.5.38 devono aspettarsi di trovare:

- Una matrice di responsabilità condivisa per ogni relazione di servizio cloud attiva, in ruolo CSC o CSP, conforme ai requisiti di contenuto minimo sopra indicati
- Accordi scritti che dichiarano, anziché sottintendere, l'allocazione dei ruoli e delle responsabilità in materia di sicurezza delle informazioni
- Prove che [Organizzazione], quando agisce in qualità di CSC, ha esaminato e confermato attivamente l'allocazione proposta dal CSP anziché accettarla per impostazione predefinita
- Prove che [Organizzazione], quando agisce in qualità di CSP, ha documentato e comunicato proattivamente la propria allocazione ai CSC anziché attendere che i CSC lo richiedano
- Prove che gli scostamenti di allocazione sono stati integrati nel processo di valutazione e trattamento del rischio, e non semplicemente annotati e lasciati aperti
- Indicatori di monitoraggio trimestrali che dimostrano una supervisione attiva della copertura della matrice, non un esercizio una tantum

---

<!-- QA_VERIFIED: 2026-08-01 -->
