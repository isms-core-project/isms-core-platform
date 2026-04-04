<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S2-IT:framework:POL:a.5.19-23-s2 -->
**ISMS-POL-A.5.19-23-S2 — Requisiti degli accordi con i fornitori**
**Controllo A.5.20: Considerazione della sicurezza delle informazioni negli accordi con i fornitori**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Requisiti degli accordi con i fornitori |
| **Tipo di documento** | Sezione di politica |
| **Identificativo del documento** | ISMS-POL-A.5.19-23-S2 |
| **Autore del documento** | Responsabile della Sicurezza delle Informazioni (RSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.5.19-23; ISMS-POL-A.5.19-23-S1; ISMS-IMP-A.5.19-23.S2-UG/TG; ISO/IEC 27001:2022 Controllo A.5.20; ISO/IEC 27036-2; RGPD Articolo 28

---

# Scopo

La presente sezione definisce i requisiti obbligatori di sicurezza delle informazioni che devono essere inclusi negli accordi con i fornitori. Garantisce che gli obblighi di sicurezza siano giuridicamente vincolanti ed eseguibili per tutta la durata della relazione.

**Principio critico**: I requisiti di sicurezza senza eseguibilità contrattuale sono semplici suggerimenti che i fornitori possono ignorare senza conseguenze. Ogni accordo con un fornitore deve includere clausole di sicurezza eseguibili, diritti di audit, requisiti di notifica degli incidenti e disposizioni sulla responsabilità.

**ISO/IEC 27001:2022 Allegato A.5.20**

> *Requisiti pertinenti di sicurezza delle informazioni devono essere stabiliti e concordati con ciascun fornitore che può accedere, elaborare, archiviare, comunicare o fornire componenti di infrastruttura IT per le informazioni dell'organizzazione.*

---

# Perimetro

## Accordi applicabili

| Tipo di accordo | Descrizione |
|----------------|-------------|
| Contratti quadro di servizi (MSA) | Contratti generali che disciplinano la relazione |
| Accordi di livello di servizio (SLA) | Impegni di performance e disponibilità |
| Accordi di trattamento dei dati (DPA) | Trattamento dei dati personali (RGPD, nLPD) |
| Accordi di non divulgazione (NDA) | Impegni di riservatezza |
| Specifiche tecniche (SOW) | Ambito specifico di progetto o servizio |
| Contratti di licenza software | Condizioni di utilizzo del software |
| Accordi sui servizi cloud | Condizioni di consumo dei servizi cloud |

## Responsabilità della revisione degli accordi

| Livello fornitore | Revisione dell'accordo da parte di |
|------------------|-----------------------------------|
| Livello 1 (Critico) | Legale + Sicurezza + Responsabile aziendale + Acquisti |
| Livello 2 (Alto) | Legale + Sicurezza + Acquisti |
| Livello 3 (Medio) | Acquisti + Sicurezza (se accesso ai dati) |
| Livello 4 (Basso) | Acquisti (condizioni standard accettabili) |

**Tempistiche di revisione**: Nuovi accordi: prima della firma del contratto; Rinnovi: almeno 60 giorni prima della scadenza; Addendum: prima dell'esecuzione dei cambiamenti significativi.

---

# Clausole di sicurezza obbligatorie

## Requisiti delle clausole per livello di fornitore

| Clausola di sicurezza | N1 | N2 | N3 | N4 |
|----------------------|----|----|----|----|
| Obblighi di riservatezza | ✓ | ✓ | ✓ | ✓ |
| Conformità alla protezione dei dati | ✓ | ✓ | ✓ | — |
| Impegno in materia di controlli di sicurezza | ✓ | ✓ | ✓ | — |
| Notifica degli incidenti | ✓ | ✓ | ✓ | — |
| Diritti di audit | ✓ | ✓ | — | — |
| Restrizioni sui sub-responsabili | ✓ | ✓ | — | — |
| Requisiti di continuità operativa | ✓ | ✓ | — | — |
| Restituzione/distruzione dei dati | ✓ | ✓ | ✓ | — |
| Disposizioni sulla responsabilità | ✓ | ✓ | ✓ | — |
| Diritti di risoluzione | ✓ | ✓ | ✓ | ✓ |
| Requisiti assicurativi | ✓ | ✓ | — | — |

## Obblighi di riservatezza

**Clausola modello**:
> «Il fornitore tratterà tutte le informazioni di [Organizzazione] come riservate e non le utilizzerà, divulgherà o riprodurrà, salvo nella misura necessaria per la fornitura dei servizi. Il fornitore proteggerà le informazioni di [Organizzazione] con almeno lo stesso livello di cura utilizzato per proteggere le proprie informazioni riservate di analoga sensibilità, e in ogni caso con cura ragionevole.»

**Elementi obbligatori**: Definizione di informazioni riservate; utilizzo autorizzato limitato alla fornitura del servizio; durata che sopravvive alla risoluzione (minimo 3 anni, o a tempo indeterminato per i segreti commerciali); restituzione/distruzione alla risoluzione con certificazione.

## Conformità alla protezione dei dati

**Elementi obbligatori per RGPD/nLPD**: Designazione dei ruoli (titolare vs. responsabile del trattamento); finalità del trattamento limitata alle finalità specificate; categorie di dati personali trattati; luogo di trattamento con restrizioni geografiche ove applicabile; misure tecniche e organizzative; regole sui sub-responsabili del trattamento (approvazione previa richiesta); diritti degli interessati (supporto per accesso, rettifica, cancellazione, portabilità); notifica delle violazioni entro 24 ore a [Organizzazione]; diritti di audit e ispezione; trasferimenti internazionali (SCC o meccanismi di adeguatezza).

## Impegno in materia di controlli di sicurezza

**Linguaggio contrattuale richiesto**:
> «Il fornitore implementerà e manterrà controlli di sicurezza amministrativi, tecnici e fisici adeguati alla classificazione dei dati a cui accede, conformemente agli standard del settore (ISO/IEC 27001, Criteri di fiducia dei servizi SOC 2) e ai requisiti specificati nell'Allegato [X] (Requisiti di sicurezza).»

**L'allegato sui requisiti di sicurezza deve specificare**: Gestione degli accessi (AMF per gli accessi privilegiati, RBAC, registrazione); cifratura (in transito TLS 1.2+, a riposo AES-256); sicurezza di rete; sicurezza delle postazioni di lavoro; sicurezza del personale; sicurezza fisica; gestione degli incidenti; gestione dei cambiamenti; gestione delle vulnerabilità; backup e ripristino.

---

# Requisiti di notifica degli incidenti

## Tempistiche di notifica

| Tipo di incidente | Tempistica | Destinatario |
|------------------|-----------|-------------|
| Violazione dei dati confermata | Entro 4 ore dalla conferma | RSSI + RSI + Responsabile aziendale |
| Sospetta violazione dei dati | Entro 24 ore dal rilevamento | RSI + Responsabile aziendale |
| Incidente di sicurezza (non violazione) | Entro 48 ore | Team di sicurezza |
| Interruzione del servizio (critico) | Entro 1 ora | Operazioni IT + Responsabile aziendale |
| Richiesta normativa | Entro 24 ore | Legale + RSSI |

**Nota — Regola di priorità**: Quando si applicano più scadenze di notifica normativa per lo stesso incidente, si applica la scadenza più breve applicabile. I fornitori devono essere operativamente in grado di soddisfare il requisito più stringente per la loro classificazione di servizio.

**Contenuto minimo della notifica iniziale**: Data e ora di scoperta; natura dell'incidente; dati/sistemi potenzialmente interessati; numero stimato di record interessati (per le violazioni dei dati); azioni di contenimento iniziali intraprese; contatto designato per l'incidente con disponibilità 24/7.

---

# Diritti di audit

## Diritti di audit per livello

| Livello fornitore | Diritti di audit richiesti |
|------------------|---------------------------|
| Livello 1 | Diritti di audit completi (in loco o da remoto, con o senza preavviso) |
| Livello 2 | Diritti di audit o accettazione di report di terzi |
| Livello 3 | Accettazione di report di terzi |
| Livello 4 | Non richiesti |

**Clausola modello per il Livello 1**:
> «[Organizzazione] avrà il diritto, previo avviso scritto di trenta (30) giorni (o immediatamente in caso di incidente di sicurezza o requisito normativo), di verificare i controlli di sicurezza, i processi e le strutture del fornitore relativi ai servizi forniti. Il fornitore fornirà cooperazione ragionevole e accesso al personale, alla documentazione e ai sistemi.»

**Alternative accettabili agli audit diretti**: SOC 2 Tipo II (12 mesi); Certificato ISO/IEC 27001 (valido + sorveglianza); report di test di penetrazione (12 mesi); certificazione CSA STAR.

---

# Requisiti sui sub-responsabili del trattamento

**Clausola modello**:
> «Il fornitore non si avvarrà di alcun sub-responsabile del trattamento per accedere, elaborare o archiviare i dati di [Organizzazione] senza la preventiva approvazione scritta di [Organizzazione]. Il fornitore garantirà che qualsiasi sub-responsabile approvato sia vincolato da obblighi scritti che offrano una protezione almeno equivalente a quella del presente accordo. Il fornitore rimane pienamente responsabile degli atti, omissioni e carenze di sicurezza dei propri sub-responsabili.»

**Clausola rafforzata per i servizi coperti da DORA**:
> «Per i servizi TIC coperti da DORA, il fornitore manterrà un registro di tutti gli accordi di sub-esternalizzazione a cascata e informerà preventivamente di qualsiasi sub-esternalizzazione a cascata pianificata ai sensi dell'Articolo 30 di DORA.»

---

# Requisiti di continuità operativa

## Requisiti BCP per livello

| Requisito | Livello 1 | Livello 2 | Livelli 3-4 |
|-----------|-----------|-----------|------------|
| Piano BCP/DRP documentato | ✓ Richiesto | ✓ Richiesto | — |
| Test annuale BCP/DRP | ✓ Richiesto | ✓ Raccomandato | — |
| Obiettivo di tempo di ripristino (RTO) | ✓ Definito nel SLA | ✓ Definito nel SLA | — |
| Obiettivo di punto di ripristino (RPO) | ✓ Definito nel SLA | ✓ Definito nel SLA | — |
| Ridondanza geografica | ✓ Basata sul rischio | — | — |
| Notifica di disastro | ✓ Entro 1 ora | ✓ Entro 4 ore | — |

**Obiettivi di disponibilità per criticità del servizio**: Critico (Livello 1): 99,95% o superiore; Alto (Livello 2): 99,9%; Medio (Livello 3): 99,5%.

---

# Restituzione e distruzione dei dati

**Clausola modello**:
> «Alla risoluzione o scadenza del presente accordo, il fornitore dovrà, a scelta di [Organizzazione], (a) restituire o (b) distruggere in modo sicuro tutti i dati di [Organizzazione] entro trenta (30) giorni. Per la restituzione dei dati, il fornitore dovrà fornire i dati nel formato [specificare] e assistere nella migrazione. Per la distruzione dei dati, il fornitore dovrà fornire una certificazione scritta di distruzione utilizzando metodi conformi a NIST SP 800-88 Rev. 2 o equivalente. Il fornitore non conserverà alcuna copia salvo obbligo di legge, in qual caso ne informerà [Organizzazione] per iscritto.»

---

# Diritti di risoluzione

## Trigger di risoluzione

| Trigger | Preavviso | Si applica a |
|---------|----------|-------------|
| Convenienza | Secondo contratto (generalmente 30-90 giorni) | Tutti i livelli |
| Violazione grave (non corretta) | Immediato dopo il periodo di correzione | Tutti i livelli |
| Incidente di sicurezza (significativo) | Immediato | Livelli 1-2 |
| Insolvenza o fallimento | Immediato | Tutti i livelli |
| Cambio di controllo | 30 giorni di preavviso o diritto di risoluzione immediata | Livelli 1-2 |
| Mancato mantenimento delle certificazioni | 30 giorni per correggere o risoluzione | Livelli 1-2 |
| Violazioni SLA ripetute | Dopo 3 mesi consecutivi o 6 mesi su 12 | Livelli 1-2 |
| Violazione dei dati da parte del fornitore | Immediato | Tutti con accesso ai dati |

---

# Responsabilità e assicurazione

**Orientamenti sulle disposizioni di responsabilità**: Massimale di responsabilità: minimo 12 volte gli onorari annuali per il Livello 1; responsabilità illimitata per violazioni dei dati, dolo, atti intenzionali; manleva per reclami di terzi derivanti da violazione degli obblighi di sicurezza del fornitore; l'esclusione dei danni consequenziali non deve applicarsi alle violazioni dei dati.

**Requisiti assicurativi (Livelli 1 e 2)**:

| Tipo di assicurazione | Copertura minima |
|----------------------|-----------------|
| Responsabilità informatica | 5 M€ min per Livello 1, 2 M€ per Livello 2 |
| Responsabilità professionale (E&O) | 5 M€ min per Livello 1, 2 M€ per Livello 2 |
| Responsabilità civile generale | 2 M€ per sinistro |
| Protezione privacy/RGPD | Inclusa nel cyber o 2 M€ separata |

---

# Requisiti normativi specifici

## Fornitori di servizi TIC terzi DORA (Articolo 29)

Gli accordi devono includere: piena cooperazione con le autorità competenti (accesso, ispezione, diritti di audit); diritto di emettere istruzioni al fornitore di servizi TIC terzo; diritto di risolvere gli accordi se necessario; descrizione chiara dei servizi forniti; luoghi di prestazione dei servizi e trattamento dei dati; notifica dei cambiamenti che incidono sulla performance del servizio; impegni di continuità e ripristino di emergenza; strategie di uscita con portabilità dei dati e assistenza alla transizione.

## Accordi di trattamento dei dati RGPD (Articolo 28)

Gli accordi di trattamento dei dati devono includere: trattamento solo su istruzioni documentate; impegni di riservatezza del personale; misure tecniche e organizzative di sicurezza; requisiti e processi di approvazione dei sub-responsabili del trattamento; supporto ai diritti degli interessati; cancellazione o restituzione al termine dei servizi; diritti di audit e ispezione; assistenza alla conformità normativa.

**Clausole contrattuali standard (SCC)**: Per i fornitori non UE/SEE, incorporare le SCC della Commissione UE (Decisione 2021/914) o gli equivalenti svizzeri approvati.

---

*«Un contratto senza clausole di sicurezza è un invito alla violazione.»*

<!-- QA_VERIFIED: 2026-04-03 -->
