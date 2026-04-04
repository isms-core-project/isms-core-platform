<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.20-22-IT:framework:POL:a.8.20-22 -->
**ISMS-POL-A.8.20-22 — Sicurezza della rete**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza della rete |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.20-22 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → Responsabile Operazioni di Rete → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.20-22.S1–S6-UG/TG; ISMS-POL-A.8.15; ISMS-POL-A.8.16; ISMS-POL-A.5.23; ISO/IEC 27001:2022 Controlli A.8.20, A.8.21, A.8.22.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di sicurezza della rete per proteggere gli asset informativi attraverso un'infrastruttura di rete sicura, servizi e segmentazione, conformemente ai Controlli A.8.20, A.8.21 e A.8.22 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutta l'infrastruttura di rete, i dispositivi di rete, i servizi di rete e i segmenti di rete indipendentemente dal modello di dispiegamento (on-premise, cloud, ibrido) o dalla tecnologia.

**Approccio a controlli combinati**: I tre controlli sono implementati come quadro unificato perché operano sulla stessa infrastruttura di rete e condividono processi comuni di scoperta, valutazione e raccolta delle prove. Ciascun controllo mantiene requisiti distinti ai fini della DdA.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Allineamento sul controllo

**A.8.20 — Sicurezza delle reti**: Le reti e i dispositivi di rete devono essere protetti, gestiti e controllati per proteggere le informazioni nei sistemi e nelle applicazioni.

**A.8.21 — Sicurezza dei servizi di rete**: I meccanismi di sicurezza, i livelli di servizio e i requisiti di gestione di tutti i servizi di rete devono essere identificati e inclusi nei relativi accordi.

**A.8.22 — Separazione delle reti**: I gruppi di servizi informativi, gli utenti e i sistemi informativi devono essere separati nelle reti dell'organizzazione.

---

# Enunciati di politica

## Sicurezza dell'infrastruttura di rete (A.8.20)

[Organizzazione] DEVE proteggere, gestire e controllare tutta l'infrastruttura di rete.

**Inventario e documentazione della rete**: Tutti i dispositivi di rete DEVONO essere registrati nell'inventario degli asset; l'architettura di rete DEVE essere documentata e aggiornata almeno annualmente e a seguito di modifiche significative; la documentazione DEVE includere i diagrammi di rete, la topologia e i flussi di traffico.

**Hardening dei dispositivi di rete**: Tutti i dispositivi di rete DEVONO implementare basi di configurazione sicure; le funzionalità, i servizi e le porte non necessari DEVONO essere disabilitati; le credenziali predefinite DEVONO essere cambiate prima del dispiegamento; le patch di sicurezza DEVONO essere applicate per ISMS-POL-A.8.8.

**Accesso ai dispositivi di rete**: L'accesso amministrativo ai dispositivi di rete DEVE essere limitato al personale IT autorizzato; l'AMF DEVE essere richiesta per l'accesso amministrativo ai dispositivi critici; tutti gli accessi amministrativi DEVONO essere registrati.

**Cifratura del traffico di rete**: Il traffico di rete che trasporta informazioni sensibili DEVE essere cifrato: TLS 1.2 minimo (TLS 1.3 preferito) per le connessioni applicative; VPN con cifratura forte per le connessioni di accesso remoto; SSH per l'amministrazione dei dispositivi di rete (Telnet vietato); TLS per la posta elettronica in transito.

## Sicurezza dei servizi di rete (A.8.21)

[Organizzazione] DEVE identificare e proteggere tutti i servizi di rete.

**Inventario dei servizi di rete**: Tutti i servizi di rete (DNS, DHCP, NTP, e-mail, proxy, VPN, accesso remoto, bilanciamento del carico) DEVONO essere inventariati; ogni servizio DEVE avere un proprietario identificato; le porte e i protocolli utilizzati da ciascun servizio DEVONO essere documentati.

**Sicurezza dei servizi di rete critici**: DNS: DNSSEC implementato per le zone critiche; monitoraggio per il dirottamento DNS; NTP: sorgenti NTP affidabili per ISMS-POL-A.8.17; VPN: autenticazione forte obbligatoria; sessioni monitorate e registrate; E-mail: SPF, DKIM, DMARC implementati; ispezione del contenuto abilitata.

**Sicurezza dei servizi di terze parti**: Gli accordi per i servizi di rete di terze parti DEVONO includere i requisiti di sicurezza; i livelli di servizio di sicurezza DEVONO essere monitorati; i fornitori di servizi DEVONO fornire prove di conformità alla sicurezza.

## Separazione delle reti (A.8.22)

[Organizzazione] DEVE implementare la segmentazione della rete per separare i sistemi e gli utenti in base ai loro requisiti di sicurezza e aziendali.

**Segmentazione minima obbligatoria**:

| Segmento | Descrizione | Accesso consentito |
|---------|-------------|-------------------|
| **DMZ** | Sistemi rivolti all'esterno (server web, proxy) | Internet → DMZ → Rete interna (limitata) |
| **Rete aziendale** | Endpoint degli utenti, workstation | Accesso agli utenti alle risorse aziendali |
| **Rete server** | Server applicativi interni | Solo dal personale IT autorizzato e dalla rete aziendale |
| **Rete dati** | Server di database | Solo dai server applicativi, non dagli endpoint |
| **Rete di gestione** | Console di gestione IT, accesso OOB | Solo dal personale IT autorizzato |
| **Rete ospiti/BYOD** | Accesso guest e BYOD | Internet; accesso interno limitato o nullo |

**Requisiti tecnici di segmentazione**: Firewall o funzionalità firewall DEVONO imporre la separazione tra i segmenti; le regole del firewall DEVONO implementare il default-deny (tutto è vietato a meno che non sia esplicitamente consentito); le regole del firewall DEVONO essere riviste trimestralmente; le modifiche alle regole DEVONO seguire il processo di gestione dei cambiamenti (ISMS-POL-A.8.32).

**Controllo del movimento laterale**: I sistemi critici DEVONO avere accesso limitato agli altri sistemi nella stessa rete; le connessioni tra le zone DEVONO essere registrate e monitorate; le anomalie nel traffico tra le zone DEVONO generare avvisi.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approvazione dell'architettura di sicurezza della rete; revisione delle eccezioni |
| **Responsabile Operazioni di Rete** | Implementazione tecnica; manutenzione dell'infrastruttura di rete; gestione delle regole del firewall |
| **Operazioni IT** | Configurazione dei dispositivi; risposta agli incidenti di rete |
| **SOC** | Monitoraggio del traffico di rete; rilevamento delle anomalie |
| **Proprietari delle applicazioni** | Definizione dei requisiti di sicurezza della rete per le applicazioni di proprietà |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti per la sicurezza della rete. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.20-22 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
