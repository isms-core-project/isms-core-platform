<!-- ISMS-CORE:POLICY:PRIV-POL-A.2.4.2-4-FR:privacy:POL:a.2.4.2-4 -->
**PRIV-POL-A.2.4.2-4 — Contrôles du cycle de vie du sous-traitant**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Contrôles du cycle de vie du sous-traitant |
| **Type de document** | Politique |
| **Identifiant du document** | PRIV-POL-A.2.4.2-4 |
| **Auteur du document** | Délégué à la Protection des Données (DPD) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit Privacy** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | DPD | Politique initiale pour la première certification ISO/IEC 27701:2025 |

**Cycle de révision** : Annuel | **Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** : Principale: DPD; Secondaire: RSSI; Autorité finale: Direction générale.

**Documents connexes** :
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.2.4.2-4-UG / TG
- PRIV-POL-A.2.2.2-7 (Accords et obligations du sous-traitant)
- PRIV-POL-A.1.4.6-10 (Cycle de vie des DCP — contrepartie côté responsable du traitement)
- PRIV-POL-A.3.5-7 (Classification et transfert)
- ISO/IEC 27701:2025 Contrôles A.2.4.2, A.2.4.3, A.2.4.4
- RGPD Article 28(3)(g) (retour ou suppression en fin de service) ; Article 32(1)(a) (sécurité des transmissions)
- LPD suisse Article 9 (mesures de sécurité équivalentes)

**Applicabilité du rôle** : Cette politique s'applique à [Organisation] agissant en tant que **Sous-traitant des DCP uniquement**. Les contrôles A.2.4.2–A.2.4.4 sont spécifiques au sous-traitant (Tableau A.2).

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] lorsqu'elle agit en tant que sous-traitant de DCP pour l'élimination des fichiers temporaires, le retour/transfert/élimination sécurisée des DCP du client en fin de service, et les contrôles de transmission des DCP — conformément aux contrôles A.2.4.2, A.2.4.3 et A.2.4.4 d'ISO/IEC 27701:2025.

**Périmètre** : Tous les fichiers temporaires créés lors du traitement des DCP des clients ; toute gestion en fin de service des DCP des clients ; toute transmission de DCP sur des réseaux de données pour le compte des clients.

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27701:2025

**Contrôle A.2.4.2 — Fichiers temporaires**
Le contrôle A.2.4.2 exige que [Organisation] veille à ce que les fichiers temporaires créés lors du traitement des DCP soient éliminés dans un délai défini et documenté selon des procédures documentées.

**Contrôle A.2.4.3 — Retour, transfert ou élimination des DCP**
Le contrôle A.2.4.3 exige que [Organisation] soit capable de retourner, transférer ou éliminer de manière sécurisée les DCP du client, et de mettre sa politique de retour/élimination à la disposition des clients.

**Contrôle A.2.4.4 — Contrôles de transmission des DCP**
Le contrôle A.2.4.4 exige que [Organisation] applique des contrôles appropriés aux DCP transmis sur des réseaux de données pour le compte des clients, afin de s'assurer que les données atteignent leur destination prévue.

## Cadre réglementaire

**Obligatoire (Niveau 1)** (per PRIV-POL-00) :
- **RGPD UE** : Article 28(3)(g) (le sous-traitant supprime ou retourne les DCP en fin de service selon le choix du responsable du traitement et supprime les copies sauf obligation légale) ; Article 32(1)(a) (pseudonymisation, chiffrement et sécurité des transmissions)
- **LPD suisse** : Article 9 (mesures de sécurité équivalentes aux exigences du responsable du traitement)
- **ISO/IEC 27701:2025** : Contrôles A.2.4.2–A.2.4.4 (normatifs)

---

# Dispositions de la politique

## A.2.4.2 — Fichiers temporaires (sous-traitant)

[Organisation] DOIT veiller à ce que les fichiers temporaires créés lors du traitement des DCP pour le compte des clients soient éliminés dans des délais documentés et précis.

Les exigences d'élimination des fichiers temporaires pour les activités de sous-traitance sont cohérentes avec la politique générale sur les fichiers temporaires de PRIV-POL-A.1.4.6-10 (A.1.4.7), appliquée aux contextes des DCP des clients :

- Fichiers de cache et de staging de traitement : éliminés dans les 48 heures suivant la fin du traitement
- Journaux d'erreurs/exceptions contenant les DCP du client : éliminés dans les 30 jours (rotation automatisée)
- Fichiers d'export générés pour la livraison au client : éliminés dans les 72 heures après la livraison confirmée au client

Les délais spécifiques sont documentés dans PRIV-IMP-A.2.4.2-4-TG. Les mécanismes de purge automatisés sont préférés.

---

## A.2.4.3 — Retour, transfert ou élimination des DCP du client

Lorsqu'un contrat client se termine ou qu'un client demande le retour ou la suppression de ses DCP, [Organisation] DOIT être capable de :

