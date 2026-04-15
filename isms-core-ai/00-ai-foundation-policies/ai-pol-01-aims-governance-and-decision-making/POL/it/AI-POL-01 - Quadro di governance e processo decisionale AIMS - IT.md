<!-- ISMS-CORE:POLICY:AI-POL-01-IT:ai:POL:01 -->
**AI-POL-01 — Quadro di governance e processo decisionale AIMS**

---

## Controllo del documento

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Quadro di governance e processo decisionale AIMS |
| **Tipo di documento** | Politica |
| **ID documento** | AI-POL-01 |
| **Autore del documento** | Responsabile della Governance IA (RGIA) / Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto AIMS** | 1.0 |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data - 4 settimane] | RGIA | Bozza iniziale — confini di governance AIMS e quadro del processo decisionale |

**Ciclo di revisione**: Annuale (o in caso di modifiche significative all'AIMS o alla normativa)
**Data della prossima revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Primaria: Responsabile della Governance IA (o RSSI designato in assenza di una funzione dedicata alla governance IA)
- Secondaria: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Conformità: Responsabile Legale / Compliance
- Autorità finale: Direzione generale

**Documenti correlati**:

- AI-POL-00 (Quadro di applicabilità normativa IA — riferimento obbligatorio)
- ISMS-POL-01 (Quadro di governance e processo decisionale ISMS — documento di governance padre)
- ISO/IEC 42001:2023 Clausola 4.3 (Determinazione del perimetro dell'AIMS)
- ISO/IEC 42001:2023 Clausola 5.1 (Leadership e impegno)
- ISO/IEC 42001:2023 Clausola 5.2 (Politica IA)
- ISO/IEC 42001:2023 Clausola 5.3 (Ruoli, responsabilità e autorità)
- ISO/IEC 42001:2023 Clausola 9.2 (Audit interno)
- ISO/IEC 42001:2023 Clausola 9.3 (Riesame della direzione)
- ISO/IEC 42001:2023 Clausola 10.2 (Non conformità e azione correttiva)

**Distribuzione**: Tutti gli stakeholder AIMS, proprietari di sistemi IA, responsabili dei rischi IA, responsabili compliance, revisori interni/esterni
**Richiamato da**: Tutti i documenti di politica AIMS, Dichiarazione di Applicabilità (DDA) AIMS, Piano di trattamento dei rischi IA

---

## Sintesi esecutiva

La presente politica stabilisce **il contesto in cui il giudizio professionale viene esercitato** all'interno del Sistema di Gestione dell'IA (AIMS) dell'[Organizzazione], garantendo che:

- **Le decisioni di progettazione AIMS siano documentate e autorizzate** (interpretazione dei controlli, applicabilità normativa, accettazione dei rischi IA)
- **L'autorità decisionale sia chiaramente attribuita** (RGIA, RSSI, Legale, Direzione generale — competenza e perimetro)
- **I criteri AIMS evolvano attraverso processi controllati** (cambiamenti normativi, nuovi standard, orientamenti delle autorità, feedback dell'audit)
- **La verifica da parte dei revisori sia obiettiva e basata su prove** (i revisori verificano la progettazione documentata, senza reinterpretare i requisiti)

**Scopo**: Consentire una **verifica d'audit obiettiva** spostando il giudizio professionale nella **fase di progettazione AIMS** (politiche documentate, valutazioni dei rischi, decisioni di applicabilità) piuttosto che nella **fase di discussione dell'audit** (interpretazione soggettiva durante la certificazione).

**Perimetro**: Tutta l'autorità decisionale AIMS, le determinazioni dell'applicabilità normativa IA, la gestione delle eccezioni ai controlli, l'evoluzione dei criteri IA e i processi di revisione della governance.

**Principio fondamentale**: **La certificazione ISO/IEC 42001:2023 richiede giudizio professionale in due fasi:**

1. **Progettazione AIMS** (Responsabilità dell'organizzazione): Interpretare ISO 42001 nel contesto organizzativo, determinare i ruoli fornitore/operatore IA, selezionare i controlli basati sul rischio, definire la sufficienza delle prove
2. **Verifica AIMS** (Responsabilità del revisore): Valutare se l'interpretazione organizzativa soddisfa ISO 42001, verificare che l'implementazione corrisponda alla documentazione

La presente politica documenta il giudizio professionale organizzativo (Fase 1) per consentire una verifica d'audit obiettiva (Fase 2).

**Relazione con ISMS-POL-01**: La presente politica è il complemento specifico per l'IA di ISMS-POL-01. Ove i principi di governance si sovrappongano (escalation delle decisioni, requisiti di competenza, controllo delle modifiche), ISMS-POL-01 prevale per la governance della sicurezza delle informazioni. AI-POL-01 stabilisce le estensioni di governance specifiche per l'IA e l'autorità distinta del RGIA.

---

## Limiti di autorità e governance

### Scopo e perimetro

La presente politica definisce l'**autorità decisionale** per la governance AIMS, garantendo:

- Chiara attribuzione della responsabilità per l'interpretazione della conformità IA
- Processi documentati per l'applicabilità, le eccezioni e l'evoluzione
- Requisiti di competenza per i decisori della governance IA
- Criteri obiettivi per la verifica da parte dei revisori

**La presente politica stabilisce:**

- I confini dell'autorità per le decisioni AIMS (Sezione 2: chi decide cosa, con quale competenza)
- L'autorità di applicabilità normativa e dei controlli IA (Sezione 3: chi determina cosa si applica)
- I processi di accettazione dei rischi IA (Sezione 4: come vengono gestiti i rischi IA che non possono essere mitigati)
- Il controllo delle modifiche ai criteri AIMS (Sezione 5: come l'AIMS evolve nel tempo)
- Il monitoraggio dell'efficacia della governance (Sezione 6: come viene valutata la qualità della governance)

**La presente politica NON stabilisce:**

- Requisiti specifici di implementazione dei controlli IA (trattati nelle politiche di gruppo di controllo AI-POL-A.x.x e nei documenti IMP)
- La metodologia di valutazione dei rischi IA (trattata nella Procedura di valutazione dei rischi AIMS)
- Le procedure di controllo dei documenti (trattate nella Procedura di controllo dei documenti ai sensi della Clausola 7.5)
- Il programma di audit interno (trattato nella Procedura di audit interno ai sensi della Clausola 9.2)

**Principio di confine**: La presente politica stabilisce l'**autorità decisionale e i processi**. Le decisioni stesse sono documentate in **AI-POL-00 (applicabilità normativa), DDA AIMS (applicabilità dei controlli) e Registro di accettazione dei rischi IA (decisioni di trattamento dei rischi)**.

**Integrazione con ISO/IEC 42001:2023**:

- **Clausola 4.2 (Parti interessate)**: La presente politica formalizza l'autorità per l'interpretazione dei requisiti normativi IA
- **Clausola 4.3 (Perimetro)**: RGIA e RSSI raccomandano congiuntamente il perimetro AIMS; la Direzione generale approva
- **Clausola 5.1 (Leadership)**: Stabilisce il percorso di escalation delle decisioni che garantisce l'impegno dell'alta direzione
- **Clausola 5.2 (Politica IA)**: Il RGIA è proprietario della suite di politiche AIMS; il RSSI è co-proprietario ove gli obblighi IA e di sicurezza si sovrappongano
- **Clausola 5.3 (Ruoli)**: Definisce l'attribuzione dell'autorità per tutti i ruoli AIMS
- **Clausola 9.3 (Riesame della direzione)**: Fornisce il quadro di governance per il riesame annuale dell'AIMS
- **Clausola 10.1 (Miglioramento continuo)**: Consente il miglioramento dei processi di governance attraverso le lezioni apprese

---

## Limiti di autorità e competenza

### Autorità decisionale

| Livello di autorità | Ruolo | Perimetro decisionale | Requisito di competenza |
|--------------------|------|-----------------------|------------------------|
| **Primario** | RGIA | Progettazione dei controlli IA, interpretazione ISO 42001/Regolamento IA, autorità VISIA, processo di valutazione dei rischi IA, applicabilità normativa (Livelli 1/2 AI-POL-00), decisioni AIMS correnti | Conoscenza ISO 42001, competenza in governance IA (Lead Implementer/Auditor ISO 42001, IAPP AI Governance Certificate o equivalente), 3+ anni di esperienza in governance/rischio IA, indipendenza dalle operazioni IA |
| **Secondario** | RSSI | Misure di sicurezza IA tecniche, architettura di sicurezza dei sistemi IA, controlli Allegato A con dimensione sicurezza (A.6.2.4, A.6.2.6, A.7.4), integrazione con ISMS | Competenza in sicurezza delle informazioni (CISSP/CISM o equivalente), conoscenza ISO 27001/42001 |
| **Terziario** | Responsabile Legale / Compliance | Interpretazione giuridica degli obblighi IA (Regolamento IA UE, RGPD Art. 22), revisione dei contratti responsabile del trattamento/fornitore, coinvolgimento con le autorità normative, valutazione della conformità al Regolamento IA UE | Formazione giuridica, conoscenza della normativa IA, accesso a consulenza IA esterna |
| **Tecnico** | Chief Technology Officer (CTO) / Responsabile IA Engineering | Decisioni sull'architettura dei sistemi IA, controlli del ciclo di vita (A.6.x), governance dei dati (A.7.x), documentazione tecnica | Profonda competenza tecnica IA/ML, pratiche di ingegneria IA responsabile |
| **Approvazione** | Direzione generale (AD / Consiglio) | Decisioni IA strategiche, modifiche al perimetro AIMS, allocazione delle risorse, accettazione dei rischi IA, decisioni relative al portafoglio di sistemi IA | Responsabilità fiduciaria per il rischio IA, comprensione degli obblighi di accountability ISO 42001, autorità di bilancio |

**Indipendenza del RGIA**:

Il RGIA DEVE operare in piena indipendenza dalle funzioni di sviluppo e deployment dell'IA:

- Riporta direttamente all'AD o all'equivalente alta direzione
- Non riceve istruzioni dai team di sviluppo IA o dal product management in merito alle determinazioni di governance IA
- Non ha conflitti di interesse — non detiene autorità sulle decisioni di progettazione dei sistemi IA che potrebbero compromettere l'obiettività della governance
- Ha accesso a tutti i sistemi IA, alla documentazione e ai processi necessari per esercitare le funzioni di governance

In assenza di un ruolo RGIA dedicato, il RSSI assume l'autorità primaria con la condizione che le responsabilità di sicurezza IA e di governance IA siano esercitate in modo indipendente.

**Percorso di escalation delle decisioni**:

1. **Decisioni correnti** (progettazione dei controlli IA, formato delle prove, documentazione AIMS):
   - **Autorità**: RGIA
   - **Documentazione**: Documenti AIMS POL/IMP, registri VISIA
   - **Revisione**: Audit interno (Clausola 9.2), riesame annuale della direzione (Clausola 9.3)

2. **Interpretazione normativa** (attribuzioni dei livelli AI-POL-00, classificazione Regolamento IA UE, requisiti VIDF del Regolamento IA):
   - **Autorità**: Il RGIA determina l'applicabilità IA; il RSSI implementa le misure tecniche; il Legale esamina le dimensioni giuridiche
   - **Documentazione**: Matrice di applicabilità normativa AI-POL-00
   - **Revisione**: Monitoraggio trimestrale, revisione annuale completa

3. **Accettazione dei rischi IA** (esclusione di controllo IA o accettazione di rischio IA residuo):
   - **Autorità**: Il RGIA propone (con la valutazione dei rischi IA); la Direzione generale approva
   - **Documentazione**: Registro di accettazione dei rischi IA
   - **Revisione**: Riesame annuale della direzione (Clausola 9.3)

4. **Modifiche strategiche** (modifica del perimetro AIMS, modifica della determinazione del ruolo IA, espansione del portafoglio di sistemi IA in categorie ad alto rischio):
   - **Autorità**: Approvazione della Direzione generale (RGIA + RSSI raccomandano; AD/Consiglio decide)
   - **Documentazione**: Verbali del riesame della direzione (Clausola 9.3), verbali del Consiglio ove applicabile
   - **Revisione**: Nell'ambito del ciclo di pianificazione strategica organizzativa

**Requisiti obbligatori**:

1. Il RGIA **deve** approvare tutte le implementazioni dei controlli IA prima del deployment.
2. Il RGIA **deve** approvare tutte le determinazioni di applicabilità normativa (attribuzioni dei livelli AI-POL-00) prima della pubblicazione o dell'aggiornamento.
3. La Direzione generale **deve** approvare tutte le decisioni di accettazione dei rischi IA ai sensi della Clausola 6.1.3 di ISO 42001:2023.
4. Il RGIA **deve** essere consultato per qualsiasi nuova acquisizione, sviluppo o modifica rilevante di un sistema IA — trigger di governance IA. Ai fini della presente politica, una **modifica rilevante** è qualsiasi modifica a un sistema IA riguardante la finalità prevista, la metodologia di addestramento, le fonti di dati, il tipo di output, il contesto operativo o il perimetro di deployment che non era stata prevista nella VISIA originale e nella valutazione del rischio. Ciò si allinea con il concetto di **modifica sostanziale** del Regolamento IA UE (Articolo 3(23)): una modifica che incide sulla conformità ai requisiti applicabili o comporta una modifica della finalità prevista valutata. Il comportamento di apprendimento continuo predeterminato dal fornitore al momento della valutazione iniziale della conformità non costituisce una modifica sostanziale.
5. L'escalation delle decisioni **deve** seguire il percorso definito sopra.

---

## Giudizio professionale nella certificazione ISO 42001:2023

### Fase 1: Progettazione AIMS (Responsabilità dell'organizzazione)

Il giudizio professionale esercitato dall'[Organizzazione] comprende:

1. **Determinazione del ruolo IA** (fornitore, operatore o entrambi per sistema IA):
   - Identificare per ciascun sistema IA se l'[Organizzazione] agisce come fornitore IA, operatore IA o entrambi
   - Documentare la determinazione per sistema IA nell'Inventario dei sistemi IA
   - Selezionare i controlli applicabili in base al ruolo — alcuni controlli si applicano principalmente ai fornitori (es. A.6.1.x, A.7.x), altri a tutti i ruoli
   - Documentato in: Inventario dei sistemi IA, DDA AIMS

2. **Determinazione del perimetro AIMS** (Clausola 4.3):
   - Quali sistemi IA rientrano nel perimetro AIMS
   - Se l'AIMS è integrato con l'ISMS ISO 27001 o gestito in modo autonomo
   - Confini geografici e organizzativi
   - Documentato in: Documento di perimetro AIMS

3. **Selezione dei controlli e DDA** (Clausola 6.1.3 / Allegato A):
   - Selezionare i controlli in base alla valutazione dei rischi IA e ai risultati della VISIA
   - Determinare l'applicabilità di tutti i 36 controlli dell'Allegato A
   - Giustificare le esclusioni — «non applicabile al nostro ruolo» o «il rischio non si applica» sono esclusioni valide; «non ancora implementato» non lo è
   - Documentato in: DDA AIMS, Piano di trattamento dei rischi IA, documenti AI-POL-A.x.x

4. **Sufficienza delle prove**:
   - Definire quali prove dimostrano l'efficacia dei controlli (registri VISIA, voci del registro dei rischi IA, rapporti di test, registri di monitoraggio)
   - Determinare la frequenza e la conservazione delle prove
   - Documentato in: Documenti IMP dei controlli (sezione prove)

5. **Applicabilità normativa IA** (AI-POL-00):
   - Determinare quali leggi IA si applicano (quadro Livelli 1/2/3 per AI-POL-00)
   - Valutare i trigger delle normative condizionali (certificazione ISO 42001, classificazione ad alto rischio del Regolamento IA UE)
   - Documentato in: Matrice di applicabilità normativa AI-POL-00

### Fase 2: Verifica AIMS (Responsabilità del revisore)

Il giudizio professionale esercitato dal revisore comprende:

1. **Valutazione della qualità dei processi**:
   - La metodologia di valutazione dei rischi IA è solida e applicata in modo coerente?
   - Le determinazioni del ruolo IA (fornitore/operatore) sono ragionevoli dato il portafoglio di sistemi IA?
   - I decisori sono competenti secondo la tabella delle autorità sopra riportata?

2. **Allineamento con ISO 42001:2023**:
   - L'interpretazione organizzativa dei controlli dell'Allegato A soddisfa gli obiettivi dei controlli?
   - La DDA AIMS è completa e giustificata (tutti i 36 controlli dell'Allegato A documentati)?
   - Le clausole obbligatorie (4–10) sono trattate?

3. **Efficacia dell'implementazione** (Fase 2):
   - L'implementazione effettiva corrisponde alla progettazione documentata (catena POL → IMP → Prove)?
   - Le prove sono sufficienti a dimostrare il funzionamento dei controlli?
   - Le non conformità e le azioni correttive vengono gestite ai sensi della Clausola 10.2?

---

## Protocollo di contestazione dell'applicabilità

**Scopo**: Processo strutturato per risolvere i disaccordi sulle determinazioni dell'applicabilità IA tra l'[Organizzazione] e il revisore.

**Quando si applica questo protocollo**:

- Il revisore mette in discussione l'applicabilità normativa IA (es. «La classificazione ad alto rischio del Regolamento IA UE è giustificata?»)
- Il revisore contesta la determinazione del ruolo IA per un sistema IA specifico
- Il revisore contesta un'esclusione di controllo nella DDA AIMS
- Il revisore ritiene che un controllo alternativo non raggiunga l'obiettivo ISO 42001:2023

**Fasi del protocollo**:

**Fase 1 — Il revisore solleva una preoccupazione**: Documenta la preoccupazione specifica — quale determinazione, quali prove sono in contraddizione, quale clausola o obiettivo di controllo ISO 42001 potrebbe non essere soddisfatto.

**Fase 2 — L'[Organizzazione] fornisce la documentazione**:

- Per l'**applicabilità normativa**: Valutazione secondo la metodologia AI-POL-00; valutazione del trigger; registro di approvazione RGIA + Legale
- Per la **determinazione del ruolo**: Descrizione del sistema IA; voce nell'inventario; motivazione del RGIA per la classificazione fornitore/operatore
- Per l'**esclusione del controllo**: Valutazione dei rischi IA che mostra perché il rischio non si applica o perché il controllo è al di fuori del perimetro organizzativo; giustificazione nella DDA; contesto organizzativo

**Fase 3 — Valutazione collaborativa**: L'[Organizzazione] e il revisore valutano congiuntamente se la motivazione documentata soddisfa i requisiti ISO 42001:2023. La discussione è basata sui fatti.

**Fase 4 — Risoluzione**:

| Esito | Azione |
|------|--------|
| Motivazione dell'organizzazione accettata | Documentare nei documenti di lavoro dell'audit; nessuna modifica richiesta |
| Lacuna confermata | L'[Organizzazione] avvia un'azione correttiva (Clausola 10.2); aggiornare DDA/AI-POL-00 ove applicabile |
| Disaccordo non risolto | Escalation al processo di risoluzione delle controversie dell'ente di certificazione |

---

## Determinazione del perimetro AIMS

### Requisiti del documento di perimetro

Il Documento di perimetro AIMS (ai sensi della Clausola 4.3 di ISO 42001:2023) deve specificare:

- **I sistemi IA nel perimetro**: Sistemi IA nominati con finalità, tipo e contesto di deployment
- **I sistemi IA esplicitamente esclusi**: Con giustificazione documentata
- **Le unità organizzative**: Quali dipartimenti, funzioni o entità giuridiche rientrano nel perimetro
- **I confini geografici**: Quali sedi o giurisdizioni sono incluse
- **L'integrazione con l'ISMS**: Se AIMS e ISMS condividono processi (riesame della direzione, audit interno, controllo delle informazioni documentate)

### Inventario dei sistemi IA

L'[Organizzazione] deve mantenere un Inventario dei sistemi IA come documento controllato. L'inventario deve includere, per ciascun sistema IA nel perimetro:

| Campo | Descrizione |
|-------|-------------|
| ID del sistema IA | Identificatore univoco |
| Nome del sistema IA | Nome comune e versione |
| Proprietario del sistema IA | Persona responsabile nominata |
| Finalità del sistema IA | Uso previsto e contesto di deployment |
| Ruolo IA | Fornitore / Operatore / Entrambi |
| Classificazione del rischio Regolamento IA UE | Vietato / Ad alto rischio / A rischio limitato / A rischio minimo / GPAI |
| Riferimento VISIA | Collegamento al registro VISIA completato |
| Nel perimetro AIMS | Sì / No (con giustificazione se No) |
| Riferimento DDA | Voce nella Dichiarazione di Applicabilità |

L'Inventario dei sistemi IA deve essere revisionato:

- Almeno annualmente in occasione del riesame della direzione
- Quando viene acquisito o sviluppato un nuovo sistema IA
- Quando un sistema IA esistente subisce una modifica rilevante (nuova finalità, nuova popolazione, nuovo contesto di deployment)
- Quando viene identificata una modifica della classificazione ai sensi del Regolamento IA UE

---

## Dichiarazione di Applicabilità (DDA) AIMS

L'[Organizzazione] deve produrre e mantenere una Dichiarazione di Applicabilità ai sensi della Clausola 6.1.3 di ISO 42001:2023. La DDA deve:

- Elencare tutti i 36 controlli dell'Allegato A
- Per ciascun controllo: indicare se è applicabile (Incluso) o non applicabile (Escluso)
- Per i controlli inclusi: documentare lo stato di implementazione e il riferimento alla politica AI-POL-A.x.x
- Per i controlli esclusi: documentare una giustificazione scritta — l'esclusione è valida solo ove il controllo non si applichi effettivamente dato il ruolo IA, il perimetro e la valutazione dei rischi dell'[Organizzazione]; «non ancora implementato» non costituisce una giustificazione valida per l'esclusione
- Essere approvata dal RGIA prima del primo utilizzo
- Essere revisionata annualmente e dopo modifiche rilevanti al portafoglio di sistemi IA o ai requisiti normativi

---

## Controllo delle modifiche AIMS

**Trigger per un aggiornamento AIMS controllato**:

- Nuova normativa IA adottata o significativamente aggiornata (atti delegati del Regolamento IA UE, legge IA svizzera)
- Nuovo standard ISO pubblicato che influisce sull'AIMS (ISO 42006, aggiornamento ISO 42005)
- Modifica rilevante al portafoglio di sistemi IA (nuovo sistema IA ad alto rischio, ritiro di un sistema nel perimetro)
- Rilievo dell'audit interno o azione correttiva che influisce sul perimetro della politica
- Decisione del riesame della direzione

**Processo di modifica**:

1. Il RGIA propone la modifica con motivazione documentata
2. Il RSSI e il Legale esaminano le dimensioni di sicurezza e giuridiche
3. La Direzione generale approva se si tratta di una decisione strategica (modifica del perimetro, allocazione delle risorse)
4. La politica aggiornata viene distribuita e comunicata ai sensi della Clausola 7.4
5. Un aggiornamento della formazione o della sensibilizzazione viene avviato se la modifica influisce sugli obblighi del personale

---

## Riesame della direzione (Clausola 9.3)

Il RGIA deve convocare o garantire un riesame annuale della direzione AIMS con la partecipazione di:

- Direzione generale (sponsor)
- RGIA (presidente)
- RSSI
- Responsabile Legale / Compliance
- CTO / Responsabile IA Engineering (ove lo sviluppo IA rientri nel perimetro)
- Proprietari di sistemi IA (per i sistemi nel perimetro)

**Punti obbligatori all'ordine del giorno** (ai sensi della Clausola 9.3.2 di ISO 42001:2023):

1. Stato delle azioni del riesame della direzione precedente
2. Cambiamenti del contesto esterno/interno che influiscono sull'AIMS
3. Cambiamenti nel panorama normativo IA (aggiornamenti AI-POL-00)
4. Risultati della valutazione dei rischi IA e della VISIA
5. Indicatori di prestazione AIMS (avanzamento degli obiettivi IA, numero di incidenti/MTTR, avanzamento della DDA)
6. Risultati dell'audit interno
7. Non conformità e azioni correttive
8. Revisione dell'adeguatezza delle risorse
9. Opportunità di miglioramento continuo

**Risultati del riesame della direzione** (Clausola 9.3.3):

Decisioni documentate e elementi d'azione comprensivi di:

- Decisioni di miglioramento continuo
- Modifiche al perimetro AIMS
- Decisioni di allocazione delle risorse
- Aggiornamenti delle politiche IA
- Decisioni relative al portafoglio di sistemi IA

I verbali del riesame della direzione devono essere conservati come prove documentate ai sensi della Clausola 7.5.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità di governance AIMS |
|------|----------------------------------|
| **RGIA** | Autorità primaria AIMS; proprietario della DDA; proprietario di AI-POL-00; proprietario del processo VISIA; monitoraggio normativo; presidente del riesame della direzione; referente con l'ente di certificazione |
| **RSSI** | Dimensioni di sicurezza dei controlli IA; integrazione ISMS/AIMS; supervisione delle misure tecniche; revisione della sicurezza A.6.2.4/A.6.2.6 |
| **Legale / Compliance** | Monitoraggio normativo IA; coordinamento della valutazione della conformità al Regolamento IA UE; clausole IA nei contratti dei fornitori IA; coinvolgimento con le autorità di vigilanza |
| **CTO / Responsabile IA Engineering** | Implementazione dei controlli A.6.x e A.7.x; documentazione del ciclo di vita dei sistemi IA; generazione delle prove tecniche |
| **Proprietari di sistemi IA** | Voci nell'inventario dei sistemi IA; completamento della VISIA per i sistemi di propria competenza; controlli operativi; segnalazione degli incidenti |
| **Direzione generale** | Accettazione dei rischi IA; allocazione delle risorse; approvazione del perimetro AIMS; partecipazione al riesame della direzione |
| **Revisore interno** | Programma di audit AIMS indipendente; rapporto dei rilievi; verifica delle azioni correttive |

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
