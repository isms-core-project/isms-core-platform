<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.11-IT:framework:POL:a.8.11 -->
**ISMS-POL-A.8.11 — Mascheramento dei dati**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Mascheramento dei dati |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.11 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → RPD → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.11.1–4-UG/TG; ISMS-CTX-A.8.11 (Riferimento tecnico sul mascheramento — NON SGSI); ISO/IEC 27001:2022 Controllo A.8.11.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di mascheramento dei dati per proteggere la riservatezza delle informazioni sensibili, conformemente al Controllo A.8.11 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutte le categorie di dati sensibili (DCP, finanziari, sanitari, credenziali, proprietari) in tutti gli ambienti (produzione, test, sviluppo, analisi, formazione, backup); tutte le tecniche di mascheramento (redazione, sostituzione, tokenizzazione, pseudonimizzazione, anonimizzazione); e tutto il personale organizzativo, gli appaltatori e le terze parti che gestiscono dati sensibili.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.11

> *Il mascheramento dei dati deve essere utilizzato in conformità con la politica specifica per argomento dell'organizzazione sul controllo degli accessi e altre politiche specifiche per argomento correlate, e con i requisiti aziendali, tenendo conto della legislazione applicabile.*

**Obiettivo del controllo**: Stabilire la politica organizzativa per i controlli di mascheramento dei dati che proteggono la riservatezza delle informazioni sensibili oscurando i dati quando non è necessaria la piena visibilità per scopi aziendali legittimi.

---

# Enunciati di politica

## Classificazione dei dati e requisiti di mascheramento

[Organizzazione] DEVE determinare quali dati richiedono il mascheramento in base alla sensibilità e al contesto di utilizzo.

**Categorie di dati che richiedono il mascheramento**:

| Categoria di dati | Mascheramento obbligatorio in | Metodo consigliato |
|------------------|-------------------------------|-------------------|
| **DCP — Dati identificativi** (nome, indirizzo, e-mail) | Ambienti non di produzione; esportazioni a utenti non autorizzati | Pseudonimizzazione; sostituzione |
| **DCP — Categorie speciali** (salute, origine etnica, dati biometrici) | TUTTI gli ambienti non di produzione; tutte le analisi | Pseudonimizzazione; anonimizzazione |
| **Dati finanziari** (numeri di carte, IBAN, numeri di conti) | Ambienti non di produzione; log; interfacce utente | Tokenizzazione; mascheramento parziale |
| **Credenziali** (password, chiavi API, token) | Tutti i log, le interfacce, i report | Redazione completa; hashing |
| **Informazioni proprietarie** (IP, segreti commerciali) | Accesso di terze parti; ambienti non di produzione | Sostituzione; riduzione della precisione |

## Tecniche di mascheramento approvate

[Organizzazione] DEVE approvare ed applicare tecniche di mascheramento appropriate.

**Tecniche approvate**:

| Tecnica | Descrizione | Caso d'uso appropriato |
|---------|-------------|------------------------|
| **Pseudonimizzazione** | Sostituzione degli identificatori con alias; reversibile con chiave | Dati di test che devono mantenere la coerenza referenziale |
| **Anonimizzazione** | Rimozione irreversibile degli identificatori | Analisi dove il re-identificazione non è necessaria |
| **Tokenizzazione** | Sostituzione dei dati con token; mapping in database sicuro | Dati finanziari (PCI DSS); ID di sessione |
| **Redazione** | Rimozione completa dei dati sensibili | Log; report; interfacce rivolte all'esterno |
| **Mascheramento parziale** | Oscuramento parziale (es. ****-****-****-1234) | Visualizzazione dell'interfaccia utente; conferme |
| **Sostituzione** | Sostituzione con dati plausibili ma fittizi | Ambienti di test/sviluppo |
| **Riduzione della precisione** | Riduzione della precisione dei dati (es. solo anno anziché data completa) | Analisi che richiedono tendenze ma non valori precisi |

**Selezione della tecnica**: La selezione DEVE considerare: il livello di sensibilità dei dati; il requisito di reversibilità; il caso d'uso (test vs. analisi vs. mascheramento nell'interfaccia utente); i requisiti normativi specifici (es. PCI DSS richiede la tokenizzazione per i dati del titolare della carta).

## Requisiti di copertura ambientale

**Ambienti non di produzione** (sviluppo, test, staging, QA): I dati sensibili di produzione NON DEVONO essere utilizzati negli ambienti non di produzione senza mascheramento; il processo di provisioning dei dati DEVE includere il mascheramento come passaggio obbligatorio; i controlli di conformità automatizzati DEVONO verificare l'assenza di dati di produzione non mascherati.

**Ambienti di produzione**: Il mascheramento DEVE essere applicato: nelle interfacce utente (mascheramento parziale per i campi sensibili durante la visualizzazione); nelle integrazioni di terze parti (ridurre al minimo l'esposizione ai dati sensibili); nei log (redazione delle credenziali, dati finanziari, DCP sensibili).

**Backup e replica**: I dati mascherati nei sistemi primari DEVONO rimanere mascherati nei backup; i processi di backup DEVONO verificare che il mascheramento venga preservato.

## Test e validazione del mascheramento

[Organizzazione] DEVE verificare l'efficacia del mascheramento attraverso test regolari.

**Requisiti di test**: Verifica che tutti i campi identificati come richiedenti il mascheramento siano mascherati; convalida dell'irreversibilità per l'anonimizzazione; test di conformità referenziale per la pseudonimizzazione; test di re-identificazione per verificare che i dati mascherati non possano essere de-mascherati senza chiave.

**Frequenza dei test**: Annuale per tutti gli ambienti; attivata dalle modifiche ai processi di mascheramento o ai sistemi di archiviazione dei dati.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; supervisione della conformità; approva le eccezioni |
| **RPD** | Supervisione del mascheramento dei DCP; conformità RGPD/nLPD |
| **Ingegneria dei dati/IT** | Implementazione tecnica delle soluzioni di mascheramento; manutenzione dei processi di provisioning dei dati |
| **Sviluppatori** | Non utilizzare dati di produzione negli ambienti non di produzione senza mascheramento; segnalare esposizioni dei dati |
| **Proprietari dei dati** | Definire i requisiti di mascheramento per i dati di proprietà; approvare le eccezioni |

---

# Conformità ed eccezioni

**Utilizzo dei dati di produzione negli ambienti non di produzione senza mascheramento**: Richiede approvazione scritta del RSSI e del RPD; implementazione di controlli di accesso avanzati; documentazione dell'uso legittimo; limite di tempo massimo di 30 giorni. **Non ammissibile**: Utilizzo di categorie speciali di DCP non mascherati negli ambienti non di produzione senza approvazione del RPD.

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **RPD** | [Nome] | [Data] |
| **Responsabile Legale/Conformità** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per il mascheramento dei dati. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.11 (UG/TG). Il riferimento tecnico è in ISMS-CTX-A.8.11 (NON SGSI).*

<!-- QA_VERIFIED: 2026-04-03 -->
