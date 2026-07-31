<!-- ISMS-CORE:POLICY:PRIV-POL-00-IT:privacy:POL:00 -->
**PRIV-POL-00 — Quadro di applicabilità normativa sulla privacy**
**Riferimento autorevole per gli obblighi di conformità del SGDP**

---

## Controllo del documento

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Quadro di applicabilità normativa sulla privacy |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | PRIV-POL-00 |
| **Autore del documento** | Responsabile della Protezione dei Dati (RPD) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 0.1 | [Data - 8 sett.] | RPD | Bozza iniziale — struttura del quadro a tre livelli, perimetro RGPD + LPD |
| 0.2 | [Data - 6 sett.] | RPD + Legale | Aggiunta dei livelli ISO 27701:2025 e ISO 27018:2025; condizioni di perimetro internazionale |
| 0.3 | [Data - 4 sett.] | RSSI | Allineamento con la metodologia ISMS-POL-00; aggiunta di riferimenti cloud e sicurezza cloud |
| 0.4 | [Data - 2 sett.] | RPD/Legale/RSSI | Incorporazione dei feedback delle parti interessate; aggiunta della nota ISO 27017 in arrivo |
| 1.0 | [Data] | RPD/Legale/RSSI | Prima versione approvata |

**Ciclo di revisione** : Annuale (o in caso di significativi cambiamenti normativi, nuove pubblicazioni di standard, o cambiamenti del perimetro di certificazione)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :

- Principale: Responsabile della Protezione dei Dati (RPD)
- Secondaria: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Conformità: Responsabile Legale/Conformità
- Autorità finale: Direzione generale

**Documenti correlati** :

- PRIV-POL-01 — Quadro di governance e processo decisionale sulla privacy
- ISMS-POL-00 — Quadro di applicabilità normativa (base SGSI — co-riferimento obbligatorio)
- ISO/IEC 27701:2025 Clausola 5.2 (Comprensione delle esigenze e aspettative delle parti interessate)
- ISO/IEC 27701:2025 Clausola 5.3 (Determinazione del perimetro del SGDP)
- Tutti i documenti di politica SGDP (riferimento obbligatorio)

**Distribuzione** : Tutte le parti interessate SGDP, responsabili della protezione dei dati, autori di politiche, proprietari di sistemi, revisori, responsabili del trattamento
**Referenziato da** : Tutti i documenti di politica SGDP (PRIV-POL-01, tutti i POL dei gruppi di controllo PRIV-POL-A.x.x)

**Strategia linguistica** : Laddove i termini tecnici o normativi siano stabiliti a livello internazionale (es. RGPD, ISO/IEC, LPD, DCP), la terminologia inglese viene mantenuta per preservare la precisione e facilitare i riferimenti normativi transfrontalieri.

---

## Riepilogo esecutivo

Questo documento costituisce il **riferimento autorevole** per interpretare l'applicabilità normativa e dei quadri di riferimento sulla privacy nell'intero Sistema di Gestione della Privacy (SGDP).

**Scopo** : Eliminare ambiguità e incoerenze nei riferimenti alle leggi sulla protezione dei dati, alle normative e agli standard nell'intera documentazione SGDP.

**Perimetro** : Tutti i riferimenti alle leggi sulla protezione dei dati, alle normative sulla privacy e ai quadri di protezione dei dati nella documentazione SGDP.

**Relazione con il SGSI** : Questa politica è il complemento specifico alla privacy di **ISMS-POL-00** (Quadro di applicabilità normativa). ISMS-POL-00 disciplina gli obblighi di sicurezza delle informazioni. PRIV-POL-00 disciplina gli obblighi di privacy e protezione dei dati. Laddove gli obblighi si sovrappongono (es. Articolo 32 del RGPD — sicurezza del trattamento), ISMS-POL-00 prevale per la dimensione sicurezza delle informazioni; PRIV-POL-00 disciplina la dimensione protezione dei dati.

**Principio chiave** : **L'applicabilità normativa sulla privacy deve essere esplicita, non presupposta.** I riferimenti alle normative e ai quadri di riferimento sulla privacy rientrano in tre categorie:

1. **Conformità obbligatoria** — Obblighi legali applicabili all'organizzazione
2. **Applicabilità condizionale** — Requisiti che si applicano solo in circostanze specifiche
3. **Riferimento informativo** — Migliori pratiche e orientamenti tecnici

**Utilizzo** : Tutte le politiche SGDP DEVONO includere una sezione «Quadro normativo» che fa riferimento a questo documento, identificando a quale livello appartiene ogni normativa/standard citato.

**Termini chiave** : Le definizioni dei termini utilizzati in questa politica (Obbligatorio, Condizionale, Livello 1/2/3, Trigger di applicabilità, DCP, Interessato, Titolare del trattamento, Responsabile del trattamento) sono fornite nel **Glossario** alla fine di questo documento.

---

## Autorità della politica e confini

### Scopo e perimetro di questa politica

Questa politica definisce l'**identificazione e l'applicabilità** dei requisiti legali, normativi e contrattuali per il Sistema di Gestione della Privacy dell'organizzazione.

**Questa politica stabilisce :**

- Quali leggi e standard sulla privacy si applicano all'organizzazione
- La categorizzazione degli obblighi in materia di privacy (Obbligatorio, Condizionale, Informativo)
- La metodologia di valutazione per determinare l'applicabilità
- I processi di revisione e aggiornamento per i cambiamenti normativi

**Questa politica NON stabilisce :**

- Le decisioni di trattamento dei rischi per la privacy (trattate nella gestione dei rischi SGDP)
- I requisiti di implementazione dei controlli (trattati nei POL e IMP dei gruppi di controllo)
- Lo stato di conformità o la verifica (trattati nei processi di monitoraggio della conformità)
- Gli obblighi di sicurezza delle informazioni (trattati in ISMS-POL-00)

Il risultato della valutazione dell'applicabilità normativa sulla privacy serve da **input** per:

- Le decisioni di perimetro dei controlli in tutti i gruppi di controllo SGDP
- La prioritizzazione della valutazione e del trattamento dei rischi per la privacy
- Le decisioni di proporzionalità per l'implementazione dei controlli (obblighi titolare vs. responsabile del trattamento)
- La pianificazione degli audit e la verifica della conformità