- **Retourner** les DCP au client dans un format structuré et convenu
- **Transférer** les DCP vers un autre sous-traitant désigné par le client
- **Éliminer** les DCP de manière sécurisée selon les méthodes d'effacement approuvées

[Organisation] DOIT choisir entre ces options conformément à l'instruction documentée du client. En l'absence d'instruction spécifique du client à la fin du contrat, [Organisation] DOIT demander des instructions et suivre le défaut spécifié dans l'accord de sous-traitance.

### Normes d'élimination

L'élimination des DCP en fin de contrat suit les méthodes définies dans PRIV-POL-A.1.4.6-10 (A.1.4.9) :
- Enregistrements de base de données : SQL DELETE ou équivalent ; ou effacement cryptographique pour les stockages chiffrés
- Système de fichiers : effacement cryptographique ou écrasement approuvé
- Supports de sauvegarde : alignés sur le calendrier de conservation des sauvegardes ; sauvegardes expirées purgées selon le calendrier ; ou suppression hors cycle sur instruction du client avec confirmation. Lorsque la prochaine expiration de sauvegarde planifiée ne survient pas dans la fenêtre de suppression requise par le client, [Organisation] DOIT immédiatement isoler et restreindre l'accès aux sauvegardes contenant les DCP de ce client comme mesure intérimaire, en attente de la suppression physique à la prochaine expiration

La confirmation de l'élimination DOIT être fournie par écrit au client dans le délai spécifié dans l'accord de sous-traitance ; le défaut organisationnel est de 30 jours après la fin du service, sauf si l'accord en spécifie autrement.

**Défaut en fin de contrat** : Lorsqu'aucune instruction du client n'est reçue et que l'accord de sous-traitance ne spécifie pas de défaut, [Organisation] DOIT demander des instructions au client dans les 5 jours ouvrables suivant la fin du service. Si aucune réponse n'est reçue dans les 30 jours suivant cette notification, [Organisation] supprimera de manière sécurisée tous les DCP du client et confirmera la suppression au client par écrit.

### Disponibilité de la politique

[Organisation] DOIT mettre à disposition des clients sa politique de retour, de transfert et d'élimination sur demande et, lorsque contractuellement requis, dans le cadre de la documentation de l'accord de sous-traitance.

---

## A.2.4.4 — Contrôles de transmission des DCP (sous-traitant)

[Organisation] DOIT soumettre les DCP transmis pour le compte des clients sur des réseaux de données à des contrôles appropriés pour garantir qu'ils atteignent leur destination prévue.

Les contrôles de transmission sont cohérents avec PRIV-POL-A.3.5-7 (règles de transfert) et PRIV-POL-A.3.23-31 (contrôles cryptographiques) :
- Tous les DCP transmis sur des réseaux DOIVENT être chiffrés en transit (minimum TLS 1.2 ; TLS 1.3 préféré)
- Les transmissions de DCP CONFIDENTIELS et RESTREINTS DOIVENT utiliser des méthodes de transfert sécurisé approuvées
- Une confirmation de livraison ou un accusé de réception DOIT être obtenu pour les transmissions de DCP RESTREINTS à des tiers
- Les journaux de transmission pour les DCP transportés sur des réseaux sont tenus per PRIV-POL-A.3.25 (journalisation)

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **DPD** | Gère le processus de retour/élimination des DCP en fin de service ; confirme l'achèvement aux clients ; tient les registres d'élimination |
| **RSSI / Équipe Sécurité IT** | Met en œuvre les mécanismes de purge des fichiers temporaires ; exécute l'élimination ; configure l'application de TLS ; fournit la confirmation d'élimination |
| **Succès client** | Coordonne avec les clients l'option de retour/élimination préférée en fin de contrat ; suit l'achèvement de l'élimination |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Enregistrements de purge des fichiers temporaires | Confirmation automatisée/manuelle de purge des fichiers temporaires DCP client | 3 ans à compter de la date de purge |
| Enregistrements d'élimination en fin de service | Confirmation écrite de retour/transfert/élimination par client | 5 ans |
| Confirmation d'élimination des DCP client | Confirmation écrite envoyée aux clients à la fin du contrat | 5 ans |
| Configuration du chiffrement des transmissions | Enregistrements de configuration TLS pour la transmission des DCP client | En cours + 3 ans |

---

# Considérations d'audit

- Délais d'élimination des fichiers temporaires documentés et mécanismes automatisés en place
- Gestion des DCP en fin de service : preuves de retour, transfert ou élimination selon instruction du client
- Confirmation écrite d'élimination fournie aux clients dans le délai contractuel
- Application de TLS pour la transmission des DCP (preuves de configuration)
- Politique de retour/élimination disponible pour les clients

---

<!-- QA_VERIFIED: 2026-04-03 -->
