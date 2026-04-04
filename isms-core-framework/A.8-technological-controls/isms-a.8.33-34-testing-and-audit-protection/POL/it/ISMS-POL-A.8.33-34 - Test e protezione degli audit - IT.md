<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.33-34-IT:framework:POL:a.8.33-34 -->
**ISMS-POL-A.8.33-34 — Test e protezione degli audit**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Test e protezione degli audit |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.33-34 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI/Responsabile Operazioni IT → RPD → Conformità → AD.

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.8.11 (Mascheramento dei dati); ISMS-POL-A.8.31 (Separazione degli ambienti); ISMS-IMP-A.8.33-34.1–2-UG/TG; ISO/IEC 27001:2022 Controlli A.8.33, A.8.34.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la protezione delle informazioni di test e la salvaguardia dei sistemi informativi durante i test di audit, conformemente ai Controlli A.8.33 e A.8.34 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutte le attività di selezione e protezione dei dati di test, a tutte le attività di audit e test di sicurezza, a tutti gli ambienti dove si eseguono test e a tutto il personale coinvolto nelle attività di test e audit.

**Principi fondamentali**: I dati di test NON DEVONO contenere DCP di produzione non protetti o dati sensibili; i dati di produzione utilizzati nei test DEVONO essere mascherati o anonimizzati; gli ambienti di test DEVONO essere isolati dai sistemi di produzione; i test di audit DEVONO essere pianificati per minimizzare le interruzioni operative; gli strumenti e i log di audit DEVONO essere protetti e controllati.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA (applicabilità condizionale per ISMS-POL-00).

---

# Allineamento sul controllo

**A.8.33 — Protezione delle informazioni di test**: Le informazioni di test devono essere selezionate, protette e gestite in modo appropriato.

**A.8.34 — Protezione dei sistemi informativi durante i test di audit**: I requisiti di test e le attività che coinvolgono la verifica dei sistemi operativi devono essere pianificati e concordati tra il richiedente e la direzione appropriata.

---

# Protezione delle informazioni di test (A.8.33)

## Selezione dei dati di test

[Organizzazione] DEVE definire i requisiti per la selezione dei dati di test.

**Preferenza della tipologia di dati di test** (in ordine decrescente): Dati sintetici generati artificialmente (preferito); dati di produzione mascherati/anonimizzati; dati di produzione campionati e mascherati (solo con approvazione del RPD e del RSSI).

**Divieto**: I dati di produzione non mascherati contenenti DCP, dati finanziari o altre informazioni sensibili NON DEVONO essere copiati negli ambienti di test senza l'approvazione documentata del RSSI e del RPD.

## Protezione dei dati di test

[Organizzazione] DEVE proteggere i dati di test in modo proporzionale alla loro sensibilità.

**Requisiti di protezione**: I dati di test che derivano dai dati di produzione DEVONO applicare lo stesso livello di classificazione dei dati di produzione originali; il mascheramento DEVE essere irreversibile per i DCP (per ISMS-POL-A.8.11); l'accesso ai dati di test sensibili DEVE essere controllato; i log di accesso ai dati di test sensibili DEVONO essere mantenuti.

**Gestione del ciclo di vita dei dati di test**: I dati di test DEVONO essere rimossi al completamento del ciclo di test; il riutilizzo dei dati di test in più sessioni richiede la revisione della sensibilità; i set di dati di test DEVONO essere documentati nel registro dei dati (inclusa la fonte, il metodo di mascheramento, la data di creazione, la data di distruzione pianificata).

## Qualità del mascheramento

[Organizzazione] DEVE verificare l'efficacia del mascheramento dei dati di test.

**Test di verifica**: Conferma che tutti i campi DCP identificati siano mascherati; verifica dell'irreversibilità del mascheramento; test di re-identificazione (verifica che non sia possibile de-mascherare senza chiave); documentazione dei risultati dei test di verifica.

---

# Protezione dei sistemi informativi durante i test di audit (A.8.34)

## Pianificazione dei test di audit

[Organizzazione] DEVE pianificare le attività di test di audit per minimizzare i rischi.

**Requisiti di pianificazione**: Tutte le attività di test di audit DEVONO essere pianificate e concordate con il proprietario del sistema e la direzione appropriata prima dell'inizio; il piano di test DEVE documentare: perimetro e obiettivi, sistemi interessati, metodi di test, impatto potenziale e misure di mitigazione, finestra temporale del test, procedure di escalation; la comunicazione del piano di test DEVE avvenire con almeno 5 giorni lavorativi di anticipo per i test pianificati.

## Autorizzazione e accesso ai test

**Requisiti di autorizzazione**: L'accesso ai sistemi di produzione per i test di audit DEVE essere: formalmente autorizzato dal proprietario del sistema e dal RSSI; limitato nel tempo (solo per il periodo di test); soggetto ad AMF; completamente registrato e monitorato; revocato immediatamente al completamento del test. **Le attività di test NON DEVONO sovrascrivere i log di produzione o i dati di configurazione.**

## Protezione degli strumenti di audit

[Organizzazione] DEVE proteggere gli strumenti e i risultati dei test di audit.

**Requisiti di protezione degli strumenti**: Gli strumenti di audit e di test di sicurezza DEVONO essere: approvati dal RSSI prima dell'uso; archiviati in modo sicuro quando non in uso; accessibili solo al personale autorizzato; rimossi dai sistemi di produzione dopo il completamento del test. **I risultati dei test DEVONO essere**: trattati come RISERVATI; archiviati in modo sicuro; condivisi solo su base need-to-know; conservati per il periodo richiesto (minimo 3 anni).

## Gestione dei risultati dei test di audit

**Documentazione**: I risultati dei test di audit DEVONO essere documentati, inclusi: data e perimetro del test; metodi e strumenti utilizzati; risultati e raccomandazioni; piano di rimedio per i risultati; firme di approvazione. **Rimedio**: I risultati dei test di sicurezza DEVONO essere rimediati per ISMS-POL-A.8.8 (Gestione delle vulnerabilità); i risultati degli audit DEVONO essere tracciati attraverso il processo di non conformità SGSI (Clausola 10.2).

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approva le attività di test ad alto rischio; supervisione della protezione degli strumenti di audit |
| **RPD** | Revisione e approvazione dell'uso dei DCP nei test |
| **Proprietari dei sistemi** | Approvazione del test dei sistemi di proprietà; garanzia della disponibilità delle risorse |
| **Team di Audit interno** | Pianificazione ed esecuzione delle attività di audit; documentazione dei risultati |
| **Operazioni IT** | Supporto tecnico per le attività di test; gestione dell'accesso |
| **Team di sviluppo** | Selezione e protezione dei dati di test; rimedio delle vulnerabilità |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **RPD** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti per i test e la protezione degli audit. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.33-34 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