**Principio di delimitazione** : Questa politica stabilisce l'applicabilità normativa sulla privacy. L'implementazione, l'applicazione e la verifica sono gestite attraverso processi SGDP distinti e politiche dei gruppi di controllo.

**Integrazione con ISO 27701:2025 :**

- **Clausola 5.2 (Parti interessate)** : I requisiti normativi sulla privacy costituiscono i principali obblighi delle parti interessate. Questa politica li identifica esplicitamente.
- **Clausola 5.3 (Perimetro)** : La determinazione del perimetro è influenzata dalle normative di Livello 1 applicabili e dal ruolo dell'organizzazione (titolare del trattamento, responsabile del trattamento, o entrambi).
- **Clausola 6 (Valutazione dei rischi)** : Gli obblighi normativi alimentano il registro dei rischi SGDP. Livello 1 = alta priorità, Livello 2 condizionale = priorità media, Livello 3 = contributo informativo.

**Integrazione con ISMS-POL-00 :**

Questa politica opera accanto a e in subordine a ISMS-POL-00 per tutte le questioni di sicurezza delle informazioni. Laddove una normativa presenta sia dimensioni di privacy che di sicurezza (es. RGPD Articolo 32, CH-nLPD Articolo 7), gli obblighi vengono affrontati congiuntamente. PRIV-POL-00 disciplina l'interpretazione della privacy; ISMS-POL-00 disciplina l'interpretazione della sicurezza.

---

## Categorie di applicabilità normativa

**Conformità obbligatoria**
Obblighi legali o contrattuali di privacy che l'organizzazione DEVE rispettare. Il mancato rispetto comporta responsabilità legale, sanzioni normative, indagini dell'autorità di controllo o perdita della certificazione.

**Caratteristiche** :

- Eseguibile dall'autorità di protezione dei dati (APD) o da un tribunale
- Il mancato rispetto ha conseguenze legali/finanziarie (sanzioni, provvedimenti coercitivi)
- Richiede prove documentate di conformità (registri di trattamento, DPIA, registrazioni del consenso)
- Soggetto ad audit normativi, ispezioni e poteri delle autorità di controllo

**Applicabilità condizionale**
Requisiti di privacy che si applicano solo quando vengono soddisfatte condizioni specifiche (es. tipi specifici di dati trattati, perimetro geografico, certificazione ricercata, contratti con i clienti, modello di servizio cloud).

**Caratteristiche** :

- L'applicabilità dipende dalle attività di trattamento, dai tipi di dati o dal perimetro geografico
- Può diventare obbligatoria in base alle attività commerciali o ai requisiti contrattuali
- Richiede una rivalutazione periodica al variare delle attività commerciali e di trattamento

**Riferimento informativo / Allineamento alle migliori pratiche**
Quadri e standard utilizzati per orientamenti tecnici e organizzativi, benchmark o allineamento volontario. Questi informano le pratiche in materia di privacy ma non costituiscono requisiti di conformità obbligatori.

**Caratteristiche** :

- Adozione volontaria per le migliori pratiche
- Nessun meccanismo legale diretto di esecuzione
- Utilizzato per l'implementazione delle misure tecniche e organizzative (MTO)
- Può diventare obbligatorio se referenziato in contratti o requisiti di certificazione

---

## Gerarchia di conformità

```
┌─────────────────────────────────────────────────────────────────┐
│           GERARCHIA DI CONFORMITÀ SULLA PROTEZIONE DEI DATI     │
├─────────────────────────────────────────────────────────────────┤
│  LIVELLO 1: OBBLIGATORIO (Legale/Contrattuale)                  │
│  • RGPD UE (se trattamento di dati personali UE)                │
│  • Legge federale svizzera sulla protezione dei dati (LPD/nLPD) │
│                                                                 │
│  LIVELLO 2: CONDIZIONALE (Dipendente dal contesto)              │
│  • ISO/IEC 27701:2025 (se certificazione ricercata o            │
│    contrattualmente richiesta)                                  │
│  • ISO/IEC 27018:2025 (responsabili del trattamento DCP cloud)  │
│  • UK GDPR (se trattamento di dati personali brit.              │
│    post-Brexit)                                                 │
│  • LGPD (se trattamento di dati personali brasiliani)           │
│  • PIPL (se trattamento di dati personali cinesi)               │
│  • Altre leggi nazionali (valutazione basata su trigger)        │
│                                                                 │
│  LIVELLO 3: INFORMATIVO (Migliori pratiche / Orientamenti tecn.)│
│  • ISO/IEC 27017:2026 (base sicurezza cloud per 27018;          │
│    sostituisce l'edizione 2015 — adozione formale in sospeso)   │
│  • ISO/IEC 27002:2022 (implementazione controlli sicurezza)     │
│  • NIST Privacy Framework 2.0 (gestione dei rischi di privacy)  │
└─────────────────────────────────────────────────────────────────┘
```

> *Se i caratteri di cornice non vengono visualizzati correttamente, fare riferimento alle sezioni seguenti per le definizioni dei livelli.*

---

# Conformità obbligatoria (Livello 1)

> **Nota sulla classificazione ISO/IEC 27701:2025** : ISO/IEC 27701:2025 è classificata **Livello 2 (Condizionale)** in questo quadro. Non è una normativa giuridicamente eseguibile. Diventa obbligatoria per [Organizzazione] quando la certificazione è attivamente ricercata o quando un contratto con un cliente la richiede esplicitamente. Laddove nessuna di queste condizioni si applica, funziona come un quadro di migliori pratiche volontario. Vedere la sezione ISO/IEC 27701:2025 nel Livello 2 per tutti i dettagli.

## Regolamento Generale sulla Protezione dei Dati (RGPD) dell'UE

**Applicabilità** : Quando si trattano dati a carattere personale di residenti UE/SEE, indipendentemente da dove è stabilita l'organizzazione.

**Requisiti chiave** :

