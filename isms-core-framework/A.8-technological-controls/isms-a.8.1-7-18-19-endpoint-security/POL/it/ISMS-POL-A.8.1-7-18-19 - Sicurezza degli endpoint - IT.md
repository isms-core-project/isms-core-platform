<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.1-7-18-19-IT:framework:POL:a.8.1-7-18-19 -->
**ISMS-POL-A.8.1-7-18-19 — Sicurezza degli endpoint**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza degli endpoint |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.1-7-18-19 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → Direttore IT → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.1-7-18-19-S1–S4-UG/TG; ISMS-POL-A.5.9; ISMS-POL-A.8.8; ISMS-POL-A.8.15; ISMS-POL-A.8.16; ISMS-POL-A.8.20-22; ISO/IEC 27001:2022 Controlli A.8.1, A.8.7, A.8.18, A.8.19.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la sicurezza degli endpoint, implementando i Controlli A.8.1 (Dispositivi endpoint degli utenti), A.8.7 (Protezione contro il malware), A.8.18 (Uso di programmi di utilità con privilegi) e A.8.19 (Installazione di software su sistemi operativi) come un quadro di sicurezza unificato.

**Perimetro**: Si applica a tutti i dispositivi endpoint degli utenti (laptop, desktop, dispositivi mobili, tablet, dispositivi IoT), indipendentemente dal tipo, dal sistema operativo o dal modello di proprietà (aziendale, BYOD, appaltatore, ospite).

**Motivazione dei controlli combinati**: A.8.1, A.8.7, A.8.18 e A.8.19 sono implementati come quadro unificato perché operano sulla stessa infrastruttura endpoint; le attività di scoperta degli endpoint servono tutti e quattro i controlli; le prove di valutazione si sovrappongono in modo significativo; la sicurezza degli endpoint richiede un'implementazione olistica.

**Allineamento normativo**: nLPD svizzera (Art. 8); RGPD dell'UE (Art. 32); ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Quadro dei requisiti di sicurezza degli endpoint

## Sicurezza dei dispositivi endpoint (A.8.1)

**Obiettivo**: Proteggere le informazioni archiviate, elaborate o accessibili tramite i dispositivi endpoint degli utenti.

### Inventario degli endpoint (Obbligatorio)

[Organizzazione] DEVE mantenere un inventario completo e aggiornato di tutti i dispositivi endpoint. **Copertura minima**: ≥95% degli endpoint connessi alla rete (obiettivo: 100%). **Frequenza di aggiornamento**: Scoperta automatizzata settimanale minima (giornaliera preferita), riconciliazione mensile.

### Classificazione degli endpoint (Obbligatorio)

[Organizzazione] DEVE classificare gli endpoint per tipo di dispositivo, modello di proprietà e criticità.

### Basi di sicurezza (Obbligatorio)

**Requisiti universali della base di sicurezza** (tutti gli endpoint): Hardening del sistema operativo (ultimi aggiornamenti di sicurezza, firewall abilitato, servizi non necessari disabilitati); controlli di autenticazione (password forti, blocco schermo, AMF dove applicabile); registrazione e monitoraggio (registrazione degli eventi di sicurezza, integrazione SIEM dove applicabile). **Obiettivo di conformità alla base**: ≥90% di conformità su tutti gli endpoint.

### Cifratura (Obbligatorio)

**Cifratura completa del disco (FDE)**:

- Tutti i laptop e desktop aziendali: FDE obbligatoria (obiettivo di copertura: ≥98%)
- Algoritmo di cifratura: Minimo AES-256
- Autenticazione pre-avvio: Obbligatoria
- Deposito delle chiavi di cifratura: Obbligatorio per i dispositivi aziendali (chiavi di recupero archiviate centralmente)

**Dispositivi mobili**: Tutti i dispositivi mobili aziendali: cifratura del dispositivo abilitata (obiettivo: ≥95%). BYOD mobili: cifratura del contenitore obbligatoria (solo app/dati aziendali).

