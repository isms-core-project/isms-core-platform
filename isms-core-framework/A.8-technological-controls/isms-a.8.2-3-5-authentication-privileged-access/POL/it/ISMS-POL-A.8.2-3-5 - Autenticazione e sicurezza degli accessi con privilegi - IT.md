<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.2-3-5-IT:framework:POL:a.8.2-3-5 -->
**ISMS-POL-A.8.2-3-5 — Autenticazione e sicurezza degli accessi con privilegi**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Politica di autenticazione e sicurezza degli accessi con privilegi |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.2-3-5 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → Responsabile Operazioni Sicurezza → Responsabile Operazioni IT → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.5.15-16-18; ISMS-IMP-A.8.2-3-5.S1–S5-UG/TG; ISO/IEC 27001:2022 Controlli A.8.2, A.8.3, A.8.5.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la sicurezza dell'autenticazione, la gestione degli accessi con privilegi e l'applicazione tecnica del controllo degli accessi conformemente alla norma ISO/IEC 27001:2022.

**Controlli affrontati**: A.8.5 (Autenticazione sicura); A.8.2 (Diritti di accesso con privilegi); A.8.3 (Restrizione dell'accesso alle informazioni).

**Allineamento normativo** (per ISMS-POL-00): Obbligatorio: nLPD svizzera (Art. 8), RGPD dell'UE (Art. 32), ISO 27001:2022. Condizionale: FINMA, DORA, NIS2 (Art. 21(2)(e) — mandato AMF), PCI DSS v4.0.1.

---

# Requisiti di autenticazione (Controllo A.8.5)

## Standard dei meccanismi di autenticazione

[Organizzazione] DEVE implementare meccanismi di autenticazione appropriati alla sensibilità delle informazioni e dei sistemi a cui si accede.

**Requisiti minimi di autenticazione**:

| Classificazione del sistema | Requisito minimo | Requisito AMF |
|----------------------------|-----------------|---------------|
| **Critico/Alto rischio** | AMF obbligatoria | Token hardware o app di autenticazione |
| **Business standard** | Password + AMF raccomandata | App di autenticazione accettabile |
| **Basso rischio/Pubblico** | Password accettabile | Opzionale |
| **Accesso con privilegi** | AMF obbligatoria | Token hardware preferito (FIDO2) |
| **Accesso remoto** | AMF obbligatoria | Obbligatoria per tutte le connessioni remote |

**Requisiti sulle password** (dove vengono utilizzate le password, per NIST SP 800-63B): Lunghezza minima: 12 caratteri (14 per gli account con privilegi); nessuna scadenza della password a meno che non sia sospettata o rilevata una compromissione; rilevamento delle violazioni (le password vengono verificate rispetto ai database di violazioni noti; le password compromesse richiedono un reset immediato); nessun riutilizzo della password: minimo 24 password nella cronologia.

## Autenticazione a più fattori (AMF)

**L'AMF DEVE essere obbligatoria per**: Tutti gli accessi con privilegi (Tier 0, 1, 2); tutto l'accesso remoto (VPN, desktop remoto, console cloud); tutto l'accesso a dati sensibili; tutte le applicazioni rivolte all'esterno; tutte le console amministrative delle piattaforme cloud.

**Metodi AMF accettabili** (in ordine di preferenza con valutazione della resistenza al phishing):

| Metodo | Resistenza al phishing | Caso d'uso |
|--------|------------------------|-----------|
| Chiavi di sicurezza hardware (FIDO2/WebAuthn) | Alta (resistente al phishing) | Obbligatorie per Tier 0, raccomandate per tutti i privilegi |
| App di autenticazione (TOTP) | Media | Accettabile per Tier 1/2 e utenti standard |
| Notifiche push (con corrispondenza numerica) | Media | Accettabile con corrispondenza numerica abilitata |
| SMS/OTP vocale | Bassa | Solo dove altri metodi non sono fattibili |

**Obiettivi di copertura AMF**: Utenti con privilegi: 100% registrazione AMF; tutti gli utenti: ≥95% entro 12 mesi; accesso remoto: 100% applicazione AMF.

**Valutazione della base di riferimento**: Prima dell'applicazione degli obiettivi, [Organizzazione] DEVE stabilire la base di copertura AMF attuale tramite i report di registrazione del provider di identità. Se la base <80%, è necessario un piano di chiusura delle lacune.

---

# Requisiti di accesso con privilegi (Controllo A.8.2)

## Principi dell'accesso con privilegi

[Organizzazione] DEVE limitare gli accessi con privilegi basandosi su: **Minimo privilegio** (accesso minimo necessario per svolgere le funzioni lavorative); **Need-to-know** (accesso solo alle informazioni necessarie per compiti specifici); **Separazione dei compiti** (funzioni critiche suddivise tra più individui); **Accesso limitato nel tempo** (provisioning Just-in-Time ove possibile).

## Modello di stratificazione degli amministratori

| Livello | Perimetro | Esempi | Requisiti |
|---------|-----------|--------|-----------|
| **Tier 0** | Dominio/Azienda | Admin di dominio, Azure Global Admin, PKI, SIEM | AMF hardware, PAW obbligatoria, registrazione sessione obbligatoria |
| **Tier 1** | Server/Applicazione | Admin server, DBA, Admin sottoscrizione cloud | AMF obbligatoria, workstation admin dedicata raccomandata |
| **Tier 2** | Workstation/Endpoint | Supporto desktop, Help desk con admin locale | AMF obbligatoria, workstation standard accettabile |

**Requisiti di isolamento dei Tier**: Gli account Tier 0 NON DEVONO MAI autenticarsi ai sistemi Tier 1 o 2; gli account Tier 1 NON DEVONO MAI autenticarsi ai sistemi Tier 2; credenziali separate richieste per Tier (es. mario.rossi.t0, mario.rossi.t1).

## Gestione degli accessi con privilegi (PAM)

**Controlli obbligatori**: Inventario degli account con privilegi (tutti documentati e classificati); vault delle password (archiviato in soluzione PAM approvata); registrazione delle sessioni (obbligatoria per Tier 0; raccomandata per Tier 1); accesso Just-in-Time (elevazione temporanea dei privilegi con revoca automatica); rotazione delle credenziali.

**Requisiti di rotazione delle credenziali**:

| Tipo di account | Rotazione predefinita | Adeguamento basato sul rischio |
|----------------|----------------------|-------------------------------|
| Account di servizio (Tier 0) | Massimo 90 giorni | Possibile estensione a 180 giorni con approvazione del Responsabile Sicurezza IT |
| Account di servizio (Tier 1/2) | Massimo 180 giorni | Possibile estensione a 365 giorni con approvazione del Responsabile Sicurezza IT |
| Account di emergenza | Dopo ogni utilizzo + max 365 giorni | Nessun adeguamento — rotazione sempre dopo l'uso |

**Stato del dispiegamento PAM**: La fase di dispiegamento PAM (valutazione, pilota, onboarding Tier 0, onboarding Tier 1, piena operazione) DEVE essere documentata nel Classeur 3. Se PAM non è pienamente operativa, i controlli compensativi DEVONO essere documentati con data di completamento del dispiegamento.

## Revisioni degli accessi con privilegi

**Frequenza di revisione**: Trimestrale per tutti i diritti di accesso con privilegi; immediatamente per cambio di ruolo, cessazione del rapporto di lavoro o incidente di sicurezza; annualmente per audit completo. **Sequenza temporale del rimedio**: Accesso revocato entro 48 ore dalla richiesta di rimozione. **Mancata risposta**: Promemoria automatico al giorno 5; escalation al giorno 8; accesso sospeso al giorno 15 se nessuna risposta.

## Accesso di emergenza (account di emergenza)

[Organizzazione] DEVE mantenere procedure di accesso di emergenza: credenziali degli account di emergenza protette con busta sigillata (cassaforte fisica o busta sigillata PAM); autorizzazione multi-persona richiesta; tutti gli utilizzi registrati, avvisati e rivisti entro 24 ore; credenziali ruotate immediatamente dopo l'utilizzo. **Test periodici**: Semestrali (Q1 e Q3).

---

# Requisiti di restrizione degli accessi (Controllo A.8.3)

## Principi di applicazione degli accessi

[Organizzazione] DEVE applicare le restrizioni degli accessi attraverso controlli tecnici: **Default Deny** (accesso negato per impostazione predefinita; richiesta autorizzazione esplicita); **RBAC** (accesso basato sui ruoli lavorativi); **Allineamento alla classificazione dei dati** (le restrizioni degli accessi corrispondono alla sensibilità dei dati).

## Controlli di accesso tecnici

**Timeout di sessione**:

| Classificazione | Timeout di inattività | Timeout assoluto |
|----------------|----------------------|-----------------|
| Sensibile/Critico | 15 minuti | 8 ore |
| Business standard | 30 minuti | 12 ore |
| Console admin con privilegi | 10 minuti | 4 ore |
| Non classificato (predefinito) | 30 minuti | 12 ore |

**Accesso al database**: Accesso diretto al database limitato ai DBA; accesso delle applicazioni tramite account di servizio con privilegi minimi.

**Accesso alle API**: Autenticazione obbligatoria (OAuth 2.0, chiavi API con rotazione); limitazione della velocità applicata; API sensibili richiedono autorizzazione aggiuntiva.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Direzione generale** | Approvare la politica; allocare il budget; scala di escalation per incidenti importanti |
| **RSSI** | Responsabilità complessiva; approvare la selezione della soluzione PAM e la strategia AMF; approvare il Modello di stratificazione degli amministratori; approvare le eccezioni |
| **Responsabile Sicurezza IT** | Gestione quotidiana dell'infrastruttura di autenticazione; monitorare gli avvisi; condurre revisioni trimestrali degli accessi con privilegi |
| **Team IAM** | Gestire il provider di identità e l'infrastruttura SSO; elaborare le richieste di accesso con privilegi; mantenere la registrazione AMF |
| **Amministratori di sistema** | Implementare i controlli degli accessi sui sistemi gestiti; rispettare i requisiti di stratificazione; utilizzare account dedicati con privilegi |
| **Tutti gli utenti** | Proteggere le credenziali di autenticazione; segnalare immediatamente la sospetta compromissione; completare la registrazione AMF; non condividere account o credenziali |

---

# Indicatori di prestazione chiave

| Metrica | Obiettivo | Frequenza |
|---------|-----------|-----------|
| Registrazione AMF (tutti gli utenti) | ≥95% | Mensile |
| Registrazione AMF (con privilegi) | 100% | Settimanale |
| Completamento della revisione degli accessi con privilegi | 100% | Trimestrale |
| Conformità alla politica sulle password | ≥98% | Mensile |
| Integrazione SSO delle applicazioni | ≥90% | Trimestrale |
| Registrazione delle sessioni con privilegi (Tier 0) | 100% | Mensile |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **Responsabile Operazioni IT** | [Nome] | [Data] |
| **Responsabile Legale/Conformità** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la sicurezza dell'autenticazione, la gestione degli accessi con privilegi e l'applicazione tecnica del controllo degli accessi. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.2-3-5 (S1-S5).*

<!-- QA_VERIFIED: 2026-04-03 -->