- Articolo 5 : Principi del trattamento (liceità, correttezza, trasparenza, limitazione della finalità, minimizzazione dei dati, esattezza, limitazione della conservazione, integrità e riservatezza, responsabilità)
- Articolo 6 : Liceità del trattamento
- Articoli 7–9 : Requisiti del consenso e dati di categoria speciale
- Articoli 13–14 : Informazioni da fornire agli interessati (informative sulla privacy)
- Articoli 15–22 : Diritti degli interessati (accesso, rettifica, cancellazione, limitazione, portabilità, opposizione, decisione automatizzata)
- Articolo 24 : Responsabilità del titolare del trattamento (accountability, politiche, misure)
- Articolo 25 : Protezione dei dati fin dalla progettazione e per impostazione predefinita
- Articolo 28 : Obblighi del responsabile del trattamento (contratto scritto, misure di sicurezza, controlli dei sub-responsabili)
- Articolo 30 : Registro delle attività di trattamento (RAT)
- Articolo 32 : Sicurezza del trattamento (cifratura, pseudonimizzazione, resilienza, test)
- Articoli 33–34 : Notifica delle violazioni (72 ore all'APD; senza indebito ritardo agli interessati per le violazioni ad alto rischio)
- Articoli 35–36 : Valutazione d'impatto sulla protezione dei dati (DPIA) per i trattamenti ad alto rischio; consultazione preventiva dell'APD quando il rischio residuo rimane elevato
- Articoli 37–39 : Obblighi del Responsabile della Protezione dei Dati (RPD) dove applicabile
- Articoli 44–49 : Restrizioni sui trasferimenti internazionali di dati

**Impatto sul SGDP** :

- Protezione dei dati fin dalla progettazione e per impostazione predefinita in tutte le attività di trattamento
- Registri delle attività di trattamento (RAT) tenuti dal titolare del trattamento e dal responsabile del trattamento
- Base giuridica documentata per ogni attività di trattamento
- Procedure dei diritti degli interessati implementate e testate
- Contratti di trattamento conformi all'Articolo 28 in atto
- Processo DPIA per i trattamenti ad alto rischio
- Procedura di notifica delle violazioni con scadenza di 72 ore
- Garanzie per i trasferimenti internazionali (decisioni di adeguatezza, Clausole Contrattuali Standard, BCR)

**Autorità di controllo** : Autorità di protezione dei dati (APD) UE/SEE competente dello stabilimento principale o del paese dell'interessato.

**Riferimento** : Regolamento (UE) 2016/679, in vigore dal 25 maggio 2018

---

## Legge federale svizzera sulla protezione dei dati (LPD/nLPD)

**Applicabilità** : Tutti i trattamenti di dati a carattere personale da parte dell'organizzazione soggetti alla giurisdizione svizzera; e qualsiasi trattamento di dati a carattere personale di residenti svizzeri dall'estero quando gli effetti si producono in Svizzera.

**Requisiti chiave** :

- Articolo 6 : Principi (liceità, buona fede, proporzionalità, limitazione della finalità)
- Articolo 7 : Sicurezza dei dati (misure tecniche e organizzative appropriate al rischio)
- Articolo 8 : Trattamento dei dati da parte di responsabili del trattamento (accordo scritto, sicurezza, sub-responsabili)
- Articolo 9 : Comunicazione all'estero (decisione di adeguatezza o garanzie appropriate)
- Articolo 10 : Rappresentanti in Svizzera (in assenza di stabilimento)
- Articolo 12 : Registro delle attività di trattamento (per titolari con >250 ETP o trattamento ad alto rischio)
- Articoli 19–21 : Obbligo di fornire informazioni (informative sulla privacy agli interessati)
- Articolo 22 : Valutazione d'impatto sulla protezione dei dati (DPIA) per i trattamenti ad alto rischio
- Articolo 25 : Protezione dei dati fin dalla progettazione e per impostazione predefinita
- Articolo 26 : Diritti degli interessati (accesso, rettifica, cancellazione, limitazione, portabilità, opposizione)
- Articolo 24 : Notifica delle violazioni all'IFPDT quando si rischia un danno elevato
- Articolo 328b CO : Sorveglianza dei dipendenti e protezione della personalità

**Allineamento LPD/RGPD** : La LPD riveduta (in vigore dal 1° settembre 2023) è sostanzialmente allineata con il RGPD in termini di struttura e principi. Per le organizzazioni soggette a entrambe, un programma allineato al RGPD soddisfa generalmente i requisiti della LPD. Differenze principali: la LPD non prevede l'obbligo di RPD; la lista di adeguatezza svizzera differisce dall'UE; nessun regime di sanzioni amministrative (sanzioni penali invece).

**Impatto sul SGDP** :

- Registro di trattamento tenuto (Art. 12)
- Contratti di trattamento conformi all'Art. 8 in atto
- Informative sulla privacy fornite agli interessati (Art. 19–21)
- Processo DPIA per i trattamenti ad alto rischio (Art. 22)
- Notifica delle violazioni ad alto rischio all'IFPDT
- Garanzie per i trasferimenti internazionali quando i dati lasciano la Svizzera

**Autorità di controllo** : Incaricato federale della protezione dei dati e della trasparenza (IFPDT — Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter, EDÖB)

**Riferimento** : Legge federale sulla protezione dei dati (RS 235.1), in vigore dal 1° settembre 2023

---

# Applicabilità condizionale (Livello 2)

Queste normative e standard si applicano **solo quando vengono soddisfatte condizioni specifiche**.

## ISO/IEC 27701:2025 — Sistema di Gestione della Privacy (SGDP)

**Standard** : ISO/IEC 27701:2025 (Seconda edizione) — Sistema di gestione della privacy delle informazioni

**Trigger di applicabilità** :

- L'organizzazione **ricerca la certificazione ISO/IEC 27701:2025** (autonoma o combinata con la certificazione ISO 27001)
- Un contratto con un cliente **richiede esplicitamente** la conformità SGDP con questo standard

**Nota di classificazione** : ISO/IEC 27701:2025 è classificata Livello 2 (Condizionale) in questo quadro. Non è una normativa giuridicamente eseguibile. Non diventa obbligatoria semplicemente perché l'organizzazione tratta DCP — il RGPD e la LPD svolgono questo ruolo. Laddove la certificazione è ricercata o contrattualmente richiesta, viene trattata come un impegno operativo vincolante equivalente al Livello 1 per la durata della certificazione.

**Requisiti chiave** :

- Clausola 5 : Contesto del SGDP (comprensione dell'organizzazione, delle parti interessate, del perimetro)
- Clausola 6 : Leadership (impegno, politica, ruoli, responsabilità)
- Clausola 7 : Pianificazione (rischi, obiettivi, trigger di privacy by design)
- Clausola 8 : Supporto (risorse, competenza, consapevolezza, comunicazione, informazioni documentate)
- Clausola 9 : Operazione (pianificazione operativa, trattamento dei rischi, processo DPIA)
- Clausola 10 : Valutazione delle prestazioni (monitoraggio, audit interno, revisione della direzione)
- Clausola 11 : Miglioramento (non conformità, azione correttiva, miglioramento continuo)
- Allegato A : Controlli specifici per il titolare del trattamento (A.1.x — 31 controlli)
- Allegato A : Controlli specifici per il responsabile del trattamento (A.2.x — 18 controlli)
- Allegato A : Controlli di sicurezza condivisi (A.3.x — 29 controlli)
- Allegato B : Mappatura dei controlli ISO/IEC 27001:2022 al SGDP (normativa)

**Impatto sul SGDP** :

- Implementazione completa di tutte le politiche dei gruppi di controllo PRIV-POL-A.x.x in 51-isms-core-privacy/
- Determinazione del ruolo documentata (titolare del trattamento, responsabile del trattamento, o entrambi per attività di trattamento)
- SGDP integrato con o sovrapposto all'ISO 27001 SGSI

**Nota sull'edizione** : ISO/IEC 27701:2025 (Seconda edizione) è uno standard SGDP autonomo, non un insieme di clausole di estensione per ISO 27001. Può essere implementato e certificato indipendentemente. Laddove un'organizzazione detenga una certificazione ISO 27001, l'Allegato B fornisce la mappatura normativa tra i controlli 27001 e i requisiti 27701.

**Riferimento** : ISO/IEC 27701:2025, Sicurezza delle informazioni, cybersecurity e protezione della privacy — Sistema di gestione della privacy delle informazioni

---

## ISO/IEC 27018:2025 — Responsabili del trattamento DCP in cloud

**Standard** : ISO/IEC 27018:2025 (Terza edizione) — Tecnologia dell'informazione — Tecniche di sicurezza — Codice di pratica per la protezione dei dati a carattere personale (DCP) nei cloud pubblici che agiscono come responsabili del trattamento di DCP

**Trigger di applicabilità** :

- L'organizzazione agisce come **responsabile del trattamento DCP che gestisce servizi cloud pubblici** (fornitore di servizi cloud che tratta DCP dei clienti)
- I contratti con i clienti **richiedono esplicitamente** la conformità o la certificazione ISO/IEC 27018
- La certificazione a ISO/IEC 27018:2025 è ricercata

**Contenuto di ISO 27018:2025** :

ISO 27018:2025 comprende due parti distinte:

- **Corpo (Clausole 5–18)** : Orientamenti di implementazione per i controlli ISO/IEC 27002:2022 negli ambienti cloud pubblici. Questi orientamenti sono informativi nel contesto e non creano requisiti obbligatori aggiuntivi oltre ISO 27002.
- **Allegato A (normativo durante la certificazione)** : 25 controlli specifici ai DCP non presenti in ISO 27002. Questi sono i genuini nuovi obblighi dei responsabili del trattamento DCP in cloud (consenso, trasparenza, limitazione della finalità, restituzione/cancellazione, divulgazione dei sub-responsabili, ecc.).

**Fornitura SGDP** : I controlli Allegato A di ISO 27018 (25 controlli) sono forniti come overlay di corrispondenza su `priv-a.2.5.7-9-sub-processor-management` e i pack responsabili adiacenti. NON sono pack autonomi.

**Valutazione** : Se l'organizzazione fornisce servizi cloud pubblici e tratta DCP dei clienti → valutare l'Allegato A di ISO 27018:2025 per l'applicabilità.

**Riferimento** : ISO/IEC 27018:2025, Terza edizione, 2025

---

## Regolamento generale sulla protezione dei dati del Regno Unito (UK GDPR)

**Normativa** : UK GDPR (diritto UE conservato come modificato dalle Data Protection, Privacy and Electronic Communications (Amendments etc) (EU Exit) Regulations 2019) + Data Protection Act 2018, come ulteriormente modificato dal **Data (Use and Access) Act 2025**

**Trigger di applicabilità** :

- L'organizzazione **tratta dati a carattere personale di residenti britannici** post-Brexit (1° gennaio 2021)
- L'organizzazione ha uno **stabilimento nel Regno Unito**
- L'organizzazione **punta o monitora individui** nel Regno Unito

**Differenze principali rispetto al RGPD UE** :

- Autorità di controllo: Information Commissioner's Office (ICO), non APD UE
- Trasferimenti internazionali: normative di adeguatezza britanniche (non decisioni di adeguatezza UE); trasferimento UE→UK coperto dalla decisione di adeguatezza UE per UK (in vigore al momento della redazione — monitorare la revisione)
- Clausole Contrattuali Standard britanniche (IDTA) o UK Addendum alle CCS UE richieste per i trasferimenti verso paesi terzi
- **Data (Use and Access) Act 2025** : Introduce modifiche mirate specifiche al UK degli obblighi di protezione dei dati; il RPD valuta l'impatto per le organizzazioni con operazioni nel UK in corso

**Valutazione** : Se l'organizzazione tratta dati personali britannici → la conformità al UK GDPR è richiesta parallelamente al RGPD UE. Per la maggior parte delle organizzazioni CH/UE con operazioni nel UK o clienti britannici, questo sarà obbligatorio. Monitorare gli orientamenti dell'ICO sull'implementazione del Data (Use and Access) Act 2025.

**Riferimento** : UK GDPR; Data Protection Act 2018 (UK); Data (Use and Access) Act 2025

---

## Lei Geral de Proteção de Dados (LGPD) — Brasile

**Normativa** : Lei n° 13.709/2018 — Lei Geral de Proteção de Dados Pessoais

**Trigger di applicabilità** :

- L'organizzazione **tratta dati a carattere personale di individui situati in Brasile**
- Il trattamento **avviene in Brasile** (indipendentemente dallo stabilimento)
- Il trattamento ha **lo scopo di offrire beni o servizi** in Brasile

**Requisiti chiave** (struttura allineata al RGPD) :

- Basi giuridiche del trattamento (10 basi giuridiche, inclusi consenso e interesse legittimo)
- Diritti degli interessati (accesso, rettifica, cancellazione, portabilità, opposizione)
- Obblighi del Responsabile della Protezione dei Dati (RPD/Encarregado)
- Notifica degli incidenti di sicurezza all'ANPD (APD brasiliana) e agli interessati
- Trasferimenti internazionali: decisione di adeguatezza, clausole contrattuali o consenso

**Valutazione** : Se l'organizzazione serve clienti brasiliani o tratta dati personali brasiliani → valutare l'applicabilità della LGPD. Strutturalmente simile al RGPD; un programma allineato al RGPD copre la maggior parte dei requisiti.

**Autorità di controllo** : Autoridade Nacional de Proteção de Dados (ANPD)

**Riferimento** : Lei n° 13.709/2018, in vigore da settembre 2020 (applicazione da agosto 2021)

---

## Legge sulla protezione delle informazioni personali (PIPL) — Cina

**Normativa** : Personal Information Protection Law (个人信息保护法), in vigore dal 1° novembre 2021

**Trigger di applicabilità** :

- L'organizzazione **tratta informazioni personali di individui situati in Cina**
- L'organizzazione fornisce **prodotti o servizi** rivolta a individui in Cina
- L'organizzazione **analizza il comportamento** di individui in Cina

**Requisiti chiave** :

- Il consenso come base giuridica principale (perimetro dell'interesse legittimo più ristretto rispetto al RGPD)
- Localizzazione dei dati: le informazioni personali di individui cinesi raccolte in Cina possono richiedere l'archiviazione locale
- Trasferimenti transfrontalieri: tre meccanismi disponibili — (1) valutazione della sicurezza da parte del CAC richiesta per i trasferimenti superiori alle soglie di volume; (2) contratto standard (CCS) per volumi inferiori; (3) certificazione di protezione delle informazioni personali da parte di un organismo riconosciuto (per i trasferimenti all'interno di gruppi multinazionali — vedere le disposizioni attuative del CAC)
- Responsabile della Protezione dei Dati: richiesto se il trattamento supera le soglie
- Notifica delle violazioni entro 24 ore al regolatore

**Valutazione** : Se l'organizzazione offre servizi a o raccoglie dati personali da individui in Cina → è richiesta una valutazione dell'applicabilità della PIPL. Nota: la PIPL è più restrittiva del RGPD sotto diversi aspetti (consenso predefinito, localizzazione, controlli dei trasferimenti transfrontalieri).

**Autorità di controllo** : Cyberspace Administration of China (CAC — 国家互联网信息办公室)

**Riferimento** : PIPL 2021; Disposizioni del CAC sui contratti standard per il trasferimento transfrontaliero di dati personali (2023)

---

## Normative condizionali aggiuntive sulla privacy

Le organizzazioni dovrebbero valutare e documentare normative aggiuntive sulla protezione dei dati in base alle loro specifiche attività di trattamento e al loro perimetro geografico:

| Normativa | Trigger | Autorità di controllo |
|-----------|---------|----------------------|
| **CCPA/CPRA** (California) | Residenti californiani; soglie di fatturato/dati | California Privacy Protection Agency (CPPA) |
| **PIPEDA** (Canada) | Trattamento commerciale di dati personali canadesi | Office of the Privacy Commissioner of Canada (OPC) |
| **PDPA** (Singapore) | Trattamento di dati personali di residenti singaporiani | Personal Data Protection Commission (PDPC) |
| **APPI** (Giappone) | Trattamento di informazioni personali di residenti giapponesi | Personal Information Protection Commission (PPC) |
| **POPIA** (Sud Africa) | Trattamento di informazioni personali di residenti sudafricani | Information Regulator |
| **Normative settoriali** | Sanità (e-health), dati finanziari, dati di minori | Autorità competente del settore |

**Approccio di valutazione** : Per ogni nuovo mercato geografico o attività di trattamento, valutare se si applica una normativa sulla protezione dei dati utilizzando i trigger sopra indicati. Documentare la determinazione nel registro di monitoraggio normativo (vedere la sezione Manutenzione).

---

# Riferimento informativo / Migliori pratiche (Livello 3)

## ISO/IEC 27017:2015 — Controlli di sicurezza per i servizi cloud

**Standard** : ISO/IEC 27017:2015 — Tecnologia dell'informazione — Tecniche di sicurezza — Codice di pratica per i controlli di sicurezza delle informazioni basati su ISO/IEC 27002 per i servizi cloud

**Ruolo in PRIV-POL-00** : ISO 27017 è uno standard di **sicurezza cloud** (non uno standard di privacy). È referenziato qui come base tecnica di supporto perché ISO 27018:2025 (Allegato A — controlli dei responsabili del trattamento DCP in cloud) si basa direttamente sul fondamento di sicurezza stabilito da ISO 27017. Le organizzazioni che implementano ISO 27018 devono trattare i controlli ISO 27017 come il fondamento di sicurezza per gli ambienti di trattamento DCP in cloud.

**Riferimento principale** : ISO 27017 è referenziato in **ISMS-POL-00** (Livello 3) come migliore pratica di sicurezza cloud. La sua presenza in PRIV-POL-00 è solo come riferimento di supporto alla privacy.

**Aree di orientamento chiave** (rilevanti per il trattamento DCP in cloud) :

- Responsabilità condivisa tra cliente cloud e fornitore di servizi cloud
- Indurimento e isolamento delle macchine virtuali
- Sicurezza operativa degli amministratori
- Monitoraggio dei servizi cloud
- Sicurezza di rete negli ambienti cloud

**Utilizzo nel SGDP** : Referenziato in `priv-a.2.4.2-4-processor-lifecycle-controls` e `priv-a.2.5.7-9-sub-processor-management` (pack overlay ISO 27018).

**Riferimento** : ISO/IEC 27017:2015, Controlli di sicurezza delle informazioni per i servizi cloud

---

## ISO/IEC 27017:2026 — Pubblicata (Adozione formale in sospeso)

**Stato** : **Pubblicata** (2026), sostituisce l'edizione 2015. Le azioni alla pubblicazione seguenti sono in sospeso.

ISO/IEC 27017:2026 è la seconda edizione dello standard sui controlli di sicurezza per i servizi cloud. Questa politica sarà aggiornata per referenziare ISO/IEC 27017:2026 al posto di (o accanto a) ISO/IEC 27017:2015 una volta completate le azioni alla pubblicazione seguenti.

**Azioni alla pubblicazione** :

1. Esaminare ISO/IEC 27017:2026 per le modifiche strutturali rispetto all'edizione 2019
2. Valutare l'impatto sui pack di controllo `priv-a.2.4.2-4` e `priv-a.2.5.7-9`
3. Aggiornare il riferimento di Livello 3 di PRIV-POL-00 dall'edizione 2019 all'edizione 2026
4. Comunicare le modifiche ai proprietari dei gruppi di controllo pertinenti
5. Aggiornare gli IMP dei pack di controllo dove sono referenziati gli orientamenti 27017

**Monitorare** : Pubblicazioni ISO.org — programma di lavoro SC 27 — WG 4 (Controlli e servizi di sicurezza)

---

## ISO/IEC 27002:2022 — Orientamenti sull'implementazione dei controlli di sicurezza

**Standard** : ISO/IEC 27002:2022 — Sicurezza delle informazioni, cybersecurity e protezione della privacy — Controlli di sicurezza delle informazioni

**Ruolo in PRIV-POL-00** : ISO 27002 fornisce orientamenti di implementazione per i controlli di sicurezza condivisi A.3.x (Allegato A.3 di ISO 27701:2025). I 29 controlli condivisi A.3 sono overlay specifici alla privacy sul quadro di controlli di sicurezza delle informazioni stabilito da ISO 27002.

**Riferimento** : ISO/IEC 27002:2022

---

## NIST Privacy Framework 2.0

**Quadro** : NIST Privacy Framework: Uno strumento per migliorare la privacy attraverso la gestione dei rischi aziendali, Versione 2.0 (2024)

**Ruolo in PRIV-POL-00** : Riferimento informativo per la metodologia di gestione dei rischi di privacy. Fornisce un vocabolario basato sulle funzioni (Identify-P, Govern-P, Control-P, Communicate-P, Protect-P) per la valutazione della maturità del programma di privacy. La versione 2.0 si allinea più strettamente con il NIST Cybersecurity Framework 2.0, aggiungendo la funzione Govern-P e rafforzando gli orientamenti sui rischi di privacy nella supply chain. Può essere utilizzato per l'analisi dei gap e il benchmark della valutazione dei rischi di privacy.

**Riferimento** : NIST Privacy Framework v2.0, NIST, 2024

---

# Determinazione dell'applicabilità normativa sulla privacy

## Processo di valutazione

Quando si valuta se una normativa sulla protezione dei dati si applica all'organizzazione, seguire questo processo decisionale:

**Passo 1: Identificare le attività di trattamento**

Documentare ogni categoria di trattamento dei DCP: quali dati, di chi (interessati), in quali territori, per quale finalità, in qualità di titolare del trattamento o responsabile del trattamento.

**Passo 2: Applicare i trigger geografici**

Per ogni normativa, valutare il trigger di applicabilità rispetto alla mappa dei trattamenti:

| Tipo di trigger | Domande |
|----------------|---------|
| **Stabilimento** | L'organizzazione è stabilita nella giurisdizione? |
| **Localizzazione degli interessati** | Esistono individui nella giurisdizione i cui dati vengono trattati? |
| **Targeting / Monitoraggio** | L'organizzazione punta o monitora individui nella giurisdizione? |
| **Fornitura di servizi** | L'organizzazione offre beni/servizi nella giurisdizione? |

**Passo 3: Determinare il ruolo titolare/responsabile del trattamento**

Gli obblighi di privacy differiscono significativamente in base al ruolo:

- **Titolare del trattamento** : Determina le finalità e i mezzi del trattamento → Gli obblighi completi di Livello 1 si applicano (RGPD Articoli 5–39)
- **Responsabile del trattamento** : Tratta per conto del titolare → Gli obblighi specifici del responsabile si applicano (RGPD Articolo 28; ISO 27701 Allegato A.2)
- **Entrambi** : Dove l'organizzazione agisce come titolare per alcuni trattamenti e responsabile per altri → Gli obblighi si applicano per attività di trattamento

**Passo 4: Classificare e documentare**

| Risultato | Azione |
|---------|--------|
| Normativa applicabile — senza condizioni | Classificare Livello 1 (Obbligatorio) |
| Normativa applicabile solo se condizione soddisfatta | Classificare Livello 2 (Condizionale) — documentare il trigger |
| Standard che fornisce orientamenti — non giuridicamente eseguibile | Classificare Livello 3 (Informativo) |
| Normativa esplicitamente non applicabile | Documentare come Non Applicabile con motivazione |

**Passo 5: Aggiornare i registri**

Aggiornare il Registro normativo sulla privacy (tenuto nel repository di documentazione SGDP) con la determinazione, la motivazione e la data di revisione.

---

## Modello di matrice di applicabilità normativa sulla privacy

Utilizzare questo modello per documentare l'applicabilità di ogni normativa:

| Normativa | Livello | Si applica? | Trigger | Data di valutazione | Valutatore | Prossima revisione |
|-----------|---------|------------|--------|---------------------|-----------|-------------------|
| RGPD UE | 1 | Sì/No | Trattamento di interessati UE | [Data] | RPD | Annualmente |
| LPD svizzera | 1 | Sì/No | Operazioni svizzere | [Data] | RPD | Annualmente |
| ISO 27701:2025 | 1/2 | Sì/No | Certificazione ricercata | [Data] | RSSI | Annualmente |
| ISO 27018:2025 | 2 | Sì/No | Responsabile del trattamento DCP cloud | [Data] | RSSI | Annualmente |
| UK GDPR | 2 | Sì/No | Interessati britannici | [Data] | RPD/Legale | Annualmente |
| LGPD | 2 | Sì/No | Interessati brasiliani | [Data] | Legale | Annualmente |
| PIPL | 2 | Sì/No | Interessati cinesi | [Data] | Legale | Annualmente |

---

## Quando rivalutare

| Evento trigger | Azione richiesta |
|---------------|-----------------|
| Nuovo mercato geografico | Valutazione completa dell'applicabilità per quella giurisdizione |
| Nuova attività di trattamento (nuovo prodotto, servizio, tipo di dati) | Ruolo titolare/responsabile + normative applicabili |
| Passaggio dal trattamento on-premise al cloud | Valutazione ISO 27018:2025 |
| Contratto con il cliente con requisiti espliciti di privacy | Aggiornamento del livello specifico al contratto |
| Nuova normativa pubblicata o adottata | Valutare l'applicabilità, aggiornare il registro |
| Normativa esistente sostanzialmente modificata | Rivalutare la classificazione del livello interessato |
| Pubblicazione di ISO 27017:2026 | Aggiornare il riferimento di Livello 3; valutare l'impatto sui pack di controllo |
| Cambiamento aziendale (acquisizione, nuova entità, outsourcing) | Rivalutazione completa dell'applicabilità per le attività interessate |

---

# Utilizzo nelle politiche SGDP

## Linguaggio di riferimento standard

Tutte le politiche dei gruppi di controllo SGDP (PRIV-POL-01 e tutti i POL dei gruppi di controllo PRIV-POL-A.x.x) DEVONO includere una sezione **Quadro normativo** utilizzando questo riferimento standard:

```
## Quadro normativo

Questa politica opera all'interno del quadro normativo sulla privacy
stabilito in PRIV-POL-00.
I seguenti obblighi sono pertinenti per questo gruppo di controllo:

**Obbligatorio (Livello 1):**
- RGPD UE: [articoli specifici pertinenti per questo gruppo di controllo]
- LPD svizzera: [articoli specifici]
- ISO/IEC 27701:2025: [clausole/controlli specifici]

**Condizionale (Livello 2):**
- ISO/IEC 27018:2025: [controlli Allegato A, se pack responsabili del trattamento]

**Informativo (Livello 3):**
- ISO/IEC 27017:2015: [se controlli relativi al cloud]
```

## Etichettatura dei ruoli nei pack di controllo

Le politiche dei gruppi di controllo DEVONO indicare chiaramente il ruolo organizzativo affrontato:

- Pack `privacy-controller/` → **«Questa politica si applica all'organizzazione che agisce come Titolare del trattamento dei DCP.»**
- Pack `privacy-processor/` → **«Questa politica si applica all'organizzazione che agisce come Responsabile del trattamento dei DCP.»**
- Pack `privacy-shared/` → **«Questa politica si applica all'organizzazione che agisce sia come Titolare del trattamento che come Responsabile del trattamento dei DCP.»**

---

# Quadro normativo (questa politica)

## Conformità obbligatoria

| Normativa | Versione | Stato | Pertinenza per il SGDP |
|-----------|---------|-------|----------------------|
| RGPD UE | 2016/679 | In vigore — Obbligatorio | Tutti i gruppi di controllo PRIV-POL-A.x.x |
| LPD svizzera/nLPD | RS 235.1 (2023) | In vigore — Obbligatorio | Tutti i gruppi di controllo PRIV-POL-A.x.x |

## Applicabilità condizionale

| Normativa | Versione | Stato | Trigger |
|-----------|---------|-------|--------|
| ISO/IEC 27701:2025 | Ed. 2, 2025 | Condizionale | Certificazione ricercata o contrattualmente richiesta |
| ISO/IEC 27018:2025 | Ed. 3, 2025 | Condizionale | Servizi cloud di responsabile del trattamento DCP |
| UK GDPR + DUA Act 2025 | 2018/2021/2025 | Condizionale | Interessati britannici |
| LGPD | 2018 | Condizionale | Interessati brasiliani |
| PIPL | 2021 | Condizionale | Interessati cinesi |

## Riferimento informativo

| Standard | Versione | Stato | Utilizzo |
|---------|---------|-------|---------|
| ISO/IEC 27017:2015 | 2015 | In vigore — Livello 3 | Base di sicurezza cloud (supporta l'implementazione 27018) |
| ISO/IEC 27017:2026 | Pubblicata (2026) | Azioni alla pubblicazione in sospeso | Sostituisce l'edizione 2015 |
| ISO/IEC 27002:2022 | 2022 | In vigore — Livello 3 | Orientamenti sui controlli di sicurezza per i controlli condivisi A.3 |
| NIST Privacy Framework | 2.0, 2024 | In vigore — Livello 3 | Metodologia di gestione dei rischi di privacy |

## Riferimenti di audit

| Requisito | Prova | Posizione |
|---------|-------|---------|
| Applicabilità normativa documentata | Questa politica + Registro normativo sulla privacy | Repository di documentazione SGDP |
| Registrazioni APD aggiornate | Certificati di registrazione | Fascicolo Legale/Conformità |
| RAT tenuto | Registri delle attività di trattamento | [Piattaforma GRC / Sistema SGSI] |
| Processo DPIA documentato | Modello DPIA + DPIA completate | [Piattaforma GRC] |
| Contratti di trattamento in atto | DPA firmati per RGPD Art. 28 | Repository dei contratti |

---

# Stato normativo attuale

## Livello 1: Conformità obbligatoria (Attivo)

| Normativa | Base di applicabilità | Confermato | Prossima revisione |
|-----------|---------------------|-----------|-------------------|
| RGPD UE | Trattamento di dati personali UE | [Data] | [Data + 12M] |
| LPD svizzera | Operazioni basate in Svizzera | [Data] | [Data + 12M] |

## Livello 2: Applicabilità condizionale

| Normativa | Stato attuale | Stato del trigger | Azione |
|-----------|--------------|-----------------|--------|
| ISO 27701:2025 | [Applicabile / Non applicabile] | [Certificazione ricercata o contrattualmente richiesta?] | [Trattare come impegno vincolante se applicabile] |
| ISO 27018:2025 | [Applicabile / Non applicabile] | [Servizi cloud di responsabile del trattamento DCP nel perimetro?] | [Implementare overlay Allegato A se applicabile] |
| UK GDPR + DUA Act 2025 | [Applicabile / Non applicabile] | [Interessati britannici nel perimetro?] | [Documentare se applicabile; monitorare gli orientamenti ICO DUA] |
| LGPD | [Applicabile / Non applicabile] | [Interessati brasiliani nel perimetro?] | [Valutare se applicabile] |
| PIPL | [Applicabile / Non applicabile] | [Interessati cinesi nel perimetro?] | [Valutare se applicabile] |

## Livello 3: Riferimento informativo (Utilizzo attivo)

| Standard | Utilizzo | Referenziato in |
|---------|---------|--------------|
| ISO/IEC 27017:2015 | Base di sicurezza cloud | Pack responsabili del trattamento priv-a.2.4 e priv-a.2.5 |
| ISO/IEC 27002:2022 | Orientamenti sui controlli di sicurezza | Tutti i pack di controllo condivisi A.3 |
| NIST Privacy Framework 2.0 | Riferimento di metodologia dei rischi | Documentazione di valutazione dei rischi SGDP |

---

# Manutenzione e aggiornamenti

## Programma di revisione

| Tipo di revisione | Frequenza | Responsabile | Deliverable |
|------------------|-----------|-------------|------------|
| Revisione annuale completa | Annuale (Q4) | RPD + RSSI + Legale | Politica aggiornata + nota alla direzione |
| Monitoraggio trimestrale | Trimestrale | RPD + Legale | Aggiornamento del registro di monitoraggio normativo |
| Valutazione innescata | Su evento trigger | RPD (lead) | Rapporto di valutazione |
| Valutazione d'impatto ISO 27017:2026 | A completamento delle azioni alla pubblicazione | RSSI | Valutazione dell'impatto sui pack di controllo |

## Fonti di monitoraggio normativo

| Fonte | Frequenza di monitoraggio | Responsabile |
|-------|--------------------------|------------|
| Gazzetta Ufficiale UE (eur-lex.europa.eu) | Mensile | Legale |
| Linee guida e pareri dell'EDPB/CEPD (edpb.europa.eu) | Mensile | RPD |
| Pubblicazioni dell'IFPDT (edoeb.admin.ch) | Trimestrale | RPD |
| ISO.org — pubblicazioni SC 27 | Trimestrale | RSSI |
| Orientamenti ICO (UK) | Trimestrale (se UK nel perimetro) | Legale |
| Orientamenti delle APD nazionali (Stati membri) | Trimestrale | RPD |

## Comunicazione

Le modifiche a questa politica DEVONO essere comunicate a:

- Tutti i proprietari di politiche dei gruppi di controllo SGDP
- Responsabili della privacy / proprietari dei dati
- Responsabili del trattamento sotto contratto con l'organizzazione
- Audit interno

---

# Documenti correlati

| Documento | Tipo | Relazione |
|---------|-----|---------|
| ISMS-POL-00 | Politica SGSI | Principale — quadro normativo sulla sicurezza delle informazioni |
| PRIV-POL-01 | Politica SGDP | Politica gemella — governance e processo decisionale sulla privacy |
| priv-a.1.2.6-9 POL | Politica di gruppo di controllo | Governance e registri sulla privacy (titolare del trattamento) |
| priv-a.3.13-16 POL | Politica di gruppo di controllo | Conformità e audit sulla privacy (condiviso) |
| ISO/IEC 27701:2025 | Standard | Standard di governance principale |
| ISO/IEC 27018:2025 | Standard | Standard supplementare per i responsabili del trattamento DCP in cloud |

---

# Glossario

| Termine | Definizione |
|---------|-------------|
| **DCP** | Dati a Carattere Personale — qualsiasi informazione che può essere utilizzata per identificare direttamente o indirettamente una persona fisica (equivalente a «dati personali» nel RGPD/LPD) |
| **Interessato** | La persona fisica alla quale si riferiscono i DCP (equivalente a «PII Principal») |
| **Titolare del trattamento** | L'entità che determina le finalità e i mezzi del trattamento dei DCP (RGPD: «data controller») |
| **Responsabile del trattamento** | L'entità che tratta i DCP per conto del titolare del trattamento (RGPD: «data processor») |
| **Trattamento** | Qualsiasi operazione effettuata sui DCP: raccolta, registrazione, conservazione, adattamento, consultazione, uso, comunicazione, cancellazione |
| **SGDP** | Sistema di Gestione della Privacy — il quadro del sistema di gestione stabilito secondo ISO/IEC 27701:2025 |
| **APD** | Autorità di Protezione dei Dati — l'autorità di controllo responsabile dell'applicazione della legge sulla privacy in una giurisdizione |
| **DPIA** | Data Protection Impact Assessment — valutazione strutturata delle attività di trattamento ad alto rischio |
| **RAT** | Registro delle Attività di Trattamento — documentazione richiesta dall'Articolo 30 del RGPD e dall'Articolo 12 della LPD |
| **Obbligatorio** | Obbligo legale, eseguibile dall'APD o da un tribunale, il mancato rispetto ha conseguenze |
| **Condizionale** | Si applica solo se vengono raggiunti trigger specifici (giurisdizione, tipo di dati, ruolo, certificazione) |
| **Informativo** | Riferimento per le migliori pratiche, non giuridicamente eseguibile, adozione volontaria |
| **Livello 1** | Conformità obbligatoria (legale, contrattuale) |
| **Livello 2** | Conformità condizionale (dipendente dal contesto) |
| **Livello 3** | Riferimento informativo (migliori pratiche, volontario) |
| **Trigger di applicabilità** | Evento o condizione che rende applicabile una normativa di Livello 2 |
| **Monitoraggio normativo** | Revisione trimestrale sistematica dei cambiamenti normativi e delle attività organizzative per rilevare le variazioni di applicabilità |


---

# Dichiarazione di chiusura

Questa politica stabilisce l'applicabilità normativa sulla privacy per il Sistema di Gestione della Privacy dell'organizzazione.

**Cosa stabilisce questa politica :**

- L'identificazione delle normative sulla protezione dei dati applicabili (obbligatorie, condizionali, informative)
- La metodologia di valutazione per determinare l'applicabilità normativa sulla privacy
- I processi di revisione e aggiornamento per i cambiamenti normativi

**Cosa questa politica NON stabilisce :**

- Le decisioni di trattamento dei rischi per la privacy (trattate nella gestione dei rischi SGDP e negli IMP dei gruppi di controllo)
- I requisiti di implementazione dei controlli (trattati nei POL e IMP dei gruppi di controllo PRIV-POL-A.x.x)
- Lo stato di conformità o la verifica (trattati nei processi di monitoraggio della conformità)
- Gli obblighi di sicurezza delle informazioni (trattati in ISMS-POL-00)

**Separazione delle responsabilità :**

- **Questa politica (PRIV-POL-00)** : Definisce QUALI normative sulla privacy si applicano
- **PRIV-POL-01** : Definisce COME il SGDP è gestito e COME vengono prese le decisioni
- **POL dei gruppi di controllo (PRIV-POL-A.x.x)** : Definiscono COSA l'organizzazione deve fare per dominio di controllo
- **IMP dei gruppi di controllo** : Definiscono COME implementare i requisiti di controllo
- **Monitoraggio della conformità** : Verifica e monitora lo stato di CONFORMITÀ

---

**FINE DI PRIV-POL-00**

*«L'applicabilità normativa sulla privacy è il fondamento. L'implementazione e la conformità sono la struttura costruita su di esso.»*

<!-- QA_VERIFIED: 2026-04-03 -->