**Eccezioni**: I computer desktop in strutture sicure POSSONO essere esentati con approvazione del RSSI e controlli compensativi. Le strutture sicure sono definite come: (a) Aree con accesso fisico controllato tramite badge/biometria; (b) Monitoraggio 24/7 o reception con personale; (c) Nessun accesso pubblico; (d) Documentate nel registro della sicurezza fisica per A.7.1-4.

### Gestione degli endpoint (Obbligatorio)

[Organizzazione] DEVE registrare tutti gli endpoint aziendali in un sistema di gestione degli endpoint (MDM per mobile, basato su agente per laptop/desktop). **Funzionalità obbligatorie**: gestione della configurazione; distribuzione del software; monitoraggio della conformità; capacità di cancellazione remota; sincronizzazione dell'inventario.

### Risposta a dispositivi persi/rubati (Obbligatorio)

**Requisiti di segnalazione**: Gli utenti DEVONO segnalare i dispositivi persi/rubati immediatamente (obiettivo: entro 1 ora dalla scoperta). **Cancellazione remota**: Avviata entro 4 ore dalla segnalazione (1 ora per i dispositivi critici).

### Smaltimento sicuro (Obbligatorio)

**Sanificazione dei dati**: Cancellazione sicura (conforme a NIST SP 800-88 Rev. 2) o distruzione fisica. **Certificato di distruzione**: Obbligatorio per tutti gli endpoint smaltiti.

### Programma BYOD (Condizionale)

**Requisiti di sicurezza BYOD**: Accordo utente BYOD obbligatorio; sicurezza minima del dispositivo; gestione containerizzata (MAM); ambito della cancellazione remota: solo del contenitore. **Protezioni della privacy BYOD**: Nessun accesso ai dati personali, nessun inventario delle app personali, nessun controllo completo del dispositivo.

---

## Protezione contro il malware (A.8.7)

**Obiettivo**: Proteggere gli endpoint dal malware attraverso controlli di rilevamento, prevenzione e ripristino, supportati dalla sensibilizzazione degli utenti.

### Soluzione anti-malware/EDR (Obbligatorio)

**Meccanismi di rilevamento obbligatori**: Rilevamento basato sulle firme; rilevamento comportamentale (euristica); rilevamento basato su ML (fortemente raccomandato); prevenzione degli exploit; protezione specifica contro il ransomware (analisi comportamentale, accesso controllato alle cartelle, capacità di rollback). **Protezione contro le manomissioni**: Abilitata per prevenire che il malware disabiliti la protezione.

### Copertura della protezione (Obbligatorio)

- Endpoint aziendali: ≥98% di copertura della protezione (obiettivo: 100%)
- Endpoint BYOD: ≥80% di copertura della protezione
- **Rimedio delle lacune**: Endpoint non protetto identificato → protezione dispiegata entro 24 ore

### Protezione in tempo reale e scansioni (Obbligatorio)

