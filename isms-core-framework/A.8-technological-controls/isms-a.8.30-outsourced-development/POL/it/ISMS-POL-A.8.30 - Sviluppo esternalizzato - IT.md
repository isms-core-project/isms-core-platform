<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.30-IT:framework:POL:a.8.30 -->
**ISMS-POL-A.8.30 — Sviluppo esternalizzato**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Politica di sviluppo esternalizzato |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.30 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DT → Approvvigionamento/Gestione Fornitori → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.8.28 (Codifica sicura); ISMS-POL-A.5.19-23 (Relazioni con i fornitori e servizi cloud); ISMS-IMP-A.8.30.1–3-UG/TG; ISO/IEC 27001:2022 Controllo A.8.30.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la gestione della sicurezza nello sviluppo esternalizzato di sistemi e software, conformemente al Controllo A.8.30 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutte le attività di sviluppo esternalizzato, inclusi: sviluppo a contratto; sviluppo offshore; sviluppatori freelance; personalizzazione di software acquisito.

**Rischio aziendale affrontato**: Le vulnerabilità di sicurezza introdotte attraverso lo sviluppo di terze parti che portano a violazioni dei dati, furto di proprietà intellettuale, compromissione della supply chain e non conformità normativa.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.30

> *L'organizzazione deve supervisionare e monitorare le attività di sviluppo del sistema esternalizzate.*

**Obiettivo del controllo**: Garantire che lo sviluppo esternalizzato soddisfi gli stessi standard di sicurezza dello sviluppo interno, attraverso la valutazione dei fornitori, i requisiti contrattuali e la supervisione.

---

# Enunciati di politica

## Valutazione e selezione dei fornitori

[Organizzazione] DEVE valutare le capacità di sicurezza dei fornitori di sviluppo prima dell'ingaggio.

**Criteri di valutazione della sicurezza**: Pratiche di codifica sicura del fornitore (conformità allo standard OWASP, uso di SAST/DAST); politica e procedure di sicurezza delle informazioni; gestione degli accessi privilegiati per il personale del fornitore; capacità di sicurezza della supply chain del software (gestione delle dipendenze, SBOM); storico e referenze sulla sicurezza.

**Processo di valutazione**: Completare il questionario di valutazione della sicurezza prima dell'ingaggio; rivalutare annualmente o in caso di incidenti di sicurezza significativi; documentare i risultati della valutazione nel Registro dei fornitori SGSI (per ISMS-POL-A.5.19-23).

## Requisiti contrattuali

[Organizzazione] DEVE includere requisiti di sicurezza nei contratti con i fornitori di sviluppo.

**Clausole contrattuali obbligatorie**: Conformità agli standard di codifica sicura di [Organizzazione] (inclusa ISMS-POL-A.8.28); diritto di audit e revisione del codice da parte di [Organizzazione]; obblighi di segnalazione degli incidenti di sicurezza (entro 24 ore dalla scoperta di qualsiasi violazione che influenzi il codice di [Organizzazione]); protezione della proprietà intellettuale e riservatezza (NDA); cancellazione di tutti i dati e il codice di [Organizzazione] alla fine del contratto; proibizione di subappaltare lo sviluppo a terze parti aggiuntive senza approvazione; conformità a ISMS-POL-A.5.19-23 (requisiti della supply chain software).

## Requisiti di sicurezza dello sviluppo

[Organizzazione] DEVE imporre che i fornitori soddisfino i requisiti di sicurezza tecnica.

**Pratiche di sviluppo**: I fornitori DEVONO seguire le stesse linee guida di codifica sicura richieste per lo sviluppo interno (ISMS-POL-A.8.28); DEVONO usare strumenti SAST e SCA durante lo sviluppo; i risultati degli strumenti di sicurezza DEVONO essere condivisi con [Organizzazione]; le vulnerabilità Critiche e Alte DEVONO essere remediate prima della consegna.

**Gestione del codice sorgente**: Tutto il codice DEVE essere archiviato nei repository di [Organizzazione] o in repository del fornitore con accesso garantito a [Organizzazione]; DEVE essere implementata la protezione dei branch con revisione del codice per le consegne; i commit DEVONO essere firmati e tracciabili al singolo sviluppatore.

**Gestione degli accessi**: L'accesso dei fornitori all'ambiente di [Organizzazione] DEVE essere: limitato nel tempo (basato sulla durata del contratto); limitato per perimetro (solo ai sistemi/repository richiesti); soggetto ad AMF; registrato e monitorato; revocato immediatamente alla fine del contratto o dell'ingaggio.

## Test di sicurezza e accettazione

[Organizzazione] DEVE verificare la sicurezza del software sviluppato esternamente prima dell'accettazione.

**Requisiti di test**: SAST e SCA eseguiti da [Organizzazione] o da un tester terzo indipendente; penetration test per software ad alto rischio (Critico/Alto); test di accettazione della sicurezza completati e documentati. **Criteri di accettazione**: Nessuna vulnerabilità Critica o Alta irrisolta; tutte le vulnerabilità Medie documentate con piano di rimedio; fornitore tenuto a correggere le vulnerabilità identificate senza costi aggiuntivi.

## Supervisione continua

[Organizzazione] DEVE supervisionare i fornitori di sviluppo durante l'ingaggio.

**Meccanismi di supervisione**: Revisioni regolari della sicurezza durante i lunghi ingaggi (mensili per progetti >3 mesi); revisioni a campione del codice per la conformità agli standard di sicurezza; report di avanzamento della sicurezza da parte del fornitore. **Risposta agli incidenti**: I fornitori DEVONO notificare a [Organizzazione] qualsiasi incidente di sicurezza entro 24 ore; [Organizzazione] mantiene il diritto di condurre audit forensi in caso di sospetta violazione.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approvazione degli ingaggi ad alto rischio; supervisione degli incidenti |
| **DT** | Supervisione tecnica dello sviluppo esternalizzato; revisione del codice |
| **Approvvigionamento/Gestione Fornitori** | Valutazione del fornitore; negoziazione del contratto; gestione delle relazioni |
| **Application Security Lead** | Definizione dei requisiti di sicurezza tecnica; test di sicurezza e accettazione |
| **Consulente Legale** | Revisione e approvazione delle clausole contrattuali di sicurezza |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DT** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti per lo sviluppo esternalizzato. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.30 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
