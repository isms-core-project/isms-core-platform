<!-- ISMS-CORE:REF:ISMS-REF-A.8.15-IT-logging-standards-reference:framework:REF:a.8.15 -->
**ISMS-REF-A.8.15 — Riferimento sugli standard di registrazione**
**Standard di formato dei registri e specifiche tecniche (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento sugli standard di registrazione |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-REF-A.8.15 |
| **Autore del documento** | Centro operativo di sicurezza (SOC) / Team di architettura della sicurezza |
| **Proprietario del documento** | Responsabile della sicurezza delle informazioni |
| **Approvato da** | RSSI (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | SOC / Architettura della sicurezza | Riferimento tecnico iniziale per la certificazione ISO 27001:2022 |

**Ciclo di revisione**: Trimestrale (gli standard di formato dei registri e le tecnologie evolvono frequentemente)  
**Prossima data di revisione**: [Data + 3 mesi]  
**Approvatori**: Responsabile SOC / Team di architettura della sicurezza (riferimento tecnico, nessuna approvazione SGSI richiesta)

**Distribuzione**: Team SOC, Ingegneri della sicurezza, Amministratori di sistema, Sviluppatori di applicazioni (per la consapevolezza tecnica dell'implementazione)

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione.

- Questo documento NON fa parte del Sistema di Gestione della Sicurezza delle Informazioni (SGSI).
- Questo documento NON definisce controlli o requisiti di registrazione obbligatori.
- Questo documento NON stabilisce requisiti vincolanti, scadenze, ICP o SLA.
- Questo documento NON impone l'uso, il divieto o la configurazione di formati di registro, strumenti o piattaforme specifici.
- Questo documento NON sostituisce né estende alcuna politica SGSI.

Tutti i requisiti di registrazione vincolanti, gli obblighi e le decisioni di governance sono definiti esclusivamente in **ISMS-POL-A.8.15 (Politica di registrazione)** e in altri documenti SGSI approvati.

Questo documento serve esclusivamente come riferimento tecnico per:

- Descrivere i formati di registro e gli standard comunemente utilizzati
- Fornire convenzioni di denominazione dei campi e standard di codifica
- Supportare la pianificazione tecnica dell'implementazione
- Informare la selezione dei formati di registro e lo sviluppo dei parser
- **Questo documento non deve essere utilizzato come prova di audit dell'implementazione**

---

# Scopo e ambito del documento

## Scopo

Questo documento fornisce un riferimento tecnico per gli standard di formato dei registri, le convenzioni di denominazione dei campi e i requisiti di codifica comunemente utilizzati nelle implementazioni di registrazione della sicurezza. È inteso a supportare:

- L'implementazione tecnica dei requisiti di registrazione per ISMS-POL-A.8.15
- La selezione di formati di registro appropriati in base al tipo di sistema e ai requisiti di integrazione
- Lo sviluppo di regole di analisi dei registri e l'integrazione SIEM
- La standardizzazione dei nomi dei campi tra le fonti di registro dell'organizzazione
- La comprensione dei formati di registro standard del settore (Syslog, CEF, JSON)

## Relazione con il SGSI

Questo documento è un **riferimento tecnico non vincolante**. Tutti i requisiti di controllo della registrazione sono definiti esclusivamente in ISMS-POL-A.8.15.

---

# Standard del formato Syslog (RFC 5424)

## Panoramica

**Syslog (RFC 5424)** è il protocollo di registrazione standard per i componenti dell'infrastruttura, i sistemi operativi e i dispositivi di rete.

**Casi d'uso comuni**:

- Dispositivi di rete (router, switch, firewall)
- Sistemi operativi Unix/Linux
- Servizi di infrastruttura (DNS, DHCP, NTP)
- Applicazioni legacy

**Protocollo**:

- UDP porta 514 (tradizionale, non crittografato — NON RACCOMANDATO per i registri di sicurezza)
- TCP porta 514 o 6514 (raccomandato per l'affidabilità)
- TLS/TCP porta 6514 (raccomandato per la trasmissione crittografata secondo ISMS-POL-A.8.15 Sezione 2.2.3)

## Formato del messaggio Syslog

**Struttura del messaggio RFC 5424**:

```
<PRI>VERSIONE TIMESTAMP HOSTNAME NOME-APP PROCID MSGID DATI-STRUTTURATI MSG
```

**Esempio**:
```
<134>1 2026-01-21T14:32:15.003+01:00 server01.example.com sshd 1234 ID47 [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"] Password errata per utente invalido admin da 10.0.1.50 porta 22 ssh2
```

## Priorità Syslog (PRI)

**Calcolo della priorità**: `PRI = (Facility × 8) + Severity`

**Codici di facility** (comuni):

| Codice | Facility | Utilizzo |
|--------|----------|----------|
| 0 | kernel | Messaggi del kernel |
| 1 | user | Messaggi a livello utente |
| 2 | mail | Sistema di posta |
| 3 | daemon | Demoni di sistema |
| 4 | auth | Sicurezza/autenticazione |
| 5 | syslog | Interno Syslog |
| 10 | authpriv | Sicurezza/autorizzazione (privato) |
| 16 | local0-7 | Uso locale (applicazioni personalizzate) |

**Livelli di gravità**:

| Codice | Gravità | Descrizione | Linea guida sull'utilizzo |
|--------|---------|-------------|--------------------------|
| 0 | Emergency | Sistema inutilizzabile | Panico del sistema, crash imminente |
| 1 | Alert | Azione immediata richiesta | Errore di risorsa critica, corruzione dei dati |
| 2 | Critical | Condizioni critiche | Errore hardware, errore di servizio critico |
| 3 | Error | Condizioni di errore | Errori non critici, errori dell'applicazione |
| 4 | Warning | Condizioni di avviso | Errori recuperabili, avvisi sulle risorse |
| 5 | Notice | Normale ma significativo | Eventi significativi (elevazione dei privilegi, modifica della configurazione) |
| 6 | Informational | Messaggi informativi | Operazioni normali, autenticazioni riuscite |
| 7 | Debug | Messaggi di debug | Informazioni dettagliate per la risoluzione dei problemi |

**Mappatura della gravità consigliata**:

- **Eventi di sicurezza**: Notice (5) per le operazioni riuscite, Warning (4) per le violazioni delle politiche, Error (3) per gli attacchi
- **Autenticazione**: Info (6) per il successo, Warning (4) per i tentativi falliti, Error (3) per i blocchi dell'account
- **Eventi di sistema**: Varia in base al contesto (Critical per gli errori del servizio, Notice per le modifiche alla configurazione)

## Formato del timestamp Syslog

**Formato richiesto**: ISO 8601 con fuso orario

```
AAAA-MM-GGTHH:MM:SS.SSSSSS+FO
```

**Esempi**:

- `2026-01-21T14:32:15+01:00` (con offset del fuso orario)
- `2026-01-21T13:32:15Z` (notazione UTC)
- `2026-01-21T14:32:15.003+01:00` (con millisecondi)

**Migliori pratiche**:

- Includere sempre le informazioni sul fuso orario
- Utilizzare la precisione in millisecondi per i sistemi ad alto volume dove l'ordinamento degli eventi è critico
- Sincronizzare gli orologi del sistema tramite NTP secondo ISMS-POL-A.8.17
- Utilizzare UTC per gli ambienti multi-sito per semplificare la correlazione

## Dati strutturati Syslog

**Formato**: Coppie chiave-valore tra parentesi quadre

```
[SD-ID@PEN chiave1="valore1" chiave2="valore2"]
```

**Esempio**:
```
[secureAuth@123456 user="mrossi" src="10.0.1.50" action="login" result="success"]
```

**Elementi di dati strutturati consigliati**:

- `user="nome_utente"` — identificatore utente
- `src="indirizzo_IP"` — IP di origine
- `dst="indirizzo_IP"` — IP di destinazione
- `action="verbo"` — azione eseguita
- `result="success|failure"` — risultato
- `reason="descrizione"` — motivo dell'errore o contesto aggiuntivo

## Esempio di configurazione Syslog

**Configurazione rsyslog Linux** (TCP con TLS):

```
# Inviare i registri di sicurezza al SIEM centrale
*.* @@(o)siem.example.com:6514
$ActionSendStreamDriverMode 1
$ActionSendStreamDriverAuthMode x509/name
$ActionSendStreamDriverPermittedPeer siem.example.com
```

**Esempio di configurazione Syslog per dispositivo di rete** (Cisco):

```
logging host 10.0.2.100 transport tcp port 6514
logging trap informational
logging origin-id hostname
logging source-interface Loopback0
```

---

# Common Event Format (CEF)

## Panoramica

**Common Event Format (CEF)** è un formato di registro standardizzato per gli eventi di sicurezza progettato per l'integrazione SIEM.

**Sviluppato da**: ArcSight (ora Micro Focus), standard di settore ampiamente adottato

**Casi d'uso comuni**:

- Strumenti di sicurezza (firewall, IDS/IPS, web application firewall)
- Piattaforme di protezione degli endpoint
- Sistemi di prevenzione della perdita di dati
- Sistemi di autenticazione e controllo degli accessi
- Integrazione SIEM da diversi prodotti di sicurezza

## Formato del messaggio CEF

**Struttura**:

```
CEF:Versione|Fornitore|Prodotto|Versione prodotto|ID firma|Nome|Gravità|Estensione
```

**Esempio**:
```
CEF:0|Palo Alto Networks|PAN-OS|9.1.0|THREAT|URL Filtering|7|rt=Jan 21 2026 14:32:15 src=10.0.1.50 dst=93.184.216.34 spt=52341 dpt=443 request=https://malicious.example.com act=blocked
```

## Campi di intestazione CEF

| Campo | Descrizione | Esempio |
|-------|-------------|---------|
| **Versione** | Versione del formato CEF | 0 (standard corrente) |
| **Fornitore** | Nome del fornitore | Palo Alto Networks, Cisco, Check Point |
| **Prodotto** | Nome del prodotto | PAN-OS, ASA, FortiGate |
| **Versione prodotto** | Versione del prodotto | 9.1.0 |
| **ID firma** | Identificatore dell'evento | THREAT, AUTH, CONFIG |
| **Nome** | Nome leggibile dell'evento | URL Filtering, Login Failed |
| **Gravità** | Scala 0-10 | 0=Basso, 5=Medio, 10=Critico |

**Scala di gravità**:

- 0-3: Basso (informativo, problemi minori)
- 4-6: Medio (avvisi, violazioni delle politiche)
- 7-8: Alto (minacce alla sicurezza, attacchi)
- 9-10: Critico (minacce gravi, compromissioni riuscite)

## Campi di estensione CEF

**Chiavi di estensione standard** (comunemente utilizzate):

| Chiave | Nome completo | Descrizione | Esempio |
|--------|---------------|-------------|---------|
| **src** | Indirizzo di origine | Indirizzo IP di origine | 10.0.1.50 |
| **dst** | Indirizzo di destinazione | Indirizzo IP di destinazione | 93.184.216.34 |
| **spt** | Porta di origine | Porta TCP/UDP di origine | 52341 |
| **dpt** | Porta di destinazione | Porta TCP/UDP di destinazione | 443 |
| **suser** | Nome utente di origine | Nome utente di origine | mrossi |
| **duser** | Nome utente di destinazione | Nome utente di destinazione | admin |
| **act** | Azione | Azione eseguita | blocked, allowed, alerted |
| **app** | Protocollo applicativo | Protocollo applicativo | HTTP, HTTPS, SSH, FTP |
| **request** | URL della richiesta | URL o comando completo | https://example.com/percorso |
| **requestMethod** | Metodo della richiesta | Metodo HTTP | GET, POST, PUT, DELETE |
| **cn1-cn3** | Numero personalizzato 1-3 | Campi numerici personalizzati | 1234 (byte trasferiti) |
| **cs1-cs6** | Stringa personalizzata 1-6 | Campi stringa personalizzati | "User-Agent: Mozilla/5.0" |
| **rt** | Ora di ricezione | Ora di ricezione dell'evento | Jan 21 2026 14:32:15 |
| **outcome** | Risultato | Risultato dell'evento | success, failure, unknown |
| **reason** | Motivo | Motivo dell'azione o dell'errore | Credenziali non valide |
| **fileHash** | Hash del file | Hash del file (MD5, SHA256) | a1b2c3d4e5f6... |
| **filePath** | Percorso del file | Percorso completo del file | /var/log/sospetto.exe |

## Esempi CEF per tipo di evento

**Evento di autenticazione** (Accesso non riuscito):
```
CEF:0|Microsoft|Windows|Server 2019|4625|An account failed to log on|5|rt=Jan 21 2026 14:32:15 suser=admin src=10.0.1.50 outcome=failure reason=Unknown user name or bad password cs1Label=Domain cs1=EXAMPLE
```

**Evento firewall** (Connessione bloccata):
```
CEF:0|Palo Alto Networks|PAN-OS|9.1.0|TRAFFIC|deny|8|rt=Jan 21 2026 14:32:15 src=10.0.1.50 dst=203.0.113.100 spt=52341 dpt=22 proto=TCP act=deny app=SSH
```

**Rilevamento di malware**:
```
CEF:0|CrowdStrike|Falcon|6.42|MALWARE|Malware Detected|9|rt=Jan 21 2026 14:32:15 src=10.0.2.15 filePath=C:\\Users\\mrossi\\Downloads\\malware.exe fileHash=a1b2c3d4e5f6 act=quarantined outcome=success
```

**Web Application Firewall** (SQL Injection bloccata):
```
CEF:0|F5 Networks|BIG-IP ASM|15.1.0|SQL_INJECTION|SQL Injection Attack|9|rt=Jan 21 2026 14:32:15 src=203.0.113.50 request=https://webapp.example.com/login?id=1' OR '1'='1 requestMethod=GET act=blocked
```

## Migliori pratiche CEF

1. **Utilizzare le chiavi di estensione standard** dove applicabile (src, dst, suser) per la compatibilità SIEM
2. **Campi personalizzati per i dati non standard** (cs1-cs6 per le stringhe, cn1-cn3 per i numeri)
3. **Includere sempre il timestamp** (campo rt) per la correlazione accurata degli eventi
4. **Eseguire l'escape dei caratteri pipe** nei valori di estensione (usare barra rovesciata: \|)
5. **Eseguire l'escape delle barre rovesciate** nei valori di estensione (usare doppia barra rovesciata: \\)
6. **Eseguire l'escape dei segni uguale** nei valori dei campi personalizzati (usare barra rovesciata: \=)

---

# Registrazione strutturata JSON

## Panoramica

**JSON (JavaScript Object Notation)** è lo standard moderno per la registrazione delle applicazioni e i registri dei servizi cloud.

**Casi d'uso comuni**:

- Applicazioni web moderne e microservizi
- Ambienti di container e Kubernetes
- Applicazioni cloud-native (AWS, Azure, GCP)
- Gateway API e funzioni serverless
- Registri di applicazioni SaaS

**Vantaggi**:

- Leggibile dall'uomo e analizzabile dalle macchine
- Supporto nativo nelle moderne piattaforme SIEM e di aggregazione dei registri
- Schema flessibile (può accogliere qualsiasi struttura di campo)
- Facile da generare dal codice dell'applicazione (librerie disponibili per tutti i linguaggi)

## Struttura del registro JSON

**Campi minimi richiesti**:

```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "INFO",
  "message": "Accesso utente riuscito",
  "logger": "auth.service",
  "context": {
    "user": "mrossi",
    "source_ip": "10.0.1.50",
    "action": "login",
    "outcome": "success"
  }
}
```

## Nomi dei campi standard

**Convenzione di denominazione JSON consigliata** (snake_case):

| Nome del campo | Tipo | Descrizione | Esempio |
|---------------|------|-------------|---------|
| **timestamp** | stringa (ISO 8601) | Timestamp dell'evento con fuso orario | "2026-01-21T14:32:15+01:00" |
| **level** | stringa | Livello di registro | "INFO", "WARN", "ERROR", "DEBUG" |
| **message** | stringa | Messaggio leggibile | "Accesso utente riuscito" |
| **logger** | stringa | Nome del logger o modulo | "auth.service", "app.controller" |
| **user_id** | stringa | Identificatore utente | "mrossi", "user@example.com" |
| **session_id** | stringa | Identificatore di sessione | "abc123def456" |
| **request_id** | stringa | ID di traccia della richiesta | "req-7f8a9b0c" |
| **source_ip** | stringa | Indirizzo IP di origine | "10.0.1.50" |
| **destination_ip** | stringa | Indirizzo IP di destinazione | "93.184.216.34" |
| **action** | stringa | Azione eseguita | "login", "create", "delete", "read" |
| **resource** | stringa | Risorsa interessata | "/api/users", "file.txt" |
| **outcome** | stringa | Risultato dell'azione | "success", "failure", "error" |
| **error_code** | stringa | Codice di errore o tipo di eccezione | "AUTH001", "NullPointerException" |
| **duration_ms** | numero | Durata in millisecondi | 250 |
| **http_method** | stringa | Metodo HTTP | "GET", "POST", "PUT", "DELETE" |
| **http_status** | numero | Codice di stato HTTP | 200, 404, 500 |
| **user_agent** | stringa | Stringa user agent | "Mozilla/5.0..." |

## Livelli di registro

**Livelli di registro standard** (equivalenza RFC 5424):

| Livello | Gravità | Utilizzo | Esempio |
|---------|---------|----------|---------|
| **TRACE** | Debug | Debug molto dettagliato | Valori delle variabili, entrata/uscita delle funzioni |
| **DEBUG** | Debug | Debug dettagliato | Flusso logico, risultati intermedi |
| **INFO** | Informativo | Operazioni normali | Servizio avviato, utente connesso, transazione completata |
| **WARN** | Avviso | Problemi potenziali | API deprecata utilizzata, tentativo di nuovo tentativo |
| **ERROR** | Errore | Condizioni di errore | Connessione al database non riuscita, errore di validazione |
| **FATAL/CRITICAL** | Critico | Errori gravi | Crash dell'applicazione, errore irrecuperabile |

**Raccomandazione per la produzione**:

- **Registri di sicurezza**: INFO e superiori (INFO per il successo, WARN per le violazioni, ERROR per gli attacchi)
- **Registri dell'applicazione**: WARN e superiori (minimizzare il rumore catturando i problemi)
- **DEBUG/TRACE**: Disabilitato in produzione (abilitare temporaneamente per la risoluzione dei problemi)

## Contesto strutturato

**Contesto nidificato per i campi correlati**:

```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "ERROR",
  "message": "Autenticazione non riuscita",
  "logger": "auth.service",
  "user": {
    "id": "mrossi",
    "email": "mrossi@example.com",
    "role": "user"
  },
  "request": {
    "id": "req-7f8a9b0c",
    "method": "POST",
    "path": "/api/auth/login",
    "source_ip": "10.0.1.50",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
  },
  "auth": {
    "method": "password",
    "outcome": "failure",
    "reason": "invalid_credentials",
    "attempts": 3
  },
  "error": {
    "code": "AUTH001",
    "type": "AuthenticationException",
    "message": "Nome utente o password non validi"
  }
}
```

## Migliori pratiche JSON

1. **Includere sempre il timestamp** con fuso orario (formato ISO 8601)
2. **Utilizzare snake_case** per i nomi dei campi (convenzione coerente)
3. **Minimizzare la nidificazione** (massimo 1-2 livelli per la leggibilità)
4. **Evitare di registrare dati sensibili** (nessuna password, numeri di carta completi, DCP salvo necessità)
5. **Includere identificatori di contesto** (request_id, session_id, user_id) per la correlazione
6. **Utilizzare dati strutturati** invece di concatenare stringhe nel campo del messaggio
7. **Schema coerente** nell'applicazione (utilizzare una libreria di registrazione con validazione dello schema)
8. **Un evento di registro per riga** (JSON delimitato da nuove righe per facilità di analisi)

---

# Standard di timestamp

## Formato richiesto: ISO 8601

**Standard**: ISO 8601 con informazioni sul fuso orario

**Formato**: `AAAA-MM-GGTHH:MM:SS.SSSSSS±HH:MM` o `AAAA-MM-GGTHH:MM:SS.SSSZ`

**Esempi**:

- `2026-01-21T14:32:15+01:00` (Ora dell'Europa centrale con offset)
- `2026-01-21T13:32:15Z` (UTC, suffisso 'Z' indica UTC)
- `2026-01-21T14:32:15.003+01:00` (con millisecondi)
- `2026-01-21T14:32:15.123456+01:00` (con microsecondi)

## Gestione del fuso orario

**Raccomandazione**: Utilizzare UTC per tutta l'archiviazione centralizzata dei registri

**Giustificazione**:

- Elimina gli errori di conversione del fuso orario
- Semplifica la correlazione tra diverse ubicazioni geografiche
- Evita le complicazioni legate all'ora legale
- Riferimento universale per le organizzazioni multi-sito

## Requisiti di precisione

**Minimo**: Precisione al secondo (`AAAA-MM-GGTHH:MM:SS`)

**Raccomandato**: Precisione al millisecondo (`AAAA-MM-GGTHH:MM:SS.SSS`)

- Richiesta per i sistemi ad alto volume (centinaia di eventi al secondo)
- Consente l'ordinamento preciso degli eventi nello stesso secondo
- Necessaria per la correlazione di sequenze di eventi rapide

## Sincronizzazione dell'orario

**Requisito**: Tutte le fonti di registro DEVONO sincronizzare l'orario con una fonte di orario autorevole secondo ISMS-POL-A.8.17 (Sincronizzazione degli orologi).

**Configurazione NTP**:

- Server NTP primario (Stratum 1 o 2)
- Server NTP secondari per la ridondanza
- Soglia massima di deriva dell'orologio: ±100 ms
- Avviso in caso di errore di sincronizzazione NTP

**Importanza**: I timestamp accurati sono fondamentali per:

- La correlazione degli eventi tra più sistemi
- La ricostruzione della cronologia degli incidenti
- L'analisi forense e le prove legali
- La verifica della conformità

---

# Convenzioni di denominazione dei campi

## Standard di denominazione

**Utilizzare una convenzione di denominazione coerente**:

| Convenzione | Esempio | Caso d'uso |
|-------------|---------|------------|
| **snake_case** | `source_ip`, `user_id`, `event_type` | Registri JSON, applicazioni Python |
| **camelCase** | `sourceIp`, `userId`, `eventType` | Applicazioni JavaScript, alcuni SIEM |
| **dot.notation** | `event.type`, `user.id`, `source.ip` | ECS (Elastic Common Schema), campi nidificati |

**Raccomandazione**: Scegliere UNA convenzione e utilizzarla in modo coerente nell'intera organizzazione. Il snake_case è sempre più comune per la registrazione della sicurezza.

## Nomi dei campi standard

**Campi di identità**:

- `user_id` / `user` / `username` — identificatore utente
- `user_email` — indirizzo email dell'utente
- `service_account` — identificatore dell'account di servizio
- `session_id` — identificatore di sessione
- `request_id` / `trace_id` — identificatore di traccia della richiesta
- `transaction_id` — identificatore di transazione

**Campi di rete**:

- `source_ip` / `src_ip` — indirizzo IP di origine
- `destination_ip` / `dst_ip` — indirizzo IP di destinazione
- `source_port` / `src_port` — porta TCP/UDP di origine
- `destination_port` / `dst_port` — porta TCP/UDP di destinazione
- `protocol` — protocollo di rete (TCP, UDP, ICMP)
- `hostname` — nome host del sistema

**Campi di azione**:

- `action` / `event_action` — azione eseguita (login, create, delete, read, update)
- `event_type` / `event_category` — categoria dell'evento (autenticazione, autorizzazione, configurazione)
- `outcome` / `result` — risultato (success, failure, error)
- `reason` — motivo del risultato o dell'azione
- `severity` / `level` — livello di gravità

**Campi di risorsa**:

- `resource` / `object` — risorsa interessata
- `file_path` — percorso del file
- `file_hash` — hash del file (MD5, SHA256)
- `url` / `request_url` — URL o endpoint
- `api_endpoint` — endpoint API

**Campi temporali**:

- `timestamp` / `event_time` — timestamp dell'evento
- `duration` / `duration_ms` — durata in millisecondi
- `start_time` — timestamp di inizio
- `end_time` — timestamp di fine

**Campi di errore**:

- `error_code` — codice di errore
- `error_type` / `exception_type` — nome della classe di eccezione
- `error_message` / `exception_message` — descrizione dell'errore
- `stack_trace` — traccia dello stack (per gli errori)

---

# Codifica dei caratteri ed escape

## Codifica dei caratteri

**Standard**: Codifica UTF-8 per tutti i registri

**Giustificazione**:

- Supporto universale per i caratteri internazionali
- Efficiente per ASCII (1 byte per carattere)
- Compatibile con JSON, XML, le applicazioni moderne

## Escape dei caratteri speciali

**Syslog (RFC 5424)**:

- Nessun escape speciale richiesto nel campo MSG
- Utilizzare il formato dei dati strutturati per le coppie chiave-valore (escape automatico)

**CEF**:

- Eseguire l'escape dei caratteri pipe: `|` → `\|`
- Eseguire l'escape delle barre rovesciate: `\` → `\\`
- Eseguire l'escape dei segni uguale nei valori di estensione: `=` → `\=`
- Eseguire l'escape delle nuove righe: `\n` → `\\n`

**JSON**:

- Le librerie JSON eseguono automaticamente l'escape dei caratteri speciali
- Escape manuale (se necessario):
  - Virgolette doppie: `"` → `\"`
  - Barre rovesciate: `\` → `\\`
  - Nuove righe: carattere di nuova riga → `\n`
  - Tabulazioni: carattere di tabulazione → `\t`

## Lunghezze massime dei campi

**Raccomandazioni** (compatibilità SIEM):

| Tipo di campo | Lunghezza massima | Giustificazione |
|--------------|-------------------|-----------------|
| **Campi stringa** | 1024 caratteri | Limiti dei campi del database SIEM |
| **Campo messaggio** | 8192 caratteri | Il messaggio può includere tracce dello stack |
| **Campi URL** | 2048 caratteri | Supporto della lunghezza URL moderna |
| **Percorso del file** | 4096 caratteri | Massimo del percorso Unix/Linux |
| **Identificatore utente** | 256 caratteri | Indirizzi email, DN LDAP |

---

# Guida all'implementazione

## Matrice di selezione del formato di registro

**Guida alla decisione**: Scegliere il formato di registro in base al tipo di sistema

| Tipo di sistema | Formato consigliato | Giustificazione |
|----------------|---------------------|-----------------|
| **Dispositivi di rete** (Firewall, Router, Switch) | Syslog (RFC 5424) | Supporto nativo, configurazione minima |
| **OS Unix/Linux** | Syslog (RFC 5424) | Supporto nativo, infrastruttura standard |
| **OS Windows** | Windows Event Log (nativo) | Supporto nativo, convertire in CEF o JSON per SIEM |
| **Strumenti di sicurezza** (IDS, Firewall, WAF) | CEF | Integrazione SIEM, eventi di sicurezza standardizzati |
| **Applicazioni web** | JSON | Facile da generare, schema flessibile |
| **Microservizi** | JSON | Cloud-native, compatibile con i container |
| **Servizi cloud** (AWS, Azure, GCP) | JSON | Formato nativo, integrazione transparente |
| **Registri del database** | JSON o Syslog | Specifico per l'applicazione, JSON preferito |

## Considerazioni sull'integrazione SIEM

**Sviluppo dei parser**:

- Syslog: Utilizzare i parser integrati, personalizzare per l'estrazione dei dati strutturati
- CEF: Utilizzare i parser CEF integrati, mappare i campi di estensione allo schema SIEM
- JSON: Configurare il parser JSON, definire i mapping dei campi

**Mapping dei campi**:

- Mappare i campi della fonte di registro allo schema comune SIEM (normalizzare i nomi dei campi)
- Creare campi calcolati per i dati derivati (es. geolocalizzazione dall'IP)
- Arricchire gli eventi con la threat intelligence (ricerche di IP malevoli)

## Raccomandazioni sulle librerie di registrazione

**Per linguaggio di programmazione**:

| Linguaggio | Libreria consigliata | Supporto registrazione strutturata |
|------------|---------------------|-------------------------------------|
| **Python** | `structlog`, `python-json-logger` | Sì (output JSON) |
| **Java** | `Logback`, `Log4j2` | Sì (encoder JSON disponibile) |
| **JavaScript/Node.js** | `winston`, `pino` | Sì (JSON nativo) |
| **Go** | `zap`, `logrus` | Sì (JSON nativo) |
| **C#/.NET** | `Serilog`, `NLog` | Sì (formatter JSON) |
| **Ruby** | `Lograge`, `semantic_logger` | Sì (output JSON) |
| **PHP** | `Monolog` | Sì (formatter JSON) |

---

# Relazione con ISMS-POL-A.8.15

Questo documento fornisce **indicazioni sull'implementazione tecnica** che possono informare:

- La selezione del formato di registro durante l'integrazione del sistema (ISMS-IMP-A.8.15.1)
- Lo sviluppo dei parser dei registri per l'integrazione SIEM (ISMS-IMP-A.8.15.2)
- La standardizzazione dei nomi dei campi tra le fonti di registro dell'organizzazione
- La formazione di sviluppatori e amministratori di sistema sugli standard di registrazione

Questo documento NON:

- Sostituisce né estende i requisiti di ISMS-POL-A.8.15
- Stabilisce selezioni di formati di registro obbligatorie
- Crea obblighi di conformità
- Definisce criteri di audit

Tutti i requisiti di controllo della registrazione sono definiti esclusivamente in ISMS-POL-A.8.15 e implementati tramite le procedure ISMS-IMP-A.8.15.

---

**FINE DEL DOCUMENTO**

*Questo è un documento di riferimento tecnico esclusivamente a scopo di sensibilizzazione. Non stabilisce requisiti SGSI e non crea obblighi di conformità.*
<!-- QA_VERIFIED: 2026-04-04 -->