- Protezione in tempo reale (scansione all'accesso) DEVE essere abilitata su tutti gli endpoint protetti
- Scansioni complete del sistema: Settimanale su tutti gli endpoint protetti
- Scansioni rapide: Giornaliera (raccomandata)

### Aggiornamenti delle firme (Obbligatorio)

**Frequenza**: Giornaliera minima (aggiornamenti in tempo reale fortemente preferiti). **Verifica**: Firme obsolete segnalate (Giallo: >24 ore, Rosso: >48 ore); rimedio entro 24 ore.

### Risposta agli incidenti malware (Obbligatorio)

**Sequenza temporale della risposta**: Triage entro 1 ora; contenimento immediato per il Critico (ransomware attivo, esfiltrazione di dati), entro 4 ore per l'Alta gravità. **Registrazione degli incidenti**: Tutti i rilevamenti di malware registrati centralmente (SIEM per ISMS-POL-A.8.15); conservazione minima di 12 mesi.

### Sensibilizzazione degli utenti (Obbligatorio)

**Requisiti di formazione**: Argomenti (riconoscimento del phishing, pratiche sicure di email/navigazione, rischi dei supporti USB, segnalazione delle attività sospette); formazione iniziale durante l'onboarding, aggiornamento annuale minimo. **Simulazioni di phishing**: Trimestrali. **Obiettivi**: ≥95% completamento formazione annuale; ≤10% tasso di clic nelle simulazioni. **Rimedio per fallimenti ripetuti**: Il personale che fallisce due simulazioni consecutive DEVE ricevere formazione correttiva mirata entro 14 giorni; tre o più fallimenti consecutivi attivano la notifica al responsabile e un monitoraggio avanzato per la politica HR.

---

## Gestione delle utilità con privilegi (A.8.18)

**Obiettivo**: Limitare e controllare rigorosamente i programmi di utilità con privilegi capaci di aggirare i controlli di sistema e delle applicazioni.

### Inventario delle utilità con privilegi (Obbligatorio)

[Organizzazione] DEVE mantenere un inventario dei programmi di utilità con privilegi, inclusi: strumenti di amministrazione del sistema; strumenti di accesso remoto; strumenti di debug e sviluppo; utilità di disco e file; strumenti di rete; strumenti di virtualizzazione; qualsiasi strumento in grado di aggirare i controlli di sicurezza. **Manutenzione dell'inventario**: Revisione trimestrale.

### Controllo degli accessi (Obbligatorio)

**Meccanismi**: Whitelisting delle applicazioni (utilità con privilegi bloccate per gli utenti standard); Privileged Access Management (PAM) per le utilità altamente privilegiate; Criteri di gruppo (Windows)/restrizioni MDM (macOS/mobile). **AMF**: L'accesso alle utilità con privilegi critiche DEVE richiedere l'autenticazione a più fattori.

### Flussi di lavoro di approvazione (Obbligatorio)

| Tipo di accesso | Approvazione | Durata |
|----------------|-------------|--------|
| Accesso permanente (assegnazione stabile) | Responsabile + RSSI | Ricertificazione annuale |
| Accesso temporaneo (limitato nel tempo) | Responsabile | 1-90 giorni; revoca automatica |
| Accesso di emergenza (account di emergenza) | Post-approvazione (accesso immediato, notifica al responsabile) | Revisione entro 24 ore |

### Monitoraggio e registrazione dell'utilizzo (Obbligatorio)

**Requisiti di registrazione**: Identità dell'utente; nome dell'utilità; timestamp; durata; identificatore dell'endpoint; azioni eseguite (se disponibili). **Conservazione del log**: Minimo 12 mesi. **Integrazione SIEM**: Log sull'utilizzo delle utilità con privilegi inoltrati al SIEM centralizzato (per ISMS-POL-A.8.15).

---

## Controlli di installazione del software (A.8.19)

**Obiettivo**: Gestire in modo sicuro l'installazione del software sui sistemi operativi attraverso controlli, autorizzazione e gestione delle vulnerabilità.

### Elenco del software approvato (Obbligatorio)

[Organizzazione] DEVE mantenere un elenco del software approvato. **Categorie**: Software aziendale obbligatorio; software specifico per ruolo; software opzionale approvato; software vietato. **Manutenzione**: Revisione annuale; aggiunte/rimozioni trimestrali secondo necessità.

### Processo di approvazione del software (Obbligatorio)

**Componenti**: Richiesta di software con giustificazione aziendale; revisione della sicurezza (valutazione delle vulnerabilità, reputazione del fornitore, revisione della privacy); decisione di approvazione; dispiegamento. **SLA di approvazione**: Richiesta standard 5 giorni lavorativi; richiesta urgente 2 giorni lavorativi; richiesta di emergenza 1 giorno lavorativo. In caso di indisponibilità del RSSI, l'autorità di approvazione di emergenza delega a: (1) RSSI delegato, (2) Direttore IT, o (3) Security Manager designato, con revisione retrospettiva del RSSI entro 5 giorni lavorativi.

### Rilevamento del software non autorizzato (Obbligatorio)

**Metodi di rilevamento**: Scansioni dell'inventario del software (giornaliera); avvisi del controllo delle applicazioni; analisi del traffico di rete. **Sequenza temporale del rimedio**: Software vietato/maligno rimosso entro 24 ore; software non approvato rimosso entro 7 giorni (o approvato se necessità aziendale legittima).

### Tecnologia di controllo delle applicazioni (Obbligatorio)

**Approcci**: Whitelisting (preferito): solo il software approvato può essere eseguito, negazione predefinita; Blacklisting (supplementare): software maligno/vietato noto bloccato. **Applicazione**: Laptop/desktop aziendali: whitelisting applicato (obbligatorio); dispositivi BYOD: solo app containerizzate; server: whitelisting rigorosa.

### Gestione delle vulnerabilità del software (Obbligatorio)

**Requisiti di patching**: Patch di sicurezza critiche entro 7 giorni; patch ad alta gravità entro 30 giorni; patch di gravità media/bassa entro 90 giorni; exploit zero-day entro 24-48 ore. **Integrazione**: Si integra con ISMS-POL-A.8.8 (Gestione delle vulnerabilità).

---

# Ruoli e responsabilità

| Ruolo | A.8.1 Endpoint | A.8.7 Malware | A.8.18 Utilità | A.8.19 Software |
|-------|----------------|---------------|----------------|-----------------|
| **RSSI** | Responsabile (A) | Responsabile (A) | Responsabile (A) | Responsabile (A) |
| **Responsabile Sicurezza IT** | Esegue (R) | Esegue (R) | Esegue (R) | Esegue (R) |
| **Amministratori endpoint** | Esegue (R) | Esegue (R) | Consulta (C) | Consulta (C) |
| **SOC** | Consulta (C) | Esegue (R) | Esegue (R) | Consulta (C) |
| **Utenti finali** | Esegue (R, conformità) | Informato (I) | Informato (I) | Informato (I) |

**RACI**: R=Responsabile (esegue), A=Accountable (autorità decisionale), C=Consultato (fornisce input), I=Informato (aggiornato).

---

# Soglie di conformità

- ✅ Conforme (Verde): ≥90%
- ⚠️ Conformità parziale (Giallo): 70-89%
- ❌ Non conforme (Rosso): <70%

---

# Gestione delle eccezioni

**Autorità di approvazione delle eccezioni**: Basso Rischio: Responsabile Sicurezza IT; Medio Rischio: RSSI (valutazione del rischio obbligatoria); Alto Rischio: RSSI + Comitato del rischio (controlli compensativi obbligatori); Eccezioni permanenti: RSSI + Comitato del rischio (ricertificazione annuale obbligatoria).

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Dispositivo endpoint** | Qualsiasi dispositivo rivolto agli utenti che archivia, elabora o accede alle informazioni organizzative |
| **EDR** | Endpoint Detection and Response — soluzione di sicurezza avanzata per gli endpoint |
| **MAM** | Mobile Application Management — gestione delle applicazioni aziendali sui dispositivi mobili |
| **MDM** | Mobile Device Management — gestione centralizzata dei dispositivi mobili |
| **Programma di utilità con privilegi** | Strumento software capace di aggirare i controlli di sicurezza di sistema e delle applicazioni |
| **BYOD** | Bring Your Own Device — programma che consente l'uso di dispositivi personali per il lavoro |
| **Base di sicurezza** | Requisiti minimi di configurazione di sicurezza per gli endpoint |
| **Controllo delle applicazioni (Whitelisting)** | Controllo di sicurezza che consente solo al software esplicitamente approvato di essere eseguito |
| **FDE** | Full Disk Encryption — cifratura dell'intero volume del disco |
| **Protezione contro le manomissioni** | Funzionalità anti-malware che impedisce la disabilitazione del software di sicurezza |
| **Drift di configurazione** | Deviazione dalla configurazione approvata della base di sicurezza |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **Responsabile Operazioni IT** | [Nome] | [Data] |
| **Responsabile Legale/Conformità** | [Nome] | [Data] |
| **Direzione generale (AD)** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.1-7-18-19 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
