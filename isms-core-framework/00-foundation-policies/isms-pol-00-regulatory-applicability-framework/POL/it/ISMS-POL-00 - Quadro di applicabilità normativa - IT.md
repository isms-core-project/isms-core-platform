<!-- ISMS-CORE:POLICY:ISMS-POL-00-IT:framework:POL:00 -->
**ISMS-POL-00 — Quadro di applicabilità normativa**
**Riferimento autorevole per gli obblighi di conformità del SGSI**

---

## Controllo del documento

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Quadro di applicabilità normativa |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-00 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da determinare] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Storico delle versioni**:

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 0.1 | [Data - 8 settimane] | RSSI | Bozza iniziale — struttura a tre livelli |
| 0.2 | [Data - 6 settimane] | RSSI + Legale | Aggiunta DORA, NIS2, AI Act (normative condizionali) |
| 0.3 | [Data - 4 settimane] | RPD | Sviluppo sezioni RGPD/LPD, aggiunta metodologia di valutazione |
| 0.4 | [Data - 2 settimane] | RSSI/Legale/RPD | Integrazione dei commenti delle parti interessate |
| 1.0 | [Data] | RSSI/Legale/RPD | Prima versione approvata per audit Fase 1 |

**Ciclo di revisione**: Annuale (o in caso di modifiche normative significative)
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondaria: Responsabile legale/conformità
- Conformità: Responsabile della Protezione dei Dati (RPD)
- Autorità finale: Direzione generale

**Documenti correlati**:

- Tutti i documenti di politica del SGSI (riferimento obbligatorio)
- ISO/IEC 27001:2022 Clausola 4.1 (Comprensione dell'organizzazione e del suo contesto)
- ISO/IEC 27001:2022 Clausola 4.2 (Comprensione delle esigenze e aspettative delle parti interessate)

**Riferimenti dettagliati ai requisiti** (mantenuti per le normative condizionali — cfr. Sezione 8.3):

- ISMS-REF-DORA — Riferimento ai requisiti del Digital Operational Resilience Act
- ISMS-REF-EU-AI-ACT — Riferimento ai requisiti del Regolamento UE sull'intelligenza artificiale
- ISMS-REF-FINMA — Riferimento ai requisiti della Circolare FINMA 2023/1
- ISMS-REF-NIS2 — Riferimento ai requisiti della Direttiva NIS2
- ISMS-REF-PCI-DSS — Riferimento ai requisiti del Payment Card Industry Data Security Standard

**Distribuzione**: Tutte le parti interessate del SGSI, autori di politiche, proprietari di sistemi, revisori
**Referenziato da**: Tutti i documenti di politica del SGSI

**Strategia linguistica**: Laddove i termini tecnici o normativi siano internazionalmente consolidati (es. GDPR, ISO/IEC, NIST), si mantiene la terminologia inglese per preservare la precisione e facilitare il riferimento normativo transfrontaliero.

---

## Sintesi esecutiva

Il presente documento costituisce il **riferimento autorevole** per l'interpretazione dell'applicabilità normativa e dei framework nell'ambito dell'intero Sistema di Gestione della Sicurezza delle Informazioni (SGSI).

**Scopo**: Eliminare ambiguità e incoerenze nel modo in cui normative e framework vengono referenziati nella documentazione del SGSI (politiche, procedure, controlli).

**Ambito**: Tutti i riferimenti a leggi, normative, standard e framework nella documentazione del SGSI.

**Principio chiave**: **L'applicabilità normativa deve essere esplicita, non presunta.** I riferimenti a normative e framework rientrano in tre categorie:

1. **Conformità obbligatoria** — Obblighi legali che si applicano all'organizzazione
2. **Applicabilità condizionale** — Requisiti che si applicano solo in circostanze specifiche
3. **Riferimento informativo** — Buone pratiche e orientamenti tecnici

**Utilizzo**: Tutte le politiche del SGSI DEVONO includere una Sezione 1.3 che fa riferimento a questo quadro, oppure includere una sezione «Quadro normativo» che incorpora direttamente queste categorie.

**Termini chiave**: Le definizioni dei termini utilizzati in questa politica (Obbligatorio, Condizionale, Livello 1/2/3, Trigger di applicabilità, ecc.) sono fornite nel **Glossario** in fondo al documento.

---

## Autorità e limiti della politica

### Scopo e ambito di questa politica

La presente politica definisce l'**identificazione e l'applicabilità** dei requisiti legali, normativi, regolamentari e contrattuali per il Sistema di Gestione della Sicurezza delle Informazioni dell'organizzazione.

**La presente politica stabilisce:**

- Quali normative e standard si applicano all'organizzazione
- La categorizzazione degli obblighi normativi (Obbligatorio, Condizionale, Informativo)
- La metodologia di valutazione per determinare l'applicabilità
- I processi di revisione e aggiornamento in risposta ai cambiamenti del panorama normativo

**La presente politica NON stabilisce:**

- Le decisioni di trattamento dei rischi (trattate nella Clausola 6 — Gestione del rischio)
- I requisiti di implementazione dei controlli (trattati nei controlli dell'Allegato A)
- Lo stato di conformità o la verifica (trattati nei processi di monitoraggio della conformità)

Il risultato della valutazione di applicabilità normativa costituisce un **input** per:

- Le decisioni di scoping dei controlli nell'Allegato A
- La prioritizzazione della valutazione e del trattamento dei rischi
- Le decisioni di proporzionalità per l'implementazione dei controlli
- La pianificazione degli audit e la verifica della conformità

**Principio di demarcazione**: La presente politica stabilisce l'applicabilità normativa. L'implementazione, l'applicazione e la verifica sono gestite attraverso processi SGSI separati.

**Integrazione con la Clausola 4 di ISO 27001:**

- **Clausola 4.1 (Contesto dell'organizzazione)**: Questa politica affronta il contesto esterno (ambiente legale/normativo). Il contesto interno (struttura organizzativa, tecnologia, cultura) è trattato nel Documento di contesto del SGSI.
- **Clausola 4.2 (Parti interessate)**: I requisiti delle parti interessate identificati attraverso questo quadro alimentano il registro delle parti interessate nel Documento di contesto del SGSI.

**Integrazione con la valutazione del rischio (Clausola 6):**

Gli obblighi normativi identificati in questa politica alimentano:

- **ISMS-RISK-METHODOLOGY** (Clausola 6.1.2): I requisiti normativi sono trattati come fattori di rischio esterni con priorità intrinseca (Livello 1 = priorità alta, Livello 2 condizionale = priorità media se applicabile, Livello 3 = input informativo)
- **ISMS-RISK-TREATMENT** (Clausola 6.1.3): La selezione e prioritizzazione dei controlli considera gli obblighi normativi insieme al rischio tecnico
- **Dichiarazione di Applicabilità (DdA)**: La giustificazione dell'applicabilità dei controlli fa riferimento alle assegnazioni di livello di POL-00

---

**Categorie di applicabilità normativa**

**Definizioni delle categorie**

**Conformità obbligatoria**
Obblighi legali o contrattuali ai quali l'organizzazione DEVE conformarsi. Il mancato rispetto comporta responsabilità legale, sanzioni normative, violazione contrattuale o perdita della certificazione.

**Caratteristiche**:

- Applicabile per legge o contratto
- Il mancato rispetto ha conseguenze legali/finanziarie
- Richiede prove documentate di conformità
- Soggetto ad audit e ispezioni normative

**Riferimento informativo / Allineamento alle buone pratiche**
Framework e standard utilizzati a fini di orientamento tecnico, benchmarking o allineamento volontario. Informano le pratiche di sicurezza ma non costituiscono requisiti di conformità obbligatoria, salvo esplicita richiesta contrattuale o normativa.

**Caratteristiche**:

- Adozione volontaria per le buone pratiche
- Nessun meccanismo di applicazione legale
- Utilizzato per orientamenti di implementazione tecnica
- Può diventare obbligatorio se referenziato in contratti

**Applicabilità condizionale**
Requisiti che si applicano solo quando si verificano condizioni specifiche (es. settore industriale, ubicazione geografica, tipo di servizio, contratti con clienti, ambito normativo).

**Caratteristiche**:

- L'applicabilità dipende dal contesto organizzativo
- Può diventare obbligatorio in base alle attività aziendali
- Richiede rivalutazione periodica all'evolversi dell'azienda
- Esempi: PCI DSS v4.0.1 (solo se si elaborano pagamenti con carta), HIPAA (solo se si trattano dati sanitari statunitensi)

**Chiarimento sulla classificazione per livelli**: La classificazione per livelli (Obbligatorio, Condizionale, Informativo) determina la **forza vincolante normativa** e non implica di per sé obblighi di implementazione. Le decisioni di implementazione vengono prese attraverso il processo di valutazione e trattamento del rischio, considerando i requisiti normativi insieme ad altri fattori quali propensione al rischio, contesto aziendale e fattibilità tecnica.

## Gerarchia di conformità

```
┌─────────────────────────────────────────────────────────────────┐
│                    GERARCHIA DI CONFORMITÀ                      │
├─────────────────────────────────────────────────────────────────┤
│  LIVELLO 1: OBBLIGATORIO (Legale/Contrattuale)                  │
│  • Legge federale svizzera sulla protezione dei dati (LPD)      │
│  • RGPD UE (se si trattano dati personali UE)                   │
│  • ISO/IEC 27001:2022 (per la certificazione)                   │
│  • Normative settoriali (ove applicabili)                       │
│  • Contratti con clienti (requisiti di sicurezza espliciti)     │
│                                                                 │
│  LIVELLO 2: CONDIZIONALE (Dipendente dal contesto)              │
│  • DORA (se entità finanziaria UE)                              │
│  • NIS2 (se entità essenziale/importante nell'UE)               │
│  • PCI DSS v4.0.1 (se si elaborano pagamenti con carta)         │
│  • HIPAA (se si trattano dati sanitari statunitensi)            │
│  • Normative settoriali (dipendenti dal settore)                │
│                                                                 │
│  LIVELLO 3: INFORMATIVO (Buone pratiche)                        │
│  • NIST SP 800 (orientamenti tecnici)                           │
│  • CIS Controls (benchmark di sicurezza)                        │
│  • OWASP (sicurezza applicativa)                                │
│  • Framework settoriali (solo di riferimento)                   │
└─────────────────────────────────────────────────────────────────┘
```

> *Se i caratteri di disegno delle caselle non vengono visualizzati correttamente, consultare le Sezioni 3–5 per le definizioni dei livelli.*

---

# Conformità obbligatoria (Livello 1)

## Legge federale svizzera sulla protezione dei dati (LPD/nLPD)

**Applicabilità**: Tutte le operazioni dell'organizzazione con sede in Svizzera o che servono clienti svizzeri

**Requisiti chiave**:

- Articolo 6: Principi (liceità, proporzionalità, limitazione della finalità)
- Articolo 7: Sicurezza dei dati (misure tecniche e organizzative adeguate)
- Articolo 8: Trattamento dei dati da parte di incaricati
- Articolo 19: Diritto all'informazione (diritti degli interessati)
- Articolo 328b CO (Codice delle Obbligazioni): Sorveglianza dei dipendenti e protezione della personalità

**Impatto sul SGSI**:

- Protezione dei dati fin dalla progettazione e per impostazione predefinita
- Misure di sicurezza tecnica (cifratura, controllo degli accessi)
- Trasparenza e proporzionalità della sorveglianza dei dipendenti
- Registri di trattamento dei dati (Art. 12)
- Notifica delle violazioni dei dati (Art. 24)

**Riferimento**: Legge federale sulla protezione dei dati (RS 235.1), in vigore dal 1° settembre 2023

## Regolamento generale sulla protezione dei dati dell'UE (RGPD)

**Applicabilità**: Quando si trattano dati personali di residenti nell'UE

**Requisiti chiave**:

- Articolo 5: Principi relativi al trattamento (liceità, correttezza, trasparenza, limitazione della finalità)
- Articolo 6: Base giuridica del trattamento
- Articolo 24: Responsabilità del titolare del trattamento (accountability)
- Articolo 25: Protezione dei dati fin dalla progettazione e per impostazione predefinita
- Articolo 28: Obblighi del responsabile del trattamento (contratti, misure di sicurezza)
- Articolo 32: Sicurezza del trattamento (cifratura, pseudonimizzazione, resilienza)
- Articolo 33: Notifica delle violazioni (72 ore all'autorità di controllo)
- Articolo 35: Valutazione d'impatto sulla protezione dei dati (DPIA) per trattamenti ad alto rischio

**Impatto sul SGSI**:

- Misure tecniche e organizzative (MTO)
- Cifratura e pseudonimizzazione
- Controlli di accesso e autenticazione
- Procedure di risposta alle violazioni dei dati
- Gestione dei fornitori (accordi di responsabilità del trattamento)
- Valutazioni d'impatto sulla privacy

**Riferimento**: Regolamento (UE) 2016/679, in vigore dal 25 maggio 2018

## ISO/IEC 27001:2022

**Applicabilità**: Quando l'organizzazione persegue la certificazione ISO 27001

**Requisiti chiave**:

- Controlli dell'Allegato A (93 controlli organizzativi, sulle persone, fisici e tecnologici)
- Clausola 4: Contesto dell'organizzazione
- Clausola 5: Leadership e impegno
- Clausola 6: Valutazione e trattamento dei rischi
- Clausola 7: Supporto (risorse, competenza, consapevolezza, comunicazione, informazioni documentate)
- Clausola 8: Attività operative (trattamento dei rischi, valutazione)
- Clausola 9: Valutazione delle prestazioni (monitoraggio, audit interno, riesame della direzione)
- Clausola 10: Miglioramento (non conformità, azioni correttive, miglioramento continuo)

**Impatto sul SGSI**:

- Implementazione del framework di politiche
- Metodologia di gestione dei rischi
- Implementazione dei controlli e raccolta delle prove
- Programma di audit interno
- Processo di riesame della direzione
- Miglioramento continuo

**Riferimento**: ISO/IEC 27001:2022 — Sistemi di gestione della sicurezza delle informazioni

## Normative obbligatorie aggiuntive

Le organizzazioni dovrebbero documentare le normative obbligatorie aggiuntive in base al loro contesto specifico:

| Normativa | Trigger | Esempi |
|-----------|---------|--------|
| **Diritto del lavoro** | Dipendenti nella giurisdizione | Codeterminazione del comitato aziendale (Germania), leggi sulla sorveglianza dei dipendenti |
| **Normative finanziarie** | Servizi finanziari | FINMA (Svizzera), BaFin (Germania), MiFID II (UE) |
| **Telecomunicazioni** | Servizi telecom | Intercettazione legale, conservazione dei dati |
| **Controllo delle esportazioni** | Operazioni transfrontaliere | Beni a duplice uso, esportazione di crittografia |
| **Diritto contrattuale** | Accordi con clienti | Requisiti di sicurezza espliciti nei contratti di servizio |

---

# Applicabilità condizionale (Livello 2)

Queste normative si applicano **solo quando si verificano condizioni aziendali specifiche**:

## Autorità federale di vigilanza sui mercati finanziari (FINMA)

**Normativa**: Autorità federale di vigilanza sui mercati finanziari (Eidgenössische Finanzmarktaufsicht)
**Circolari principali**:

- Circolare FINMA 2023/1 (Rischi operativi e resilienza — banche, in vigore dal 1° gennaio 2024)
- Circolare FINMA 2008/7 (Esternalizzazione — banche)
- Circolare FINMA 2018/3 (Esternalizzazione — assicuratori)

**Trigger di applicabilità**:

- L'organizzazione è un **istituto finanziario svizzero** regolamentato dalla FINMA:
  - Banche (licenza bancaria FINMA)
  - Commercianti di valori mobiliari (licenza di commerciante in valori mobiliari)
  - Compagnie di assicurazione (licenza assicurativa)
  - Fornitori di infrastrutture dei mercati finanziari (borse, depositari centrali)
  - Organismi di investimento collettivo (licenze di gestione fondi)

**Requisiti chiave**:

- **Resilienza operativa**: Gestione dei rischi ICT, continuità operativa, ripristino dopo disastri
- **Esternalizzazione**: Gestione dei rischi di terze parti, due diligence, contratti, strategie di uscita
- **Protezione dei dati**: Sicurezza, riservatezza e disponibilità dei dati dei clienti
- **Segnalazione degli incidenti**: Incidenti operativi significativi alla FINMA
- **Controlli interni**: Governance, gestione dei rischi, audit interno
- **Registro di sub-esternalizzazione** (Circolare FINMA 2023/1 Sezione 15): Le banche devono tenere un registro degli accordi di sub-esternalizzazione in cui i fornitori di servizi delegano ulteriormente servizi rilevanti. Il registro deve documentare: identità del sub-appaltatore, servizi forniti, accesso ai dati, ubicazione geografica, valutazione dei rischi, stato di approvazione.

**Impatto sul SGSI**:

- Controlli rafforzati di continuità operativa e ripristino dopo disastri
- Gestione completa dei rischi di terze parti (A.5.19-23)
- Procedure di risposta agli incidenti e segnalazione (A.5.24-28)
- Strutture di governance e supervisione (A.5.1, 5.4)
- Trasparenza e approvazione della sub-esternalizzazione (A.5.19-23 S3)

**Valutazione**: Se l'organizzazione detiene una licenza o registrazione FINMA → **Conformità obbligatoria**

## Digital Operational Resilience Act (DORA)

**Normativa**: Regolamento (UE) 2022/2554 sulla resilienza operativa digitale del settore finanziario
**Data di applicazione**: 17 gennaio 2025

**Trigger di applicabilità**:

- L'organizzazione è un'**entità finanziaria nell'UE**:
  - Istituti di credito (banche)
  - Istituti di pagamento e istituti di moneta elettronica
  - Imprese di investimento
  - Fornitori di servizi per cripto-attività
  - Imprese di assicurazione e riassicurazione
  - Fornitori terzi di servizi ICT per entità finanziarie (designazione critica/importante)

**Requisiti chiave**:

- **Gestione dei rischi ICT**: Framework completo che copre identificazione, protezione, rilevamento, risposta e ripristino
- **Segnalazione degli incidenti**: Incidenti ICT rilevanti alle autorità competenti
- **Test di resilienza operativa digitale**: Test regolari inclusi test di penetrazione basati sulle minacce (TLPT)
- **Rischi di terze parti**: Supervisione dei fornitori ICT, contratti, strategie di uscita
- **Condivisione delle informazioni**: Scambio di informazioni sulle minacce e sulla cybersicurezza

**Impatto sul SGSI**:

- Framework avanzato di gestione dei rischi ICT (oltre ISO 27001)
- Rilevamento e risposta agli incidenti rafforzati (A.5.24-28)
- Programmi di test di resilienza obbligatori
- Gestione dei rischi dei fornitori con supervisione normativa (A.5.19-23)
- Accordi di condivisione delle informazioni

**Valutazione**: Se l'organizzazione è un'entità finanziaria UE o un fornitore ICT critico → **Conformità obbligatoria**

## Direttiva sulla sicurezza delle reti e dei sistemi informativi 2 (NIS2)

**Direttiva**: Direttiva (UE) 2022/2555 recante misure per un livello comune elevato di cybersicurezza
**Scadenza di recepimento**: 17 ottobre 2024 (gli Stati membri UE devono recepire nel diritto nazionale)

**Trigger di applicabilità**:

- L'organizzazione è un'**entità essenziale o importante** nell'UE nei settori coperti:

**Entità essenziali** (requisiti più stringenti): Energia, trasporti, settore bancario, sanità, acqua potabile e acque reflue, infrastrutture digitali, gestione dei servizi ICT (MSP, MSSP), pubblica amministrazione, spazio.

**Entità importanti** (requisiti meno stringenti): Servizi postali, gestione dei rifiuti, produzione chimica, produzione alimentare, produzione manifatturiera, fornitori digitali, organizzazioni di ricerca.

**Requisiti chiave**:

- **Gestione dei rischi**: Valutazione dei rischi di cybersicurezza e politiche di sicurezza
- **Gestione degli incidenti**: Capacità di rilevamento, risposta e ripristino
- **Continuità operativa**: Gestione dei backup, ripristino dopo disastri
- **Sicurezza della supply chain**: Gestione dei rischi di terze parti
- **Sicurezza delle reti**: Controlli di accesso, cifratura, autenticazione a più fattori
- **Notifica degli incidenti**: Allerta precoce entro 24 ore, rapporto dettagliato entro 72 ore al CSIRT/autorità competente nazionale
- **Supervisione**: Audit periodici, valutazioni di sicurezza, monitoraggio ex post

**Sanzioni**: Fino a 10 milioni EUR o 2% del fatturato annuo mondiale (entità essenziali), 7 milioni EUR o 1,4% (entità importanti)

**Valutazione**: Se l'organizzazione opera in un settore coperto nell'UE e soddisfa le soglie di dimensione/criticità → **Conformità obbligatoria**

## Payment Card Industry Data Security Standard (PCI DSS v4.0.1)

**Standard**: PCI DSS v4.0.1 (in vigore dal 31 marzo 2024)
**Organismo di governance**: PCI Security Standards Council

**Trigger di applicabilità**:

- L'organizzazione **archivia, elabora o trasmette** dati dei titolari di carta:
  - Esercenti che accettano carte di credito/debito
  - Elaboratori di pagamenti e gateway
  - Fornitori di servizi che gestiscono dati dei titolari di carta
  - Qualsiasi entità con accesso all'ambiente dei dati dei titolari di carta (CDE)

**Requisiti chiave** — 12 requisiti in 6 obiettivi di controllo:

1. Installare e mantenere controlli di sicurezza della rete
2. Applicare configurazioni sicure a tutti i componenti del sistema
3. Proteggere i dati dell'account archiviati
4. Proteggere i dati dei titolari di carta con crittografia robusta durante la trasmissione
5. Proteggere sistemi e reti da software dannoso
6. Sviluppare e mantenere sistemi e software sicuri
7. Limitare l'accesso ai dati dei titolari di carta in base alla necessità di conoscere
8. Identificare gli utenti e autenticare l'accesso ai componenti del sistema
9. Limitare l'accesso fisico ai dati dei titolari di carta
10. Registrare e monitorare tutti gli accessi ai componenti del sistema e ai dati dei titolari di carta
11. Testare regolarmente la sicurezza di sistemi e reti
12. Supportare la sicurezza delle informazioni con politiche e programmi organizzativi

**Valutazione**: Se l'organizzazione gestisce carte di pagamento → **Conformità obbligatoria**

## Regolamento UE sull'intelligenza artificiale (AI Act)

**Normativa**: Regolamento (UE) 2024/1689 che stabilisce regole armonizzate sull'intelligenza artificiale
**Data di entrata in vigore**: 1° agosto 2024 (implementazione graduale fino ad agosto 2028)

**Trigger di applicabilità**:

- L'organizzazione è un **fornitore** (sviluppa o commissiona sistemi AI immessi sul mercato UE)
- L'organizzazione è un **deployer** (utilizza sistemi AI sotto la propria autorità nell'UE)
- L'organizzazione è un **importatore o distributore** di sistemi AI nell'UE
- Gli output dei sistemi AI riguardano persone ubicate nell'UE

**Classificazione del rischio** (determina il livello di obblighi):

| Livello di rischio | Esempi | Obblighi chiave |
|--------------------|--------|----------------|
| **Inaccettabile** | Punteggio sociale, identificazione biometrica in tempo reale, tecniche di manipolazione | **Vietato** |
| **Alto rischio** | Decisioni occupazionali, scoring creditizio, accesso a servizi essenziali, infrastrutture critiche | Valutazione di conformità, gestione dei rischi, governance dei dati, trasparenza, supervisione umana, documentazione |
| **Rischio limitato** | Chatbot, riconoscimento delle emozioni, generazione di deepfake | Obblighi di trasparenza |
| **Rischio minimo** | Filtri antispam, strumenti di sviluppo assistiti da AI | Nessun obbligo specifico |

**Calendario di implementazione**:

- **Febbraio 2025**: Divieti sui sistemi AI a rischio inaccettabile
- **Agosto 2025**: Obblighi per i modelli AI di uso generale
- **Dicembre 2027**: Piena applicazione per i sistemi AI ad alto rischio (rinviata da agosto 2026 dal Digital Omnibus, Regolamento (UE) 2026/1744, in vigore dal 27 luglio 2026)
- **Agosto 2028**: AI ad alto rischio in prodotti regolamentati (rinviata da agosto 2027 dallo stesso Digital Omnibus)

**Valutazione**: Se l'organizzazione sviluppa, distribuisce o commercializza sistemi AI che riguardano persone nell'UE → Valutare la classificazione del rischio e gli obblighi applicabili

## Health Insurance Portability and Accountability Act (HIPAA)

**Normativa**: Legge federale statunitense che protegge le informazioni sanitarie

**Trigger di applicabilità**: L'organizzazione è un'**entità coperta** o un **business associate** che gestisce informazioni sanitarie protette (PHI) statunitensi.

**Valutazione**: Se l'organizzazione tratta dati sanitari statunitensi (PHI) → **Conformità obbligatoria**

## Normative condizionali aggiuntive

| Normativa | Trigger di applicabilità | Regione/Ambito |
|-----------|--------------------------|----------------|
| **Sarbanes-Oxley (SOX)** | Società quotata in borsa statunitense | Stati Uniti |
| **GLBA** | Istituto finanziario statunitense | Stati Uniti |
| **CCPA/CPRA** | Trattamento di dati di residenti californiani | California, USA |
| **PIPL (Cina)** | Trattamento di informazioni personali di residenti cinesi | Cina |
| **LGPD** | Trattamento di dati personali brasiliani | Brasile |
| **Settoriale** | Dipendente dal settore (telecom, energia, pharma) | Variabile |

---

# Riferimento informativo / Buone pratiche (Livello 3)

Questi framework forniscono **orientamenti tecnici e buone pratiche** ma non sono giuridicamente vincolanti:

## Pubblicazioni speciali NIST (serie SP 800)

**Descrizione**: Orientamenti di cybersicurezza del National Institute of Standards and Technology
**Applicabilità**: Adozione volontaria per le buone pratiche (salvo richiesta da contratti FISMA/FedRAMP)

**Pubblicazioni chiave**: NIST SP 800-53 (controlli di sicurezza e privacy), NIST Cybersecurity Framework (CSF), NIST SP 800-61 (gestione degli incidenti), NIST SP 800-63 (identità digitale)

## CIS Controls

**Descrizione**: Controlli critici di sicurezza del Center for Internet Security
**Versione**: CIS Controls v8.1 (18 controlli)
**Applicabilità**: Adozione volontaria per il benchmarking della sicurezza

## OWASP (Open Web Application Security Project)

**Descrizione**: Standard di sicurezza delle applicazioni web portati dalla comunità
**Risorse chiave**: OWASP Top 10, OWASP ASVS, OWASP SAMM, OWASP Cheat Sheets

## ISO/IEC 27002:2022

**Descrizione**: Codice di buone pratiche per i controlli di sicurezza delle informazioni
**Applicabilità**: Orientamento di supporto per l'implementazione di ISO 27001 (non certificabile separatamente)

## Cloud Security Alliance (CSA)

**Descrizione**: Buone pratiche di sicurezza del cloud computing
**Framework chiave**: CSA Cloud Controls Matrix (CCM), CSA STAR, CAIQ

## Framework aggiuntivi di riferimento

| Framework | Descrizione | Caso d'uso |
|-----------|-------------|------------|
| **COBIT** | Governance e gestione IT | Allineamento alla governance IT |
| **ITIL** | Gestione dei servizi IT | Processi di erogazione dei servizi |
| **ISO 22301** | Gestione della continuità operativa | Struttura del programma BCM |
| **ISO 27017/27018** | Sicurezza e privacy nel cloud | Controlli specifici per il cloud |
| **Linee guida ENISA** | Orientamenti dell'agenzia europea per la cybersicurezza | Contesto normativo UE |

---

# Requisiti federali statunitensi (Categoria speciale)

**Principio**: I requisiti federali statunitensi di cybersicurezza (FISMA, FIPS, FedRAMP, NIST CSF 2.0) si applicano **solo quando l'organizzazione ha obblighi contrattuali federali statunitensi espliciti**.

**Stato predefinito**: **Non applicabile**, salvo se:

- L'organizzazione detiene contratti federali statunitensi
- L'organizzazione fornisce servizi ad agenzie federali statunitensi
- Il contratto richiede esplicitamente controlli NIST o autorizzazione FedRAMP

**Utilizzo nel SGSI**:

- I framework NIST possono essere utilizzati come **riferimento informativo** (Livello 3)
- FISMA/FedRAMP diventano **obbligatori** (Livello 1) solo con contratti federali

---

# Determinazione dell'applicabilità normativa

## Processo di valutazione

Le organizzazioni DEVONO condurre valutazioni annuali di applicabilità normativa:

**Passo 1**: Identificare le attività aziendali (ubicazioni geografiche, settori, tipi di dati elaborati, base clienti, servizi forniti)

**Passo 2**: Mappare le normative alle attività:

| Attività aziendale | Normative attivate |
|--------------------|--------------------|
| Trattamento di dati di residenti UE | RGPD (obbligatorio) |
| Operazioni in Svizzera | LPD svizzera (obbligatorio) |
| Obiettivo di certificazione ISO 27001 | ISO 27001 (obbligatorio) |
| Elaborazione di carte di pagamento | PCI DSS v4.0.1 (condizionale — se sì, obbligatorio) |
| Servizi finanziari UE | DORA (condizionale — se sì, obbligatorio) |
| Sviluppo/distribuzione di sistemi AI che riguardano l'UE | AI Act UE (condizionale — se sì, obbligatorio) |
| Contratti federali statunitensi | FISMA/FedRAMP (condizionale — se sì, obbligatorio) |

**Passo 3**: Documentare la determinazione di applicabilità, creare una matrice di applicabilità normativa, documentare la motivazione, assegnare la responsabilità, aggiornare annualmente.

## Modello di matrice di applicabilità normativa

| Normativa | Livello | Stato | Trigger | Responsabile | Ultima revisione | Rivisto da | Approvato da |
|-----------|---------|--------|---------|-------------|------------------|------------|--------------|
| LPD svizzera | 1 - Obbligatorio | Applicabile | Operazioni svizzere | RPD | [Data] | [Nome RPD] | [Direzione] |
| RGPD UE | 1 - Obbligatorio | Applicabile | Dati clienti UE | RPD | [Data] | [Nome RPD] | [Direzione] |
| ISO 27001 | 1 - Obbligatorio | Applicabile | Obiettivo di certificazione | RSSI | [Data] | [Nome RSSI] | [Direzione] |
| DORA | 2 - Condizionale | Non applicabile | Non è un'entità finanziaria | N/A | [Data] | [RSSI/Legale] | [RSSI] |
| PCI DSS v4.0.1 | 2 - Condizionale | Applicabile | Elaborazione carte | RSSI | [Data] | [Nome RSSI] | [Direzione] |
| AI Act UE | 2 - Condizionale | [Da valutare] | Sviluppo/distribuzione sistemi AI | RSSI | [Data] | [RSSI/Legale] | [TBD] |
| NIST SP 800-53 | 3 - Informativo | Solo riferimento | Orientamento tecnico | RSSI | [Data] | [Nome RSSI] | [RSSI] |

## Quando rivalutare

**Trigger per la rivalutazione**:

- Nuova linea di business o offerta di servizi
- Espansione in nuovi mercati geografici
- Acquisizione o fusione
- Nuovi contratti con clienti con requisiti normativi
- Modifiche normative (nuove leggi, standard aggiornati)
- Modifiche all'ambito della certificazione ISO 27001

**Frequenza**: Annuale minimo + rivalutazioni attivate

**Responsabilità**: RSSI + Legale/Conformità + RPD (monitoraggio trimestrale), approvazione della Direzione generale (revisione annuale completa)

## Approccio di monitoraggio per le normative condizionali

| Normativa | Metodo di monitoraggio | Frequenza | Responsabile |
|-----------|------------------------|-----------|-------------|
| **DORA** | Revisione dei contratti con clienti per clausole di conformità DORA | Trimestrale | RSSI + Legale |
| **NIS2** | Monitoraggio dei piani di sviluppo aziendale per espansione nei settori coperti | Trimestrale + Ad hoc | RSSI + Legale |
| **FINMA** | Monitoraggio dello sviluppo aziendale per richieste di licenza di servizi finanziari | Trimestrale | Legale + RSSI |
| **PCI DSS** | Monitoraggio delle decisioni di elaborazione dei pagamenti | Trimestrale | RSSI |
| **AI Act UE** | Monitoraggio delle decisioni di sviluppo/distribuzione di sistemi AI | Trimestrale + Attivato | RSSI |
| **HIPAA** | Monitoraggio dei tipi di dati dei clienti | Trimestrale | RPD + RSSI |

**Escalation**: Se il monitoraggio rileva un probabile trigger di applicabilità → Avviare una valutazione dettagliata entro 30 giorni → Aggiornare la matrice Sezione 8 → Informare la Direzione generale in caso di transizione Livello 2 → Livello 1.

---

# Utilizzo nelle politiche del SGSI

## Formulazione di riferimento standard

Tutte le politiche del SGSI DEVONO includere una delle seguenti formulazioni:

**Opzione A: Riferimento Sezione 1.3** (consigliata per la maggior parte delle politiche):

```markdown
## Applicabilità dei framework normativi

I riferimenti a standard, framework e normative in questo SGSI sono
categorizzati ai sensi di ISMS-POL-00 (Quadro di applicabilità normativa):

**Conformità obbligatoria:**

- Legge federale svizzera sulla protezione dei dati (LPD)
- RGPD UE (in caso di trattamento di dati personali di residenti UE)
- ISO/IEC 27001:2022
- [Normative obbligatorie aggiuntive ai sensi di ISMS-POL-00]

**Riferimento informativo / Allineamento alle buone pratiche:**

- Pubblicazioni speciali NIST (serie SP 800)
- [Altri framework ai sensi di ISMS-POL-00]

**Requisiti federali statunitensi:**
I framework federali statunitensi (FISMA, FedRAMP, NIST) si applicano solo
in presenza di obblighi contrattuali federali statunitensi espliciti
(cfr. ISMS-POL-00, sezione Requisiti federali statunitensi).

Per la categorizzazione normativa completa, consultare ISMS-POL-00.
```

---

# Manutenzione e aggiornamenti

## Calendario di revisione

**Revisione trimestrale** (RSSI + Legale + RPD): Monitorare le modifiche normative, tracciare i cambiamenti organizzativi, aggiornare la matrice se i trigger cambiano.

**Revisione annuale** (approvazione della Direzione generale): Valutazione completa del panorama normativo, aggiornamento di ISMS-POL-00, approvazione degli obblighi di conformità.

**Revisione attivata**: Pubblicazione di una nuova normativa, espansione aziendale, fusione/acquisizione, contratto importante con nuovi requisiti normativi.

**Responsabilità**:

- **Monitoraggio normativo**: Responsabile legale/conformità (principale), RSSI (supporto)
- **Valutazione dell'applicabilità**: RSSI + Legale/Conformità + RPD (responsabilità congiunta)
- **Aggiornamenti della matrice**: RSSI (proprietario), RPD (normative di protezione dei dati)
- **Aggiornamenti della politica**: RSSI (autore), Direzione generale (approvazione)

---

# Stato normativo attuale

**Stato della valutazione di applicabilità (al [Data]):**

## Livello 1: Conformità obbligatoria (Attiva)

| Normativa | Motivazione di applicabilità | Stato di implementazione | Prossima revisione |
|-----------|------------------------------|--------------------------|-------------------|
| **LPD svizzera** | ✅ Applicabile — Organizzazione con sede in Svizzera | Controlli implementati (A.5.12-14, A.5.34) | [Data + 12 mesi] |
| **RGPD UE** | ✅ Applicabile — Trattamento di dati personali di residenti UE tramite relazioni con clienti | Controlli implementati (A.5.34, A.8.11, A.8.10) | [Data + 12 mesi] |
| **ISO/IEC 27001:2022** | ✅ Applicabile — Persegue la certificazione | 48/93 controlli implementati (52%), Fase 1 raggiunta | Continuativo |

## Livello 2: Applicabilità condizionale

### Attualmente non applicabile (sotto monitoraggio)

| Normativa | Stato valutazione | Decisione attuale | Trigger di monitoraggio | Responsabile |
|-----------|------------------|-------------------|------------------------|-------------|
| **DORA** | ✅ Valutato | **Non applicabile** | Cambio modello di business | RSSI + Legale |
| **NIS2** | ✅ Valutato | **Non applicabile** | Espansione in settori coperti | RSSI + Legale |
| **PCI DSS v4.0.1** | ✅ Valutato | **Non applicabile** | Inizio elaborazione carte | RSSI |
| **FINMA** | ✅ Valutato | **Non applicabile** | Acquisizione licenza FINMA | Legale + RSSI |

### In corso di valutazione (decisione in attesa)

| Normativa | Stato valutazione | Completamento previsto | Responsabile |
|-----------|------------------|------------------------|-------------|
| **AI Act UE** | 🔄 In corso | TBD — in attesa di atti delegati | RSSI + Legale |

## Livello 3: Riferimento informativo (Uso attivo)

| Framework | Utilizzo | Referenziato in |
|-----------|----------|-----------------|
| **NIST SP 800** | Orientamenti di implementazione tecnica | Vari controlli Allegato A |
| **CIS Controls v8.1** | Benchmarking della sicurezza | Analisi interna delle lacune |
| **OWASP** | Pratiche di sviluppo sicuro | A.8.25-28 |
| **ISO/IEC 27002:2022** | Orientamenti di implementazione dei controlli | Tutti i controlli Allegato A |

## Riferimenti dettagliati ai requisiti

| Normativa | Documento di riferimento | Stato di manutenzione |
|-----------|--------------------------|----------------------|
| **DORA** | ISMS-REF-DORA | Mantenuto |
| **FINMA** | ISMS-REF-FINMA | Mantenuto |
| **NIS2** | ISMS-REF-NIS2 | Mantenuto |
| **PCI DSS v4.0.1** | ISMS-REF-PCI-DSS | Mantenuto |
| **AI Act UE** | ISMS-REF-EU-AI-ACT | In sviluppo |

---

# Glossario

| Termine | Definizione |
|---------|-------------|
| **Applicabile** | La normativa si applica all'organizzazione in base alle sue attività, deve conformarsi |
| **Condizionale** | La normativa si applica solo se si verificano trigger specifici (settore, geografia, tipo di dati) |
| **Obbligatorio** | Obbligo legale, applicabile per legge o contratto, il mancato rispetto ha conseguenze |
| **Informativo** | Riferimento per le buone pratiche, non giuridicamente vincolante, adozione volontaria |
| **Livello 1** | Conformità obbligatoria (legale, contrattuale) |
| **Livello 2** | Conformità condizionale (dipendente dal contesto) |
| **Livello 3** | Riferimento informativo (buone pratiche, volontario) |
| **Forza vincolante** | Applicabilità legale o contrattuale di una normativa |
| **Obbligo di implementazione** | Requisito di implementare controlli specifici (determinato attraverso la valutazione del rischio) |
| **Monitoraggio normativo** | Revisione trimestrale sistematica delle modifiche normative e degli eventi trigger organizzativi |
| **Trigger di applicabilità** | Evento o condizione che fa passare una normativa condizionale (Livello 2) a obbligatoria (Livello 1) |
| **Valutazione attivata** | Valutazione di applicabilità normativa non pianificata avviata dal rilevamento di un trigger |

---

# Allegato A: Calendari di implementazione normativa

| Normativa | Date chiave di implementazione | Rilevanza organizzativa |
|-----------|-------------------------------|------------------------|
| **DORA** | **17 gennaio 2025**: Piena applicazione per le entità finanziarie | Monitorare: Se l'organizzazione diventa entità finanziaria UE prima del 2025-01-17 |
| **AI Act UE** | **Feb 2025**: Divieti; **Ago 2025**: AI di uso generale; **Dic 2027**: Alto rischio (rinviata da ago 2026 dal Digital Omnibus, Regolamento (UE) 2026/1744); **Ago 2028**: Alto rischio in prodotti regolamentati (rinviata da ago 2027) | Monitorare: Scadenze applicabili ai sistemi AI sviluppati/distribuiti |
| **PCI DSS v4.0.1** | **31 marzo 2024**: v4.0 in vigore; **31 marzo 2025**: Nuovi requisiti obbligatori | Non applicabile attualmente. Se inizia l'elaborazione delle carte → v4.0 applicabile immediatamente |
| **NIS2** | **17 ottobre 2024**: Recepimento nazionale UE | Monitorare: Implementazioni nazionali che possono influire sulla determinazione dell'applicabilità |

---

# Dichiarazione conclusiva

La presente politica stabilisce l'applicabilità normativa per il Sistema di Gestione della Sicurezza delle Informazioni dell'organizzazione.

**Separazione delle responsabilità:**

- **Questa politica (POL-00)**: Definisce QUALI normative si applicano
- **Gestione del rischio (Clausola 6)**: Determina COME rispondere ai requisiti normativi
- **Implementazione dei controlli (Allegato A)**: Implementa i CONTROLLI SPECIFICI
- **Monitoraggio della conformità**: Verifica e traccia lo STATO DI CONFORMITÀ

---

**FINE DI ISMS-POL-00-IT**

*«L'applicabilità normativa è il fondamento. L'implementazione e la conformità sono la struttura costruita su di esso.»*

<!-- QA_VERIFIED: 2026-07-31 -->
